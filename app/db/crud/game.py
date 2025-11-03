from sqlalchemy.orm import Session, joinedload
from app.db import models
from app.schemas import GameCreateSchema


def create_game(db: Session, game: GameCreateSchema):
    db_game = models.Game()
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_game_by_id(db: Session, game_id: int):
    return (
        db.query(models.Game)
        .options(joinedload(models.Game.hands))
        .filter(models.Game.id == game_id)
        .first()
    )


def list_games(db: Session):
    return db.query(models.Game).all()
