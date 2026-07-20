# Progress: thk-commands

## Status: implementation complete, not yet committed

## Done

- `specs/thk-commands/{README,spec,plan,tasks,findings}.md` written.
- Branch `feat/thk-commands` created from updated `origin/main` (after
  `specs/bootstrap-command`'s PR #8 merged); the `thk-bootstrap` rename
  commit (`770e947`, cherry-picked from the old branch) is the first
  commit here.
- `thk-spec.md`, `thk-ship.md`, `thk-research.md` written in the
  payload, dogfooded, and mirrored in Korean.
- `CHANGELOG.md` / `docs/ko/CHANGELOG.md` updated (one bundled entry
  covering all three).
- `tests/test_cli.py`: added `test_ships_thk_spec_command`,
  `test_ships_thk_ship_command`, `test_ships_thk_research_command`.
- `tests/test_packaging.py`: added all three paths to
  `EXPECTED_WHEEL_MEMBERS`.
- `uv run pytest` (14 passed) and `uv run ruff check .` both clean.

## What's next

- Nothing implemented is left — all `tasks.md` items done.
- Not yet committed or pushed — confirm with the user before either
  (each git action has been separately authorized this session).
- `/thk-debug` (`reproducible-debugging`) intentionally not built — see
  `findings.md`.

## Files that matter

- `src/agent_scaffold/source-structure/common/.claude/commands/thk-{spec,ship,research}.md`
  — canonical sources.
- `.claude/commands/thk-{spec,ship,research}.md` — dogfood copies, must
  stay byte-identical.
- `docs/ko/commands/thk-{spec,ship,research}.md` — Korean mirrors.
