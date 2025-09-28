from sqlalchemy.orm import Session
from app.db import models
from app.schemas.hand import HandSchema


def create_hand(db: Session, hand_data: HandSchema, game_id: int):
    db_hand = models.Hand(**hand_data.dict(), game_id=game_id)
    db.add(db_hand)
    db.commit()
    db.refresh(db_hand)
    return db_hand


def get_hands_by_game(db: Session, game_id: int):
    return db.query(models.Hand).filter(models.Hand.game_id == game_id).all()
