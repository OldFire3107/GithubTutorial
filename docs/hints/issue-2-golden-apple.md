# Issue #2 — GoldenApple

**Goal:** Add a `GoldenApple`. Rare. Worth **+10** points.

**Difficulty:** easy — pure subclass, no engine changes.

**Files you'll touch:**
- `items/golden_apple.py` (new)
- `items/__init__.py` (register it)

---

## Hint 1 — where to start

This is just an apple that gives more points and is harder to come by.
Copy `items/apple.py` as a starting point and tweak.

For "rare," think about how `ITEMS` controls spawn frequency. Look at how
many times `Apple` appears in the list vs. `Star`. If you list something
once and apples three times, which is rarer?

---

## Hint 2 — what to override

You'll subclass `FallingItem`. Most of the apple's code is fine — change:

- `color` to gold-ish (e.g. `(255, 215, 0)`)
- `on_collect` to add 10 to `game.score`

To make it rare, in `ITEMS["good"]` list `GoldenApple` **once** while listing
`Apple` two or three times. Random choice from the list naturally weighs
common items higher.

---

## Hint 3 — sketch

```python
"""A rare golden apple. Catching one gives +10 points."""

import pygame
from .base import FallingItem


class GoldenApple(FallingItem):
    radius = 14
    color = (255, 215, 0)
    base_fall_speed = 7   # falls a touch faster so it's a real challenge

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        # bright highlight
        pygame.draw.circle(
            surface, (255, 245, 200),
            (self.x - 3, self.y - 3), self.radius // 3
        )

    def on_collect(self, game):
        game.score += 10
        super().on_collect(game)
```

In `items/__init__.py`:

```python
from .golden_apple import GoldenApple
...
ITEMS = {
    "good": [Apple, Apple, Apple, Star, GoldenApple],   # 1-in-5 spawns
    "bad":  [],
}
```

Test: play long enough to catch one. Score jumps by 10.
