from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List
from .hand import ScoredHandOutSchema
from .player import PlayerOutSchema, PlayerCreateSchema


class GameCreateSchema(BaseModel):
    players: Optional[list[PlayerCreateSchema]] = None
    # wip # east_player: PlayerSlot = PlayerSlot.FIRST
    # wip # round_wind: WindValue = WindValue.EAST

    model_config = ConfigDict(from_attributes=True)


class GameOutSchema(BaseModel):
    id: int
    created_at: Optional[datetime]
    # wip # round_wind: WindValue = WindValue.EAST
    # wip # east_player: int

    model_config = ConfigDict(from_attributes=True)


class GameDetailSchema(GameOutSchema):
    hands: List[ScoredHandOutSchema]
    players: List[PlayerOutSchema]
