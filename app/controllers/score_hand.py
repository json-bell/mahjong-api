from fastapi import APIRouter
from app.models import Hand
from app.services.mahjong import calculate_hand_score

router = APIRouter()


@router.post("/score_hand")
def score_hand_endpoint(hand: Hand):
    return calculate_hand_score(hand)
