from app.domain import Player
from app.schemas import PlayerCreateSchema


class PlayerMapper:
    @staticmethod
    def from_schema(schema: PlayerCreateSchema) -> Player:
        return Player(name=schema.name, player_index=schema.player_index)
