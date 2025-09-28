from fastapi import FastAPI
from pathlib import Path
import json
from app.controllers.score_hand import router as score_router
from app.controllers import game_controllers


app = FastAPI(title="Mahjong Score Tracker")

app.include_router(score_router)
app.include_router(game_controllers.router)


BASE_DIR = Path(__file__).resolve().parent
ENDPOINTS_JSON_PATH = BASE_DIR / "endpoints.json"


@app.get("/", operation_id="readRoot")
def read_root():
    return {
        "message": "GET the /api endpoint to receive a JSON of the available endpoints, "
        "or the /openapi.json endpoint for the auto-generated OpenAPI specifications"
    }


@app.get("/healthz", operation_id="getHealthCheck")
def healthz():
    """Checks API health"""
    return {"status": "ok"}


@app.get("/api", operation_id="getApiEndpointSummary")
def read_api():
    with open(ENDPOINTS_JSON_PATH, "r") as f:
        data = json.load(f)
    return data
