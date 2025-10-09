from sqlalchemy.orm import Session
from app.db import models
from app.schemas.hand import HandCreateSchema


def create_hand(db: Session, hand_data: HandCreateSchema, game_id: int):
    db_hand = models.Hand(**hand_data.model_dump(), game_id=game_id)
    db.add(db_hand)
    db.commit()
    db.refresh(db_hand)
    return db_hand


def list_hands_by_game(db: Session, game_id: int):
    return db.query(models.Hand).filter(models.Hand.game_id == game_id).all()


def list_hands(db: Session):
    return db.query(models.Hand).all()
