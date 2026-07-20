# Changelog

**🇺🇸 English | [🇰🇷 한국어](docs/ko/CHANGELOG.md)**

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `reproducible-debugging` skill: the template's first concrete skill,
  enforcing a reproduce → root-cause → fix → verify loop before any bug
  fix. See README Credits for sources.
- `spec-driven-development` skill: maintains a `specs/<slug>/` folder
  (background, spec, plan, tasks, findings, resumption log) for
  non-trivial feature work.
- `release-versioning` skill: classifies a change against Semantic
  Versioning and drafts the CHANGELOG entry.
- `research-brief` skill: structures an open-ended research question
  into a scoped brief with sources and a stop condition before handing
  it off to a long or unattended session.
- `.claude/settings.json` and two hooks: `auto-format` (`PostToolUse`)
  best-effort formats the file just edited with the project's own
  formatter, and `session-brief` (`SessionStart`) surfaces in-progress
  specs and unread research findings at the start of a session.
- `second-opinion` subagent: an isolated-context, review-only reviewer
  for work outside full confidence, with confidence-filtered findings
  (zero findings is a valid result).
- `bootstrap` command: the template's first command, an interview that
  fills in `CLAUDE.md` (overview, build/test, code style, and a new Git
  Workflow section for branch/commit conventions) and hands off into the
  `spec-driven-development` skill for the project's first goal.

## [0.1.0] - 2026-07-16

### Added

- `agent-scaffold` CLI: copies a template `CLAUDE.md` +
  `.claude/{skills,commands,rules,agents}/` into a target directory,
  skipping existing files unless `--force` is passed.
- Template payload: a skeleton `CLAUDE.md` and empty `.claude/skills/`,
  `.claude/commands/`, `.claude/rules/`, `.claude/agents/` directories (each
  documented by a `README.md` in this repo that isn't copied to targets).
- CI workflow (lint + test).
