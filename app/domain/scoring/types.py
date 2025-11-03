from typing import TypedDict
from .enums import RuleSlug


class RuleExplanation(TypedDict):
    slug: RuleSlug
    name: str
    score: int
    description: str
