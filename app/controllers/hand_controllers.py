from fastapi import APIRouter
from app.schemas.hand import HandCreateSchema
from app.domain.hand import Hand
from app.services.scoring import calculate_hand_score

router = APIRouter(prefix="/hands", tags=["hands"])


@router.post("/score", operation_id="scoreHand")
def score_hand_endpoint(hand_schema: HandCreateSchema):
    # Convert schema to domain object
    hand = Hand.from_schema(hand_schema)

    # Return a simple JSON response
    return calculate_hand_score(hand)
