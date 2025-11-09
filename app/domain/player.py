from dataclasses import dataclass
from .enums import PlayerIndex


@dataclass
class Player:
    name: str
    player_index: PlayerIndex
    score: int = 0
