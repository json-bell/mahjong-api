from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from app.schemas.meld import MeldSchema
from app.schemas.tile import TileSchema


class HandCreateSchema(BaseModel):
    melds: List[MeldSchema]
    pair: TileSchema
    game_id: int


class HandOutSchema(HandCreateSchema):
    id: int
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
