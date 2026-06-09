# Issue #8 — Cloud obstacle

**Goal:** Add a `Cloud`. It's a *neutral* obstacle — it falls slowly, it
doesn't give or take score points, and it doesn't count as a miss if it
falls off the screen. Its only job is to be visual noise: a thing you might
mistakenly chase, distracting you from the real items.

**Difficulty:** easy — pure subclass, no engine changes.

**Files you'll touch:**
- `items/cloud.py` (new)
- `items/__init__.py` (register it)

---

## Hint 1 — where to start

Most of `FallingItem`'s default behavior is fine for a cloud. The only thing
you really need to change is `on_missed` — by default, `on_missed` bumps
`game.misses`, but clouds shouldn't count.

Look at `FallingItem.on_missed` in `items/base.py` to see what you'd be
overriding.

---

## Hint 2 — what to override

Three methods to think about:

- `draw` — make it look like a cloud (a few overlapping white-ish circles,
  or a soft gray puff)
- `on_collect` — fine to inherit the default (the cloud just disappears, no
  score change)
- `on_missed` — **override this so it doesn't count as a miss.** Just set
  `self.alive = False` without bumping `game.misses`.

Where does it go in `ITEMS`? You have two options:

- Add it to `"bad"` — but then `spawn_item` will only roll for it 20% of the
  time, and it's not really "bad," just neutral.
- Add a `"neutral"` key and adjust `spawn_item` to roll it in.

The simpler path is `"bad"` — keep the spawn logic untouched.

---

## Hint 3 — sketch

```python
"""Cloud. A neutral obstacle — doesn't score, doesn't punish, just distracts."""

import pygame
from .base import FallingItem


class Cloud(FallingItem):
    radius = 22
    base_fall_speed = 2
    color = (220, 220, 230)

    def draw(self, surface):
        # three overlapping circles for a puffy cloud silhouette
        pygame.draw.circle(surface, self.color, (self.x - 10, self.y),     14)
        pygame.draw.circle(surface, self.color, (self.x + 10, self.y),     14)
        pygame.draw.circle(surface, self.color, (self.x,      self.y - 6), 16)

    def on_missed(self, game):
        # override: clouds don't count as missed items
        self.alive = False
```

In `items/__init__.py`:

```python
from .cloud import Cloud
...
ITEMS = {
    "good": [Apple, Apple, Star],
    "bad":  [Cloud],
}
```

Test: play for a minute. Catch a cloud — nothing happens, it just disappears.
Let one fall off the bottom — the misses counter doesn't tick up.

> **Optional extension:** make clouds bigger and partially transparent, so
> they actually *block view* of items behind them. That turns Cloud from a
> visual gag into a real difficulty mechanic.
