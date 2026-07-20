from __future__ import annotations

import argparse
import sys
from pathlib import Path

from agent_scaffold._template import _copy_template


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agent-scaffold",
        description="Scaffold CLAUDE.md + .claude/{skills,commands,rules,agents,hooks} into a project.",
    )
    parser.add_argument(
        "target", nargs="?", default=".", help="Target directory (default: current directory)."
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    target = Path(args.target)
    target.mkdir(parents=True, exist_ok=True)
    for line in _copy_template(target, force=args.force):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
