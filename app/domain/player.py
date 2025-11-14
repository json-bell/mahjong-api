from dataclasses import dataclass
from .enums import PlayerSlot


@dataclass
class Player:
    name: str
    player_slot: PlayerSlot
    score: int = 0
