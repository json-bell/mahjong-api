from app.domain.enums import MeldType, NumberValue
from app.domain.tile import Tile
from app.schemas.meld import MeldSchema
from app.domain.exceptions import InvalidTileError, InvalidMeldError


class Meld:
    def __init__(self, type: MeldType, tile: Tile):
        self.type = type
        self.tile = tile  # the first tile of the meld
        # for chows this is the lowest tile, for pongs and kongs this is any tile
        self._validate()

    @property
    def label(self):
        if self.type != MeldType.CHOW:
            return f"{self.tile.label} {self.type.label}"
        if not isinstance(self.type, MeldType):
            raise InvalidMeldError(
                f"Meld type must have a value in {MeldType.values()}", type=self.type
            )
        else:
            return f"{self.tile.chow_sequence} {self.tile.suit.label} Chow"

    def _validate(self):
        tile = self.tile
        type = self.type

        if not isinstance(self.tile, Tile):
            raise InvalidTileError("Tile is missing suit or value.", tile=tile)

        if type == MeldType.CHOW:
            if tile.value in (NumberValue.EIGHT, NumberValue.NINE):
                raise InvalidMeldError(
                    "A chow's value is the lowest number value (7-8-9 is recorded as 7).",
                    meld=self,
                )
            elif tile.is_honour:
                raise InvalidMeldError("Honour tiles cannot form chows.", meld=self)

    def to_dict(self):
        return {"type": self.type.value, "tile": self.tile.to_dict()}

    @classmethod
    def from_schema(cls, schema: MeldSchema) -> "Meld":
        return cls(schema.type, Tile.from_schema(schema.tile))

    @classmethod
    def from_short(cls, code: str):
        from app.domain.mahjong_factory import MahjongFactory

        return MahjongFactory.meld_from_short(code)
