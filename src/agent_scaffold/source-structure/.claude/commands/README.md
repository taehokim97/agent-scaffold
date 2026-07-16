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

This scaffold ships with no commands by default — it only sets up the
directory so you have somewhere to put your own. When you add a command that
was adapted from, or inspired by, someone else's work, credit it in your
project's README with an `inspired by` or `based on` tag and a link, the
same way this project credits its own influences.
