from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List
from .enums import RuleSlug
from app.domain.hand import Hand


@dataclass(frozen=True)
class ScoringRule(ABC):
    slug: RuleSlug
    description: str
    score_value: int
    supersedes: List[RuleSlug] = field(default_factory=list)

    @abstractmethod
    def matches(self, hand: Hand) -> bool:
        """Check whether this rule applies to the hand."""
        raise NotImplementedError

    def score_fan(self, hand: Hand, matched: bool | None = None) -> int:
        if matched is None:
            matched = self.matches(hand)
        return self.score_value if matched else 0


RULES: Dict[RuleSlug, ScoringRule] = {}


def register_rule(rule: ScoringRule):
    """Registers a rule to the RULES dict"""
    RULES[rule.slug] = rule
    return rule
