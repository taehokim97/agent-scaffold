---
description: Pre-flight the project's own build/test/lint, then classify the current change and draft a CHANGELOG entry using the release-versioning skill, before treating it as ready to ship.
---

# /thk-ship

An explicit front door to the `release-versioning` skill, with one thing
added it doesn't cover: a pre-flight check, so a broken build never gets
a changelog entry drafted for it.

## Pre-flight

Read `CLAUDE.md`'s `## Build & Test` section and run whatever it
specifies (don't hardcode a command — it varies per project). If any of
it fails, stop here and say what failed. Don't classify or draft a
changelog entry for a change that doesn't build or pass its own tests.

## Classify and draft

Once the pre-flight is clean, follow the `release-versioning` skill
exactly as documented:

1. Classify the change (MAJOR / MINOR / PATCH) against Semantic
   Versioning.
2. Draft the `[Unreleased]` entry in `CHANGELOG.md`, Keep a Changelog
   format.
3. If the project keeps a translated CHANGELOG, mirror the same entry
   there.

## Confirm before final

State the classification and the drafted entry, and ask the human to
confirm before treating it as final — this is the one step the skill
file itself doesn't include, since the skill assumes it's being run
mid-workflow rather than as the last word on whether something ships.
