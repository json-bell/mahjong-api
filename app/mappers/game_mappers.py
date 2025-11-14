from app.domain import Game
from app.schemas import GameOutSchema, GameDetailSchema, GameCreateSchema
from app.db.models import GameModel
from .scored_hand_mappers import ScoredHandMapper
from .player_mappers import PlayerMapper


class GameMapper:
    @staticmethod
    def from_schema(schema: GameCreateSchema) -> Game:
        return Game()

    @staticmethod
    def to_out_schema(game: Game, game_id: int) -> GameOutSchema:
        return GameOutSchema(
            created_at=game.created_at,
            id=game_id,
        )

    # @staticmethod
    # """No to detail schema since it requires hand and player ids,
    # not easily available or passable from the Game domain object"""
    # def to_detail_schema(game: Game, game_id: int) -> GameDetailSchema:
    #     base = GameMapper.to_out_schema(game, game_id)
    #     return GameDetailSchema(
    #         **base.model_dump(),
    #         hands=[ScoredHandMapper.to_schema(h, game_id) for h in game.hands],
    #         players=[PlayerMapper.to_schema(p, game_id) for p in game.players],
    #     )

    @staticmethod
    def from_model(model: GameModel) -> Game:
        return Game(
            created_at=model.created_at,
            hands=[ScoredHandMapper.from_model(h) for h in model.hands],
            players=[PlayerMapper.from_model(p) for p in model.players],
        )

    @staticmethod
    def to_model(game: Game) -> GameModel:
        return GameModel(
            **({"created_at": game.created_at} if game.created_at else {}),
        )

    # Convenience round trip mappers:
    @staticmethod
    def model_to_detail_schema(model: GameModel) -> GameDetailSchema:
        base = GameMapper.model_to_out_schema(model)
        return GameDetailSchema(
            **base.model_dump(),
            game_id=model.id,
            hands=[ScoredHandMapper.model_to_schema(h) for h in model.hands],
            players=[PlayerMapper.model_to_schema(h) for h in model.players],
        )

    @staticmethod
    def model_to_out_schema(model: GameModel) -> GameOutSchema:
        return GameMapper.to_out_schema(
            GameMapper.from_model(model),
            game_id=model.id,
        )

    @staticmethod
    def schema_to_model(schema: GameCreateSchema) -> GameModel:
        return GameMapper.to_model(
            GameMapper.from_schema(schema),
        )
