import sys

import uvicorn
from fastapi import FastAPI

from prediction_core import predict_subtitles_level
from data_preprocessing import data_preprocess

app = FastAPI()


@app.get("/subtitles_level/")
async def get_subtitles_level(subs: str):
    try:
        list_seq, list_mask = data_preprocess(subs)
        subtitles_level, confidence = predict_subtitles_level(list_seq, list_mask)
        print(subtitles_level, confidence)
        return {"subtitles_level": subtitles_level, "confidence": float(confidence)}
    except:
        error_type = sys.exc_info()[0]
        return {"error": "Error: " + str(error_type) + ". Please, check your input data."}


if __name__ == "__main__":
    uvicorn.run(app)

