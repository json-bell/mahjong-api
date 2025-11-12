from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from .meld import MeldSchema
from .tile import TileSchema
from app.domain import PlayerSlot


class HandSchema(BaseModel):
    melds: List[MeldSchema]
    pair: TileSchema

    model_config = ConfigDict(from_attributes=True)


class ScoredHandCreateSchema(BaseModel):
    hand: HandSchema
    player_slot: PlayerSlot
    game_id: int

    model_config = ConfigDict(from_attributes=True)


class ScoredHandOutSchema(ScoredHandCreateSchema):
    id: int
    created_at: Optional[datetime]
    score: int
