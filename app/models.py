from pydantic import BaseModel, model_validator
from typing import Literal, List, get_args

# All allowed suits
Suit = Literal["circle", "bamboo", "character", "wind", "dragon"]

# Allowed values
NumberValue = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
WindValue = Literal["east", "south", "west", "north"]
DragonValue = Literal["red", "green", "white"]


class Tile(BaseModel):
    suit: Suit
    value: NumberValue | WindValue | DragonValue

    def is_honor(self) -> bool:
        return self.suit == "honor"

    @model_validator(mode="after")  # runs after model is initialized
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


# --- Hand model ---
class Hand(BaseModel):
    tiles: List[Tile]  # List of Tile objects
    win_type: str  # "ron" or "tsumo"
