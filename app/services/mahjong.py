from app.models import Hand


def calculate_hand_score(hand: Hand):
    return {
        "description": hand.describe(),
        "chow_count": hand.chowCount(),
        "score": "implementation pending",
    }
