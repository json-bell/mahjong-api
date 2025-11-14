from sqlalchemy.orm import Session
from ..models import PlayerModel
from app.schemas import PlayerCreateSchema, PlayerOutSchema
from app.mappers import PlayerMapper


def create_players(
    db: Session, players: list[PlayerCreateSchema], game_id: int
) -> None:
    db_players = [PlayerMapper.schema_to_model(player, game_id) for player in players]
    db.add_all(db_players)
    db.commit()


def list_players_by_game(db: Session, game_id: int) -> list[PlayerOutSchema]:
    db_players = db.query(PlayerModel).filter(PlayerModel.game_id == game_id).all()
    return [PlayerMapper.model_to_schema(p) for p in db_players]
