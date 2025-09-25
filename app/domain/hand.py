from typing import List
from app.domain.enums import MeldType
from app.domain.tile import Tile
from app.domain.meld import Meld
from app.schemas.hand import HandSchema


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
    def from_schema(cls, schema: HandSchema) -> "Hand":
        # Convert schema melds to domain Meld objects
        melds = [
            Meld(m.type, Tile(t.suit, t.value)) for m in schema.melds for t in [m.tile]
        ]
        # Convert pair to domain Tile
        pair = Tile(schema.pair.suit, schema.pair.value)
        return cls(melds, pair)
