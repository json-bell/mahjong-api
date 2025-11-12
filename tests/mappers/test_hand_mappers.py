from app.domain import Tile, Meld, Hand, Suit, MeldType, NumberValue
from app.mappers import HandMapper
from app.schemas import HandSchema, MeldSchema, TileSchema
import pytest


@pytest.fixture
def hand_schema_fixture():
    # Create HandSchema with 4 melds and a pair
    tile_schema = TileSchema(suit=Suit.CIRCLE, value=NumberValue.FIVE)
    meld_schemas = [MeldSchema(type=MeldType.CHOW, tile=tile_schema) for _ in range(4)]
    return HandSchema(melds=meld_schemas, pair=tile_schema)


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


def test_hand_from_dict(example_hand_tiles):
    hand = HandMapper.from_dict(example_hand_tiles)
    assert isinstance(hand, Hand)
    assert len(hand.melds) == 4
    assert isinstance(hand.pair, Tile)
    assert all(isinstance(m, Meld) for m in hand.melds)


def test_hand_to_and_from_dict():
    hand = HandMapper.from_short(melds=["CBa4", "KDrG", "PWiE", "CCh2"], pair="DrR")
    dicted_hand = HandMapper.to_dict(hand)
    reversed_hand = HandMapper.from_dict(dicted_hand)
    assert reversed_hand == hand
