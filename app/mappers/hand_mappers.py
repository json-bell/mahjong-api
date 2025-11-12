from app.domain import Hand, InvalidHandError
from app.schemas import HandSchema
from typing import List
from .meld_mappers import MeldMapper
from .tile_mappers import TileMapper


class HandMapper:
    @staticmethod
    def to_dict(hand: Hand) -> dict:
        return {
            "melds": [MeldMapper.to_dict(meld) for meld in hand.melds],
            "pair": TileMapper.to_dict(hand.pair),
        }

    @staticmethod
    def from_dict(dictionary: dict) -> Hand:
        return Hand(
            melds=[MeldMapper.from_dict(m) for m in dictionary["melds"]],
            pair=TileMapper.from_dict(dictionary["pair"]),
        )

    @staticmethod
    def from_schema(schema: HandSchema) -> Hand:
        melds = [MeldMapper.from_schema(meld) for meld in schema.melds]
        pair = TileMapper.from_schema(schema.pair)
        return Hand(melds, pair)

    @staticmethod
    def from_short(melds: List[str], pair: str) -> Hand:
        if len(melds) != 4:
            raise InvalidHandError(f"Invalid meld length: {str(melds)}")

        return Hand(
            melds=[MeldMapper.from_short(meld_code) for meld_code in melds],
            pair=TileMapper.from_short(pair),
        )
