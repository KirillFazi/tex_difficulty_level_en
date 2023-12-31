import sys

import uvicorn
from fastapi import FastAPI

from prediction_core import predict_subtitles_level
from data_preprocessing import data_preprocess

app = FastAPI()


@app.get("/subtitle_level/")
async def get_subtitles_level(subs: str):
    try:
        list_seq, list_mask = data_preprocess(subs)
        subtitle_level, confidence = predict_subtitles_level(list_seq, list_mask)
        return {'response_type': 200, "subtitle_level": subtitle_level, "confidence": float(confidence)}
    except FileNotFoundError:
        return {'response_type': 404, "error": "File not found", "error_message": f'{sys.exc_info()[1]}'}
    except:
        return {'response_type': 500, "error": "Internal server error", "error_message": f'{sys.exc_info()[1]}'}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
