from app.domain import Tile, Meld
from app.domain.enums import Suit, MeldType, NumberValue, WindValue
from app.mappers import MeldMapper
from app.schemas.tile import TileSchema
from app.schemas.meld import MeldSchema
import pytest


@pytest.fixture
def base_tile_schema():
    return TileSchema(suit=Suit.CIRCLE, value=NumberValue.FIVE)


@pytest.fixture
def meld_schema(base_tile_schema):
    return MeldSchema(type=MeldType.CHOW, tile=base_tile_schema)


def test_meld_from_schema(meld_schema):
    meld = MeldMapper.from_schema(meld_schema)
    assert isinstance(meld, Meld)
    assert meld.type == meld_schema.type
    assert isinstance(meld.tile, Tile)
    assert meld.tile.suit == meld_schema.tile.suit
    assert meld.tile.value == meld_schema.tile.value


def test_chow_meld_from_short():
    meld = MeldMapper.from_short("CBa5")
    assert isinstance(meld, Meld)
    assert meld.type == MeldType.CHOW
    assert isinstance(meld.tile, Tile)
    assert meld.tile.suit == Suit.BAMBOO
    assert meld.tile.value == NumberValue.FIVE


def test_pong_meld_from_short():
    meld = MeldMapper.from_short("PWiW")
    assert isinstance(meld, Meld)
    assert meld.type == MeldType.PONG
    assert isinstance(meld.tile, Tile)
    assert meld.tile.suit == Suit.WIND
    assert meld.tile.value == WindValue.WEST
