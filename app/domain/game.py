from app.schemas.game import GameOutSchema


class Game:
    def __init__(self, game_id: int):
        self.game_id = game_id
        self._validate()

    def _validate(self):
        pass

    @classmethod
    def from_schema(cls, schema: GameOutSchema) -> "Game":
        game_id = schema.id
        return cls(game_id)
