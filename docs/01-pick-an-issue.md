# 01 — Pick an issue

In real projects, work doesn't start with code — it starts with an **issue**.
An issue is a ticket: a description of a bug, a feature request, or a task.
You pick one up, do the work, and your PR references it so people can trace
*why* the code changed.

---

## 1. Browse the issues

On the upstream repo's GitHub page, click the **Issues** tab. You'll see a
list like:

- `#1` Add a Bomb item — subtracts 5 points when caught  *(good-first-feature)*
- `#2` Add a GoldenApple — rare, worth 10 points  *(good-first-feature)*
- `#3` Add a Freeze powerup — slows all items for 3 seconds  *(good-first-feature)*
- ...

The `good-first-feature` **label** tells you this issue is small and
self-contained — a good place to start.

> **Filtering tip:** Use `is:open is:issue label:good-first-feature` in the
> search box to narrow it down.

## 2. Claim one

Pick one that nobody else has claimed. Then **leave a comment** like:

> I'd like to take this one!

If you have write access to the upstream repo, also click **Assign yourself**
in the right sidebar. If you don't (which is normal for forks), the comment
is enough — others will see you've claimed it.

> **Why claim it?** So two people don't accidentally build the same feature.

## 3. Read the issue carefully

Each issue has a description with what should happen, acceptance criteria,
and sometimes a hint about where to start. Re-read it before coding. Ask
clarifying questions as a comment if anything is ambiguous.

## 4. Note the issue number

You'll need it later. When you open your pull request, you'll write
**`Closes #N`** in the description — GitHub will auto-close the issue when
the PR merges and link the two together forever.

> **Why `Closes`?** GitHub recognizes the keywords `closes`, `fixes`, and
> `resolves` (plus variations like `closed`, `fixed`). Any of these followed
> by `#N` create an automatic link.

---

→ [Next: 02 — Branch and build](02-branch-and-build.md)
