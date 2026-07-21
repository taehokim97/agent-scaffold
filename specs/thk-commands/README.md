# thk-commands

## Background

This scaffold ships four skills (`spec-driven-development`,
`release-versioning`, `research-brief`, `reproducible-debugging`), each
triggered only by Claude Code matching its `description` against the
current conversation. That auto-trigger is probabilistic, not guaranteed
— this repo hit it directly while building `/thk-bootstrap`
(`specs/bootstrap-command/`): a project-scoped skill went undiscovered
by the `Skill` tool until a file under its directory had been read in
the same session, purely because of a cwd mismatch. A skill that isn't
discovered doesn't get used, no matter how good its description is.

Explicit commands don't have that failure mode — the human decides when
to invoke them. Following up on `/thk-bootstrap` (see
`specs/bootstrap-command/`) and the naming-prefix decision made there
(`thk-`, documented in `commands/README.md`), this adds an explicit
command for three of the four skills:

- `/thk-spec` → `spec-driven-development`
- `/thk-ship` → `release-versioning`
- `/thk-research` → `research-brief`

`reproducible-debugging` is explicitly left out for now — not ruled out
forever, just not part of this batch (the user's call when scoping this
work).

## Why not just thin wrappers

A command that says nothing but "go read skill X" would duplicate the
skill's own description and add a maintenance burden (two places to keep
in sync) without adding value. Each command earns its place by doing
something the skill file alone doesn't:

- `/thk-spec` — turns "explore facts yourself" into an explicit nudge to
  delegate wide codebase exploration to a subagent, so survey output
  doesn't pollute the interview's context (the context-drift mitigation
  raised when this was discussed).
- `/thk-ship` — chains a concrete pre-flight (run the project's own
  test/lint commands from `CLAUDE.md`) before classifying and drafting,
  so a broken build never gets shipped a changelog entry.
- `/thk-research` — turns the skill's four brief fields (question, in
  scope, out of scope, stop condition) into an explicit short interview,
  and asks up front whether this is a foreground or handed-off session
  (surfacing the skill's "never bypass permissions to fake unattended"
  rule as a decision point, not a rule the user has to already know).

## Bundling

All three ship in the same PR as the `thk-bootstrap` rename
(`specs/bootstrap-command/findings.md`, 2026-07-20 entry) — the user's
call, made explicit because the project is still pre-1.0 (`0.1.0`) and
not tightly bound by one-PR-per-change discipline yet.
