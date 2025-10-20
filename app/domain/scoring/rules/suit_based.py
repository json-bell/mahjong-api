from app.domain.scoring.rule import ScoringRule, register_rule
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand
from app.domain.enums import Suit, DragonValue, MeldType


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


class JadeDragon(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.JADE_DRAGON,
            description="Hand is composed of pungs (or kongs) of bamboo tiles and a pung of green dragons.",
            score_value=13,
            supersedes=[RuleSlug.HALF_FLUSH, RuleSlug.ALL_PUNGS, RuleSlug.ALL_KONGS],
        )

    def matches(self, hand: Hand) -> bool:
        suits = set(hand.suits)
        # Suits are Bamboo & Dragon
        if suits != {Suit.BAMBOO, Suit.DRAGON}:
            return False

        # Dragon melds are exactly Green Dragon
        dragon_meld_values = [
            meld.tile.value for meld in hand.melds if meld.tile.suit == Suit.DRAGON
        ]
        if dragon_meld_values != [DragonValue.GREEN]:
            return False

        if any(meld.type == MeldType.CHOW for meld in hand.melds):
            return False

        # Pair is bamboo
        if hand.pair.suit != Suit.BAMBOO:
            return False

        return True


register_rule(JadeDragon())


class RubyDragon(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.RUBY_DRAGON,
            description="Hand is composed of pungs (or kongs) of character tiles and a pung of red dragons.",
            score_value=13,
            supersedes=[RuleSlug.HALF_FLUSH, RuleSlug.ALL_PUNGS, RuleSlug.ALL_KONGS],
        )

    def matches(self, hand: Hand) -> bool:
        suits = set(hand.suits)
        # Suits are Character & Dragon
        if suits != {Suit.CHARACTER, Suit.DRAGON}:
            return False

        # Dragon melds are exactly Green Dragon
        dragon_meld_values = [
            meld.tile.value for meld in hand.melds if meld.tile.suit == Suit.DRAGON
        ]
        if dragon_meld_values != [DragonValue.RED]:
            return False

        if any(meld.type == MeldType.CHOW for meld in hand.melds):
            return False

        # Pair is Character
        if hand.pair.suit != Suit.CHARACTER:
            return False

        return True


register_rule(RubyDragon())


class PearlDragon(ScoringRule):
    def __init__(self):
        super().__init__(
            slug=RuleSlug.PEARL_DRAGON,
            description="Hand is composed of pungs (or kongs) of circle tiles and a pung of white dragons.",
            score_value=13,
            supersedes=[RuleSlug.HALF_FLUSH, RuleSlug.ALL_PUNGS, RuleSlug.ALL_KONGS],
        )

    def matches(self, hand: Hand) -> bool:
        suits = set(hand.suits)
        # Suits are Circle & Dragon
        if suits != {Suit.CIRCLE, Suit.DRAGON}:
            return False

        # Dragon melds are exactly Green Dragon
        dragon_meld_values = [
            meld.tile.value for meld in hand.melds if meld.tile.suit == Suit.DRAGON
        ]
        if dragon_meld_values != [DragonValue.WHITE]:
            return False

        if any(meld.type == MeldType.CHOW for meld in hand.melds):
            return False

        # Pair is Circle
        if hand.pair.suit != Suit.CIRCLE:
            return False

        return True


register_rule(PearlDragon())
