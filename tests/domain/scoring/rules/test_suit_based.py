from app.domain.scoring.engine import ScoringEngine
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand
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
    explanation = engine.explain_hand(hand)

    assert score == expected_score
    slugs = [rule["slug"] for rule in explanation]
    assert [expected_only_slug] == slugs


@pytest.mark.parametrize(
    "melds, pair, expected_slug, expected_not_slug",
    [
        # Pair is considered in full v half flush
        (["CCi2", "CCi4", "PCi9", "PCi8"], "DrR", RuleSlug.HALF_FLUSH, RuleSlug.FULL_FLUSH),
        # Green Dragon pair isn't sufficient for Jade Dragon
        (["PBa2", "PBa4", "PBa7", "PBa8"], "DrG", RuleSlug.HALF_FLUSH, RuleSlug.JADE_DRAGON),
        # Green Dragon requires Pongs
        (["PBa2", "CBa4", "PDrG", "PBa8"], "Ba3", RuleSlug.HALF_FLUSH, RuleSlug.JADE_DRAGON),
        # Other Dragons can't be included in Jade Dragon
        (["PBa2", "PDrG", "PDrR", "PBa8"], "Ba3", RuleSlug.HALF_FLUSH, RuleSlug.JADE_DRAGON),
    ],
)
def test_set_rule_fails(melds, pair, expected_slug, expected_not_slug):
    hand = Hand.from_short(melds=melds, pair=pair)
    engine = ScoringEngine()
    explanation = engine.explain_hand(hand)

    slugs = [rule["slug"] for rule in explanation]
    assert expected_not_slug not in slugs
    assert expected_slug in slugs
