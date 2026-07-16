# .claude/hooks/

This directory holds hook **scripts** — shell scripts Claude Code runs in
response to events (e.g. `PreToolUse`, `Stop`).

Unlike skills, commands, rules, and subagents, hooks are not auto-discovered
markdown files. A script placed here does nothing on its own — it must also
be registered in `.claude/settings.json`, which maps events (and optional
tool matchers) to the command that runs:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/check-command.sh" }
        ]
      }
    ]
  }
}
```

So a hook has two parts: the script in this directory, and its matcher entry
in `settings.json`. This scaffold ships with no hooks by default — it only
sets up the directory so you have somewhere to put your own. When you add a
hook that was adapted from, or inspired by, someone else's work, credit it in
your project's README with an `inspired by` or `based on` tag and a link, the
same way this project credits its own influences.
