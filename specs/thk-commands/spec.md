# Spec: thk-commands

## Requirements

### Shared

- Three new files under
  `src/agent_scaffold/source-structure/common/.claude/commands/`:
  `thk-spec.md`, `thk-ship.md`, `thk-research.md`. Same frontmatter
  shape as `thk-bootstrap.md` (`description` only, no arguments/
  `$ARGUMENTS` — confirmed: interview-style, matching `thk-bootstrap`).
  No new "Naming" doc changes needed — `commands/README.md` already
  documents the `thk-` prefix.
- Each dogfooded byte-identical to `.claude/commands/<name>.md`, and
  mirrored in Korean at `docs/ko/commands/<name>.md` with the standard
  translation-note header.
- `CHANGELOG.md` / `docs/ko/CHANGELOG.md`: one `[Unreleased]`/`Added`
  entry per command (MINOR each, per `CONTRIBUTING.md`).
- `tests/test_cli.py`: one `test_ships_thk_<name>_command` per command
  (matches the `test_ships_thk_bootstrap_command` pattern already
  there).
- `tests/test_packaging.py`: all three paths added to
  `EXPECTED_WHEEL_MEMBERS`.
- `uv run pytest` and `uv run ruff check .` pass.

### `/thk-spec` (→ `spec-driven-development`)

- States purpose: open (or resume) a `specs/<slug>/` for a piece of work
  using the `spec-driven-development` skill.
- Before interviewing, explicitly says: if the codebase or the area of
  work is large/unfamiliar, delegate the "explore facts yourself" step
  (reading existing code and conventions the skill calls for) to a
  subagent, and bring back only what's needed to ask good questions —
  don't let a wide survey fill up the main conversation.
- Then follows the skill's own flow as documented (interview → README.md
  → spec.md → plan.md → tasks.md) — this command doesn't reinvent that
  sequence, it's the explicit front door to it.
- Handles resume: if `specs/<slug>/progress.md` already exists for the
  named piece of work, read it first and continue from there instead of
  starting the interview over.

### `/thk-ship` (→ `release-versioning`)

- States purpose: classify the current diff and draft a CHANGELOG entry
  before shipping.
- Pre-flight, before classifying: run the project's own build/test/lint
  commands (read from `CLAUDE.md`'s `## Build & Test` section — don't
  hardcode a command, since target projects vary). If they fail, stop
  and say so instead of drafting a changelog entry for a broken build.
- Then follows the `release-versioning` skill as documented (classify →
  draft the `[Unreleased]` entry → mirror to a translated CHANGELOG if
  one exists).
- Ends by stating the entry it drafted and asking the human to confirm
  before it's considered final — the skill file itself doesn't include a
  confirmation step, the command adds it.

### `/thk-research` (→ `research-brief`)

- States purpose: turn an open research question into a scoped brief
  before running it.
- Asks, one at a time, for the skill's four brief fields: the question,
  what's in scope, what's explicitly out of scope, and the stop
  condition (time-boxed / N sources / confidence reached) — the skill
  file assumes these are already known; this command is what actually
  elicits them.
- Asks explicitly whether this is a foreground session (answer now) or
  being handed off to run unattended (a long/self-paced session) —
  surfacing the skill's "never fake unattended by bypassing permission
  prompts" rule as something confirmed up front, not assumed.
- Writes `research/<slug>/findings.md`'s header block per the skill,
  then proceeds (or hands off) to research.

## Out of scope

- `/thk-debug` (`reproducible-debugging`) — explicitly excluded from
  this batch.
- `$ARGUMENTS`/`argument-hint` support for any command — confirmed
  interview-style only, no inline arguments.
- Any change to `_template.py`/`cli.py`.

## Done means

- [ ] All three commands exist in the payload, dogfooded copy, and
      Korean mirror, consistent with each other.
- [ ] Each has a stated differentiated value (see README.md "Why not
      just thin wrappers") actually present in its prompt body, not just
      a skill-invocation one-liner.
- [ ] `CHANGELOG.md` / `docs/ko/CHANGELOG.md` updated (one entry each or
      bundled — writer's call at drafting time).
- [ ] `pytest` and `ruff check` pass.
