from pydantic import BaseModel, ConfigDict
from app.domain import PlayerSlot


class PlayerCreateSchema(BaseModel):
    player_slot: PlayerSlot
    name: str
    game_id: int
    score: int = 0

    model_config = ConfigDict(from_attributes=True)


class PlayerOutSchema(PlayerCreateSchema):
    id: int
