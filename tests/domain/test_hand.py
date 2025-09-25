import pytest
from app.domain.enums import Suit, NumberValue, MeldType
from app.domain.tile import Tile
from app.domain.meld import Meld
from app.domain.hand import Hand
from app.schemas.hand import HandSchema
from app.schemas.meld import MeldSchema
from app.schemas.tile import TileSchema


# ----------------------
# Fixtures
# ----------------------
@pytest.fixture
def number_tile():
    return Tile(Suit.CIRCLE, NumberValue.FIVE)


@pytest.fixture
def meld_fixture(number_tile):
    return Meld(MeldType.CHOW, number_tile)


@pytest.fixture
def hand_schema_fixture(number_tile, meld_fixture):
    # Create HandSchema with 4 melds and a pair
    tile_schema = TileSchema(suit=number_tile.suit, value=number_tile.value)
    meld_schemas = [MeldSchema(type=MeldType.CHOW, tile=tile_schema) for _ in range(4)]
    return HandSchema(melds=meld_schemas, pair=tile_schema)


# ----------------------
# Tests
# ----------------------
def test_hand_init_valid(meld_fixture, number_tile):
    hand = Hand([meld_fixture] * 4, number_tile)
    assert len(hand.melds) == 4
    assert hand.pair == number_tile
    assert all(isinstance(m, Meld) for m in hand.melds)


def test_hand_validate_errors(number_tile, meld_fixture):
    # Fewer than 4 melds
    with pytest.raises(ValueError):
        Hand([meld_fixture] * 3, number_tile)

    # Pair not a Tile
    with pytest.raises(TypeError):
        Hand([meld_fixture] * 4, "not_a_tile")

    # Meld not a Meld instance
    with pytest.raises(TypeError):
        Hand(["not_a_meld"] * 4, number_tile)


def test_hand_label_property(meld_fixture, number_tile):
    hand = Hand([meld_fixture] * 4, number_tile)
    expected = ", ".join([f"a {meld_fixture.label}" for _ in range(4)])
    expected += f" and a pair of {number_tile.label}"
    assert hand.label == expected


def test_hand_suits_and_chow_count(meld_fixture, number_tile):
    hand = Hand([meld_fixture] * 4, number_tile)
    # All melds use the same suit
    assert hand.suits == [meld_fixture.tile.suit]
    # All melds are chow
    assert hand.chow_count == 4


def test_hand_from_schema(hand_schema_fixture):
    hand = Hand.from_schema(hand_schema_fixture)
    assert isinstance(hand, Hand)
    assert len(hand.melds) == 4
    assert isinstance(hand.pair, Tile)
    assert all(isinstance(m, Meld) for m in hand.melds)
