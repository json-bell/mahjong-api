from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas import HandSchema, ScoredHandOutSchema
from app.mappers import HandMapper
from app.services.scoring import ScoringService, HandScoreExplanation
from app.db.crud import hand as hand_crud


router = APIRouter(prefix="/hands", tags=["hands"])


@router.post("/score", response_model=HandScoreExplanation, operation_id="scoreHand")
def score_hand_endpoint(hand_schema: HandSchema):
    service = ScoringService()
    # Convert schema to domain object
    hand = HandMapper.from_schema(hand_schema)

    # Return a simple JSON response
    return service.calculate_and_explain(hand)


@router.get("/", response_model=list[ScoredHandOutSchema], operation_id="readHands")
def read_hands(db: Session = Depends(get_db)) -> list[ScoredHandOutSchema]:
    return hand_crud.list_hands(db)
