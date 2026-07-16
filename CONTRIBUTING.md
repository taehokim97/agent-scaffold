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

## Adding a skill, command, rule, or subagent to the template

If you're adapting one from another project, add it under the matching
`src/agent_scaffold/source-structure/.claude/{skills,commands,rules,agents}/`
directory, following the format described in that directory's `README.md`
(that file itself is never copied to target projects — see
`_template.py`), and credit the source in this project's `README.md` under
Credits with an `inspired by` or `based on` tag and a link.

## Branching

Small early-stage changes may land directly on `main`. As the project
grows, contributions should go through a feature branch + PR instead of
pushing to `main` directly.
