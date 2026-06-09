# Issue #5 — LifeHeart

**Goal:** Add a `LifeHeart`. Catching one **undoes** a missed item — your
`misses` counter goes down by 1 (but never below 0).

**Difficulty:** easy — pure subclass, no engine changes.

**Files you'll touch:**
- `items/life_heart.py` (new)
- `items/__init__.py` (register it)

---

## Hint 1 — where to start

This is the *mirror image* of a bomb. Bomb subtracts from `game.score`;
LifeHeart subtracts from `game.misses`. Same pattern, different attribute.

Use Python's `max()` to keep `misses` from going negative — getting a heart
when you have 0 misses shouldn't suddenly make you immortal.

---

## Hint 2 — what to override

Same two methods as any other item: `draw` and `on_collect`. Draw a pink/red
heart-ish shape (two circles + a triangle works, or just use a single circle
for v1 and call it good). In `on_collect`, decrement `game.misses` with a
floor of 0.

For balance, make it rare — list it once in `ITEMS["good"]`.

---

## Hint 3 — sketch

```python
"""LifeHeart. Catching one removes one missed item from your counter."""

import pygame
from .base import FallingItem


class LifeHeart(FallingItem):
    radius = 12
    color = (220, 70, 130)
    base_fall_speed = 3   # slow & rare — a real reward

    def draw(self, surface):
        # two circles + downward triangle = heart
        pygame.draw.circle(surface, self.color, (self.x - 5, self.y - 2), 7)
        pygame.draw.circle(surface, self.color, (self.x + 5, self.y - 2), 7)
        pygame.draw.polygon(
            surface, self.color,
            [(self.x - 11, self.y), (self.x + 11, self.y), (self.x, self.y + 12)],
        )

    def on_collect(self, game):
        game.misses = max(0, game.misses - 1)
        super().on_collect(game)
```

In `items/__init__.py`:

```python
from .life_heart import LifeHeart
...
ITEMS = {
    "good": [Apple, Apple, Star, LifeHeart],   # rare
    "bad":  [],
}
```

Test: deliberately miss two items, then catch a heart. The HUD's `Misses`
counter should drop from `2/5` to `1/5`.
