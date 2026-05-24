# Catch the Falling Items — a Git & GitHub workshop

A tiny [Pygame](https://www.pygame.org/) game built as a hands-on excuse to
practice the parts of Git and GitHub that day-to-day `add` / `commit` / `push`
doesn't teach you: **branches, pull requests, code review, stashing, and merge
conflicts you actually have to think about**.

You play it. You add a feature to it. You open a PR. Then halfway through, the
maintainer merges a big refactor into `main` and you have to deal with the
fallout — just like real life.

---

## What it looks like

A basket at the bottom of the screen, items falling from the top. Catch the
good ones, dodge the bad ones, don't miss too many.

The starter repo ships with **apples** (+1 point) and **stars** (+3 points).
Everything else — bombs, powerups, golden apples, magnets — is something you
get to build during the workshop.

---

## Quick start

### Mac, Linux, WSL
```bash
./install.sh
source .venv/bin/activate
python main.py
```

### Windows
```cmd
install.bat
.venv\Scripts\activate
python main.py
```

The install script auto-detects your platform (macOS / Debian-Ubuntu / Arch /
Windows), checks for Python 3.8+, creates a `.venv`, and installs `pygame`.

**Controls:** ← → (or A / D) to move the basket. **Esc** to quit.

---

## The tutorial

Lessons live in [docs/](docs/) and are numbered. Work through them in order.
The first six are the **core path** (≈ 90 min total). The `bonus-*` files are
extensions you can do same-session or come back to later.

| # | Lesson | What you'll learn |
|---|---|---|
| 00 | [Setup](docs/00-setup.md) | Fork, clone, add upstream remote, install, run |
| 01 | [Pick an issue](docs/01-pick-an-issue.md) | Browse issues, self-assign, the `Closes #N` convention |
| 02 | [Branch and build](docs/02-branch-and-build.md) | Feature branches; create your falling item |
| 03 | [Open a PR](docs/03-open-a-pr.md) | Push your branch, open a pull request, link the issue |
| 04 | [Stash side-quest](docs/04-stash-side-quest.md) | `git stash` when you need to switch contexts mid-feature |
| 05 | [The conflict](docs/05-the-conflict.md) | `newupdate` refactored the base class — resolve the merge conflicts |
| 06 | [Review and merge](docs/06-review-and-merge.md) | Review a teammate's PR, request changes, approve, merge |

### Bonus (each ≈ 20–30 min)

| # | Lesson | What you'll learn |
|---|---|---|
| B1 | [Reflog & sync your fork](docs/bonus-1-reflog-and-sync-fork.md) | Recover from a bad `reset --hard`; keep your fork in sync with upstream |
| B2 | [Issues, labels, milestones](docs/bonus-2-issues-labels-milestones.md) | Real project management on GitHub |
| B3 | [Interactive rebase](docs/bonus-3-rebase.md) | Squash, reword, reorder commits before opening a PR |
| B4 | [GitHub Actions & releases](docs/bonus-4-actions-and-releases.md) | Run checks on every PR; tag a release |
| B5 | [Going further](docs/bonus-5-going-further.md) | Pointers to protected branches, CODEOWNERS, signed commits, and more |

---

## For instructors

- Pre-create the GitHub issues listed in `main.py`'s docstring (one per
  participant minimum), labeled `good-first-feature`.
- Have the `newupdate` branch ready on the upstream repo **before** the
  workshop. Do not merge it. Merge it into `upstream/main` partway through
  lesson 05 — once everyone has pushed their feature branches and opened PRs.
- Allow ~10 min for setup help on lesson 00 (Windows users especially).
