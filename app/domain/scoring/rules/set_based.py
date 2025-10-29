from app.domain.scoring.rule import ScoringRule, register_rule
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand


class AllPungsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.ALL_PUNGS,
            description="Hand consists of all pungs.",
            score_value=3,
        )

    def matches(self, hand: Hand) -> bool:
        return all(meld.type != "chow" for meld in hand.melds)


register_rule(AllPungsRule())


class AllChowsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.ALL_CHOWS,
            description="Hand consists only of chows and a pair of suit tiles.",
            score_value=1,
        )

    def matches(self, hand: Hand) -> bool:
        if hand.pair.is_honour:
            return False
        return all(meld.type == "chow" for meld in hand.melds)


register_rule(AllChowsRule())


class AllKongsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.ALL_KONGS,
            description="Hand has four kongs and a pair.",
            score_value=13,
            supersedes=[RuleSlug.ALL_PUNGS],
        )

    def matches(self, hand: Hand) -> bool:
        return all(meld.type == "kong" for meld in hand.melds)


register_rule(AllKongsRule())
