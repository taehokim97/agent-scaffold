---
description: Interview to bootstrap a freshly scaffolded project — fills in CLAUDE.md (overview, build/test, code style, and a new Git Workflow section for branch/commit conventions) and hands off into spec-driven-development for the first goal.
---

# /thk-bootstrap

Run this once, right after scaffolding a project with `agent-scaffold`
(or any time `CLAUDE.md` is still mostly TODOs). It turns the blank
skeleton into a real constitution for the project, then opens the first
`specs/<slug>/` for whatever gets built first.

## Before asking anything

Read what the repo already tells you:

- Manifest files (`package.json`, `pyproject.toml`, `Cargo.toml`,
  `go.mod`, `Gemfile`, etc.) for the install/build/test/lint commands.
- Lint/format config (`.eslintrc*`, `ruff.toml`/`[tool.ruff]`,
  `.prettierrc*`, `.editorconfig`, etc.) for naming, formatting, and
  style conventions already decided.
- Existing source files, if any, for patterns already in use.

Only ask the human about what you couldn't determine yourself, or what's
genuinely their call. Don't make them restate what you already found.

## Check before overwriting

Read the current `CLAUDE.md`. If `Project Overview`, `Build & Test`, or
`Code Style` already hold real content — not the shipped
`<!-- TODO: ... -->` placeholders — say so and ask whether to proceed
before writing over it. Don't clobber existing answers silently.

## The interview

Ask one question at a time. Skip any question you already answered by
reading the repo — confirm your finding in one line instead of asking it
as an open question.

1. **Project identity** — one sentence: what is this, who is it for?
2. **Build & test** — confirm (or fill in) the exact install/build/
   test/lint commands an agent should run.
3. **Code style** — confirm (or fill in) formatting, naming, error
   handling, and other conventions.
4. **Scale** — is this a solo project or demo, or a team/production
   codebase? (Drives the suggested default for the next question, not a
   hard rule.)
5. **Branch strategy** — exactly two options:
   - Commit directly to `main`, no PR. Suggested default for demo/solo.
   - Feature branch + PR before merge. Suggested default for
     team/production.
   Let the human pick either regardless of what Q4 suggested.
6. **Commit convention** — recommend [Conventional
   Commits](https://www.conventionalcommits.org/) (`feat:`/`fix:`/
   `docs:`/`chore:`/`test:`/`ci:`, imperative subject line) as the
   default. If the human pushes back, freeform descriptive commits are
   the explicit alternative — don't invent a third scheme unprompted.
7. **Notes for agents** — anything else an agent should know that isn't
   obvious from the code: gotchas, invariants, do-not-touch areas.
8. **Initial goal** — what's being built first?

## Write CLAUDE.md

Fill in, in place, matching the shipped skeleton's headings:

- The one-line description at the top.
- `## Project Overview`
- `## Build & Test`
- `## Code Style`
- `## Notes for Agents`

Then add one section the skeleton doesn't ship with:

```markdown
## Git Workflow

- Branching: <answer to Q5>
- Commits: <answer to Q6>
```

## Hand off to the first spec

Once `CLAUDE.md` is written, use the `spec-driven-development` skill for
the goal from Q8: interview toward a `specs/<slug>/README.md` and
`spec.md` (slug derived from the goal). Stop there — don't write
`plan.md`/`tasks.md` yet; those come once the spec itself is agreed,
which the skill treats as its own step.
