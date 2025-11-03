from pydantic import BaseModel
from app.domain import Suit, TileValue


class TileSchema(BaseModel):
    suit: Suit
    value: TileValue
