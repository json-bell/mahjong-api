from fastapi import FastAPI
from pathlib import Path
import json
from app.controllers.score_hand import router as score_router

app = FastAPI()

app.include_router(score_router)

BASE_DIR = Path(__file__).resolve().parent
ENDPOINTS_JSON_PATH = BASE_DIR / "endpoints.json"


@app.get("/")
def read_root():
    return {
        "message": "GET the /api endpoint to receive a JSON of the available endpoints"
    }


@app.get("/api")
def read_api():
    with open(ENDPOINTS_JSON_PATH, "r") as f:
        data = json.load(f)
    return data
