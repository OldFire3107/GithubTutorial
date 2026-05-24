"""
The FallingItem base class.

Every item that falls from the sky (apple, star, and the ones YOU add) inherits
from this class. To add a new item, create a new file in items/ and subclass
FallingItem. See items/apple.py for the simplest example.
"""


class FallingItem:
    """A thing that falls from the top of the screen and can be caught."""

    # subclasses can override these
    fall_speed = 5
    radius = 12

    def __init__(self, x, y):
        # x, y is the center of the item in screen pixels
        self.x = x
        self.y = y
        self.alive = True

    def update(self):
        """Move one frame's worth of motion. Called every tick by the game loop."""
        self.y += self.fall_speed

    def draw(self, surface):
        """Render this item onto the given pygame surface. Subclasses override."""
        raise NotImplementedError("Subclasses must implement draw()")

    def on_caught(self, game):
        """
        Called once when the basket catches this item.
        Override to add score, trigger effects, etc., then call super().on_caught(game)
        so the item is removed from the screen.
        """
        self.alive = False

    def on_missed(self, game):
        """Called once when this item falls off the bottom of the screen."""
        self.alive = False
        game.misses += 1
