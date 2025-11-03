from pydantic import BaseModel
from .tile import TileSchema
from app.domain import MeldType


class MeldSchema(BaseModel):
    type: MeldType
    tile: TileSchema
