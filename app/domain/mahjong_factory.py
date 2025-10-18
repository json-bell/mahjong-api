from typing import List
from app.domain.tile import Tile
from app.domain.meld import Meld
from app.domain.hand import Hand
from app.domain.enums import (
    Suit,
    WindValue,
    DragonValue,
    NumberValue,
    MeldType,
    TileValue,
)
from app.domain.exceptions import InvalidHandError, InvalidMeldError, InvalidTileError


class MahjongFactory:
    @classmethod
    def tile_from_short(cls, code: str) -> Tile:
        """
        Generates a Tile from a string encoding, e.g.
        "Ba6" -> 6 of Bamboo
        "DrG" -> Green Dragon
        "WiN" -> North Wind

        For internal use e.g. for making tests
        """
        code = code.strip()
        suit_code = code[:2].capitalize()
        value_code = code[2:].upper()

        # Map two-letter codes to Suit enum
        SUIT_MAP = {
            "Ba": Suit.BAMBOO,
            "Ch": Suit.CHARACTER,
            "Ci": Suit.CIRCLE,
            "Wi": Suit.WIND,
            "Dr": Suit.DRAGON,
        }

        DRAGON_VALUE_MAP = {
            "R": DragonValue.RED,
            "G": DragonValue.GREEN,
            "W": DragonValue.WHITE,
        }
        WIND_VALUE_MAP = {
            "E": WindValue.EAST,
            "N": WindValue.NORTH,
            "S": WindValue.SOUTH,
            "W": WindValue.WEST,
        }

        if suit_code not in SUIT_MAP:
            raise InvalidTileError(f"Invalid suit code: {suit_code}")

        suit = SUIT_MAP[suit_code]
        value: TileValue

        if suit == Suit.WIND:
            value = WIND_VALUE_MAP[value_code]
        elif suit == Suit.DRAGON:
            value = DRAGON_VALUE_MAP[value_code]
        else:
            value = NumberValue(value_code)

        return Tile(suit, value)

    @classmethod
    def meld_from_short(cls, code: str) -> Meld:
        code = code.strip()
        type_code = code[:1].upper()
        tile_code = code[1:]

        TYPE_MAP = {"P": MeldType.PONG, "C": MeldType.CHOW, "K": MeldType.KONG}

        if type_code not in TYPE_MAP:
            raise InvalidMeldError(f"Invalid meld type code: {type_code}")

        type = TYPE_MAP[type_code]

        return Meld(type, tile=cls.tile_from_short(tile_code))

    @classmethod
    def hand_from_short(cls, melds: List[str], pair: str) -> Hand:
        if len(melds) != 4:
            raise InvalidHandError(f"Invalid meld length: {str(melds)}")

        return Hand(
            melds=[cls.meld_from_short(meld_code) for meld_code in melds],
            pair=cls.tile_from_short(pair),
        )
