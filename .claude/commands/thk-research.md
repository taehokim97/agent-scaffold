---
description: Turn an open research question into a scoped brief (question, in/out of scope, stop condition) using the research-brief skill, before running or handing it off.
---

# /thk-research

An explicit front door to the `research-brief` skill. The skill file
assumes the brief's four fields are already decided; this command is
what actually elicits them, one at a time:

1. **Question** — what are you actually trying to find out?
2. **In scope** — what should get checked?
3. **Out of scope** — what NOT to chase, even if it looks interesting?
4. **Stop condition** — time-boxed, N sources checked, or confidence
   reached?

## Foreground or handoff?

Ask explicitly: is this being researched right now in this session, or
handed off to run in a long/unattended one? If it's a handoff, say
plainly that it must run as a single long session or via the harness's
own scheduling with normal permission prompts intact — never wired with
elevated or bypassed permissions to fake "truly unattended." The skill
states this rule; this command is where it actually gets confirmed
before the handoff happens, not assumed.

## Then

Write `research/<kebab-case-slug>/findings.md` with the brief header
block from the four answers above, and proceed exactly as the
`research-brief` skill documents from there: one finding entry per
claim, every claim sourced, `needs verification` instead of guessing.
