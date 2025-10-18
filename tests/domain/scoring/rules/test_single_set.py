from app.domain.scoring.engine import ScoringEngine
from app.domain.scoring.enums import RuleSlug
from app.domain.hand import Hand
import pytest


@pytest.mark.parametrize(
    "melds, pair, expected_slug, expected_score",
    [
        (["CCi2", "CCi4", "CBa3", "CBa6"], "DrG", RuleSlug.ALL_CHOWS, 1),
        (["PCi2", "PCi4", "PBa3", "PBa6"], "DrG", RuleSlug.ALL_PUNGS, 3),
        (["PCi2", "KCi4", "PBa3", "KBa6"], "DrG", RuleSlug.ALL_PUNGS, 3),
        # TODO - superceding logic # (["KCi2", "KCi4", "KBa3", "KBa6"], "DrG", RuleSlug.ALL_KONGS, 13),
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
