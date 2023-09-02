import numpy as np
import torch
import pickle

from torch import nn

from transformers import AutoModel

BERT = AutoModel.from_pretrained('sentence-transformers/all-mpnet-base-v2')
for param in BERT.parameters():
    param.requires_grad = False


class BertArch(nn.Module):
    """
    BERT-based model for subtitles level prediction. BERT-based model + 2 fully-connected layers
    """
    def __init__(self, bert):
        super(BertArch, self).__init__()
        self.bert = bert
        self.dropout = nn.Dropout(0.1)
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(768, 512)
        self.fc2 = nn.Linear(512, 4)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, sent_id, mask):
        _, cls_hs = self.bert(sent_id, attention_mask=mask, return_dict=False)
        x = self.fc1(cls_hs)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.softmax(x)

        return x


def predict_subtitles_level(list_seq: np.array, list_mask: np.array) -> tuple:
    """
    Predict subtitles level by list of sequences and masks of tokens from tokenized text
    :param list_seq: List of sequences
    :param list_mask: List of masks
    :return: Tuple of subtitles level and confidence in this level
    """
    level_dict = {
        0: 'A2',
        1: 'B1',
        2: 'B2',
        3: 'C1'
    }

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    weights = torch.load('model/saved_weights.pt', map_location=device)

    model = BertArch(BERT).to(device)

    model.load_state_dict(weights)

    predictions = []

    for seq_elem, mask_elem in zip(list_seq, list_mask):
        with torch.no_grad():
            preds = model(seq_elem.to(device), mask_elem.to(device))
            predictions.append(preds.detach().cpu().numpy())

    predictions = np.concatenate(predictions, axis=0)

    subtitle_level = np.argmax(predictions, axis=1)
    confidence = np.max(predictions, axis=1)

    subtitle_level = int(subtitle_level.mean().round())
    confidence = np.mean(confidence)

    return level_dict[subtitle_level], confidence
