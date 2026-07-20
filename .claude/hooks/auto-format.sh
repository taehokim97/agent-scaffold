#!/usr/bin/env bash
# PostToolUse hook (Edit|Write): best-effort auto-format the file that was
# just written, using whichever formatter the project already has
# configured. Never blocks or fails the tool call — errors are swallowed.

input="$(cat)"
file_path="$(printf '%s' "$input" | python3 -c '
import json, sys
try:
    data = json.load(sys.stdin)
    print(data.get("tool_input", {}).get("file_path", ""))
except Exception:
    pass
' 2>/dev/null)"

[ -n "$file_path" ] || exit 0
[ -f "$file_path" ] || exit 0

project_root="${CLAUDE_PROJECT_DIR:-$(dirname "$file_path")}"

case "$file_path" in
  *.py)
    if [ -f "$project_root/pyproject.toml" ] || [ -f "$project_root/ruff.toml" ]; then
      command -v ruff >/dev/null 2>&1 && ruff format "$file_path" >/dev/null 2>&1
    fi
    ;;
  *.js | *.jsx | *.ts | *.tsx | *.json | *.css | *.md)
    if [ -f "$project_root/package.json" ] && grep -q '"prettier"' "$project_root/package.json" 2>/dev/null; then
      command -v npx >/dev/null 2>&1 && npx --no-install prettier --write "$file_path" >/dev/null 2>&1
    fi
    ;;
  *.rs)
    if [ -f "$project_root/Cargo.toml" ]; then
      command -v cargo >/dev/null 2>&1 && cargo fmt -- "$file_path" >/dev/null 2>&1
    fi
    ;;
  *.go)
    command -v gofmt >/dev/null 2>&1 && gofmt -w "$file_path" >/dev/null 2>&1
    ;;
esac

exit 0
