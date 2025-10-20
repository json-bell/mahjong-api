from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.domain.exceptions import MahjongError
from pathlib import Path
import json
from app.controllers import game_controllers, hand_controllers, score_controllers
from app.config import settings


app = FastAPI(title="Mahjong Score Tracker")

origins = [settings.frontend_url] if settings.frontend_url else []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(MahjongError)
async def mahjong_error_handler(request: Request, exc: MahjongError):
    return JSONResponse(content=exc.to_dict(), status_code=400)


app.include_router(hand_controllers.router)
app.include_router(game_controllers.router)
app.include_router(score_controllers.router)


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
