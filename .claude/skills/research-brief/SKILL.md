---
name: research-brief
description: Use when handing off an open-ended research question to run
  in a long or unattended session — e.g. before stepping away. Structures
  the question into a scoped brief with sources and a stop condition, and
  writes findings to a file instead of leaving them only in chat.
---

# Research brief

An open question run unattended without a scope will either stop too
early or run forever. Write the brief before starting, not while
researching.

## Before starting

Write `research/<kebab-case-slug>/findings.md` with a header block:

```markdown
## Brief
- Question: <what you're actually trying to find out>
- In scope: <what to check>
- Out of scope: <what NOT to chase, even if it looks interesting>
- Stop condition: <time-boxed, N sources checked, or confidence reached>
```

Then research, appending one entry per finding:

```markdown
## <date> — <topic>
- Finding: <the claim>
- Evidence: <source link — no source, no entry>
- Confidence: <high | medium | low>
```

## While researching

Every claim needs a source link. A plausible-sounding claim with no
citation doesn't go in `findings.md` — mark it `needs verification`
instead of stating it as fact. If you hit the stop condition or get stuck
before reaching it, stop and write down exactly what's blocking — that's
a finding too, not a failure to hide.

## Handing off

Never wire this to run with elevated or bypassed permissions (e.g. a cron
job invoking the agent with all confirmation prompts skipped) to make it
"truly unattended." Run it in a single long session, or via the harness's
own scheduling (like a self-paced loop) that keeps normal permission
prompts intact — the human reviews before anything destructive happens.

## Resuming (the morning after)

When picking this back up, read the whole `findings.md`, not just the
last entry — earlier "needs verification" markers matter as much as the
final conclusion. Act on it explicitly: reference specific findings when
giving instructions, rather than re-asking the same question from
scratch.

## Rationalization check

| Thought | Rebuttal |
|---|---|
| "This claim is almost certainly true, I'll skip the source." | "Almost certainly" without a source is a guess wearing a finding's clothes. Mark it `needs verification` instead. |
| "I'm stuck, I'll just guess and move on quietly." | A stuck point is information the next session needs. Write it down instead of papering over it. |
| "I'll keep going past the stop condition, I'm close." | The stop condition exists precisely to prevent "just a bit more" from becoming unbounded. Stop, write down what's left, hand it back. |
