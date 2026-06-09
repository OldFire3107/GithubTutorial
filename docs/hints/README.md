# Hints

Stuck on your issue? Each file below has **three levels of hints**. Read level 1
first and try it. If still stuck, read level 2. Save level 3 for when you've
genuinely tried — it's nearly the answer.

| Issue | Hint file | Difficulty |
|---|---|---|
| #1 Bomb | walked through in [02 — Branch and build](../02-branch-and-build.md) | easy — pure subclass |
| #2 GoldenApple | [issue-2-golden-apple.md](issue-2-golden-apple.md) | easy — pure subclass |
| #3 Freeze powerup | [issue-3-freeze.md](issue-3-freeze.md) | medium — touches `Game` |
| #4 Magnet powerup | [issue-4-magnet.md](issue-4-magnet.md) | medium — touches `Game` |
| #5 LifeHeart | [issue-5-life-heart.md](issue-5-life-heart.md) | easy — pure subclass |
| #6 Shrink debuff | [issue-6-shrink.md](issue-6-shrink.md) | medium — touches `Basket` |
| #7 DoublePoints | [issue-7-double-points.md](issue-7-double-points.md) | medium — touches `Game` + items |
| #8 Cloud obstacle | [issue-8-cloud.md](issue-8-cloud.md) | easy — pure subclass |

> Issue #1 (Bomb) doesn't have a hint file because it's the worked example in
> [lesson 02](../02-branch-and-build.md) — anything a hint file would say is
> already there.

## How to use these

1. Pick your issue and open the hint file.
2. **Try level 1 first.** It tells you where to look and what pattern to follow.
   That's usually enough.
3. If you're stuck after a real attempt, level 2 narrows it down further.
4. Level 3 is the "show me a sketch" tier. The skeleton is there but you still
   need to wire it up and decide values.

You're not graded on hints — read them freely. Just *try first* so the
"I figured it out" feeling actually happens.

## Note on the conflict (lesson 05)

These hints describe the feature against the **post-newupdate** API
(`__init__(self, pos, weight=1.0)`, `on_collect`, `ITEMS = {"good": [...], "bad": [...]}`).
If you built your feature before the `newupdate` merge, your code uses the
**old** API — you'll need to translate. See [05 — The conflict](../05-the-conflict.md).
