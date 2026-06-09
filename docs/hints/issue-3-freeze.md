# Issue #3 — Freeze powerup

**Goal:** Add a `Freeze` powerup. Catching one slows **all** falling items
for ~3 seconds.

**Difficulty:** medium — pure subclass for the item, but `Game` needs a
small piece of new state to track *when* the slow effect ends.

**Files you'll touch:**
- `items/freeze.py` (new)
- `items/__init__.py` (register it)
- `main.py` (add a `slow_until` field on `Game`, and use it in `update()`)

---

## Hint 1 — where to start

Two halves:

1. The Freeze item itself is a normal subclass. Its `on_collect` records
   "the slow effect should be active for the next 3000 ms" on the game.
2. The `Game` class needs to *honor* that — somewhere in `Game.update`,
   if the slow is still active, items should move less.

Look at how `pygame.time.get_ticks()` works (returns ms since pygame.init).
You'll compare it against a stored "deadline" value.

---

## Hint 2 — what to think about

Add a field on `Game.__init__` (or in `reset()`):

```python
self.slow_until = 0   # ms; if get_ticks() < this, items move slowly
```

In `Game.update`, after `item.update()`, you can compensate for the speed.
Each item moves `base_fall_speed * weight` pixels per frame. To slow them
to ~30 %, *subtract* most of that distance back when the slow is active:

```python
slow_active = pygame.time.get_ticks() < self.slow_until
...
if slow_active:
    item.y -= item.base_fall_speed * item.weight * 0.7
```

This is uglier than passing a speed multiplier into `item.update()`, but it
doesn't require changing the `FallingItem` base class — which would
otherwise cascade through every other item.

---

## Hint 3 — sketch

```python
# items/freeze.py
"""Freeze powerup. Catching one slows all falling items for 3 seconds."""

import pygame
from .base import FallingItem


class Freeze(FallingItem):
    radius = 13
    color = (130, 200, 255)
    base_fall_speed = 4

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        # snowflake-ish cross
        for dx, dy in [(-8, 0), (8, 0), (0, -8), (0, 8)]:
            pygame.draw.line(surface, (255, 255, 255),
                             (self.x, self.y), (self.x + dx, self.y + dy), 2)

    def on_collect(self, game):
        game.slow_until = pygame.time.get_ticks() + 3000
        super().on_collect(game)
```

In `main.py`:

```python
# In Game.reset() (which is also called by __init__):
self.slow_until = 0

# In Game.update(), before checking catches/misses:
slow_active = pygame.time.get_ticks() < self.slow_until
for item in self.items:
    item.update()
    if slow_active:
        item.y -= item.base_fall_speed * item.weight * 0.7
    # ... existing catch/miss logic ...
```

In `items/__init__.py`: add `Freeze` to `ITEMS["good"]`, once (rare).

Test: catch a Freeze, watch everything *visibly* slow for 3 seconds, then
snap back to normal.

> **Optional polish:** while slow is active, draw a thin blue tint at the top
> of the screen as a visual indicator.
