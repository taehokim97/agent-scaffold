---
description: Open (or resume) a specs/<slug>/ folder for a piece of work using the spec-driven-development skill, as an explicit entry point instead of relying on the skill auto-triggering.
---

# /thk-spec

An explicit front door to the `spec-driven-development` skill, for
whenever you don't want to rely on Claude Code matching the skill's
description on its own — that matching is probabilistic, not
guaranteed, especially for project-scoped skills.

## Resume check first

Ask what piece of work this is for, then check whether
`specs/<slug>/progress.md` already exists for it. If it does, read the
whole `specs/<slug>/` folder — not just `progress.md` — before doing
anything else, and continue from there instead of starting the interview
over.

## If this is new

Delegate wide exploration, don't do it inline. Before interviewing, if
the codebase or the area of work is large or unfamiliar, use a subagent
to survey existing code and conventions relevant to this work, and bring
back only what's needed to ask good questions. The skill's "explore
facts yourself" step is meant to keep the human from re-explaining what
you could find out — it isn't meant to fill your own context with a wide
file-by-file survey.

From there, follow the `spec-driven-development` skill exactly as
documented: interview one question at a time, write `README.md` (why)
before `spec.md` (what), then `plan.md` and `tasks.md` once the spec is
agreed. This command doesn't change that sequence — it's the explicit
trigger for it.
