from app.domain.enums import LabelledEnum


class RuleSlug(LabelledEnum):
    # from http://mahjong.wikidot.com/rules:hong-kong-old-style-scoring
    # 1 fan
    NO_FLOWERS_AND_NO_SEASONS = "no_flowers_and_no_seasons"
    SEAT_FLOWER = "seat_flower"
    SEAT_SEASON = "seat_season"
    ALL_CHOWS = "all_chows"  # set-based
    DRAGON_PUNG = "dragon_pung"  # Terminals/Honors
    SEAT_WIND = "seat_wind"
    PREVALENT_WIND = "prevalent_wind"
    SELF_DRAWN_WIN = "self_drawn_win"
    LAST_TILE_DRAW = "last_tile_draw"
    LAST_TILE_DISCARD = "last_tile_discard"
    ROBBING_THE_KONG = "robbing_the_kong"
    OUT_ON_REPLACEMENT = "out_on_replacement"
    # 2 fan
    ALL_FLOWERS = "all_flowers"
    ALL_SEASONS = "all_seasons"
    # 3 fan
    ALL_PUNGS = "all_pungs"  # set-based
    HALF_FLUSH = "half_flush"  # suit-based
    # 4 fan
    LITTLE_THREE_DRAGONS = "little_three_dragons"  # Terminals/Honors
    SEVEN_PAIRS = "seven_pairs"
    # 6 fan
    FULL_FLUSH = "full_flush"  # suit-based
    # limit
    FOUR_CONCEALED_PUNGS = "four_concealed_pungs"
    BIG_THREE_DRAGONS = "big_three_dragons"  # Terminals/Honors
    LITTLE_FOUR_WINDS = "little_four_winds"  # Terminals/Honors
    BIG_FOUR_WINDS = "big_four_winds"  # Terminals/Honors
    ALL_HONORS = "all_honors"
    ALL_TERMINALS = "all_terminals"
    NINE_GATES = "nine_gates"
    THIRTEEN_ORPHANS = "thirteen_orphans"
    ALL_KONGS = "all_kongs"  # set-based
    JADE_DRAGON = "jade_dragon"  # suit-based
    RUBY_DRAGON = "ruby_dragon"  # suit-based
    PEARL_DRAGON = "pearl_dragon"  # suit-based
    BLESSING_OF_HEAVEN = "blessing_of_heaven"
    BLESSING_OF_EARTH = "blessing_of_earth"
