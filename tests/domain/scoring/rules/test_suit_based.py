from app.domain.scoring.enums import RuleSlug
from app.domain import Hand, ScoringEngine
from app.domain.enums import DragonValue
import pytest


@pytest.mark.parametrize(
    "melds, pair, expected_only_slug, expected_score",
    [
        (["CCi2", "CCi4", "PWiE", "PCi8"], "DrG", RuleSlug.HALF_FLUSH, 3),
        (["CCi2", "CCi4", "PCi9", "PCi8"], "Ci3", RuleSlug.FULL_FLUSH, 6),
        (["PBa2", "PBa4", "PDrG", "PBa8"], "Ba3", RuleSlug.JADE_DRAGON, 13),
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


def test_pair_negates_full_flush():
    hand = Hand.from_short(melds=["CCi2", "CCi4", "PCi9", "PCi8"], pair="DrR")
    engine = ScoringEngine()
    explanation = engine.explain_hand(hand)

    slugs = [rule["slug"] for rule in explanation]
    assert RuleSlug.FULL_FLUSH not in slugs
    assert RuleSlug.HALF_FLUSH in slugs


# Jade / Ruby / Pearl dragon tests - checking various non-valid cases
CASES = [
    (RuleSlug.JADE_DRAGON, DragonValue.GREEN, "Ba", "G", "R"),
    (RuleSlug.RUBY_DRAGON, DragonValue.RED, "Ch", "R", "G"),
    (RuleSlug.PEARL_DRAGON, DragonValue.WHITE, "Ci", "W", "R"),
]
dragon_hand_params = pytest.mark.parametrize(
    "rule_slug, dragon_value, suit_code, dragon_code, diff_dragon_code", CASES
)


@dragon_hand_params
def test_dragon_pairs_are_not_sufficient(
    rule_slug, dragon_value, suit_code, dragon_code, diff_dragon_code
):
    hand = Hand.from_short(
        melds=[f"P{suit_code}2", f"P{suit_code}4", f"P{suit_code}7", f"P{suit_code}8"],
        pair=f"Dr{dragon_code}",
    )
    engine = ScoringEngine()
    slugs = [r.slug for r in engine.applied_rules(hand)]
    assert rule_slug not in slugs
    assert RuleSlug.HALF_FLUSH in slugs


@dragon_hand_params
def test_requires_all_pongs(rule_slug, dragon_value, suit_code, dragon_code, diff_dragon_code):
    hand = Hand.from_short(
        melds=[f"P{suit_code}2", f"C{suit_code}4", f"PDr{dragon_code}", f"P{suit_code}8"],
        pair=f"{suit_code}1",
    )
    engine = ScoringEngine()
    slugs = [r.slug for r in engine.applied_rules(hand)]
    assert rule_slug not in slugs
    assert RuleSlug.HALF_FLUSH in slugs


@dragon_hand_params
def test_other_dragons_not_allowed(rule_slug, dragon_value, suit_code, dragon_code, diff_dragon_code):
    hand = Hand.from_short(
        melds=[f"P{suit_code}2", f"P{suit_code}4", f"PDr{dragon_code}", f"PDr{diff_dragon_code}"],
        pair=f"{suit_code}1",
    )
    engine = ScoringEngine()
    slugs = [r.slug for r in engine.applied_rules(hand)]
    assert rule_slug not in slugs
    assert RuleSlug.HALF_FLUSH in slugs
    assert RuleSlug.ALL_PUNGS in slugs
