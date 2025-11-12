from dataclasses import dataclass
from .enums import Suit, TileValue, NumberValue, DragonValue, WindValue
from .exceptions import InvalidTileError


@dataclass
class Tile:
    suit: Suit
    value: TileValue

    def __post_init__(self):
        self._validate()

    @property
    def is_honour(self) -> bool:
        return self.suit == Suit.WIND or self.suit == Suit.DRAGON

    @property
    def label(self):
        connector = "" if self.is_honour else " of"
        return f"{self.value.label}{connector} {self.suit.label}"

    @property
    def chow_sequence(self) -> str:
        if not isinstance(self.value, NumberValue):
            raise InvalidTileError("Honour tiles cannot form chows", tile=self)

        if self.value in (NumberValue.EIGHT, NumberValue.NINE):
            raise InvalidTileError("Chows must start from 1-7", tile=self)

        return "-".join([str(i + self.value.number) for i in [0, 1, 2]])

    def _validate(self):
        suit = self.suit
        value = self.value

        if not isinstance(suit, Suit):
            raise InvalidTileError(
                f"Suit must have value in {Suit.values()}", suit=suit
            )
        if suit == Suit.WIND and not isinstance(value, WindValue):
            raise InvalidTileError(
                f"Wind suit tiles must have value in {WindValue.values()}", tile=self
            )
        elif suit == Suit.DRAGON and not isinstance(value, DragonValue):
            raise InvalidTileError(
                f"Dragon suit tiles must have value in {DragonValue.values()}",
                tile=self,
            )
        elif suit in (Suit.BAMBOO, Suit.CHARACTER, Suit.CIRCLE) and not isinstance(
            value, NumberValue
        ):
            raise InvalidTileError(
                f"{suit.label} suit tiles must have value in {NumberValue.values()}",
                tile=self,
            )
