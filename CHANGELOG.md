# Changelog

**🇺🇸 English | [🇰🇷 한국어](docs/ko/CHANGELOG.md)**

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `.claude/hooks/` to the scaffolded layout (empty for now — hook scripts
  are registered separately via `.claude/settings.json`).

## [0.1.0] - 2026-07-16

### Added

- `agent-scaffold` CLI: copies a template `CLAUDE.md` +
  `.claude/{skills,commands,rules,agents}/` into a target directory,
  skipping existing files unless `--force` is passed.
- Template payload: a skeleton `CLAUDE.md` and empty `.claude/skills/`,
  `.claude/commands/`, `.claude/rules/`, `.claude/agents/` directories (each
  documented by a `README.md` in this repo that isn't copied to targets).
- CI workflow (lint + test).
