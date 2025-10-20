# Registers all the rules with a single import

from . import set_based
from . import suit_based
from . import terminal_honours

__all__ = ["set_based", "suit_based", "terminal_honours"]
