# .claude/skills/

This directory holds agent skills — packaged, reusable instructions an agent
loads on demand for a specific kind of task.

Each skill is a subdirectory containing at least a `SKILL.md` with YAML
frontmatter:

```markdown
---
name: my-skill
description: One line, specific enough for an agent to know when to use it.
---

Instructions the agent follows when this skill is invoked.
```

This scaffold ships with no skills by default — it only sets up the
directory so you have somewhere to put your own. When you add a skill that
was adapted from, or inspired by, someone else's work, credit it in your
project's README with an `inspired by` or `based on` tag and a link, the
same way this project credits its own influences.
