from app.domain import Meld, MeldType, InvalidMeldError
from .tile_mappers import TileMapper
from app.schemas import MeldSchema


class MeldMapper:
    @staticmethod
    def to_dict(meld: Meld) -> dict:
        return {"type": meld.type.value, "tile": TileMapper.to_dict(meld.tile)}

    @staticmethod
    def from_dict(dictionary: dict) -> Meld:
        return Meld(
            type=dictionary["type"], tile=TileMapper.from_dict(dictionary["tile"])
        )

    @staticmethod
    def from_schema(schema: MeldSchema) -> Meld:
        return Meld(schema.type, TileMapper.from_schema(schema.tile))

    @staticmethod
    def to_schema(meld: Meld) -> MeldSchema:
        return MeldSchema(type=meld.type, tile=TileMapper.to_schema(meld.tile))

    @staticmethod
    def from_short(code: str):
        code = code.strip()
        type_code = code[:1].upper()
        tile_code = code[1:]

        TYPE_MAP = {"P": MeldType.PONG, "C": MeldType.CHOW, "K": MeldType.KONG}

        if type_code not in TYPE_MAP:
            raise InvalidMeldError(f"Invalid meld type code: {type_code}")

        type = TYPE_MAP[type_code]

        return Meld(type, tile=TileMapper.from_short(tile_code))
