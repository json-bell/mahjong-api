from typing import List
from pydantic import BaseModel
from app.schemas.meld import MeldSchema
from app.schemas.tile import TileSchema


class HandSchema(BaseModel):
    melds: List[MeldSchema]
    pair: TileSchema
