# Contributing

**🇺🇸 English | [🇰🇷 한국어](docs/ko/CONTRIBUTING.md)**

## Setup

```bash
git clone https://github.com/taehokim97/agent-scaffold
cd agent-scaffold
uv sync --dev
```

## Running checks

```bash
uv run pytest
uv run ruff check .
```

Both must pass before opening a PR.

## Commit conventions

Commits follow [Conventional Commits](https://www.conventionalcommits.org/):
a short imperative subject line prefixed with one of `feat`, `fix`, `docs`,
`chore`, `test`, `ci` (e.g. `feat: add --dry-run flag`). Keep each commit to
one logical change.

## Versioning

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** — a breaking change: a CLI flag or subcommand is removed/renamed,
  or a file the template always shipped is removed.
- **MINOR** — a backward-compatible addition: a new skill/command in the
  template, a new CLI flag or subcommand.
- **PATCH** — a bug fix, or a wording/doc fix with no behavior change.

Update `CHANGELOG.md` (Keep a Changelog format) alongside any user-visible
change.

## Adding a skill, command, rule, hook, or subagent to the template

The template payload is split into `src/agent_scaffold/source-structure/common/`
(profile-agnostic: `CLAUDE.md`, the empty `.claude/*` category dirs, and
each category's format-doc `README.md`, which is never copied to target
projects — see `_template.py`) and
`src/agent_scaffold/source-structure/profiles/{dev,research}/` (the actual
skills/commands/rules/agents/hooks content, split by which profile it's
meant for).

Add new content under the matching
`profiles/{dev,research}/.claude/{skills,commands,rules,agents,hooks}/`
directory, following the format described in `common/.claude/<category>/README.md`.
Hooks are the odd one out: a script alone does nothing, it must also be
registered in that profile's `.claude/settings.json` (see
`common/.claude/hooks/README.md` for the two-part shape).

If you're adapting content from another project, credit the source in this
project's `README.md` under Credits with an `inspired by` or `based on` tag
and a link. Check the license first — see the license-review notes in the
relevant category PR/issue before adopting copyleft or unlicensed content.

## Branching

All work goes through a feature branch + PR — no direct pushes to `main`.
Use one branch per logical unit of work (e.g. a structural change, or all
the content for one category like `feat/skills-from-public-repos`); don't
mix unrelated categories in the same branch, since one branch getting stuck
on license review shouldn't block the others from merging. Open the PR once
`uv run pytest` and `uv run ruff check .` both pass locally.
