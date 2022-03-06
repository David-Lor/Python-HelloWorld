"""RUNNER
"""

import sys

__all__ = ("run",)


def run():
    args = sys.argv[1:]
    print(f"Called with args: {args}")
