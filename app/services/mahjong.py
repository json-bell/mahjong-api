def calculate_hand_score(tiles, win_type):
    """
    Placeholder scoring logic:
    - 1 fan per 3 tiles
    - 1000 points per fan
    """
    fan = len(tiles) // 3
    points = fan * 1000
    return {
        "fan": fan,
        "points": points,
        "tiles": tiles,
        "win_type": win_type
    }