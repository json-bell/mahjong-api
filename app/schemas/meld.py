from pydantic import BaseModel
from app.schemas.tile import TileSchema
from app.domain import MeldType


class MeldSchema(BaseModel):
    type: MeldType
    tile: TileSchema
