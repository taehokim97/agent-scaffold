# .claude/agents/

This directory holds subagent definitions — specialized assistants Claude
Code delegates to for a specific kind of task, each running in its own
context window.

Each subagent is a single markdown file with YAML frontmatter:

```markdown
---
name: my-subagent
description: One line, specific enough for Claude to know when to delegate to this.
tools: Read, Grep, Glob
model: haiku
---

The subagent's system prompt: how it should approach the task.
```

Only `name` and `description` are required; `tools` and `model` are
optional. This scaffold ships with no subagents by default — it only sets
up the directory so you have somewhere to put your own.
