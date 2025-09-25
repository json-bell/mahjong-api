from app.domain.enums import (
    Suit,
    TileValue,
    NumberValue,
    DragonValue,
    WindValue,
)


class Tile:
    def __init__(self, suit: Suit, value: TileValue):
        self.suit = suit
        self.value = value
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
        if self.value in (NumberValue.EIGHT, NumberValue.NINE):
            raise ValueError(f"Chows cannot be made starting from {self.value.number}")
        if self.is_honour:
            raise ValueError("Honour tiles cannot form chows")

        return "-".join([str(i + self.value.number) for i in [0, 1, 2]])

    def _validate(self):
        suit = self.suit
        value = self.value

        if not isinstance(suit, Suit):
            raise TypeError("suit must be a Suit enum")
        if suit == Suit.WIND and not isinstance(value, WindValue):
            raise ValueError(f"Wind suit tiles must have value in {WindValue.values()}")
        elif suit == Suit.DRAGON and not isinstance(value, DragonValue):
            raise ValueError(
                f"Dragon suit tiles must have value in {DragonValue.values()}"
            )
        elif suit in (Suit.BAMBOO, Suit.CHARACTER, Suit.CIRCLE) and not isinstance(
            value, NumberValue
        ):
            raise ValueError(
                f"{suit.label} suit tiles must have value in {NumberValue.values()}"
            )
