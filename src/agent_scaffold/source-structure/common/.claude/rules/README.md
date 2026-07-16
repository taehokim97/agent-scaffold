# .claude/rules/

This directory holds project rules — markdown files Claude Code loads
automatically alongside `CLAUDE.md`, useful for splitting instructions into
focused files instead of one large `CLAUDE.md`.

Every `.md` file in the tree loads automatically; subdirectories are fine
for grouping (e.g. `rules/frontend/react.md`). Optionally scope a rule to
specific files with a `paths` field in frontmatter:

```markdown
---
paths: ["src/frontend/**"]
---

Rule content, loaded only when working in matching files.
```

This scaffold ships with no rules by default — it only sets up the
directory so you have somewhere to put your own.
