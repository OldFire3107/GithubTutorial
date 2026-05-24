# Bonus 1 — `reflog` and syncing your fork

Two safety/hygiene skills that pair naturally with what you've already done:

- **`git reflog`** lets you recover commits you thought you destroyed.
- **Syncing your fork** keeps `origin/main` from drifting out of step with
  `upstream/main`.

---

## Part A: `git reflog` — nothing is truly lost

### The setup (simulate a disaster)

Make sure you're on a throwaway branch first, so we don't damage real work:

```bash
git checkout -b reflog-practice
```

Make three commits — content doesn't matter, just commit any tiny edits to
a scratch file:

```bash
echo "one"   >> scratch.txt && git add scratch.txt && git commit -m "one"
echo "two"   >> scratch.txt && git add scratch.txt && git commit -m "two"
echo "three" >> scratch.txt && git add scratch.txt && git commit -m "three"
git log --oneline
# abc1234 three
# def5678 two
# 9876543 one
# ... (previous history)
```

### The disaster

Now wipe them out:

```bash
git reset --hard HEAD~3
git log --oneline
# (the three commits are gone — log shows only history before "one")
```

Your three commits seem to have vanished. **They haven't.**

### The recovery

```bash
git reflog
# abc1234 HEAD@{0}: reset: moving to HEAD~3
# 1112223 HEAD@{1}: commit: three
# 4445556 HEAD@{2}: commit: two
# 7778889 HEAD@{3}: commit: one
# ...
```

`git reflog` is a journal of every move `HEAD` has made — every commit,
checkout, reset, merge. Even when commits aren't on any branch anymore,
they're still in the reflog (for ~90 days by default).

Recover by resetting back to the commit hash of `three`:

```bash
git reset --hard 1112223
git log --oneline
# 1112223 three
# 4445556 two
# 7778889 one
```

Done. All three back.

> **Why this matters:** Almost no Git operation actually deletes data
> immediately. `reset --hard`, `rebase`, `commit --amend`, even deleting
> branches — they all leave traces in the reflog. If you ever think you've
> lost work, **`git reflog` first, panic never.**

### Clean up

```bash
git checkout main
git branch -D reflog-practice
rm scratch.txt    # if it survived the reset
```

---

## Part B: Sync your fork with upstream

Over the course of the workshop, `upstream/main` has gained your teammates'
merged PRs. But your fork's `origin/main` is still where it was when you
forked. Time to catch up.

### 1. Fetch upstream

```bash
git fetch upstream
```

This downloads upstream's new commits but doesn't apply them anywhere.

### 2. Update your local main

```bash
git checkout main
git merge upstream/main           # fast-forward, no conflict expected
```

If you've been disciplined about never committing directly to `main`,
this will be a fast-forward — no merge commit, just moves `main`'s pointer
forward.

### 3. Push to your fork

```bash
git push origin main
```

Now `origin/main` matches `upstream/main`. Your fork is in sync.

### The whole thing as one command (for next time)

```bash
git fetch upstream && git checkout main && git merge upstream/main && git push origin main
```

Or with `rebase` instead of `merge` — same result on a clean main:

```bash
git fetch upstream && git checkout main && git rebase upstream/main && git push origin main
```

### When sync goes wrong

If you ever accidentally commit on `main` locally, `git merge upstream/main`
might create a merge commit you don't want. The cleanest fix:

```bash
git reset --hard upstream/main    # discard local main commits (use reflog if you regret it)
git push --force-with-lease origin main
```

> `--force-with-lease` is the safer cousin of `--force` — it refuses if
> someone else has pushed in between. Use it instead of plain `--force`.

---

→ [Next: B2 — Issues, labels, milestones](bonus-2-issues-labels-milestones.md)
