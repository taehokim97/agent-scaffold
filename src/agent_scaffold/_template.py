from __future__ import annotations

import importlib.resources as resources
from importlib.resources.abc import Traversable
from pathlib import Path

# `common/` holds everything the CLI ships: CLAUDE.md and the
# .claude/{skills,commands,rules,agents,hooks}/ content, copied as-is into
# the target project's root.
_TEMPLATE_ROOT = "source-structure"


def _copy_template(target_dir: Path, force: bool) -> list[str]:
    """Copy the packaged scaffold template into target_dir.

    Returns one human-readable status line per file.
    """
    target_dir = target_dir.resolve()
    package_root = resources.files("agent_scaffold") / _TEMPLATE_ROOT
    messages: list[str] = []

    def _copy(src: Traversable, dst: Path) -> None:
        if src.is_dir():
            dst.mkdir(parents=True, exist_ok=True)
            for child in src.iterdir():
                _copy(child, dst / child.name)
            return
        if src.name == "README.md":
            # Documents the format for this repo's contributors; not meant
            # for the target project.
            return
        if dst.exists() and not force:
            messages.append(
                f"skip  {dst.relative_to(target_dir)} (already exists, use --force to overwrite)"
            )
            return
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
        messages.append(f"write {dst.relative_to(target_dir)}")

    common_root = package_root / "common"
    for child in common_root.iterdir():
        _copy(child, target_dir / child.name)

    return messages
