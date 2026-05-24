# 03 — Open a pull request

A **pull request** (PR) is the proposal: "I think this code should go into
your branch — please review it." It's a conversation, not a one-shot.

---

## 1. Push your branch to your fork

```bash
git push -u origin feature/bomb-item
```

The `-u` (short for `--set-upstream`) tells Git to remember the mapping
between your local branch and `origin/feature/bomb-item`. Future pushes can
just be `git push`.

> **Why push to `origin`, not `upstream`?** You don't have write access to
> the upstream repo. Your fork is where you publish. The PR is how you ask
> for that work to be pulled across.

After pushing, GitHub will print something like:

```
remote: Create a pull request for 'feature/bomb-item' on GitHub by visiting:
remote:      https://github.com/<your-username>/GitHubTutorial/pull/new/feature/bomb-item
```

Click that link, or go to your fork on GitHub — there'll be a yellow banner
prompting you to open a PR.

## 2. Fill in the PR

GitHub's "Open a pull request" page has two important things to set:

- **base repository:** `<UPSTREAM-OWNER>/GitHubTutorial`, branch `main`
- **head repository:** `<your-username>/GitHubTutorial`, branch `feature/bomb-item`

(Read it as: "merge **head** *into* **base**.")

Then a title and description. Keep the title short and action-oriented, like
your commit message:

> Add Bomb item that subtracts 5 points when caught

For the description, a useful template:

```markdown
## What

Adds a Bomb falling item. Bombs are dark circles with a red fuse spark; catching
one subtracts 5 points from the player's score.

## Why

Closes #1.

## How to test

1. `python main.py`
2. Move the basket under a black item.
3. Verify the score decreases by 5.

## Screenshots

![bomb](https://...)  <!-- optional -->
```

The magic line is **`Closes #1`** — when this PR merges, issue #1 automatically
closes and links to the PR forever.

Click **Create pull request**.

## 3. What just happened

- A PR now exists on the upstream repo
- A "Files changed" tab shows the diff
- A "Conversation" tab is where review comments live
- A "Checks" tab will show any automated tests (more on this in [bonus 4](bonus-4-actions-and-releases.md))

If you push more commits to `feature/bomb-item` on your fork, the PR updates
automatically. **No need to re-open it.** This is one of GitHub's nicer
properties: a PR tracks the branch, not a fixed snapshot.

## 4. (Optional) Draft PRs

If your work isn't ready for review but you want to share progress, open the
PR as a **draft** (there's a dropdown next to the "Create pull request"
button). Draft PRs can't be merged, and reviewers know not to nitpick yet.

---

→ [Next: 04 — Stash side-quest](04-stash-side-quest.md)
