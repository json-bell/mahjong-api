from app.domain import Tile, Meld, Hand, Suit, MeldType, NumberValue
from app.mappers import HandMapper
from app.schemas.hand import HandCreateSchema
from app.schemas.meld import MeldSchema
from app.schemas.tile import TileSchema
import pytest


@pytest.fixture
def hand_schema_fixture():
    # Create HandSchema with 4 melds and a pair
    tile_schema = TileSchema(suit=Suit.CIRCLE, value=NumberValue.FIVE)
    meld_schemas = [MeldSchema(type=MeldType.CHOW, tile=tile_schema) for _ in range(4)]
    return HandCreateSchema(melds=meld_schemas, pair=tile_schema, game_id=1)


def test_hand_from_schema(hand_schema_fixture):
    hand = HandMapper.from_schema(hand_schema_fixture)
    assert isinstance(hand, Hand)
    assert len(hand.melds) == 4
    assert isinstance(hand.pair, Tile)
    assert all(isinstance(m, Meld) for m in hand.melds)


def test_hand_from_short():
    hand = HandMapper.from_short(melds=["CBa4", "KDrG", "PWiE", "CCh2"], pair="DrR")
    assert isinstance(hand, Hand)
    assert len(hand.melds) == 4
    assert isinstance(hand.pair, Tile)
    assert all(isinstance(m, Meld) for m in hand.melds)
    assert ([meld.tile.suit.value for meld in hand.melds]) == (
        [
            Suit.BAMBOO.value,
            Suit.DRAGON.value,
            Suit.WIND.value,
            Suit.CHARACTER.value,
        ]
    )
