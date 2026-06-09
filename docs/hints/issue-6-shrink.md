# Issue #6 — Shrink debuff

**Goal:** Add a `Shrink` debuff. Catching one (it looks tempting!) makes
the basket **smaller** for ~5 seconds.

**Difficulty:** medium — the item is a simple subclass, but `Basket` needs to
support a temporary reduced width, and `Game` needs to pass time-of-day
information through.

**Files you'll touch:**
- `items/shrink.py` (new)
- `items/__init__.py` (register it)
- `basket.py` (add `base_width`, `shrink_until`, use the smaller width while active)

---

## Hint 1 — where to start

Two halves:

1. The `Shrink` item just records "the basket should be small until time T"
   on `game.basket`.
2. The `Basket` class needs to actually *be* smaller while the debuff is
   active — both visually (in `draw`) and for catch detection (in `catches`).

Right now `basket.width` is set once in `__init__`. You need it to be
*dynamic* — a function of the current time and the shrink deadline.

---

## Hint 2 — what to think about

Add to `Basket.__init__`:

```python
self.base_width = BASKET_WIDTH    # the "normal" size
self.shrink_until = 0             # ms deadline; <= now means full size
```

Replace the constant `self.width` everywhere it's used with a computed
"current width." A `@property` works well here so callers don't have to
think:

```python
@property
def current_width(self):
    if pygame.time.get_ticks() < self.shrink_until:
        return self.base_width // 2
    return self.base_width
```

Then update `draw()` and `catches()` to use `self.current_width` instead of
`self.width`. (You can also re-clamp `self.x` so the basket can't slide
off-screen when it shrinks asymmetrically — optional polish.)

---

## Hint 3 — sketch

In `basket.py`, replace:

```python
self.width = BASKET_WIDTH
```

with:

```python
self.base_width = BASKET_WIDTH
self.shrink_until = 0
```

Add the property:

```python
@property
def current_width(self):
    if pygame.time.get_ticks() < self.shrink_until:
        return self.base_width // 2
    return self.base_width
```

In `Basket.draw`:

```python
pygame.draw.rect(
    surface, BASKET_COLOR,
    (self.x, self.y, self.current_width, self.height),
    border_radius=6,
)
```

In `Basket.catches`:

```python
within_x = self.x <= item.x <= self.x + self.current_width
within_y = self.y <= item.y <= self.y + self.height
return within_x and within_y
```

In `Basket.handle_input` clamp `self.x`:

```python
self.x = max(0, min(WIDTH - self.current_width, self.x))
```

The item:

```python
"""Shrink debuff. Makes the basket smaller for 5 seconds."""

import pygame
from .base import FallingItem


class Shrink(FallingItem):
    radius = 13
    color = (160, 70, 200)
    base_fall_speed = 5

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        # downward arrows
        for dy in (-4, 4):
            pygame.draw.polygon(
                surface, (255, 255, 255),
                [(self.x - 6, self.y + dy - 3),
                 (self.x + 6, self.y + dy - 3),
                 (self.x, self.y + dy + 4)],
            )

    def on_collect(self, game):
        game.basket.shrink_until = pygame.time.get_ticks() + 5000
        super().on_collect(game)
```

In `items/__init__.py`: add `Shrink` to `ITEMS["bad"]`.

Test: catch a Shrink. The basket should immediately halve in width. After
~5 seconds it snaps back to full size.

> **Why a `@property` instead of a `width` field that gets set/reset?**
> Because nothing has to *remember* to flip it back. The property is just a
> live answer to "what's my width right now?" — when the deadline passes,
> the value automatically reverts. Fewer bugs.
