from app.domain import Player, PlayerIndex


def test_player_class():
    new_player = Player(name="Mock name", score=12, player_index=PlayerIndex(3))
    assert new_player.name == "Mock name"
    assert new_player.score == 12
    assert new_player.player_index == PlayerIndex(3)


def test_defaults_zero_score():
    new_player = Player(name="Mock name", player_index=PlayerIndex(1))
    assert new_player.name == "Mock name"
    assert new_player.score == 0
