from .hand import Hand
from .enums import PlayerSlot
from typing import Optional
from datetime import datetime
from dataclasses import dataclass


@dataclass
class ScoredHand:
    hand: Hand
    player_slot: PlayerSlot
    score: int
    created_at: Optional[datetime]
