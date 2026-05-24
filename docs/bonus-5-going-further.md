# Bonus 5 — Going further

You've covered the day-to-day collaborative workflow. Here's a curated list
of next things to learn, roughly in order of how often you'll meet them on
a real team.

This page is **pointers, not lessons** — each link goes somewhere with a
better explanation than this doc could fit.

---

## Git fundamentals you'll keep deepening

| Topic | Why it matters | Where to learn |
|---|---|---|
| **`git diff` deep-dive** | The fastest way to know what's about to change | [`git help diff`](https://git-scm.com/docs/git-diff), then practice with `--stat`, `--word-diff`, `-w` |
| **`git blame`** | Find out *who* and *why* for any line | [git blame docs](https://git-scm.com/docs/git-blame) — try `git blame -L 10,20 main.py` |
| **`git bisect`** | Binary-search through history to find the commit that broke something | [Atlassian: git bisect](https://www.atlassian.com/git/tutorials/advanced-overview#git-bisect) |
| **`git cherry-pick`** | Apply a single commit from one branch onto another | [git cherry-pick docs](https://git-scm.com/docs/git-cherry-pick) |
| **The reflog (deeper)** | Recover from *any* accident, not just `reset` | [git reflog docs](https://git-scm.com/docs/git-reflog) |
| **`.gitattributes`** | Line-ending normalization, diff/merge drivers, marking generated files | [Pro Git: Customizing Git → Git Attributes](https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes) |
| **Hooks** | Run scripts on commit, push, etc. — auto-format, run tests, prevent secrets | [Pro Git: Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) |

The classic book — free, well-written — is **[Pro Git](https://git-scm.com/book/en/v2)**. Chapter 7 covers the advanced stuff.

---

## GitHub collaboration features

| Feature | Why | Where |
|---|---|---|
| **Protected branches** | Prevent direct pushes to `main`, require reviews, require passing CI | Settings → Branches |
| **`CODEOWNERS` file** | Auto-request reviews from the right people for the right files | [docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) |
| **Required reviewers** | "This PR cannot merge until N approvals from group X" | Branch protection rules |
| **Draft PRs** | Open early for visibility, mark ready for review later | Dropdown on PR creation |
| **Suggested changes** | Reviewers propose exact replacement text, author one-clicks | The "+" button in a diff comment |
| **PR templates** | Auto-fill the PR description like issue templates | `.github/pull_request_template.md` |
| **Discussions** | Forum-style threads attached to the repo, not tied to issues/PRs | Settings → enable Discussions |
| **Projects (v2)** | Kanban / table view across multiple repos | Repo's Projects tab |
| **`gh` CLI** | Drive GitHub from the terminal — PRs, issues, reviews, releases | [cli.github.com](https://cli.github.com) |

---

## Security and signing

| Topic | Why |
|---|---|
| **GPG/SSH signed commits** | A "Verified" badge proves the commit came from your key, not a spoof |
| **`gh auth` + fine-grained PATs** | Modern personal access tokens with per-repo scope |
| **Dependabot** | GitHub auto-opens PRs to bump vulnerable dependencies |
| **`secrets`** | Encrypted variables Actions workflows can access without exposing them |

[GitHub docs: Securing your account](https://docs.github.com/en/authentication) is the entry point.

---

## Interactive playgrounds

These let you practice Git commands in a sandbox without breaking anything
real:

- **[Learn Git Branching](https://learngitbranching.js.org/)** — visualizes branches as you type commands. The single best way to build intuition for `merge`, `rebase`, `cherry-pick`.
- **[GitHub Skills](https://skills.github.com/)** — free GitHub-run courses, each one a real repo you fork and work in. The "Resolve merge conflicts" course is a nice complement to lesson 05.
- **[Oh Shit, Git!?!](https://ohshitgit.com/)** — "I committed and now I want to undo" cheat sheet for common mistakes.

---

## Books and long reads

- **[Pro Git](https://git-scm.com/book/en/v2)** — free online, exceptionally well-written
- **[Think Like (a) Git](http://think-like-a-git.net/)** — when Git's mental model finally clicks
- **["A successful Git branching model"](https://nvie.com/posts/a-successful-git-branching-model/)** (gitflow) — read once for vocabulary; most teams use something simpler now
- **["Trunk Based Development"](https://trunkbaseddevelopment.com/)** — the modern counterpoint to gitflow

---

## Workflow patterns to be aware of

You'll see all of these in the wild. None is universally "right":

- **GitHub Flow** — `main` is always deployable; short-lived feature branches; PR to merge. (This tutorial.)
- **Git Flow** — long-lived `develop` and `release/*` branches alongside `main`. Heavier; mostly seen in versioned products.
- **Trunk-Based Development** — tiny, very-short-lived branches; feature flags hide unfinished work in production. Common at big tech.
- **Release Train** — scheduled merge windows; everything that's ready by date X ships.

---

## What to build next

If you want to extend this game further:

- Replace colored shapes with sprite images (pygame's `image.load`)
- Add sound effects on catch / miss (pygame's `mixer`)
- Add a high-score file (`json` or `pickle`)
- Animate the basket / items
- Make a second level with a different background
- Port to the web with [pygbag](https://pypi.org/project/pygbag/)

Each is its own issue, branch, PR. Same loop, more practice.

---

**You're done with the workshop.** Go forth and contribute.
