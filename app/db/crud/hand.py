from sqlalchemy.orm import Session
from ..models import HandModel
from app.schemas import ScoredHandCreateSchema, ScoredHandOutSchema
from app.mappers import ScoredHandMapper


def create_hand(
    db: Session, hand_data: ScoredHandCreateSchema, game_id: int
) -> ScoredHandOutSchema:
    model_hand = ScoredHandMapper.schema_to_model(hand_data, game_id)
    db.add(model_hand)
    db.commit()
    db.refresh(model_hand)

    return ScoredHandMapper.model_to_schema(model_hand)


def list_hands_by_game(db: Session, game_id: int) -> list[ScoredHandOutSchema]:
    model_hands = db.query(HandModel).filter(HandModel.game_id == game_id).all()
    return [ScoredHandMapper.model_to_schema(hand) for hand in model_hands]


def list_hands(db: Session) -> list[ScoredHandOutSchema]:
    model_hands = db.query(HandModel).all()
    return [ScoredHandMapper.model_to_schema(hand) for hand in model_hands]
