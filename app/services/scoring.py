from app.domain.hand import Hand


def calculate_hand_score(hand: Hand):
    return {
        "description": hand.label,
        "chow_count": hand.chow_count,
        "score": "implementation pending",
    }
