from pydantic import BaseModel, ConfigDict
from app.domain import PlayerIndex


class PlayerCreateSchema(BaseModel):
    player_index: PlayerIndex
    name: str
    game_id: int
    score: int = 0

    model_config = ConfigDict(from_attributes=True)


class PlayerOutSchema(PlayerCreateSchema):
    id: int
