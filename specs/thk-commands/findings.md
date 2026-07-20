# Findings: thk-commands

## 2026-07-20 — scope trimmed to 3 of 4 skills

User selected `/thk-spec`, `/thk-ship`, `/thk-research` and explicitly
left out `/thk-debug` (`reproducible-debugging`) when scoping this batch
— not a rejection, just not part of this round. No command exists for
`reproducible-debugging` yet.

## 2026-07-20 — no argument support

Considered `$ARGUMENTS`/`argument-hint` (e.g. `/thk-research <question>`)
so commands could take input inline instead of via interview. User chose
interview-only, matching `thk-bootstrap`'s existing pattern — keeps all
four `thk-*` commands consistent and avoids adding an
argument-hint convention to `commands/README.md` that only some commands
would use.
