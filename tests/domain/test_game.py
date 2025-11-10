import pytest
from app.domain import Player, Game, InvalidGameError, PlayerSlot
from app.mappers import HandMapper
from datetime import datetime


# ----------------------
# Fixtures
# ----------------------


@pytest.fixture
def mock_time():
    return datetime(2025, 11, 3, 9)


@pytest.fixture
def mock_player():
    def _make_player(player_slot: int = 1):
        return Player(name=f"Player {player_slot}", score=0, player_slot=PlayerSlot(player_slot))

    return _make_player


def test_game_init_valid():
    game = Game()
    assert game.hands == []
    assert game.players is None
    assert game.created_at is None


def test_game_options(mock_time, mock_player):
    game = Game(
        created_at=mock_time,
        hands=[HandMapper.from_short(melds=["CCh6", "CBa6", "PDrG", "PWiE"], pair="Ba3")],
        players=[mock_player(i) for i in range(1, 5)],
    )
    assert len(game.hands) == 1
    assert len(game.players) == 4
    assert game.created_at == mock_time


def test_game_validate_errors(mock_player):
    # Empty players
    with pytest.raises(InvalidGameError):
        Game(players=[])

    # Wrong number of players
    with pytest.raises(InvalidGameError):
        Game(players=[mock_player()])
