"""RUNNER
"""

from .helpers import get_greet

__all__ = ("run",)


def run():
    print(get_greet())
