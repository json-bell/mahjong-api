from .hand import Hand
from .player import Player
from .exceptions import InvalidGameError
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Game:
    created_at: datetime | None = None
    players: list[Player] | None = None
    hands: list[Hand] | None = field(default_factory=list)

    def __post_init__(self):
        self._validate()

    def _validate(self):
        if not (self.players is None or len(self.players) == 4):
            raise InvalidGameError(
                f"Invalid number of players: {len(self.players)}", players=self.players
            )
