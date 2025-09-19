from fastapi import APIRouter
from app.models import Tile
from app.services.mahjong import calculate_hand_score

router = APIRouter()


@router.post("/score_hand")
def score_hand_endpoint(tile: Tile):
    return {"status": "success", "tile": tile}
