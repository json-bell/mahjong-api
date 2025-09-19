from app.models import Hand


def calculate_hand_score(hand: Hand):
    pair = hand.pair
    handStr = f"Your hand has: {', '.join([f'a {meld.type} of {meld.tile.value} {meld.tile.suit}' for meld in hand.melds])}\n and a pair of {pair.value} {pair.suit}"
    return {"hand": handStr}
