import pytest
from app.domain import Tile
from app.domain.enums import Suit, NumberValue, DragonValue, WindValue
from app.schemas.tile import TileSchema
from app.domain.exceptions import InvalidTileError


# ----------------------
# Fixtures
# ----------------------
@pytest.fixture
def number_tile():
    return Tile(Suit.CIRCLE, NumberValue.FIVE)


@pytest.fixture
def wind_tile():
    return Tile(Suit.WIND, WindValue.EAST)


@pytest.fixture
def dragon_tile():
    return Tile(Suit.DRAGON, DragonValue.RED)


@pytest.fixture
def number_tile_schema():
    return TileSchema(suit=Suit.BAMBOO, value=NumberValue.SEVEN)


# ----------------------
# Tests
# ----------------------
def test_tile_initialization_valid(number_tile, wind_tile, dragon_tile):
    # Number tile
    assert number_tile.suit == Suit.CIRCLE
    assert number_tile.value == NumberValue.FIVE
    assert number_tile.is_honour is False

    # Wind tile
    assert wind_tile.is_honour is True
    assert wind_tile.suit == Suit.WIND

    # Dragon tile
    assert dragon_tile.is_honour is True
    assert dragon_tile.suit == Suit.DRAGON


def test_tile_label_property(number_tile, wind_tile, dragon_tile):
    # Number tile
    assert number_tile.label == f"{number_tile.value.label} of {number_tile.suit.label}"
    # Wind tile
    assert wind_tile.label == f"{wind_tile.value.label} {wind_tile.suit.label}"
    # Dragon tile
    assert dragon_tile.label == f"{dragon_tile.value.label} {dragon_tile.suit.label}"


def test_chow_sequence_valid(number_tile):
    # NumberValue.FIVE => 5-6-7
    assert number_tile.chow_sequence == "5-6-7"


def test_chow_sequence_errors():
    wind = Tile(Suit.WIND, WindValue.NORTH)
    dragon = Tile(Suit.DRAGON, DragonValue.GREEN)
    for tile in (wind, dragon):
        with pytest.raises(InvalidTileError):
            _ = tile.chow_sequence

    tile8 = Tile(Suit.CIRCLE, NumberValue.EIGHT)
    tile9 = Tile(Suit.CIRCLE, NumberValue.NINE)
    for tile in (tile8, tile9):
        with pytest.raises(InvalidTileError):
            _ = tile.chow_sequence


def test_validate_errors():
    # Invalid suit type
    with pytest.raises(InvalidTileError):
        Tile("circle", NumberValue.ONE)  # suit must be Suit enum

    # Wrong value type for wind
    with pytest.raises(InvalidTileError):
        Tile(Suit.WIND, NumberValue.ONE)

    # Wrong value type for dragon
    with pytest.raises(InvalidTileError):
        Tile(Suit.DRAGON, NumberValue.TWO)

    # Wrong value type for number suit
    with pytest.raises(InvalidTileError):
        Tile(Suit.CIRCLE, DragonValue.RED)


def test_tile_from_schema(number_tile_schema):
    tile = Tile.from_schema(number_tile_schema)
    assert isinstance(tile, Tile)
    assert tile.suit == number_tile_schema.suit
    assert tile.value == number_tile_schema.value


def test_dragon_tile_from_short():
    tile = Tile.from_short("DrG")
    assert isinstance(tile, Tile)
    assert tile.suit == Suit.DRAGON
    assert tile.value == DragonValue.GREEN


def test_wind_tile_from_short():
    tile = Tile.from_short("WiE")
    assert isinstance(tile, Tile)
    assert tile.suit == Suit.WIND
    assert tile.value == WindValue.EAST


def test_number_tile_from_short():
    tile = Tile.from_short("Ch3")
    assert isinstance(tile, Tile)
    assert tile.suit == Suit.CHARACTER
    assert tile.value == NumberValue.THREE
