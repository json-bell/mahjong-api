from app.domain import Meld, MeldType, InvalidMeldError
from .tile_mappers import TileMapper
from app.schemas.meld import MeldSchema


class MeldMapper:
    @staticmethod
    def to_dict(meld: Meld):
        return {"type": meld.type.value, "tile": TileMapper.to_dict(meld.tile)}

    @staticmethod
    def from_schema(schema: MeldSchema) -> Meld:
        return Meld(schema.type, TileMapper.from_schema(schema.tile))

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
