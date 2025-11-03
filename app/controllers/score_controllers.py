from fastapi import APIRouter
from typing import Dict
from app.domain import RuleSlug, ScoringRule, RULES


router = APIRouter(prefix="/score", tags=["hands"])


@router.get(
    "/rules",
    response_model=Dict[RuleSlug, ScoringRule],
    operation_id="read_scoring_rules",
)
def read_scoring_rules():
    return RULES
