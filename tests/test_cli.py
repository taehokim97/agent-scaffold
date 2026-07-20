from __future__ import annotations

import stat
from pathlib import Path

import pytest

from agent_scaffold.cli import main

EXPECTED_CATEGORY_DIRS = [
    ".claude/skills",
    ".claude/commands",
    ".claude/rules",
    ".claude/agents",
    ".claude/hooks",
]

# Categories with no shipped content yet, so they should stay empty.
EXPECTED_EMPTY_DIRS = [
    ".claude/rules",
]


def test_creates_expected_files(tmp_path: Path) -> None:
    rc = main([str(tmp_path)])
    assert rc == 0
    assert (tmp_path / "CLAUDE.md").is_file()
    for rel in EXPECTED_CATEGORY_DIRS:
        assert (tmp_path / rel).is_dir()


def test_does_not_copy_readme(tmp_path: Path) -> None:
    main([str(tmp_path)])
    for rel in EXPECTED_EMPTY_DIRS:
        assert list((tmp_path / rel).iterdir()) == []


SHIPPED_SKILLS = [
    "reproducible-debugging",
    "spec-driven-development",
    "release-versioning",
    "research-brief",
]


def test_ships_expected_skills(tmp_path: Path) -> None:
    main([str(tmp_path)])
    for name in SHIPPED_SKILLS:
        skill = tmp_path / f".claude/skills/{name}/SKILL.md"
        assert skill.is_file()
        assert name in skill.read_text()
    # The category's format-doc README.md must not be copied alongside them.
    assert not (tmp_path / ".claude/skills/README.md").exists()


SHIPPED_HOOKS = ["auto-format.sh", "session-brief.sh"]


def test_ships_expected_hooks_and_settings(tmp_path: Path) -> None:
    main([str(tmp_path)])
    settings = tmp_path / ".claude/settings.json"
    assert settings.is_file()
    assert "auto-format.sh" in settings.read_text()
    assert "session-brief.sh" in settings.read_text()
    for name in SHIPPED_HOOKS:
        hook = tmp_path / f".claude/hooks/{name}"
        assert hook.is_file()
        # settings.json invokes hooks by path, so they must be executable
        # regardless of how the package was built/installed.
        assert hook.stat().st_mode & stat.S_IXUSR
    # The category's format-doc README.md must not be copied alongside them.
    assert not (tmp_path / ".claude/hooks/README.md").exists()


def test_ships_second_opinion_subagent(tmp_path: Path) -> None:
    main([str(tmp_path)])
    agent = tmp_path / ".claude/agents/second-opinion.md"
    assert agent.is_file()
    assert "second-opinion" in agent.read_text()
    # The category's format-doc README.md must not be copied alongside it.
    assert not (tmp_path / ".claude/agents/README.md").exists()


def test_ships_bootstrap_command(tmp_path: Path) -> None:
    main([str(tmp_path)])
    command = tmp_path / ".claude/commands/bootstrap.md"
    assert command.is_file()
    assert "spec-driven-development" in command.read_text()
    # The category's format-doc README.md must not be copied alongside it.
    assert not (tmp_path / ".claude/commands/README.md").exists()


def test_skips_existing_without_force(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (tmp_path / "CLAUDE.md").write_text("sentinel")
    rc = main([str(tmp_path)])
    assert rc == 0
    assert (tmp_path / "CLAUDE.md").read_text() == "sentinel"
    assert "skip" in capsys.readouterr().out


def test_force_overwrites(tmp_path: Path) -> None:
    (tmp_path / "CLAUDE.md").write_text("sentinel")
    main([str(tmp_path), "--force"])
    assert (tmp_path / "CLAUDE.md").read_text() != "sentinel"


def test_defaults_target_to_cwd(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    rc = main([])
    assert rc == 0
    assert (tmp_path / "CLAUDE.md").is_file()
    for rel in EXPECTED_CATEGORY_DIRS:
        assert (tmp_path / rel).is_dir()
