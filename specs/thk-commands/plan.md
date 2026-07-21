# Plan: thk-commands

## Phase 1 — Draft the three commands (English, canonical)

Write `thk-spec.md`, `thk-ship.md`, `thk-research.md` under
`src/agent_scaffold/source-structure/common/.claude/commands/`, each per
`spec.md`'s per-command requirements. Match `thk-bootstrap.md`'s tone and
structure (purpose line, numbered/tabled steps, explicit handoff to the
underlying skill).

## Phase 2 — Dogfood copies

Copy each byte-for-byte to `.claude/commands/<name>.md`.

## Phase 3 — Korean mirrors

Translate each into `docs/ko/commands/<name>.md` with the standard
translation-note header.

## Phase 4 — Process

- Add `CHANGELOG.md` / `docs/ko/CHANGELOG.md` entries.
- Add the three new paths to `EXPECTED_WHEEL_MEMBERS` in
  `tests/test_packaging.py`.
- Add `test_ships_thk_spec_command`, `test_ships_thk_ship_command`,
  `test_ships_thk_research_command` to `tests/test_cli.py`.

## Phase 5 — Verify

- `uv run pytest`
- `uv run ruff check .`
- Re-read each command against `spec.md`'s per-command requirements and
  the "Why not just thin wrappers" differentiation.

## Phase 6 — Findings/progress hygiene

Log decisions/tradeoffs to `findings.md` as they happen. Update
`progress.md` before ending the session.
