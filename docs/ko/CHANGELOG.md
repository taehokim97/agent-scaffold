# Changelog

**🇰🇷 한국어 | [🇺🇸 English](../../CHANGELOG.md)**

이 프로젝트의 모든 주요 변경점은 이 파일에 기록됩니다.

문서 형식은 [Keep a Changelog](https://keepachangelog.com/ko/1.1.0/)를 따르며,
이 프로젝트는 [Semantic Versioning](https://semver.org/lang/ko/spec/v2.0.0.html)을 준수합니다.

## [Unreleased]

### Added

- 스캐폴드 레이아웃에 `.claude/hooks/` 추가 (현재는 비어 있음 — 훅 스크립트는
  `.claude/settings.json`을 통해 별도로 등록됩니다).
- `reproducible-debugging` 스킬 추가: 템플릿의 첫 번째 실제 스킬로, 버그를
  고치기 전에 재현 → 원인 → 수정 → 검증 루프를 강제합니다. 출처는 README
  Credits 참고.

## [0.1.0] - 2026-07-16

### Added

- `agent-scaffold` CLI: 템플릿 `CLAUDE.md` + `.claude/{skills,commands,rules,agents}/`를
  대상 디렉터리에 복사합니다. `--force`를 주지 않으면 이미 있는 파일은 건너뜁니다.
- 템플릿 페이로드: 스켈레톤 `CLAUDE.md`와 빈 `.claude/skills/`, `.claude/commands/`,
  `.claude/rules/`, `.claude/agents/` 디렉터리(각각 이 리포 안의 `README.md`로
  포맷이 설명되어 있으며, 대상 프로젝트로는 복사되지 않습니다).
- CI 워크플로우(린트 + 테스트).
