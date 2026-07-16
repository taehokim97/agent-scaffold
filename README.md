# agent-scaffold

**🇺🇸 English | [🇰🇷 한국어](docs/ko/README.md)**

A CLI that scaffolds Claude Code's `CLAUDE.md` + `.claude/{skills,commands,rules,agents}/`
layout into any project.
It's intentionally an empty scaffold — just the directories Claude Code
looks for, with nothing opinionated inside.

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
    ├── skills/        # empty — skill format documented in this repo's source
    ├── commands/      # empty — slash command format documented in this repo's source
    ├── rules/         # empty — project rule format documented in this repo's source
    └── agents/        # empty — subagent format documented in this repo's source
```

The format docs that live alongside each directory in this repo
(`README.md`) aren't copied into your project.

## Roadmap

This targets Claude Code only for now — it's the only agent I use day to
day, and there's no point generalizing before there's a second real use
case. Once there is, a `--agent codex|claude` flag can pick between
Claude Code's native layout and a tool-agnostic `AGENTS.md`-standard
output.

## Credits

The `CLAUDE.md` + `.claude/{skills,commands,rules,agents}/` layout mirrors
[Claude Code](https://docs.claude.com/en/docs/claude-code)'s own
conventions for project memory, skills, slash commands, rules, and
subagents — this scaffold just automates setting them up.

This scaffold ships no concrete skills or commands yet. When any are added,
they'll be credited here with an `inspired by` or `based on` tag and a link
to the source.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
