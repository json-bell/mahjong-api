from fastapi import APIRouter
from app.schemas.hand import HandCreateSchema
from app.mappers import HandMapper
from app.services.scoring import ScoringService, HandScoreExplanation
from app.db.crud import hand as hand_crud


router = APIRouter(prefix="/hands", tags=["hands"])


@router.post("/score", response_model=HandScoreExplanation, operation_id="scoreHand")
def score_hand_endpoint(hand_schema: HandCreateSchema):
    service = ScoringService()
    # Convert schema to domain object
    hand = HandMapper.from_schema(hand_schema)

    # Return a simple JSON response
    return service.calculate_and_explain(hand)


@router.get("/")
def read_hands():
    return hand_crud.list_hands()
