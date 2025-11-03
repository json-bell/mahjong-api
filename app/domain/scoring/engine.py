from .rule import RULES, ScoringRule
from .types import RuleExplanation
from ..hand import Hand

# Registers all rules
from . import rules  # noqa: F401


class ScoringEngine:
    def __init__(self):
        self.rules = RULES

    def applied_rules(self, hand: Hand) -> list[ScoringRule]:
        matched_rules = [r for r in RULES.values() if r.matches(hand)]

        active_slugs = {r.slug for r in matched_rules}
        for rule in matched_rules:
            for superseded in rule.supersedes:
                active_slugs.discard(superseded)

        return [r for r in matched_rules if r.slug in active_slugs]

    def superseded_rules(self, hand: Hand) -> list[ScoringRule]:
        matched_rules = [r for r in RULES.values() if r.matches(hand)]
        superseded_slugs = {s for r in matched_rules for s in r.supersedes}
        superseded_rules = [r for r in matched_rules if r.slug in superseded_slugs]
        return superseded_rules

    def score_hand(self, hand: Hand) -> int:
        applied_rules = self.applied_rules(hand)

        total_score = sum(r.score_fan(hand, matched=True) for r in applied_rules)
        return total_score

    def explain_hand(self, hand: Hand) -> list[RuleExplanation]:
        return [
            {
                "slug": rule.slug,
                "name": rule.slug.value.replace("_", " ").title(),
                "score": rule.score_value,
                "description": rule.description,
            }
            for rule in self.applied_rules(hand)
        ]
