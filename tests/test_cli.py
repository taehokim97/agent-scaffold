from __future__ import annotations

from pathlib import Path

import pytest

from agent_scaffold.cli import main

EXPECTED_EMPTY_DIRS = [
    ".claude/skills",
    ".claude/commands",
    ".claude/rules",
    ".claude/agents",
    ".claude/hooks",
]


def test_creates_expected_files(tmp_path: Path) -> None:
    rc = main([str(tmp_path), "--profile", "dev"])
    assert rc == 0
    assert (tmp_path / "CLAUDE.md").is_file()
    for rel in EXPECTED_EMPTY_DIRS:
        assert (tmp_path / rel).is_dir()


def test_does_not_copy_readme(tmp_path: Path) -> None:
    main([str(tmp_path), "--profile", "dev"])
    for rel in EXPECTED_EMPTY_DIRS:
        assert list((tmp_path / rel).iterdir()) == []


def test_skips_existing_without_force(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (tmp_path / "CLAUDE.md").write_text("sentinel")
    rc = main([str(tmp_path), "--profile", "dev"])
    assert rc == 0
    assert (tmp_path / "CLAUDE.md").read_text() == "sentinel"
    assert "skip" in capsys.readouterr().out


def test_force_overwrites(tmp_path: Path) -> None:
    (tmp_path / "CLAUDE.md").write_text("sentinel")
    main([str(tmp_path), "--profile", "dev", "--force"])
    assert (tmp_path / "CLAUDE.md").read_text() != "sentinel"


def test_defaults_target_to_cwd(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    rc = main(["--profile", "dev"])
    assert rc == 0
    assert (tmp_path / "CLAUDE.md").is_file()
    for rel in EXPECTED_EMPTY_DIRS:
        assert (tmp_path / rel).is_dir()


def test_research_profile_also_creates_expected_dirs(tmp_path: Path) -> None:
    rc = main([str(tmp_path), "--profile", "research"])
    assert rc == 0
    assert (tmp_path / "CLAUDE.md").is_file()
    for rel in EXPECTED_EMPTY_DIRS:
        assert (tmp_path / rel).is_dir()


def test_profile_is_required(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        main([])
    assert "--profile" in capsys.readouterr().err


def test_rejects_unknown_profile(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        main(["--profile", "bogus"])
    assert "--profile" in capsys.readouterr().err
