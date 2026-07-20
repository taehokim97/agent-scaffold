# Progress: bootstrap-command

## Status: implementation complete, awaiting review/PR

## Done

- `specs/bootstrap-command/{README,spec,plan,tasks,findings}.md` written.
- Feature branch `feat/bootstrap-command` created.
- `src/agent_scaffold/source-structure/common/.claude/commands/bootstrap.md`
  written: 8-question interview, explore-before-ask, overwrite guard,
  `CLAUDE.md` write-back (4 existing sections + new `## Git Workflow`),
  spec-driven-development handoff (README.md + spec.md only, not
  plan/tasks).
- Dogfooded to `.claude/commands/bootstrap.md` (byte-identical, verified
  with `diff`).
- Korean mirror at `docs/ko/commands/bootstrap.md`, translation-note
  header pointing at the English source (same format as
  `docs/ko/agents/second-opinion.md`).
- `CHANGELOG.md` and `docs/ko/CHANGELOG.md` `[Unreleased]`/`Added`
  entries added.
- `tests/test_packaging.py`: `bootstrap.md` added to
  `EXPECTED_WHEEL_MEMBERS`.
- `tests/test_cli.py`: removed `.claude/commands` from
  `EXPECTED_EMPTY_DIRS` (see `findings.md`), added
  `test_ships_bootstrap_command`.
- `uv run pytest` (11 passed) and `uv run ruff check .` both clean.

## What's next

- Nothing implemented is left — all `tasks.md` items are done.
- Not yet done: opening the PR (branch exists locally, nothing pushed or
  committed yet — no commit has been made in this session). Whoever
  resumes should review the diff, commit, push, and open the PR per
  `CONTRIBUTING.md`.
- Not in scope for this spec (see `spec.md` Out of scope): a 3rd
  branch-strategy tier, and any `_template.py`/`cli.py` changes (none
  were needed).

## Files that matter

- `src/agent_scaffold/source-structure/common/.claude/commands/bootstrap.md`
  — canonical source, edit here first.
- `.claude/commands/bootstrap.md` — must stay byte-identical to the
  above (dogfood copy).
- `docs/ko/commands/bootstrap.md` — Korean mirror, update after the
  English source if content changes.
