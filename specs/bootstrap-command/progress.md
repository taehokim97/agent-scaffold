# Progress: bootstrap-command

## Status: implementation complete (including rename to `thk-bootstrap`), first commit pushed; rename commit not yet pushed

## Done

- `specs/bootstrap-command/{README,spec,plan,tasks,findings}.md` written.
- Feature branch `feat/bootstrap-command` created, pushed, tracking
  `origin/feat/bootstrap-command`.
- Command written: 8-question interview, explore-before-ask, overwrite
  guard, `CLAUDE.md` write-back (4 existing sections + new `## Git
  Workflow`), spec-driven-development handoff (README.md + spec.md only,
  not plan/tasks).
- Dogfooded copy and Korean mirror kept in sync (byte-identical for the
  dogfood copy, verified with `diff`).
- `CHANGELOG.md` and `docs/ko/CHANGELOG.md` `[Unreleased]`/`Added`
  entries added.
- `tests/test_packaging.py` / `tests/test_cli.py` updated accordingly
  (see `findings.md` for the stale-test fix).
- First commit (`feat: add bootstrap command`) made and pushed.
- **Renamed `bootstrap.md` → `thk-bootstrap.md` everywhere** (see
  `findings.md` 2026-07-20 entry) after a follow-up discussion concluded
  commands need a collision-avoiding filename prefix, since
  `.claude/commands/` has no directory-based namespacing. Also added a
  "Naming" section to `commands/README.md` documenting the `thk-`
  convention for future commands. `uv run pytest` (11 passed) and
  `uv run ruff check .` both clean after the rename.

## What's next

- The rename is committed locally but not yet pushed / not yet part of
  a PR — confirm with the user before pushing again (each push was
  separately authorized in this session).
- Consider whether more skills should get an explicit `thk-`-prefixed
  command entry point (discussed: `/thk-spec`, `/thk-ship`, `/thk-debug`,
  `/thk-research` mirroring `spec-driven-development`,
  `release-versioning`, `reproducible-debugging`, `research-brief`) — no
  decision made yet, this was still at the brainstorming stage.
- Not in scope for this spec (see `spec.md` Out of scope): a 3rd
  branch-strategy tier, and any `_template.py`/`cli.py` changes (none
  were needed).

## Files that matter

- `src/agent_scaffold/source-structure/common/.claude/commands/thk-bootstrap.md`
  — canonical source, edit here first.
- `.claude/commands/thk-bootstrap.md` — must stay byte-identical to the
  above (dogfood copy).
- `docs/ko/commands/thk-bootstrap.md` — Korean mirror, update after the
  English source if content changes.
- `src/agent_scaffold/source-structure/common/.claude/commands/README.md`
  — documents the `thk-` naming convention for contributors.
