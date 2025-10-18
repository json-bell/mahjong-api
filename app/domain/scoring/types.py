from typing import TypedDict
from app.domain.scoring.enums import RuleSlug


class RuleExplanation(TypedDict):
    slug: RuleSlug
    name: str
    score: int
    description: str
