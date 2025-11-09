from app.domain import Player, PlayerSlot


def test_player_class():
    new_player = Player(name="Mock name", score=12, player_slot=PlayerSlot(3))
    assert new_player.name == "Mock name"
    assert new_player.score == 12
    assert new_player.player_slot == PlayerSlot(3)


def test_defaults_zero_score():
    new_player = Player(name="Mock name", player_slot=PlayerSlot(1))
    assert new_player.name == "Mock name"
    assert new_player.score == 0
