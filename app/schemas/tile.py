from pydantic import BaseModel
from app.domain.enums import Suit, TileValue


class TileSchema(BaseModel):
    suit: Suit
    value: TileValue
