from app.domain.scoring.rule import ScoringRule, register_rule
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand
from app.domain.enums import Suit


class HalfFlushRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.HALF_FLUSH,
            description="Hand consists only of honors and suit tiles of one suit.",
            score_value=3,
        )

    def matches(self, hand: Hand) -> bool:
        return len(set(hand.suits) & {Suit.BAMBOO, Suit.CHARACTER, Suit.CIRCLE}) == 1


register_rule(HalfFlushRule())


class FullFlushRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.FULL_FLUSH,
            description="Hand consists only of suit tiles of one suit.",
            score_value=6,
            supersedes=[RuleSlug.HALF_FLUSH],
        )

    def matches(self, hand: Hand) -> bool:
        suits = set(hand.suits)
        return (
            len(suits) == 1
            and len(suits & {Suit.BAMBOO, Suit.CHARACTER, Suit.CIRCLE}) == 1
        )


register_rule(FullFlushRule())
