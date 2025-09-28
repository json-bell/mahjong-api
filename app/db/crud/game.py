from sqlalchemy.orm import Session
from app.db import models
from app.schemas.game import GameSchema


def create_game(game: GameSchema, db: Session):
    db_game = models.Game()
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_game_by_id(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def list_games(db: Session):
    return db.query(models.Game).all()
