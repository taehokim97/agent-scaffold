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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
