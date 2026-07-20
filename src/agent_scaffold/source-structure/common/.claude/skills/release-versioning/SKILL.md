---
name: release-versioning
description: Use when a change is ready to ship and needs a version-bump
  decision and a CHANGELOG entry. Classifies the change against Semantic
  Versioning and drafts the entry in Keep a Changelog format.
---

# Release versioning

## Classify the change

- **MAJOR** — breaking: a public API, CLI flag, or config shape is
  removed or changed incompatibly; a file the project always shipped is
  removed.
- **MINOR** — a backward-compatible addition: a new feature, flag, or
  file that doesn't change existing behavior.
- **PATCH** — a bug fix, or a wording/doc change with no behavior change.

Before writing a "Breaking" entry, check whether the change it's undoing
ever actually shipped in a released version. A change that only ever
existed under `[Unreleased]` isn't breaking anything for anyone who
installed a release — reverting it is just editing history that hasn't
gone out yet, not a MAJOR bump.

## Draft the entry

Add to the `[Unreleased]` section of `CHANGELOG.md`, under the matching
Keep a Changelog heading (`Added`, `Changed`, `Deprecated`, `Removed`,
`Fixed`, `Security`). One line per change, imperative mood, written for
someone deciding whether to upgrade — not implementation detail.

```markdown
## [Unreleased]

### Added

- Short, user-facing description of what changed and why it matters.
```

If the project keeps a translated CHANGELOG (e.g. `docs/ko/CHANGELOG.md`),
mirror the same entry there.

## Rationalization check

| Thought | Rebuttal |
|---|---|
| "This is minor, I'll skip the changelog entry." | If it's user-visible at all, it belongs in the changelog — that's what "minor" (lowercase) means, not "skip it." |
| "I'll just call everything Added, it's simpler." | Wrong category makes the changelog unreadable at release time. Removed and Changed exist for a reason — use them. |
| "I already know it's a MAJOR bump, no need to check if it shipped." | Checking costs one look at the last released version's changelog. Bumping MAJOR for something nobody ever depended on trains people to ignore your MAJOR bumps. |
