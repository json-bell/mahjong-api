from enum import Enum, unique
from typing import Union


class LabelledEnum(str, Enum):
    @classmethod
    def values(cls):
        return [v.value for v in cls]

    @property
    def label(self):
        return self.value.capitalize()


@unique
class Suit(LabelledEnum):
    CIRCLE = "circle"
    BAMBOO = "bamboo"
    CHARACTER = "character"
    WIND = "wind"
    DRAGON = "dragon"


@unique
class NumberValue(LabelledEnum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"

    @property
    def number(self):
        return int(self.value)


@unique
class WindValue(LabelledEnum):
    EAST = "east"
    SOUTH = "south"
    WEST = "west"
    NORTH = "north"


@unique
class DragonValue(LabelledEnum):
    RED = "red"
    GREEN = "green"
    WHITE = "white"


TileValue = Union[NumberValue, WindValue, DragonValue]


def parse_tile_value(value: str) -> TileValue:
    for enum_cls in (NumberValue, WindValue, DragonValue):
        try:
            return enum_cls(value)
        except ValueError:
            continue
    raise ValueError(f"{value} is not a valid TileA, TileB, or TileC value")


@unique
class MeldType(LabelledEnum):
    CHOW = "chow"
    PONG = "pong"
    KONG = "kong"


@unique
class PlayerSlot(int, Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
