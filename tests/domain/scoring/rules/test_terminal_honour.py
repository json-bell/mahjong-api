from app.domain.scoring.engine import ScoringEngine
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand
import pytest


@pytest.mark.parametrize(
    "melds, pair, expected_only_slug, expected_score",
    [
        (["CCi2", "CBa4", "PBa3", "PDrR"], "Ch3", RuleSlug.DRAGON_PUNG, 1),
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
