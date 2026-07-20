---
name: spec-driven-development
description: Use when starting non-trivial feature work, when a design
  decision or mistake happens mid-implementation, or when resuming work
  after a break. Maintains a specs/<slug>/ folder — background, spec,
  plan, tasks, findings, and a resumption log — instead of losing that
  context to chat history.
---

# Spec-driven development

A one-line fix doesn't need this. Anything that takes more than one
sitting, or that a decision could get lost from, does.

## The specs/`<slug>`/ folder

Every non-trivial feature gets its own directory,
`specs/<kebab-case-slug>/`, holding six files:

| File | Holds |
|---|---|
| `README.md` | Background — why this work exists, what problem it solves |
| `spec.md` | Requirements — what "done" means, in testable terms |
| `plan.md` | Implementation plan — phases, in the order they'll be built |
| `tasks.md` | Actionable checklist — check items off as you go |
| `findings.md` | Discoveries, decisions, and mistakes, with dates |
| `progress.md` | A resumption log: what's done, what's next, what to reload |

## Starting a spec

Interview first, don't draft alone. One question at a time. Explore facts
yourself (read the code, check existing conventions); ask the human only
for decisions. Write `README.md` (the "why") before `spec.md` (the
"what") — a spec without a stated background invites scope creep later.

Once the spec is agreed, write `plan.md` (phases) and `tasks.md`
(concrete, checkable steps derived from the plan) before touching code.

## While implementing

Append to `findings.md` the moment a decision, a rejected alternative, or
a mistake happens — not at the end of the session. Each entry: date, what
happened, why, what was rejected and why. A decision made without writing
down the alternative looks arbitrary to whoever reads it later (including
you, next week).

Update `progress.md` before ending a session, before a long-running task,
or whenever you sense the context is about to get compacted. Write it for
someone with zero memory of this conversation: what's done, what's next,
which files matter, what NOT to redo.

## Rationalization check

| Thought | Rebuttal |
|---|---|
| "This is small enough to skip the spec folder." | If it fits in one sitting with no decisions worth remembering, it probably is small enough — but check that assumption before skipping, not after finding out mid-implementation that it wasn't. |
| "I'll batch the findings at the end." | By the end you won't remember why you rejected the first two approaches. Write it down when it's still obvious. |
| "I'll update progress.md when I actually stop." | Context compaction and interruptions don't send a warning. Update it at natural checkpoints, not just at the end. |
