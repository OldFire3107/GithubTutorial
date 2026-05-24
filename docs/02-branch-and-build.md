# 02 — Branch and build

Now the actual work. You'll create a branch, build your feature, and commit
your changes. Don't push yet — that's the next lesson.

---

## 1. Make sure `main` is up to date

```bash
git checkout main
git pull upstream main
```

> **Why pull from `upstream` not `origin`?** `origin/main` is your fork's main,
> which might be stale. `upstream/main` is the source of truth.

## 2. Create your feature branch

Branch names should describe what you're doing. The convention here is
`feature/<short-name>`:

```bash
git checkout -b feature/bomb-item
```

`-b` means "create and switch to". You're now on a branch that exists only
on your machine. Verify:

```bash
git branch
# * feature/bomb-item
#   main
```

> **Why a branch?** It isolates your work. You can experiment, commit, throw
> things away, all without touching `main`. Until you merge, your changes
> don't affect anyone else.

## 3. Build your feature

Say you took issue #1 (Bomb). Two files to touch:

### a) Create `items/bomb.py`

```python
"""A bomb. Catching one subtracts 5 points."""

import pygame
from .base import FallingItem


class Bomb(FallingItem):
    radius = 14
    color = (40, 40, 40)
    fall_speed = 6

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        # red fuse spark
        pygame.draw.circle(surface, (240, 80, 40), (self.x, self.y - self.radius - 3), 3)

    def on_caught(self, game):
        game.score -= 5
        super().on_caught(game)
```

### b) Register it in `items/__init__.py`

```python
from .apple import Apple
from .star import Star
from .bomb import Bomb         # <-- new

ITEMS = [
    Apple,
    Apple,
    Star,
    Bomb,                       # <-- new
]
```

### c) Test it

```bash
python main.py
```

You should see black bombs falling. Catch one — your score should go down by 5.

> **Tip:** if the game crashes on import, check for typos in the class name and
> the import. Python will tell you the exact line.

## 4. Commit

```bash
git status                    # see what changed
git add items/bomb.py items/__init__.py
git commit -m "Add Bomb item that subtracts 5 points when caught"
```

> **Commit message style:** start with a verb ("Add", "Fix", "Refactor"), keep
> the subject line under ~70 chars, describe *what* the change does (not how).
> Most teams have their own convention — match what you see in `git log`.

Want to make multiple smaller commits as you work? Go ahead — you can clean
them up later with [interactive rebase](bonus-3-rebase.md).

## 5. Don't push yet

Take a breath. Look at your work with `git log --oneline` and `git diff main`.
Then move on.

---

→ [Next: 03 — Open a PR](03-open-a-pr.md)
