from app.domain.scoring.rule import ScoringRule, register_rule
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand
from app.domain.enums import Suit


class DragonPungRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.DRAGON_PUNG,
            description="Hand includes a pung (or kong) of dragons.",
            score_value=1,
        )

    def matches(self, hand: Hand) -> bool:
        return any(meld.tile.suit == Suit.DRAGON for meld in hand.melds)

    def score_fan(self, hand: Hand, matched: bool | None = None) -> int:
        return len([meld for meld in hand.melds if meld.tile.suit == Suit.DRAGON])


register_rule(DragonPungRule())
