from typing import List
from .enums import MeldType, Suit
from .tile import Tile
from .meld import Meld
from .exceptions import InvalidTileError, InvalidMeldError, InvalidHandError
from app.schemas.hand import HandCreateSchema


class Hand:
    def __init__(self, melds: List[Meld], pair: Tile):
        self.melds = melds
        self.pair = pair
        self._validate()

    @property
    def label(self) -> str:
        meld_descriptions = ", ".join([f"a {meld.label}" for meld in self.melds])
        return f"{meld_descriptions} and a pair of {self.pair.label}"

    @property
    def suits(self) -> list[Suit]:
        return [*[meld.tile.suit for meld in self.melds], self.pair.suit]

    @property
    def chow_count(self) -> int:
        return [meld.type for meld in self.melds].count(MeldType.CHOW)

    def _validate(self):
        if len(self.melds) != 4:
            raise InvalidHandError(
                "A hand must have exactly 4 melds.", length=len(self.melds), hand=self
            )
        if not isinstance(self.pair, Tile):
            raise InvalidTileError("Pair must have a suit and value", pair=self.pair)
        for meld in self.melds:
            if not isinstance(meld, Meld):
                raise InvalidMeldError(
                    "All melds must be have a tile and type", meld=meld
                )

    def to_dict(self):
        return {
            "melds": [meld.to_dict() for meld in self.melds],
            "pair": self.pair.to_dict(),
        }

    @classmethod
    def from_schema(cls, schema: HandCreateSchema) -> "Hand":
        melds = [Meld.from_schema(meld) for meld in schema.melds]
        pair = Tile.from_schema(schema.pair)
        return cls(melds, pair)

    @classmethod
    def from_short(cls, melds: List[str], pair: str):
        from app.domain.mahjong_factory import MahjongFactory

        return MahjongFactory.hand_from_short(melds, pair)
