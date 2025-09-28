from fastapi import APIRouter
from app.schemas.hand import HandSchema
from app.domain.hand import Hand
from app.services.scoring import calculate_hand_score

router = APIRouter()


@router.post("/score_hand", operation_id="scoreHand")
def score_hand_endpoint(hand_schema: HandSchema):
    # Convert schema to domain object
    hand = Hand.from_schema(hand_schema)

    # Return a simple JSON response
    return calculate_hand_score(hand)
