from app.mappers import PlayerMapper
from app.schemas import PlayerCreateSchema
from app.domain import PlayerSlot, Player


def test_player_from_schema():
    player_schema = PlayerCreateSchema(game_id=1, name="Mock name", player_slot=PlayerSlot(2), score=4)
    new_player = PlayerMapper.from_schema(player_schema)

    assert isinstance(new_player, Player)
    assert new_player.name == "Mock name"
    assert new_player.score == 4
