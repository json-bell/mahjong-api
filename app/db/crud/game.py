from sqlalchemy.orm import Session, joinedload
from ..models import GameModel
from app.schemas import GameCreateSchema, GameOutSchema, GameDetailSchema
from app.mappers import GameMapper
from .player import create_players


def create_game(db: Session, game: GameCreateSchema) -> GameDetailSchema:
    db_game = GameMapper.schema_to_model(game)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    if game.players is not None:
        game_id: int = db_game.id
        create_players(db, players=game.players, game_id=game_id)

    return GameMapper.model_to_detail_schema(db_game)


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
