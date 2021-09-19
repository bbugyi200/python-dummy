"""Tests the bugyi.dummy.cli module."""

from bugyi.dummy.cli import main


def test_main() -> None:
    """Tests main() function."""
    assert main([""]) == 0
