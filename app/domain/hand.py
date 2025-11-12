from dataclasses import dataclass
from .enums import MeldType, Suit
from .tile import Tile
from .meld import Meld
from .exceptions import InvalidTileError, InvalidMeldError, InvalidHandError


@dataclass
class Hand:
    melds: list[Meld]
    pair: Tile

    def __post_init__(self):
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
