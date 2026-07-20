# bootstrap-command

## Background

`agent-scaffold` ships `CLAUDE.md` as a bare TODO skeleton (four headings,
each with an HTML-comment placeholder) and `.claude/commands/` empty by
design — the `commands/README.md` format doc says "this scaffold ships
with no commands by default." Every end user who runs `agent-scaffold` in
a fresh project has to hand-write `CLAUDE.md` from a blank template and has
no example command to learn the command format from.

Filling in `CLAUDE.md` well requires information that's scattered across a
few different concerns — what the project is, how to build/test it, code
style, and (not currently covered by the skeleton at all) how the team
wants to branch and commit — and a demo repo needs much less ceremony
here than a production one does. Asking all of this as a single wall of
questions produces worse answers than an interview that explores what it
can on its own (build commands from the manifest, style from lint config)
and only asks the human for things that are genuinely their call.

## What this adds

A new slash command, `/bootstrap`, meant to be the first thing run in a
freshly scaffolded project. It interviews the user, fills in `CLAUDE.md`
(including a new Git Workflow section this skeleton doesn't currently
have), and — since the interview naturally ends with "what are you
building first" — hands off into the `spec-driven-development` skill to
open the first `specs/<slug>/` for that goal, so the project starts with
both its constitution (`CLAUDE.md`) and its first tracked unit of work in
place.

This also doubles as the scaffold's first real command: a template
contributors can look at when writing their own.

## Non-goals

- Not changing the shipped `CLAUDE.md` skeleton's default TODO
  placeholders — those stay as they are for anyone who doesn't run
  `/bootstrap`.
- Not a 3rd branch-strategy tier (release/production branches) — the
  interview stays at two tiers (direct-to-main, or feature branch + PR);
  a project that outgrows that can restructure `CLAUDE.md` by hand.
- Not a code/tooling change — `/bootstrap` is a markdown prompt, like
  every other command; no changes to `cli.py` or `_template.py` are
  needed (per `CLAUDE.md`, new files under `source-structure/common/` are
  picked up automatically).
