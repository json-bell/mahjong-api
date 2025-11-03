from app.domain import Tile
from app.domain.enums import Suit, DragonValue, NumberValue, WindValue
from app.mappers import TileMapper
from app.schemas.tile import TileSchema
import pytest


@pytest.fixture
def number_tile_schema():
    return TileSchema(suit=Suit.BAMBOO, value=NumberValue.SEVEN)


def test_tile_from_schema(number_tile_schema):
    tile = TileMapper.from_schema(number_tile_schema)
    assert isinstance(tile, Tile)
    assert tile.suit == number_tile_schema.suit
    assert tile.value == number_tile_schema.value


def test_dragon_tile_from_short():
    tile = TileMapper.from_short("DrG")
    assert isinstance(tile, Tile)
    assert tile.suit == Suit.DRAGON
    assert tile.value == DragonValue.GREEN


def test_wind_tile_from_short():
    tile = TileMapper.from_short("WiE")
    assert isinstance(tile, Tile)
    assert tile.suit == Suit.WIND
    assert tile.value == WindValue.EAST


def test_number_tile_from_short():
    tile = TileMapper.from_short("Ch3")
    assert isinstance(tile, Tile)
    assert tile.suit == Suit.CHARACTER
    assert tile.value == NumberValue.THREE
