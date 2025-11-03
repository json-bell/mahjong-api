from app.domain.scoring.enums import RuleSlug
from app.domain import ScoringEngine
from app.mappers import HandMapper
import pytest


@pytest.mark.parametrize(
    "melds, pair, expected_only_slug, expected_score",
    [
        (["CCi2", "CBa4", "PBa3", "PDrR"], "Ch3", RuleSlug.DRAGON_PUNG, 1),
        (["CCi2", "CBa4", "PDrG", "PDrR"], "Ch3", RuleSlug.DRAGON_PUNG, 2),
        (["PDrW", "PDrR", "PBa4", "CCi6"], "DrG", RuleSlug.LITTLE_THREE_DRAGONS, 4),
        (["PDrW", "PDrR", "PDrG", "PBa6"], "Ba4", RuleSlug.BIG_THREE_DRAGONS, 13),
        (["PWiE", "PWiW", "PWiN", "PBa6"], "WiS", RuleSlug.LITTLE_FOUR_WINDS, 13),
        (["PWiE", "PWiW", "PWiN", "PWiS"], "Ba6", RuleSlug.BIG_FOUR_WINDS, 13),
        (["PWiE", "PWiW", "PDrG", "PDrW"], "DrR", RuleSlug.ALL_HONORS, 13),
        (["PBa1", "PBa9", "PCi1", "PCh1"], "Ch9", RuleSlug.ALL_TERMINALS, 13),
    ],
)
def test_basic_rules(melds, pair, expected_only_slug, expected_score):
    hand = HandMapper.from_short(melds=melds, pair=pair)
    engine = ScoringEngine()
    score = engine.score_hand(hand)
    applied_rules = engine.applied_rules(hand)

    assert score == expected_score
    slugs = [rule.slug for rule in applied_rules]
    assert [expected_only_slug] == slugs
