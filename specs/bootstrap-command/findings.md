# Findings: bootstrap-command

## 2026-07-20 — `test_does_not_copy_readme` needed updating

`tests/test_cli.py`'s `EXPECTED_EMPTY_DIRS` asserted `.claude/commands`
stayed empty after scaffolding — true before this change, since the
scaffold shipped no commands. Adding `bootstrap.md` broke that assertion.

Fixed by removing `.claude/commands` from `EXPECTED_EMPTY_DIRS` (only
`.claude/rules` still ships empty) and adding a dedicated
`test_ships_bootstrap_command` test, matching the existing pattern used
for `test_ships_second_opinion_subagent` and
`test_ships_expected_hooks_and_settings` — each shipped category gets its
own "ships expected content + doesn't leak README.md" test rather than
being folded into the generic empty-dirs check.

Not anticipated in `plan.md`/`tasks.md` because those were written before
running the test suite; not a design change, just a pre-existing test
that encoded "ships nothing yet" as its own assertion.

## 2026-07-20 — renamed `bootstrap.md` → `thk-bootstrap.md`

Follow-up discussion (outside this spec's original scope) concluded
commands need a collision-avoiding prefix, since `.claude/commands/`
doesn't support the directory-based `/namespace:command` mechanism that
`.claude/skills/` has — a command's trigger is always just its filename.
User picked `thk-` as this project's prefix for shipped commands.
Renamed the file at all three locations (payload, dogfooded copy, Korean
mirror), updated the in-file `# /bootstrap` heading, the Korean mirror's
translation-note link, `CHANGELOG.md`/`docs/ko/CHANGELOG.md`, both
touched tests, and added a "Naming" section to `commands/README.md` so
future commands follow the same convention without re-litigating it.
`spec.md`/`plan.md`/`tasks.md` above still say `bootstrap.md` — left as
the historical record of what was planned/done at the time; the current
filename is `thk-bootstrap.md` throughout, see `progress.md`.
