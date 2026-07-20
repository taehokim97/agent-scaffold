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
- `spec-driven-development` 스킬 추가: 비트리비얼한 기능 작업을 위해
  `specs/<slug>/` 폴더(배경, 요구사항, 계획, 작업목록, 발견사항, 재개
  로그)를 관리합니다.
- `release-versioning` 스킬 추가: 변경 사항을 Semantic Versioning 기준으로
  분류하고 CHANGELOG 항목을 초안 작성합니다.
- `research-brief` 스킬 추가: 열려 있는 조사 질문을 출처와 중단 조건이
  있는 스코프 있는 브리프로 구조화한 뒤 긴 세션이나 무인 세션에
  넘깁니다.

## [0.1.0] - 2026-07-16

### Added

- `agent-scaffold` CLI: 템플릿 `CLAUDE.md` + `.claude/{skills,commands,rules,agents}/`를
  대상 디렉터리에 복사합니다. `--force`를 주지 않으면 이미 있는 파일은 건너뜁니다.
- 템플릿 페이로드: 스켈레톤 `CLAUDE.md`와 빈 `.claude/skills/`, `.claude/commands/`,
  `.claude/rules/`, `.claude/agents/` 디렉터리(각각 이 리포 안의 `README.md`로
  포맷이 설명되어 있으며, 대상 프로젝트로는 복사되지 않습니다).
- CI 워크플로우(린트 + 테스트).
