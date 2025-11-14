from .scored_hand import ScoredHand
from .player import Player
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Game:
    created_at: datetime | None = None
    players: list[Player] | None = None
    hands: list[ScoredHand] | None = field(default_factory=list)
