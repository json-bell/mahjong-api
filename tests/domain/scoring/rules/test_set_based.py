from app.domain.scoring.engine import ScoringEngine
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand
import pytest


@pytest.mark.parametrize(
    "melds, pair, expected_only_slug, expected_score",
    [
        (["CCi2", "CCi4", "CBa3", "CBa6"], "Ch3", RuleSlug.ALL_CHOWS, 1),
        (["PCi2", "PCi4", "PBa3", "PBa6"], "DrG", RuleSlug.ALL_PUNGS, 3),
        (["PCi2", "KCi4", "PBa3", "KBa6"], "DrG", RuleSlug.ALL_PUNGS, 3),
        (["KCi2", "KCi4", "KBa3", "KBa6"], "DrG", RuleSlug.ALL_KONGS, 13),
    ],
)
def test_basic_rules(melds, pair, expected_only_slug, expected_score):
    hand = Hand.from_short(melds=melds, pair=pair)
    engine = ScoringEngine()
    score = engine.score_hand(hand)
    applied_rules = engine.applied_rules(hand)

    assert score == expected_score
    slugs = [rule.slug for rule in applied_rules]
    assert [expected_only_slug] == slugs


def test_all_kongs_rule():
    hand = Hand.from_short(
        melds=[
            "KCi2",
            "KCi4",
            "KBa3",
            "KBa6",
        ],
        pair="DrR",
    )
    engine = ScoringEngine()
    score = engine.score_hand(hand)
    applied_rules = engine.applied_rules(hand)
    slugs = [rule.slug for rule in applied_rules]

    assert RuleSlug.ALL_PUNGS not in slugs
    assert [RuleSlug.ALL_KONGS] == slugs
    assert score == 13


def test_all_chows_requires_suit_pair():
    hand = Hand.from_short(melds=["CCi2", "CCi4", "CBa3", "CBa6"], pair="DrG")
    engine = ScoringEngine()
    score = engine.score_hand(hand)
    applied_rules = engine.applied_rules(hand)
    slugs = [rule.slug for rule in applied_rules]

    assert RuleSlug.ALL_CHOWS not in slugs
    assert score == 0
