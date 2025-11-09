class MahjongError(Exception):
    """Base class for all domain-level Mahjong validation errors."""

    def __init__(self, message: str, **details):
        """
        :param message: Human-readable error message
        :param details: Optional context (tile, hand, meld, etc.)
        """
        super().__init__(message)
        self.message = message
        self.details = details
        self.code = getattr(self, "code", "MAHJONG_ERROR")

    def to_dict(self) -> dict:
        """
        Serialize the error to a JSON-friendly dict.
        Only includes details that are present.
        """
        error_dict = {"error": {"code": self.code, "message": self.message}}
        if self.details:

            def serialize_value(v):
                if v is None:
                    return None
                elif hasattr(v, "to_dict") and callable(v.to_dict):
                    return v.to_dict()
                else:
                    return str(v)

            error_dict["error"]["details"] = {
                k: serialize_value(v) for k, v in self.details.items() if v is not None
            }
        return error_dict


class InvalidTileError(MahjongError):
    """Raised when a tile has an invalid suit or value."""

    code = "INVALID_TILE"


class InvalidMeldError(MahjongError):
    """Raised when a meld (chow, pong or kong) is invalid."""

    code = "INVALID_MELD"


class InvalidHandError(MahjongError):
    """Raised when a Mahjong hand is invalid."""

    code = "INVALID_HAND"


class InvalidGameError(MahjongError):
    """Raised for an invalid game"""

    code = "INVALID_GAME"
