from app.domain.scoring.rule import RULES
from app.domain.hand import Hand

# Registers all rules
import app.domain.scoring.rules  # noqa: F401


class ScoringEngine:
    def __init__(self):
        self.rules = RULES

    def score_hand(self, hand: Hand) -> int:
        return sum(rule.score(hand) for rule in self.rules.values())

    def explain_hand(self, hand: Hand):
        return [
            {
                "slug": rule.slug.value,
                "value": rule.score_value,
                "description": rule.description,
            }
            for rule in self.rules.values()
            if rule.matches(hand)
        ]
