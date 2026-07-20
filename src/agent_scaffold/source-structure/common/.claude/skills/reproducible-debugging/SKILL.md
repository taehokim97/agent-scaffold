---
name: reproducible-debugging
description: Use when investigating a bug, a failing test, or unexpected
  behavior. Enforces reproducing the failure deterministically and naming
  its root cause with evidence before any fix is written.
---

# Reproducible debugging

A bug that can't be reproduced can't be fixed. Work through these four
phases in order, without skipping any.

## Phase 1 — Reproduce

- Build one deterministic command that reproduces the failure (a test, a
  script, a curl call, etc.).
- If you can't reproduce it, that's the actual task right now — don't move
  on with "it fails sometimes."
- Record the repro command and its actual output (error message, stack
  trace, diff).

## Phase 2 — Root-cause

- Bisect or isolate the reproduced failure to narrow down the cause.
- You may move on only once you can state the cause in one sentence backed
  by evidence (a log line, a stack trace, a failing diff). "Probably this"
  is not a cause.

## Phase 3 — Fix

- Fix only the cause named in Phase 2. Don't fix other issues you noticed
  along the way.

## Phase 4 — Verify

- Confirm the Phase 1 repro command now passes.
- Run the relevant test suite to confirm no regression.

## Rationalization check

If you're thinking any of these, that's a signal to follow the phase, not
skip it.

| Thought | Rebuttal |
|---|---|
| "This bug is obvious enough to fix without reproducing it first." | Most "obvious" causes turn out to be wrong. A fix without reproduction is an unverified guess. |
| "I'm pretty sure I know the cause, so I'll skip gathering evidence." | "Pretty sure" and "confirmed with evidence" are different. Skip the evidence and Phase 3 fixes the wrong thing. |
| "While I'm in here, let me fix that other bug I noticed too." | Out-of-scope fixes go in a separate issue. They make this fix harder to verify. |
