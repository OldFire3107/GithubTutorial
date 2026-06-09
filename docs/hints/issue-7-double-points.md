# Issue #7 — DoublePoints powerup

**Goal:** Add a `DoublePoints` powerup. While active (~10 seconds), every
point-scoring item is worth **2x**.

**Difficulty:** medium — the item itself is a simple subclass, but you have
to decide how *other* items learn about the multiplier.

**Files you'll touch:**
- `items/double_points.py` (new)
- `items/__init__.py` (register it)
- `main.py` (add `double_until` on `Game`, plus a way for scoring items to query the multiplier)
- *(maybe)* `items/apple.py`, `items/star.py`, etc. — depends on which approach you pick (see below)

---

## Hint 1 — where to start

Same time-deadline pattern as Freeze and Magnet — `Game` gets a
`double_until` field. The new twist is that *other* items (Apple, Star,
maybe GoldenApple) need to read it when scoring.

You have **two design choices** for how they do that. Read hint 2 before
picking.

---

## Hint 2 — pick your approach

**Option A — `Game.add_score(n)` helper.** Add a method on `Game`:

```python
def add_score(self, points):
    multiplier = 2 if pygame.time.get_ticks() < self.double_until else 1
    self.score += points * multiplier
```

Then change every scoring item from `game.score += N` to `game.add_score(N)`.
This is cleaner long-term, but you have to touch Apple, Star, and any other
scoring item you've added.

**Option B — `Game.score_multiplier` property.** Add a `@property` on `Game`:

```python
@property
def score_multiplier(self):
    return 2 if pygame.time.get_ticks() < self.double_until else 1
```

Each scoring item writes `game.score += N * game.score_multiplier`. This
requires touching the same number of files, but the change to each one is
smaller (no method introduced, just a multiplication).

For a workshop PR, **option A** reads better in a diff (the intent is
visible). But it touches every scoring item — so if you haven't added an
explanatory commit message, reviewers might be surprised by the spread.

---

## Hint 3 — sketch (option A)

```python
# items/double_points.py
"""DoublePoints powerup. 2x scoring for 10 seconds."""

import pygame
from .base import FallingItem


class DoublePoints(FallingItem):
    radius = 13
    color = (255, 170, 60)
    base_fall_speed = 5

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        # "x2" text-ish
        pygame.draw.line(surface, (255, 255, 255),
                         (self.x - 5, self.y - 4), (self.x + 5, self.y + 4), 2)
        pygame.draw.line(surface, (255, 255, 255),
                         (self.x - 5, self.y + 4), (self.x + 5, self.y - 4), 2)

    def on_collect(self, game):
        game.double_until = pygame.time.get_ticks() + 10000
        super().on_collect(game)
```

In `main.py`:

```python
# Game.reset():
self.double_until = 0

# Add method on Game:
def add_score(self, points):
    multiplier = 2 if pygame.time.get_ticks() < self.double_until else 1
    self.score += points * multiplier
```

In `items/apple.py`, change:

```python
def on_collect(self, game):
    game.score += 1
    super().on_collect(game)
```

to:

```python
def on_collect(self, game):
    game.add_score(1)
    super().on_collect(game)
```

Same change in `items/star.py` (3 → `add_score(3)`), and any other scoring
item.

Register in `items/__init__.py` under `"good"` (rare).

Test: catch a DoublePoints. While active, an Apple gives **+2** and a Star
gives **+6**. Misses don't matter — DoublePoints only multiplies *positive*
score gains.

> **Edge case:** what about Bomb? Currently bomb does `game.score -= 5`. If
> you change it to `game.add_score(-5)`, DoublePoints will *amplify* the
> penalty too — `-10` instead of `-5`. That's a design choice. Decide and
> document it.
