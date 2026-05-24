# Bonus 4 — GitHub Actions & releases

Two things real projects don't ship without:

- **Continuous Integration (CI)** — automated checks that run on every PR
- **Releases** — tagged snapshots that you (and users) can come back to

GitHub provides both for free with **GitHub Actions** and **Releases**.

---

## Part A: A first CI workflow

Goal: every PR runs a syntax check + a lint check. If either fails, the PR
is blocked from merging.

### 1. Create the workflow file

```bash
mkdir -p .github/workflows
```

Create `.github/workflows/check.yml`:

```yaml
name: check

on:
  pull_request:
  push:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install ruff
        run: pip install ruff

      - name: Syntax check
        run: python -m compileall -q .

      - name: Lint
        run: ruff check .
```

### 2. Commit and push

```bash
git checkout -b ci/add-checks
git add .github/workflows/check.yml
git commit -m "Add CI: syntax check + ruff lint on PRs"
git push -u origin ci/add-checks
```

Open a PR for it. On the PR's **Checks** tab you'll see the workflow run
live — green ✓ if everything passes, red ✗ otherwise.

### 3. What `on:` does

```yaml
on:
  pull_request:
  push:
    branches: [main]
```

- Run on **every PR** (any branch → any branch)
- Run on **direct pushes to `main`** (which shouldn't happen if you have
  branch protection, but belt-and-braces)

You can also trigger on:
- `schedule:` — cron jobs
- `workflow_dispatch:` — manual button on the Actions tab
- specific events: `issues`, `release`, etc.

### 4. (Optional) Require checks to pass

In **Settings → Branches → Branch protection rules**, add a rule for `main`:

- ✅ Require status checks to pass before merging
- Select `lint` from the list

Now the **Merge** button is greyed out on any PR with failing checks.

---

## Part B: Tagging a release

Once enough features have merged that you want a "v1.0" snapshot:

### 1. Make sure local main is up to date

```bash
git checkout main
git pull upstream main
```

### 2. Tag the commit

```bash
git tag -a v1.0 -m "v1.0: first playable release"
git push upstream v1.0
```

`-a` makes an *annotated* tag (it stores the message, your name, and the
date — recommended for releases). A *lightweight* tag (`git tag v1.0`
without `-a`) is just a pointer.

### 3. Draft the release on GitHub

On the upstream repo: **Releases → Draft a new release**.

- **Choose a tag:** select `v1.0`
- **Release title:** `v1.0 - Workshop release`
- **Description:** click **Generate release notes** — GitHub auto-fills with
  the list of merged PRs and contributors since the last tag. Edit as needed.
- Optionally attach binaries (zipped build, screenshots, etc.) by dragging
  into the description box.
- Click **Publish release**.

You now have a permanent URL like `github.com/.../releases/tag/v1.0` that
anyone can download and run.

### What good release notes look like

```markdown
## v1.0 — first playable release

### New items
- Bomb — subtracts 5 points when caught (#1, @alice)
- GoldenApple — rare, worth 10 points (#2, @bob)
- Freeze powerup — slows all items for 3s (#3, @carol)

### Internals
- Refactored `FallingItem` base class to use `pos` tuples and `weight`
- New `ITEMS` registry shape: `{"good": [...], "bad": [...]}`

### Thanks
First-time contributors: @alice, @bob, @carol, @dave
```

---

## Versioning convention

The standard is [Semantic Versioning](https://semver.org): `MAJOR.MINOR.PATCH`.

- `v1.0.1` — bugfix only
- `v1.1.0` — backward-compatible new feature
- `v2.0.0` — breaking change

For a workshop game it doesn't matter much, but it's a useful habit.

---

→ [Next: B5 — Going further](bonus-5-going-further.md)
