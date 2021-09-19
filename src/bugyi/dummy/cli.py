"""Contains the bugyi.dummy package's main entry point."""

import sys
from typing import Sequence


def main(argv: Sequence[str] = None) -> int:
    """Main entry point."""
    if argv is None:
        argv = sys.argv

    return 0


def foobar(x: int) -> int:
    """Foobar.

    Args:
        x: Some variable...
    """
    return x * 2
