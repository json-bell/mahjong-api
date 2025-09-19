from pydantic import BaseModel, Field, model_validator
from typing import Literal, List, get_args

Suit = Literal["circle", "bamboo", "character", "wind", "dragon"]

NumberValue = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
WindValue = Literal["east", "south", "west", "north"]
DragonValue = Literal["red", "green", "white"]

MeldType = Literal["chow", "pong", "kong"]


class Tile(BaseModel):
    suit: Suit
    value: NumberValue | WindValue | DragonValue

    def is_honour(self) -> bool:
        return self.suit == "wind" or self.suit == "dragon"

    @model_validator(mode="after")
    def check_suit_value_combination(cls, tile: "Tile"):
        suit = tile.suit
        value = tile.value

        if suit == "wind":
            if value not in get_args(WindValue):
                raise ValueError(f"Wind suits must have value in {get_args(WindValue)}")
        elif suit == "dragon":
            if value not in get_args(DragonValue):
                raise ValueError(
                    f"Dragon suits must have value in {get_args(DragonValue)}"
                )
        else:
            if value not in get_args(NumberValue):
                raise ValueError(
                    f"{suit.capitalize} suit must have value in {get_args(NumberValue)}"
                )

        return tile


class Meld(BaseModel):
    type: MeldType
    tile: Tile  # the first tile of the meld - for chows this is the lowest tile, for pongs and kongs this is any tile

    @model_validator(mode="after")
    def check_meld(cls, meld: "Meld"):
        tile = meld.tile
        type = meld.type
        if type == "chow":
            if tile.value == "8" or tile.value == "9":
                raise ValueError(
                    "Chows should use the lowest tile value (789 should be recorded as 7)"
                )
            if tile.is_honour():
                raise ValueError("Honour tiles cannot form chows")
        return meld


class Hand(BaseModel):
    melds: List[Meld] = Field(..., min_length=4, max_length=4)
    pair: Tile
