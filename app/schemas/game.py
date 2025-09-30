from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List
from app.schemas.hand import HandOutSchema


class GameCreateSchema(BaseModel):
    pass


class GameOutSchema(BaseModel):
    id: int
    created_at: Optional[datetime] = None
    # wip # score: int
    # wip # round_wind: WindValue = WindValue.EAST
    # wip # east_player: int

    model_config = ConfigDict(from_attributes=True)


class GameDetailSchema(GameOutSchema):
    hands: List[HandOutSchema]
    # wip # players: List[Player]
