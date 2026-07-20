#!/usr/bin/env bash
# SessionStart hook: surface any in-progress specs/<slug>/progress.md
# (from the spec-driven-development skill) or unread research/<slug>/
# findings.md (from the research-brief skill) so they aren't missed at
# the start of a new session. Silent when there's nothing to show.

project_root="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$project_root" 2>/dev/null || exit 0

found=0
output=""

if [ -d specs ]; then
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    dir="$(dirname "$f")"
    output="${output}- in-progress spec: ${dir} (see ${dir}/progress.md)
"
    found=1
  done < <(find specs -mindepth 2 -maxdepth 2 -name progress.md 2>/dev/null)
fi

if [ -d research ]; then
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    dir="$(dirname "$f")"
    output="${output}- research findings: ${dir} (see ${dir}/findings.md)
"
    found=1
  done < <(find research -mindepth 2 -maxdepth 2 -name findings.md 2>/dev/null)
fi

[ "$found" = "1" ] || exit 0

printf 'session-brief:\n%s' "$output"
