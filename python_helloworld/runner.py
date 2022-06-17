"""RUNNER
"""

import signal
from .helpers import get_greet

__all__ = ("run",)


def run():
    print(get_greet())
    print("Sleeping forever...")
    signal.signal(signal.SIGINT, lambda *_: print("Signal: SIGINT"))
    signal.signal(signal.SIGTERM, lambda *_: print("Signal: SIGTERM"))
    signal.pause()
