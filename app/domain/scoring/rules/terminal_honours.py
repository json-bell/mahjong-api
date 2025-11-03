from ..rule import ScoringRule, register_rule
from ..enums import RuleSlug
from ...hand import Hand
from ...enums import Suit, NumberValue


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


class LittleThreeDragonsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.LITTLE_THREE_DRAGONS,
            description="Hand has two dragon pungs and a pair of the third dragon.",
            score_value=4,
            supersedes=[RuleSlug.DRAGON_PUNG],
        )

    def matches(self, hand: Hand) -> bool:
        if hand.pair.suit != Suit.DRAGON:
            return False

        dragonPungs = [meld for meld in hand.melds if meld.tile.suit == Suit.DRAGON]
        return len(dragonPungs) == 2


register_rule(LittleThreeDragonsRule())


class BigThreeDragonsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.BIG_THREE_DRAGONS,
            description="Hand has three dragon pungs.",
            score_value=13,
            supersedes=[
                RuleSlug.DRAGON_PUNG,
                RuleSlug.ALL_PUNGS,
                RuleSlug.ALL_KONGS,
                RuleSlug.FULL_FLUSH,
                RuleSlug.HALF_FLUSH,
            ],
        )

    def matches(self, hand: Hand) -> bool:
        dragonPungs = [meld for meld in hand.melds if meld.tile.suit == Suit.DRAGON]
        return len(dragonPungs) == 3


register_rule(BigThreeDragonsRule())


class LittleFourWindsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.LITTLE_FOUR_WINDS,
            description="Hand has three pungs and a pair of winds.",
            score_value=13,
            supersedes=[
                RuleSlug.ALL_PUNGS,
                RuleSlug.ALL_KONGS,
                RuleSlug.FULL_FLUSH,
                RuleSlug.HALF_FLUSH,
            ],
        )

    def matches(self, hand: Hand) -> bool:
        if hand.pair.suit != Suit.WIND:
            return False

        windPungs = [meld for meld in hand.melds if meld.tile.suit == Suit.WIND]
        return len(windPungs) == 3


register_rule(LittleFourWindsRule())


class BigFourWindsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.BIG_FOUR_WINDS,
            description="Hand has four pungs of winds.",
            score_value=13,
            supersedes=[
                RuleSlug.ALL_PUNGS,
                RuleSlug.ALL_KONGS,
                RuleSlug.FULL_FLUSH,
                RuleSlug.HALF_FLUSH,
            ],
        )

    def matches(self, hand: Hand) -> bool:
        windPungs = [meld for meld in hand.melds if meld.tile.suit == Suit.WIND]
        return len(windPungs) == 4


register_rule(BigFourWindsRule())


class AllHonoursRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.ALL_HONORS,
            description="Hand consists only of honor tiles.",
            score_value=13,
            supersedes=[
                RuleSlug.ALL_PUNGS,
                RuleSlug.ALL_KONGS,
                RuleSlug.FULL_FLUSH,
                RuleSlug.HALF_FLUSH,
                RuleSlug.LITTLE_THREE_DRAGONS,
                RuleSlug.BIG_THREE_DRAGONS,
                RuleSlug.LITTLE_FOUR_WINDS,
                RuleSlug.BIG_FOUR_WINDS,
            ],
        )

    def matches(self, hand: Hand) -> bool:
        suits = set(hand.suits)
        return suits.isdisjoint({Suit.BAMBOO, Suit.CHARACTER, Suit.CIRCLE})


register_rule(AllHonoursRule())


class AllTerminalsRule(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.ALL_TERMINALS,
            description="Hand consists only of terminals.",
            score_value=13,
            supersedes=[
                RuleSlug.ALL_PUNGS,
                RuleSlug.ALL_KONGS,
                RuleSlug.FULL_FLUSH,
                RuleSlug.HALF_FLUSH,
            ],
        )

    def matches(self, hand: Hand) -> bool:
        values = {meld.tile.value for meld in hand.melds}
        return values.issubset({NumberValue.ONE, NumberValue.NINE})


register_rule(AllTerminalsRule())
