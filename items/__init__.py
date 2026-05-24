"""
The item registry.

Every item type that the game can spawn must be listed in ITEMS below.
When you add a new item, you must do TWO things:
    1. import your class here
    2. add it to the ITEMS list

The game picks a random class from this list each time it spawns something.
Want your item to be rarer? Add it once. Want it to be common? Add it multiple times.
"""

from .apple import Apple
from .star import Star

# TODO (issue #1): from .bomb import Bomb         -> subtracts points
# TODO (issue #2): from .golden_apple import GoldenApple  -> rare, big points
# TODO (issue #3): from .freeze import Freeze     -> slows all items briefly
# TODO (issue #4): from .magnet import Magnet     -> pulls items toward basket

ITEMS = [
    Apple,
    Apple,   # listed twice so apples are twice as common as stars
    Star,
]
