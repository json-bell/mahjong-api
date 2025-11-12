from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List
from .hand import ScoredHandOutSchema


class GameCreateSchema(BaseModel):
    # wip # east_player: PlayerSlot = PlayerSlot.FIRST
    # wip # round_wind: WindValue = WindValue.EAST
    pass


class GameOutSchema(BaseModel):
    id: int
    created_at: Optional[datetime]
    # wip # round_wind: WindValue = WindValue.EAST
    # wip # east_player: int

    model_config = ConfigDict(from_attributes=True)


class GameDetailSchema(GameOutSchema):
    hands: List[ScoredHandOutSchema]
    # wip #players: List[PlayerOutSchema]
