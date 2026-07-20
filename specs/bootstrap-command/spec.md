# Spec: bootstrap-command

## Requirements

### 1. Command file

`src/agent_scaffold/source-structure/common/.claude/commands/bootstrap.md`
exists, follows the format in that directory's `README.md`
(`description` frontmatter + prompt body), and is named after its
trigger (`/bootstrap`).

### 2. Interview behavior (the prompt content)

When run, the command:

- States its purpose in one line before starting.
- Explores facts itself before asking: reads manifest files (e.g.
  `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`) for build/test
  commands, and lint/format config (`.eslintrc`, `ruff.toml`,
  `pyproject.toml` `[tool.ruff]`, `.prettierrc`, etc.) for code style —
  and only asks the human to confirm or fill gaps, never to restate what's
  already inferable.
- Asks the human, one question at a time, only for things that are
  genuinely their call:
  1. Project identity — one-line description, what it is, who it's for.
  2. Confirmation/gaps for build & test commands.
  3. Confirmation/gaps for code style conventions.
  4. Project scale — demo/solo vs. team/production (drives the default
     answer to the next question, not a hard gate).
  5. Branch strategy — exactly two options: (a) commit directly to
     `main`, no PR; (b) feature branch + PR before merge. Suggest (a) for
     demo/solo and (b) for team/production based on Q4, but let the human
     override.
  6. Commit convention — recommend Conventional Commits
     (`feat:`/`fix:`/`docs:`/`chore:`/`test:`/`ci:`) as the default;
     accept freeform as an explicit alternative if the human pushes back.
  7. Anything else agents should know (gotchas, invariants, do-not-touch
     areas) for Notes for Agents.
  8. Initial goal — what's being built first.
- Before writing, checks whether `CLAUDE.md`'s sections already have real
  content (not just the shipped TODO placeholders). If so, says so and
  asks whether to proceed before overwriting — never clobbers silently.
- Writes the answers into `CLAUDE.md` in place: the top one-liner,
  `## Project Overview`, `## Build & Test`, `## Code Style`, and
  `## Notes for Agents` (matching the shipped skeleton's existing
  headings), plus a new `## Git Workflow` section (branch strategy +
  commit convention — this section doesn't exist in the shipped skeleton
  today).
- After `CLAUDE.md` is written, uses the `spec-driven-development` skill
  to create `specs/<slug>/README.md` and `spec.md` (slug derived from the
  stated initial goal) via its normal interview — and stops there.
  `plan.md`/`tasks.md` are explicitly out of scope for `/bootstrap`: per
  the skill, those come only once the spec itself is agreed, which may
  take more back-and-forth than a single bootstrap run should force.

### 3. Distribution

- The same content is mirrored (dogfooded) at
  `.claude/commands/bootstrap.md` in this repo's own root, matching how
  every other category in this repo mirrors its shipped payload.
- A Korean translation exists at `docs/ko/commands/bootstrap.md`, with the
  standard "this is a translation, here's the shipped source" note at the
  top (see `docs/ko/agents/second-opinion.md` for the exact note format),
  and no links back into this repo from the shipped English version.

### 4. Process

- `CHANGELOG.md` gets an `[Unreleased]` / `Added` entry — this is a MINOR
  addition per `CONTRIBUTING.md`'s versioning policy ("a new skill/command
  in the template").
- `uv run pytest` and `uv run ruff check .` both pass.
- Work happens on a feature branch, per this repo's own branching rule.

## Out of scope

- A third (release/production) branch-strategy tier.
- Any change to `cli.py`, `_template.py`, or the shipped `CLAUDE.md`
  skeleton's default placeholders.
- Building `plan.md`/`tasks.md` for the user's *own* first goal — only
  `README.md` + `spec.md` are created by the handoff.

## Done means

- [ ] `bootstrap.md` exists in the payload, dogfooded copy, and Korean
      mirror, all consistent with each other (English is canonical).
- [ ] Manually walking through the interview logic (read as a reviewer,
      not executed against a live project) covers all 8 questions above
      in order, with the explore-before-ask behavior stated explicitly.
- [ ] `CHANGELOG.md` updated.
- [ ] `pytest` and `ruff check` pass.
