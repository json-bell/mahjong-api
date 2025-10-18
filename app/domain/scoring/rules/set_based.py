from app.domain.scoring.rule import ScoringRule, register_rule
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand


class AllPungsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.ALL_PUNGS,
            description="All melds are pungs.",
            score_value=3,
        )

    def matches(self, hand: Hand) -> bool:
        return all(meld.type != "chow" for meld in hand.melds)


register_rule(AllPungsRule())


class AllChowsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.ALL_CHOWS,
            description="All melds are chows.",
            score_value=1,
        )

    def matches(self, hand: Hand) -> bool:
        return all(meld.type == "chow" for meld in hand.melds)


register_rule(AllChowsRule())


class AllKongsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.ALL_KONGS,
            description="All melds are chows.",
            score_value=13,
        )

    def matches(self, hand: Hand) -> bool:
        return all(meld.type == "kong" for meld in hand.melds)

    # TODO MAH-19


register_rule(AllKongsRule())
