# Bonus 3 — Interactive rebase

You probably made several messy commits while building your feature:

```
git log --oneline feature/bomb-item
abc1111 add bomb
def2222 fix typo
ghi3333 oops forgot to register
jkl4444 actually subtract 5 not 50
mno5555 fix comment
```

Five commits for one logical change. The reviewer doesn't want to read five
diffs — they want to see one clean "Add Bomb item" commit. **Interactive
rebase** lets you rewrite history before you push (or before the PR is
merged).

> **⚠️ Hazard:** Rebasing rewrites commits, which changes their hashes.
> NEVER rebase commits that have been pushed to a branch others are pulling
> from. On your own feature branch before review? Totally fine.

---

## 1. Start an interactive rebase

```bash
git checkout feature/bomb-item
git rebase -i main
```

Git opens your editor with something like:

```
pick abc1111 add bomb
pick def2222 fix typo
pick ghi3333 oops forgot to register
pick jkl4444 actually subtract 5 not 50
pick mno5555 fix comment

# Commands:
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# d, drop = remove commit
# ...
```

The commits are listed **oldest first** (the opposite of `git log`).

## 2. Decide what you want

For our messy history, the goal is one clean commit. Change `pick` to
`squash` (or `s`) on all but the first:

```
pick abc1111 add bomb
squash def2222 fix typo
squash ghi3333 oops forgot to register
squash jkl4444 actually subtract 5 not 50
squash mno5555 fix comment
```

Save and close the editor.

## 3. Edit the combined message

Git opens a second editor with the concatenated messages of all five commits.
Delete everything and write the one good message:

```
Add Bomb item that subtracts 5 points when caught

Closes #1.
```

Save and close.

## 4. Verify

```bash
git log --oneline feature/bomb-item
# pqr6666 Add Bomb item that subtracts 5 points when caught
# ... (main's history)
```

One commit. Clean.

## 5. Push (force, carefully)

Because rebasing changed commit hashes, plain `git push` will fail — your
local branch and `origin/feature/bomb-item` now have different histories.
You need to force-push, but **use `--force-with-lease`** to avoid stomping
on someone else's accidental push:

```bash
git push --force-with-lease
```

Your PR updates automatically. The "Files changed" tab is identical, but
"Commits" now shows one tidy commit instead of five.

---

## Other common rebase actions

### Reword a commit message

```
pick abc1111 add bomb
reword def2222 fix typo        # ← change this line
pick ghi3333 register bomb
```

When you save, Git pauses at `def2222` and lets you edit its commit message.

### Drop a commit you regret

```
pick abc1111 add bomb
drop  def2222 add giant explosion gif    # ← removed
pick ghi3333 register bomb
```

Or just delete the line entirely — same effect.

### Reorder commits

Reorder the lines in the editor. Git replays them in the new order.
(Conflicts may occur if commits depend on each other.)

### Stop mid-rebase to edit a commit

```
edit abc1111 add bomb
```

Git pauses after applying `abc1111`. Make your fixes, then:

```bash
git add ...
git commit --amend
git rebase --continue
```

### If you panic

```bash
git rebase --abort           # back to where you started
```

Or use `git reflog` and `git reset --hard <pre-rebase-hash>`. See
[Bonus 1](bonus-1-reflog-and-sync-fork.md).

---

## Rebase vs merge: when to use which

| | Merge | Rebase |
|---|---|---|
| Preserves branch shape | yes (merge commit) | no (linear history) |
| Safe on shared branches | yes | no |
| Use when... | bringing public branches together | cleaning your own private branch before review |

Many teams pick a convention: **rebase locally, merge to integrate.** That is,
clean your feature branch with interactive rebase, then merge (or squash-merge)
the PR. You get both clean per-PR history *and* clear "feature landed here"
points on main.

---

→ [Next: B4 — GitHub Actions & releases](bonus-4-actions-and-releases.md)
