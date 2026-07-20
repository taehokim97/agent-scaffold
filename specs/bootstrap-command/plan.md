# Plan: bootstrap-command

## Phase 1 — Branch

Create a feature branch (`feat/bootstrap-command`), per this repo's
branching rule (no direct pushes to `main`).

## Phase 2 — Draft the command (English, canonical)

Write
`src/agent_scaffold/source-structure/common/.claude/commands/bootstrap.md`:
frontmatter (`description`) + prompt body implementing the 8-question
interview, explore-before-ask behavior, the overwrite-guard check, the
`CLAUDE.md` write-back (four existing sections + new Git Workflow
section), and the spec-driven-development handoff. Match the tone/format
of the existing skills (`spec-driven-development/SKILL.md`,
`release-versioning/SKILL.md`) — short, imperative, tables where useful.

## Phase 3 — Dogfood copy

Copy the finished `bootstrap.md` byte-for-byte to
`.claude/commands/bootstrap.md` at the repo root.

## Phase 4 — Korean mirror

Translate into `docs/ko/commands/bootstrap.md`, with the standard
translation-note header linking back to the English source (matching
`docs/ko/agents/second-opinion.md`'s format).

## Phase 5 — Process

- Add a `CHANGELOG.md` `[Unreleased]` / `Added` entry (release-versioning
  skill).
- Add the new file's wheel path to `EXPECTED_WHEEL_MEMBERS` in
  `tests/test_packaging.py` for packaging-regression coverage, matching
  how `second-opinion.md` is already listed there.

## Phase 6 — Verify

- `uv run pytest`
- `uv run ruff check .`
- Re-read `bootstrap.md` once as a reviewer against `spec.md`'s "Done
  means" checklist.

## Phase 7 — Findings/progress hygiene

Log any decisions made mid-implementation (e.g. exact wording choices, if
they involved a tradeoff) to `findings.md`. Update `progress.md` at the
end of the session.
