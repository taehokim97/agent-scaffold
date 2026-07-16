# AGENTS.md

## Project Overview

`agent-scaffold` is a small CLI that scaffolds Claude Code's
`CLAUDE.md` + `.claude/{skills,commands,rules,agents}/` layout into any
project. It's meant to be run directly from its git repository with
`uvx --from git+...` — no installation step for end users.

Two things share this repo and are easy to confuse:

- `src/agent_scaffold/{__init__,cli,_template}.py` — the tool itself (the
  CLI you're editing).
- `src/agent_scaffold/source-structure/` — the **template payload**
  (`CLAUDE.md` + `.claude/{skills,commands,rules,agents}/`). These are the
  files `agent-scaffold` copies into a target project. Editing them
  changes what end users receive, not how this repo behaves. Each `.claude/`
  subdirectory's `README.md` documents that directory's file format for
  contributors — `_template.py` deliberately excludes `README.md` from what
  gets copied, so the target project's directories start genuinely empty.

## Build & Test

```bash
uv sync --dev        # install deps (Python >=3.11)
uv run pytest        # run tests
uv run ruff check .  # lint
uv build              # build sdist + wheel into dist/
```

`tests/test_packaging.py` builds a real wheel and inspects its contents —
this is the test that catches a broken `[tool.hatch.build.targets.wheel]`
config, since editable installs bypass wheel file-selection entirely. Don't
skip it when touching `pyproject.toml` packaging settings.

## Code Style

- Zero runtime dependencies (stdlib `argparse` + `importlib.resources` only)
  — keep it that way unless there's a concrete reason to add one.
- No comments explaining *what* code does; only *why*, when it's non-obvious.
- Ruff defaults; run `uv run ruff check .` before committing.

## Notes for Agents

- See [CONTRIBUTING.md](CONTRIBUTING.md) for commit conventions and semver
  policy.
- `src/agent_scaffold/_template.py` copies everything under
  `source-structure/` as-is. New files added there are picked up
  automatically — no changes needed in `_template.py`.
