from app.domain.hand import Hand
from app.domain.scoring.types import RuleExplanation
from app.domain.scoring.engine import ScoringEngine
from typing import TypedDict


class HandScoreExplanation(TypedDict):
    score: int
    explanation: list[RuleExplanation]


class ScoringService:
    def __init__(self):
        self.engine = ScoringEngine()

    def calculate_and_explain(self, hand: Hand) -> HandScoreExplanation:
        score = self.engine.score_hand(hand)
        explanation = self.engine.explain_hand(hand)
        return {"score": score, "explanation": explanation}
