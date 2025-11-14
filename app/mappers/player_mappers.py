from app.domain import Player, PlayerSlot
from app.schemas import PlayerCreateSchema, PlayerOutSchema
from app.db.models import PlayerModel


class PlayerMapper:
    @staticmethod
    def from_schema(schema: PlayerCreateSchema) -> Player:
        return Player(
            name=schema.name, player_slot=schema.player_slot, score=schema.score
        )

    @staticmethod
    def to_schema(player: Player, game_id: int, id: int) -> PlayerOutSchema:
        return PlayerOutSchema(
            name=player.name,
            player_slot=player.player_slot,
            score=player.score,
            game_id=game_id,
            id=id,
        )

    @staticmethod
    def from_model(model: PlayerModel) -> Player:
        return Player(
            name=model.name,
            player_slot=PlayerSlot(model.player_slot),
            score=model.score,
        )

    @staticmethod
    def to_model(player: Player, game_id: int) -> PlayerModel:
        return PlayerModel(
            name="test",
            game_id=game_id,
            player_slot=player.player_slot,
            score=player.score,
        )

    # Convenience round trip mappers:
    @staticmethod
    def model_to_schema(model: PlayerModel) -> PlayerOutSchema:
        return PlayerMapper.to_schema(
            PlayerMapper.from_model(model),
            game_id=model.game_id,
            id=model.id,
        )

    @staticmethod
    def schema_to_model(schema: PlayerCreateSchema, game_id: int) -> PlayerModel:
        return PlayerMapper.to_model(
            PlayerMapper.from_schema(schema),
            game_id=game_id,
        )
