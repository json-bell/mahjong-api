from app.domain.enums import MeldType, NumberValue
from app.domain.tile import Tile


class Meld:
    def __init__(self, type: MeldType, tile: Tile):
        self.type = type
        self.tile = tile  # the first tile of the meld - for chows this is the lowest tile, for pongs and kongs this is any tile
        self._validate()

    @property
    def label(self):
        if self.type != MeldType.CHOW:
            return f"{self.tile.label} {self.type.label}"
        if not isinstance(self.type, MeldType):
            raise TypeError("type must be a MeldType enum")
        else:
            return f"{self.tile.chow_sequence} {self.tile.suit.label} Chow"

    def _validate(self):
        tile = self.tile
        type = self.type

        if not isinstance(self.tile, Tile):
            raise TypeError("The tile must be a Tile instance")
        if type == MeldType.CHOW:
            if tile.value in (NumberValue.EIGHT, NumberValue.NINE):
                raise ValueError(
                    "Chow's value is the lowest number value (7-8-9 is recorded as 7)"
                )
            elif tile.is_honour:
                raise ValueError("Honour tiles cannot form chows")
