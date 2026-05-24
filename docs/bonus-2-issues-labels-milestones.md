# Bonus 2 — Issues, labels, milestones, PR linking

You've used issues as pickup tickets. Time to see how teams actually organize
them: labels for filtering, milestones for grouping work toward a release,
templates so every issue arrives with the info you need, and PR auto-linking
so nothing falls through the cracks.

---

## 1. Labels

Labels are colored tags you attach to issues and PRs. They're the primary
way to filter.

On the upstream repo (instructor demo): **Issues → Labels → New label**.

Useful labels for this tutorial repo:

| Label | Color | Meaning |
|---|---|---|
| `good-first-feature` | green | small, self-contained, ideal for newcomers |
| `bonus` | purple | harder; for fast finishers |
| `bug` | red | something is broken |
| `enhancement` | blue | improving existing behavior |
| `docs` | gray | docs only, no code change |
| `needs-design` | yellow | not ready to implement — discuss first |
| `blocked` | dark red | waiting on something/someone |

Apply labels by opening an issue and clicking **Labels** in the right sidebar.

> **Tip:** Once labels exist, search with `is:open is:issue label:bug` to
> filter. You can combine them: `label:bug label:good-first-feature`.

## 2. Milestones

A milestone groups issues toward a deliverable, usually a version or a date.

**Issues → Milestones → New milestone**:

- Title: `v1.0`
- Due date: end of the workshop
- Description: "First playable release with at least 5 new item types"

Then attach issues to it via the **Milestone** sidebar option. The milestone
page shows a progress bar — % closed vs open.

> **When to use milestones:** when several issues only matter together
> ("the release we're cutting Friday"). Don't use one per issue — that's
> what labels are for.

## 3. Issue templates

Every issue arriving with the same minimum info saves enormous time. Add an
issue template to the repo:

Create `.github/ISSUE_TEMPLATE/feature.md`:

```markdown
---
name: Feature request
about: Suggest a new falling item, powerup, or game mechanic
title: 'Add a ... '
labels: 'enhancement'
assignees: ''
---

## What
<!-- One-sentence description -->

## Acceptance criteria
- [ ] ...
- [ ] ...

## Notes / hints
<!-- Implementation ideas, files to look at, etc. -->
```

After committing this file, GitHub's **New issue** page will offer "Feature
request" as a template choice. Anyone who clicks it gets the form pre-filled.

You can have multiple templates (`bug.md`, `docs.md`, etc.) — each one
becomes a button on the New Issue page.

## 4. PR auto-linking with `Closes #N`

You already used this in [lesson 03](03-open-a-pr.md). The mechanics in full:

In a PR description (or any commit message that ends up on `main`), write
**any of these**:

```
Closes #1
closes #1
fixes #1
Fixed #1
resolves #1
```

When the PR merges, issue #1 is automatically closed and a "linked PR"
appears on the issue page. This means anyone reading the issue can jump
straight to the PR that solved it, and `git log --grep="#1"` finds the
commit.

> **For multi-issue PRs:** `Closes #1, closes #2, closes #3` works — but
> you must repeat the keyword. `Closes #1, #2, #3` only closes #1.

## 5. Putting it together

A realistic workflow on a team:

1. PM files issues from the backlog, labels them, attaches to current milestone
2. Engineer browses `is:open milestone:v1.0 label:good-first-feature no:assignee`
3. Self-assigns, opens a feature branch, builds
4. PR description has `Closes #42` — the linkage is automatic
5. PR merges → issue closes → milestone progress bar advances
6. When the milestone hits 100%, the release goes out

No process tool needed beyond GitHub itself.

---

→ [Next: B3 — Interactive rebase](bonus-3-rebase.md)
