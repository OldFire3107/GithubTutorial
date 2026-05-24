# 00 — Setup

By the end of this lesson you will have:

- A **fork** of the upstream repo on your own GitHub account
- A **local clone** of your fork
- An `upstream` remote pointing at the original repo
- A working `.venv` with `pygame` installed
- The game running on your machine

---

## 1. Fork the repo

On the upstream repo's GitHub page, click **Fork** (top right) → **Create fork**.
Leave the defaults. After a few seconds, GitHub redirects you to your own copy
at `github.com/<your-username>/GitHubTutorial`.

> **Why fork?** A fork is your personal copy on GitHub. You can push anything
> you like to it without needing permission on the original repo. When you're
> ready to share your work, you open a pull request from your fork back to the
> original — and the maintainers decide whether to merge.

## 2. Clone your fork locally

```bash
git clone https://github.com/<your-username>/GitHubTutorial.git
cd GitHubTutorial
```

`git clone` creates a local copy and automatically sets your fork as the
remote named `origin`. Check:

```bash
git remote -v
# origin  https://github.com/<your-username>/GitHubTutorial.git (fetch)
# origin  https://github.com/<your-username>/GitHubTutorial.git (push)
```

## 3. Add the upstream remote

The original repo isn't a remote yet. Add it:

```bash
git remote add upstream https://github.com/<UPSTREAM-OWNER>/GitHubTutorial.git
git remote -v
# origin    https://github.com/<your-username>/GitHubTutorial.git (fetch)
# origin    https://github.com/<your-username>/GitHubTutorial.git (push)
# upstream  https://github.com/<UPSTREAM-OWNER>/GitHubTutorial.git (fetch)
# upstream  https://github.com/<UPSTREAM-OWNER>/GitHubTutorial.git (push)
```

> **Why two remotes?**
> - `origin` = your fork. You **push** here.
> - `upstream` = the original. You **pull from** here to stay up to date.
>
> Later, when the maintainer changes `upstream/main`, you'll `git fetch upstream`
> to pull those changes into your local repo.

## 4. Install and run

### Mac / Linux / WSL
```bash
./install.sh
source .venv/bin/activate
python main.py
```

### Windows (cmd or PowerShell)
```cmd
install.bat
.venv\Scripts\activate
python main.py
```

You should see a window with a basket at the bottom and apples + stars falling.
Move the basket with ← → (or A / D). Catch some. Press **Esc** to quit.

> **What's a `.venv`?** A *virtual environment* — an isolated copy of Python
> just for this project. Installing `pygame` into `.venv` means it doesn't
> conflict with anything else on your system. The `.venv/` folder is in
> `.gitignore`, so it never gets committed.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `python: command not found` | Try `python3`. On Windows install from python.org and tick "Add Python to PATH". |
| `No module named venv` (Debian/Ubuntu) | `sudo apt install python3-venv` |
| `pygame` install fails on M1 Mac | Make sure you're on Python 3.10+ — older versions don't have prebuilt arm64 wheels |
| Window opens but nothing happens | Click the window first so it has keyboard focus |

---

When the game runs, you're done. → [Next: 01 — Pick an issue](01-pick-an-issue.md)
