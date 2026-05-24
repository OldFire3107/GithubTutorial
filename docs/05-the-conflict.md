# 05 — The conflict

This is the lesson everyone remembers. Here's what just happened:

> While you were building your feature, another contributor opened a PR called
> **`newupdate`** that refactored the `FallingItem` base class. The maintainer
> merged it into `upstream/main`. Now your branch is based on an old version
> of the base class. When you try to update, Git can't figure out which version
> wins for one file — and the *other* files merge cleanly but **silently leave
> your code in a broken state**. You have to fix both.

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

```text
Auto-merging items/__init__.py
CONFLICT (content): Merge conflict in items/__init__.py
Auto-merging items/base.py
Auto-merging items/apple.py
Auto-merging items/star.py
Auto-merging main.py
Automatic merge failed; fix conflicts and then commit the result.
```

> **Read carefully:** Git lists every file it touched. Most say "Auto-merging"
> (combined cleanly with no human input). One says "CONFLICT" — that's the
> file you need to edit. **But "Auto-merging" doesn't mean "still works."**
> Files that merged cleanly can still be broken, because a merge only looks
> at *text* — it doesn't run your code.

Don't panic. This is exactly what we want.

## 2. See what's conflicting

```bash
git status
# ...
# Unmerged paths:
#   both modified:   items/__init__.py
```

Just one file. Open it.

## 3. Read the conflict markers

In `items/__init__.py` you'll see:

```python
from .apple import Apple
from .bomb import Bomb
from .star import Star

<<<<<<< HEAD
ITEMS = [
    Apple,
    Apple,
    Star,
    Bomb,
]
=======
ITEMS = {
    "good": [
        Apple,
        Apple,
        Star,
    ],
    "bad": [],
}
>>>>>>> upstream/main
```

The format:

- `<<<<<<< HEAD` ... `=======` — **your** changes (what's currently on your branch)
- `=======` ... `>>>>>>> upstream/main` — **their** changes (what came from upstream)

You have to pick one, or combine them, or write something new. Git doesn't
care — it just wants the markers gone and the file in a working state.

## 4. Decide what's correct

This is the part that requires thinking. Read `items/base.py` (which came down
from upstream cleanly — no conflict markers, but it's a *totally different*
base class now):

```python
def __init__(self, pos, weight=1.0):     # was: (self, x, y)
    self.x, self.y = pos
    self.weight = weight
    ...

def on_collect(self, game):              # was: on_caught
    self.alive = False
```

So the refactor:

- Renamed `__init__(self, x, y)` → `__init__(self, pos, weight=1.0)` where `pos` is a tuple
- Renamed `on_caught` → `on_collect`
- Restructured `ITEMS` from a flat list to a dict with `"good"` and `"bad"` categories

The conflict in `items/__init__.py` is about the third change. Resolve it by
keeping the new dict shape and putting your bomb in the right category:

```python
ITEMS = {
    "good": [Apple, Apple, Star],
    "bad": [Bomb],              # bombs subtract points → "bad"
}
```

Delete the `<<<<<<<`, `=======`, `>>>>>>>` markers. Save.

## 5. Now find the silent breakage

`git status` looks clean, but the game is still broken — your bomb file uses
the **old** base-class API. Run the game and see:

```bash
python main.py
```

You'll get a crash like:

```text
TypeError: Bomb.__init__() got an unexpected keyword argument 'pos'
```

Open `items/bomb.py`. You wrote:

```python
def __init__(self, x, y):
    super().__init__(x, y)        # ← old signature
    ...

def on_caught(self, game):        # ← old method name
    game.score -= 5
    super().on_caught(game)       # ← old method name
```

Three things must change:

```python
def __init__(self, pos, weight=1.0):
    super().__init__(pos, weight)
    self.flash = 0

def on_collect(self, game):
    game.score -= 5
    super().on_collect(game)
```

Also rename the class attribute `fall_speed` to `base_fall_speed` — the base
class renamed it too, and yours is being silently ignored otherwise.

Save. Run again. The game should now work — bombs spawn occasionally and
subtract 5 points when caught.

> **The bigger lesson:** Git's "no conflicts" message only means *no
> contradictory text edits*. It says nothing about whether the merged code
> compiles, passes tests, or makes sense. **Always run your code after a
> merge.** This is exactly why teams require CI to pass on PRs
> ([Bonus 4](bonus-4-actions-and-releases.md)).

## 6. Mark resolved and commit

```bash
git add items/__init__.py items/bomb.py
git status                          # should say "All conflicts fixed"
git commit                          # opens editor with a pre-filled merge message
```

The default merge commit message is fine — just save and close.

## 7. Push, and watch your PR update

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
| The game crashes after merge but `git status` is clean | That's the silent breakage from step 5 — read the traceback, find the file, fix the old API call |

---

→ [Next: 06 — Review and merge](06-review-and-merge.md)
