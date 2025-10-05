import pytest
from app.domain.enums import MeldType, NumberValue, Suit, WindValue
from app.domain.tile import Tile
from app.domain.meld import Meld
from app.schemas.tile import TileSchema
from app.schemas.meld import MeldSchema
from app.domain.exceptions import InvalidMeldError, InvalidTileError


# ----------------------
# Fixtures
# ----------------------
@pytest.fixture
def base_tile():
    return Tile(Suit.CIRCLE, NumberValue.FIVE)


@pytest.fixture
def honour_tile():
    return Tile(Suit.WIND, WindValue.EAST)


@pytest.fixture
def base_tile_schema():
    return TileSchema(suit=Suit.CIRCLE, value=NumberValue.FIVE)


@pytest.fixture
def meld_schema(base_tile_schema):
    return MeldSchema(type=MeldType.CHOW, tile=base_tile_schema)


# ----------------------
# Tests
# ----------------------
def test_meld_init_valid(base_tile):
    # Chow
    meld_chow = Meld(MeldType.CHOW, base_tile)
    assert meld_chow.type == MeldType.CHOW
    assert meld_chow.tile == base_tile

    # Pong
    meld_pong = Meld(MeldType.PONG, base_tile)
    assert meld_pong.type == MeldType.PONG
    assert meld_pong.tile == base_tile


def test_meld_label_property_chow(base_tile):
    meld = Meld(MeldType.CHOW, base_tile)
    # Chow label should include the chow_sequence and suit
    expected = f"{base_tile.chow_sequence} {base_tile.suit.label} Chow"
    assert meld.label == expected


def test_meld_label_property_non_chow(base_tile):
    meld = Meld(MeldType.PONG, base_tile)
    expected = f"{base_tile.label} {meld.type.label}"
    assert meld.label == expected


def test_meld_validate_errors(base_tile, honour_tile):
    # tile not a Tile instance
    with pytest.raises(InvalidTileError):
        Meld(MeldType.CHOW, "not_a_tile")

    # Chow with honour tile should raise ValueError
    with pytest.raises(InvalidMeldError):
        Meld(MeldType.CHOW, honour_tile)

    # Chow starting with 8 or 9 should raise ValueError
    tile8 = Tile(Suit.CIRCLE, NumberValue.EIGHT)
    tile9 = Tile(Suit.CIRCLE, NumberValue.NINE)
    for tile in (tile8, tile9):
        with pytest.raises(InvalidMeldError):
            Meld(MeldType.CHOW, tile)


def test_meld_from_schema(meld_schema):
    meld = Meld.from_schema(meld_schema)
    assert isinstance(meld, Meld)
    assert meld.type == meld_schema.type
    assert isinstance(meld.tile, Tile)
    assert meld.tile.suit == meld_schema.tile.suit
    assert meld.tile.value == meld_schema.tile.value
