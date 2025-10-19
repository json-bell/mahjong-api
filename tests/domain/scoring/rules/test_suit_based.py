from app.domain.scoring.engine import ScoringEngine
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand
import pytest


@pytest.mark.parametrize(
    "melds, pair, expected_slug, expected_score",
    [
        (["CCi2", "CCi4", "PWiE", "PCi8"], "DrG", RuleSlug.HALF_FLUSH, 3),
        (["CCi2", "CCi4", "PCi9", "PCi8"], "DrG", RuleSlug.HALF_FLUSH, 3),
        (["CCi2", "CCi4", "PCi9", "PCi8"], "Ci3", RuleSlug.FULL_FLUSH, 6),
    ],
)
def test_basic_rules(melds, pair, expected_slug, expected_score):
    hand = Hand.from_short(melds=melds, pair=pair)
    engine = ScoringEngine()
    score = engine.score_hand(hand)
    explanation = engine.explain_hand(hand)

    assert score == expected_score
    slugs = [rule["slug"] for rule in explanation]
    assert [expected_slug] == slugs
