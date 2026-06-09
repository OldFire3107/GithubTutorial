# Issue #4 — Magnet powerup

**Goal:** Add a `Magnet` powerup. While active (~5 seconds), all falling items
drift horizontally toward the basket as they fall — easier to catch the good
ones, harder to dodge the bad ones.

**Difficulty:** medium — `Game` tracks a `magnet_until` deadline and nudges
items toward `basket.x` each frame while active.

**Files you'll touch:**
- `items/magnet.py` (new)
- `items/__init__.py` (register it)
- `main.py` (add `magnet_until`, nudge items in `update()`)

---

## Hint 1 — where to start

Same shape as Freeze: an item that records a deadline on the game, and the
game's `update()` checks the deadline every frame.

The difference is *what* the game does while the effect is active: instead of
slowing items, it nudges their `x` toward the basket's center.

---

## Hint 2 — what to think about

State on `Game`:

```python
self.magnet_until = 0
```

Where the basket's center is:

```python
basket_center = self.basket.x + self.basket.width // 2
```

Per frame, for each item: if `item.x` is left of the basket center, push it
right; if right, push it left. A constant pixel nudge (3–4 px/frame) feels
right at 60 FPS.

You don't need a special drawing for the magnet — a red horseshoe-ish shape
is fine (or just a flat color until you feel like polishing).

---

## Hint 3 — sketch

```python
# items/magnet.py
"""Magnet powerup. While active, falling items drift toward the basket."""

import pygame
from .base import FallingItem


class Magnet(FallingItem):
    radius = 13
    color = (220, 60, 60)
    base_fall_speed = 4

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(surface, (40, 40, 40), (self.x, self.y), self.radius // 2)

    def on_collect(self, game):
        game.magnet_until = pygame.time.get_ticks() + 5000
        super().on_collect(game)
```

In `main.py`:

```python
# Game.reset():
self.magnet_until = 0

# Game.update(), after item.update() but before catch-detection:
if pygame.time.get_ticks() < self.magnet_until:
    basket_center = self.basket.x + self.basket.width // 2
    for item in self.items:
        if item.x < basket_center:
            item.x += 3
        elif item.x > basket_center:
            item.x -= 3
```

Register in `items/__init__.py` under `"good"` (rare).

Test: catch a magnet, then move the basket far to one side and watch a few
falling items curve toward you.

> **Optional polish:** draw a faint red glow around the basket while the
> magnet is active.
