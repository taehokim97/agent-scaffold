from __future__ import annotations

import importlib.resources as resources
import subprocess
import zipfile
from pathlib import Path

import pytest

EXPECTED_WHEEL_MEMBERS = [
    "agent_scaffold/source-structure/common/CLAUDE.md",
    "agent_scaffold/source-structure/common/.claude/skills/README.md",
    "agent_scaffold/source-structure/common/.claude/skills/reproducible-debugging/SKILL.md",
    "agent_scaffold/source-structure/common/.claude/skills/spec-driven-development/SKILL.md",
    "agent_scaffold/source-structure/common/.claude/skills/release-versioning/SKILL.md",
    "agent_scaffold/source-structure/common/.claude/skills/research-brief/SKILL.md",
    "agent_scaffold/source-structure/common/.claude/commands/README.md",
    "agent_scaffold/source-structure/common/.claude/rules/README.md",
    "agent_scaffold/source-structure/common/.claude/agents/README.md",
    "agent_scaffold/source-structure/common/.claude/hooks/README.md",
]


def test_template_discoverable_via_importlib_resources(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    root = resources.files("agent_scaffold") / "source-structure" / "common"
    assert (root / "CLAUDE.md").is_file()
    assert (root / ".claude" / "skills" / "README.md").is_file()
    assert (root / ".claude" / "commands" / "README.md").is_file()
    assert (root / ".claude" / "rules" / "README.md").is_file()
    assert (root / ".claude" / "agents" / "README.md").is_file()
    assert (root / ".claude" / "hooks" / "README.md").is_file()


def test_wheel_actually_contains_template_files(tmp_path: Path) -> None:
    # Editable installs bypass wheel file-selection entirely, so the test
    # above can't catch a broken `packages = [...]` setting in pyproject.toml.
    # This builds a real wheel and inspects its contents to guard against
    # that regression.
    subprocess.run(
        ["uv", "build", "--wheel", "--out-dir", str(tmp_path)],
        check=True,
        cwd=Path(__file__).resolve().parents[1],
    )
    wheel = next(tmp_path.glob("*.whl"))
    names = zipfile.ZipFile(wheel).namelist()
    for member in EXPECTED_WHEEL_MEMBERS:
        assert any(n.endswith(member) for n in names), f"{member} missing from wheel"
