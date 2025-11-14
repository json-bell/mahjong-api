from sqlalchemy.orm import Session, joinedload
from ..models import GameModel
from app.schemas import GameCreateSchema, GameOutSchema, GameDetailSchema
from app.mappers import GameMapper


def create_game(db: Session, game: GameCreateSchema):
    db_game = GameModel()
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_game_by_id(db: Session, game_id: int) -> GameDetailSchema | None:
    db_game = (
        db.query(GameModel)
        .filter(GameModel.id == game_id)
        .options(joinedload(GameModel.hands))
        .options(joinedload(GameModel.players))
        .first()
    )
    if db_game is None:
        return None
    return GameMapper.model_to_detail_schema(db_game)


def list_games(db: Session) -> list[GameOutSchema]:
    db_games = db.query(GameModel).all()
    return [GameMapper.model_to_out_schema(g) for g in db_games]
