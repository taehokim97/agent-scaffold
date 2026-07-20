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
