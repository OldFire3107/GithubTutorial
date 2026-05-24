# 05 — The conflict

This is the lesson everyone remembers. Here's what just happened:

> While you were building your feature, another contributor opened a PR called
> **`newupdate`** that refactored the `FallingItem` base class. The maintainer
> merged it into `upstream/main`. Now your branch is based on an old version
> of the base class. When you try to update, Git can't figure out which version
> wins. **You have to tell it.**

Wait for your instructor to confirm `newupdate` has been merged into
`upstream/main`, then proceed.

---

## 1. Pull the new upstream/main onto your feature branch

You're still on `feature/<your-thing>`. Bring in the upstream changes:

```bash
git fetch upstream                  # downloads new commits but doesn't apply them
git merge upstream/main             # apply them on top of your branch
```

You'll see something like:

```
Auto-merging items/__init__.py
CONFLICT (content): Merge conflict in items/__init__.py
Auto-merging items/bomb.py
CONFLICT (content): Merge conflict in items/bomb.py
Automatic merge failed; fix conflicts and then commit the result.
```

Don't panic. This is exactly what we want.

> **What just happened?** Git tried to combine your changes with the upstream
> changes. For *most* lines it figured it out automatically. For lines where
> both sides edited the same thing, it gave up and asked you to decide.

## 2. See what's conflicting

```bash
git status
# ...
# Unmerged paths:
#   both modified:   items/__init__.py
#   both modified:   items/bomb.py
```

## 3. Read the conflict markers

Open `items/bomb.py`. You'll see something like:

```python
class Bomb(FallingItem):
    radius = 14
    color = (40, 40, 40)
    fall_speed = 6

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

<<<<<<< HEAD
    def on_caught(self, game):
        game.score -= 5
        super().on_caught(game)
=======
    def on_collect(self, game):
        game.score -= 5
        super().on_collect(game)
>>>>>>> upstream/main
```

The format:
- `<<<<<<< HEAD` ... `=======` — **your** changes (what's currently on your branch)
- `=======` ... `>>>>>>> upstream/main` — **their** changes (what came from upstream)

You have to pick one, or combine them, or write something new. Git doesn't
care — it just wants the markers gone and the file in a working state.

## 4. Decide what's correct

This is the part that requires thinking. Read `items/base.py` (which also
came down from upstream):

```python
def __init__(self, pos, weight=1.0):     # was: (self, x, y)
    self.x, self.y = pos
    ...

def on_collect(self, game):              # was: on_caught
    self.alive = False
```

So the refactor:
- Renamed `__init__(self, x, y)` → `__init__(self, pos, weight=1.0)`
- Renamed `on_caught` → `on_collect`
- Restructured the `ITEMS` list into a dict with `"good"` and `"bad"` categories

Your bomb needs to:
1. Use the new `__init__` signature (and pass `pos` through to `super()`)
2. Rename its `on_caught` to `on_collect`
3. Go into the **`"bad"`** category in the registry (it subtracts points)

So the resolved `items/bomb.py` becomes:

```python
import pygame
from .base import FallingItem


class Bomb(FallingItem):
    radius = 14
    color = (40, 40, 40)
    fall_speed = 6

    def __init__(self, pos, weight=1.0):
        super().__init__(pos, weight)
        # any extra setup goes here

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(surface, (240, 80, 40), (self.x, self.y - self.radius - 3), 3)

    def on_collect(self, game):
        game.score -= 5
        super().on_collect(game)
```

Delete the `<<<<<<<`, `=======`, `>>>>>>>` markers. Save.

## 5. Resolve `items/__init__.py`

Open it. You'll see your line `from .bomb import Bomb` and the line you added
to `ITEMS`, both inside conflict markers because upstream restructured the
list into a dict.

Resolved version:

```python
from .apple import Apple
from .star import Star
from .bomb import Bomb

ITEMS = {
    "good": [Apple, Apple, Star],
    "bad": [Bomb],                  # bombs are "bad" — they subtract points
}
```

Save.

## 6. Test before committing

**Critically important.** Conflict resolution is editing code blind — easy to
introduce bugs. Run the game:

```bash
python main.py
```

If it crashes on import, fix the import. If bombs don't spawn, check the
registry. If catching a bomb doesn't subtract points, check the method name.

## 7. Mark resolved and commit

```bash
git add items/bomb.py items/__init__.py
git status                          # should say "All conflicts fixed"
git commit                          # opens editor with a pre-filled merge message
```

The default merge commit message is fine — just save and close.

## 8. Push, and watch your PR update

```bash
git push
```

Go to your PR on GitHub. The "Files changed" tab now shows your bomb code in
its new shape. The "This branch has no conflicts with the base branch"
message should appear. You're ready for review.

---

## What to do if it goes wrong

| Situation | Fix |
|---|---|
| You panicked mid-merge | `git merge --abort` — back to where you were before the merge |
| You committed the conflict markers | `git commit --amend` after editing the files (only on un-pushed commits!) |
| You're not sure what's "yours" vs "theirs" | `git checkout --ours <file>` or `--theirs <file>` to pick one whole side; you can then re-edit |
| You want to start the resolution over | `git checkout --merge <file>` resets the file back to its conflicted state |

---

→ [Next: 06 — Review and merge](06-review-and-merge.md)
