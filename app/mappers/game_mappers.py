from app.domain import Game
from app.schemas import GameOutSchema


class GameMapper:
    @staticmethod
    def from_schema(schema: GameOutSchema) -> Game:
        return Game()
