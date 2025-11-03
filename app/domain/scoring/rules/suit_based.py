from ..rule import ScoringRule, register_rule
from ..enums import RuleSlug
from ...hand import Hand
from ...enums import Suit, DragonValue, MeldType


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


class DragonSuitRule(ScoringRule):
    def __init__(self, slug, description, suit, dragon_value):
        super().__init__(
            slug=slug,
            description=description,
            score_value=13,
            supersedes=[
                RuleSlug.HALF_FLUSH,
                RuleSlug.ALL_PUNGS,
                RuleSlug.ALL_KONGS,
                RuleSlug.DRAGON_PUNG,
            ],
        )
        self.suit = suit
        self.dragon_value = dragon_value

    def matches(self, hand: Hand) -> bool:
        suits = set(hand.suits)
        if suits != {self.suit, Suit.DRAGON}:
            return False

        dragon_meld_values = [
            meld.tile.value for meld in hand.melds if meld.tile.suit == Suit.DRAGON
        ]
        if dragon_meld_values != [self.dragon_value]:
            return False

        if any(meld.type == MeldType.CHOW for meld in hand.melds):
            return False

        if hand.pair.suit != self.suit:
            return False

        return True


class JadeDragonRule(DragonSuitRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.JADE_DRAGON,
            description="Hand is composed of pungs (or kongs) of bamboo tiles and a pung of green dragons.",
            suit=Suit.BAMBOO,
            dragon_value=DragonValue.GREEN,
        )


register_rule(JadeDragonRule())


class RubyDragonRule(DragonSuitRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.RUBY_DRAGON,
            description="Hand is composed of pungs (or kongs) of character tiles and a pung of red dragons.",
            suit=Suit.CHARACTER,
            dragon_value=DragonValue.RED,
        )


register_rule(RubyDragonRule())


class PearlDragonRule(DragonSuitRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.PEARL_DRAGON,
            description="Hand is composed of pungs (or kongs) of circle tiles and a pung of white dragons.",
            suit=Suit.CIRCLE,
            dragon_value=DragonValue.WHITE,
        )


register_rule(PearlDragonRule())
