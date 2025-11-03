from app.domain import Game
from app.schemas import GameOutSchema


class GameMapper:
    @staticmethod
    def from_schema(schema: GameOutSchema) -> Game:
        game_id = schema.id
        return Game(game_id)
