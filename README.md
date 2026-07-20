# agent-scaffold

**🇺🇸 English | [🇰🇷 한국어](docs/ko/README.md)**

A CLI that scaffolds Claude Code's `CLAUDE.md` + `.claude/{skills,commands,rules,agents,hooks}/`
layout into any project.

## Install & run

No install step — run it straight from source with [uv](https://docs.astral.sh/uv/):

```bash
uvx --from git+https://github.com/taehokim97/agent-scaffold agent-scaffold
```

This copies the scaffold into the current directory. Pass a path to target
somewhere else, and `--force` to overwrite files that already exist:

```bash
uvx --from git+https://github.com/taehokim97/agent-scaffold agent-scaffold path/to/project --force
```

## What gets created

```
.
├── CLAUDE.md          # skeleton: overview, build/test, code style, notes for agents
└── .claude/
    ├── skills/        # skill format documented in this repo's source
    ├── commands/      # slash command format documented in this repo's source
    ├── rules/         # project rule format documented in this repo's source
    ├── agents/        # subagent format documented in this repo's source
    └── hooks/         # hook scripts; registered separately in .claude/settings.json
```

Every run copies the same payload (see Credits for what's included and
where it came from).

The format docs that live alongside each directory in this repo
(`README.md`) aren't copied into your project.

## Roadmap

This targets Claude Code only for now — it's the only agent I use day to
day, and there's no point generalizing before there's a second real use
case. Once there is, a `--agent codex|claude` flag can pick between
Claude Code's native layout and a tool-agnostic `AGENTS.md`-standard
output.

## Credits

The `CLAUDE.md` + `.claude/{skills,commands,rules,agents,hooks}/` layout
mirrors [Claude Code](https://docs.claude.com/en/docs/claude-code)'s own
conventions for project memory, skills, slash commands, rules, subagents,
and hooks — this scaffold just automates setting them up.

- **`reproducible-debugging`** skill — inspired by the reproduction-gated
  debugging loop in [mattpocock/skills](https://github.com/mattpocock/skills)'s
  `diagnosing-bugs`, and the rationalization-check table technique used
  across [obra/superpowers](https://github.com/obra/superpowers)'s skills.
  Rewritten from scratch, not copied. A Korean translation lives at
  [`docs/ko/skills/reproducible-debugging/`](docs/ko/skills/reproducible-debugging/SKILL.md)
  (reference only — the CLI ships the English version above).
- **`spec-driven-development`** skill — inspired by the resumption ledger
  in [obra/superpowers](https://github.com/obra/superpowers)'s
  `subagent-driven-development` and its `writing-plans` skill, and the
  `grill-with-docs` → `to-spec` interview chain in
  [mattpocock/skills](https://github.com/mattpocock/skills). Rewritten
  from scratch, not copied. Korean translation:
  [`docs/ko/skills/spec-driven-development/`](docs/ko/skills/spec-driven-development/SKILL.md).
- **`release-versioning`** skill — provided by: user. Operationalizes
  this project's own [CONTRIBUTING.md](CONTRIBUTING.md) versioning
  policy as a reusable skill, not adapted from an external repo. Korean
  translation:
  [`docs/ko/skills/release-versioning/`](docs/ko/skills/release-versioning/SKILL.md).
- **`research-brief`** skill — inspired by the `to_human/` progress-report
  convention in
  [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
  and the protocol-lock discipline in
  [wanshuiyin/ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep).
  Rewritten from scratch, not copied — and deliberately excludes the
  unattended, permission-bypassing automation pattern found in some
  research-skill repos surveyed alongside these. Korean translation:
  [`docs/ko/skills/research-brief/`](docs/ko/skills/research-brief/SKILL.md).
- **`auto-format`** hook (`PostToolUse`) — inspired by the format-code.js
  auto-formatting hook in
  [karanb192/claude-code-hooks](https://github.com/karanb192/claude-code-hooks).
  Rewritten from scratch, not copied. Best-effort: detects a formatter
  already configured in the project (ruff, prettier, rustfmt, gofmt) and
  runs it on the file just edited; silently no-ops otherwise.
- **`session-brief`** hook (`SessionStart`) — inspired by the
  SessionStart config-check banner in
  [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill).
  Rewritten from scratch, not copied. Surfaces in-progress
  `specs/<slug>/progress.md` and unread `research/<slug>/findings.md`
  files at the start of a session; silent when there's nothing to show.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
