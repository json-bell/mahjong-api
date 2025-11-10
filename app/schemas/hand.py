from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from .meld import MeldSchema
from .tile import TileSchema
from app.domain import PlayerSlot


class HandCreateSchema(BaseModel):
    melds: List[MeldSchema]
    pair: TileSchema
    game_id: int
    player_slot: PlayerSlot

    model_config = ConfigDict(from_attributes=True)


class HandOutSchema(HandCreateSchema):
    id: int
    created_at: Optional[datetime] = None
    melds: List[MeldSchema]
    pair: TileSchema
