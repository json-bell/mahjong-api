import pytest
from app.domain import (
    Tile,
    Meld,
    Hand,
    Suit,
    NumberValue,
    MeldType,
    InvalidTileError,
    InvalidMeldError,
    InvalidHandError,
    PlayerSlot,
)


# ----------------------
# Fixtures
# ----------------------
@pytest.fixture
def number_tile():
    return Tile(Suit.CIRCLE, NumberValue.FIVE)


@pytest.fixture
def meld_fixture(number_tile):
    return Meld(MeldType.CHOW, number_tile)


# ----------------------
# Tests
# ----------------------
def test_hand_init_valid(meld_fixture, number_tile):
    hand = Hand([meld_fixture] * 4, number_tile, player_slot=PlayerSlot.FIRST)
    assert len(hand.melds) == 4
    assert hand.pair == number_tile
    assert all(isinstance(m, Meld) for m in hand.melds)


def test_hand_validate_errors(number_tile, meld_fixture):
    # Fewer than 4 melds
    with pytest.raises(InvalidHandError):
        Hand([meld_fixture] * 3, number_tile, player_slot=PlayerSlot.FIRST)

    # Pair not a Tile
    with pytest.raises(InvalidTileError):
        Hand([meld_fixture] * 4, "not_a_tile", player_slot=PlayerSlot.FIRST)

    # Meld not a Meld instance
    with pytest.raises(InvalidMeldError):
        Hand(["not_a_meld"] * 4, number_tile, player_slot=PlayerSlot.FIRST)


def test_hand_label_property(meld_fixture, number_tile):
    hand = Hand([meld_fixture] * 4, number_tile, player_slot=PlayerSlot.FIRST)
    expected = ", ".join([f"a {meld_fixture.label}" for _ in range(4)])
    expected += f" and a pair of {number_tile.label}"
    assert hand.label == expected


def test_hand_suits(meld_fixture, number_tile):
    hand = Hand([meld_fixture] * 4, number_tile, player_slot=PlayerSlot.FIRST)
    assert hand.suits == [meld_fixture.tile.suit for _ in range(5)]


def test_hand_chow_count(meld_fixture, number_tile):
    hand = Hand([meld_fixture] * 4, number_tile, player_slot=PlayerSlot.FIRST)
    assert hand.chow_count == 4
