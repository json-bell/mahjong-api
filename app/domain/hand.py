from typing import List
from app.domain.enums import MeldType
from app.domain.tile import Tile
from app.domain.meld import Meld
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
    def suits(self) -> List[str]:
        return list(set([meld.tile.suit for meld in self.melds]))

    @property
    def chow_count(self) -> int:
        return [meld.type for meld in self.melds].count(MeldType.CHOW)

    def _validate(self):
        if len(self.melds) != 4:
            raise ValueError(f"A hand must have exactly 4 melds, got {len(self.melds)}")
        if not isinstance(self.pair, Tile):
            raise TypeError("pair must be a Tile instance")
        for meld in self.melds:
            if not isinstance(meld, Meld):
                raise TypeError("All melds must be Meld instances")

    @classmethod
    def from_schema(cls, schema: HandCreateSchema) -> "Hand":
        melds = [Meld.from_schema(meld) for meld in schema.melds]
        pair = Tile.from_schema(schema.pair)
        return cls(melds, pair)
