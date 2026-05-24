# 06 — Review and merge

The PR doesn't go in until someone else reads it. Reviewing each other's PRs
is how teams catch bugs, share knowledge, and keep code consistent.

---

## 1. Pair up

Find a partner. You'll review their PR; they'll review yours.

## 2. Open their PR

On GitHub, click **Pull requests** on the upstream repo and find your
partner's. Open it.

## 3. Read the description first

- Does the title describe what's changing?
- Does the body say *why*?
- Is the linked issue clear?

If the description is empty or unclear, that's the first piece of feedback:
ask them to add context. Future you (or anyone reading `git log` in a year)
will thank them.

## 4. Read the diff

Click the **Files changed** tab. Look at every line that changed.

Things to look for, in roughly this order:

1. **Does it do what the issue asked?** If issue said "subtracts 5 points"
   and the code subtracts 10, that's a bug.
2. **Does it work?** Pull the branch and run the game if you can:
   ```bash
   git fetch origin pull/<PR-NUMBER>/head:review-<their-feature>
   git checkout review-<their-feature>
   python main.py
   ```
3. **Is it readable?** Could someone new to the codebase understand it?
4. **Does it follow the style of the rest of the codebase?** Match the
   existing patterns unless there's a reason not to.
5. **Are there obvious bugs?** Edge cases? Off-by-one? Missing
   `super().__init__()` call?

## 5. Leave comments

Hover over a line in the diff and click the **+** that appears. Type your
comment. You can:

- **Comment** — just a thought, no action required
- **Request changes** — block the merge until addressed
- **Approve** — looks good to merge

> **Reviewer etiquette:**
> - Be specific. "This could be clearer" → "Could `c` be renamed `color` here?"
> - Distinguish must-fix from nit. Many teams prefix optional comments with
>   `nit:` so the author knows they can skip them.
> - Praise good code too. PRs are a conversation, not a critique.

When you're done, click **Review changes** at the top right of the Files tab
and submit your review (with one of Comment / Approve / Request changes).

## 6. Address comments on your PR

When your reviewer leaves comments:

- For each one, either fix it or reply explaining why you disagree
- Push new commits to your branch — the PR updates automatically
- Once everything's addressed, click **Re-request review** to ping them

## 7. Merge

Once you have an approval (and the conversation is resolved), click **Merge
pull request**. GitHub gives you three options:

| Option | What it does | When to use |
|---|---|---|
| **Create a merge commit** | Adds a "Merge pull request #N" commit on top, preserving all your branch's history | Default. Honest about how the branch evolved. |
| **Squash and merge** | Collapses all your branch's commits into one new commit on main | When your branch has messy WIP commits you don't want in history |
| **Rebase and merge** | Replays your commits one by one on top of main (no merge commit) | When you want a linear history |

For a small feature, **squash and merge** is usually cleanest. The squashed
commit message will reference the PR number — and since you wrote
`Closes #1`, issue #1 auto-closes too.

## 8. Delete the branch

GitHub offers a **Delete branch** button after merging. Click it. The branch
is preserved in the PR forever; deleting it just removes the dangling
reference. Then locally:

```bash
git checkout main
git pull upstream main           # gets the merged version
git branch -d feature/bomb-item
```

> Note: `-d` (lowercase) refuses to delete if the branch isn't merged. Use
> `-D` (uppercase) to force-delete — only when you're sure.

---

## 🎉 You shipped a feature

Take a moment. You forked a repo, picked an issue, branched, built, opened a
PR, dealt with an upstream refactor, resolved real conflicts, got it
reviewed, and merged it. That's the full collaborative loop.

If you have time, keep going with the bonus modules — they cover the rest
of the GitHub workflow you'll see in real teams:

→ [B1 — Reflog & sync your fork](bonus-1-reflog-and-sync-fork.md)
→ [B2 — Issues, labels, milestones](bonus-2-issues-labels-milestones.md)
→ [B3 — Interactive rebase](bonus-3-rebase.md)
→ [B4 — GitHub Actions & releases](bonus-4-actions-and-releases.md)
→ [B5 — Going further](bonus-5-going-further.md)
