# .claude/commands/

This directory holds slash commands — short, user-invoked prompts an agent
runs on demand (e.g. `/deploy`, `/review`).

Each command is a single markdown file, named after the command it defines:

```markdown
---
description: One line describing what this command does.
---

The prompt/instructions to run when this command is invoked.
```

## Naming

Unlike `.claude/skills/`, Claude Code doesn't namespace commands by
directory — a command's trigger is always just its filename, flat, with
no `/prefix:name` mechanism available. Since these files get copied
as-is into someone else's project (which may already have its own
`.claude/commands/`), prefix the filename to avoid collisions: this
project's own commands use `thk-` (e.g. `thk-bootstrap.md` →
`/thk-bootstrap`). Keep using that prefix for new commands added here
rather than picking a new one per command.

## Credit

When you add a command that was adapted from, or inspired by, someone
else's work, credit it in your project's README with an `inspired by` or
`based on` tag and a link, the same way this project credits its own
influences.
