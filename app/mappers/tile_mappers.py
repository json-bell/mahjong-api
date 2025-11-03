from app.domain import Tile
from app.schemas.tile import TileSchema
from app.domain.enums import Suit, WindValue, DragonValue, NumberValue, TileValue
from app.domain.exceptions import InvalidTileError


class TileMapper:
    @staticmethod
    def to_dict(tile: Tile):
        return {"suit": tile.suit.value, "tile": tile.value.value}

    @staticmethod
    def from_schema(schema: TileSchema) -> Tile:
        return Tile(schema.suit, schema.value)

    @staticmethod
    def from_short(code: str) -> Tile:
        """
        Generates a Tile from a string encoding, e.g.
        "Ba6" -> 6 of Bamboo
        "DrG" -> Green Dragon
        "WiN" -> North Wind

        to_dict is the standard serialisation - from_short is used
        in tests & example hands
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
