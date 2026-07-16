# Changelog

**🇰🇷 한국어 | [🇺🇸 English](../../CHANGELOG.md)**

이 프로젝트의 모든 주요 변경점은 이 파일에 기록됩니다.

문서 형식은 [Keep a Changelog](https://keepachangelog.com/ko/1.1.0/)를 따르며,
이 프로젝트는 [Semantic Versioning](https://semver.org/lang/ko/spec/v2.0.0.html)을 준수합니다.

## [0.1.0] - 2026-07-16

### Added

- `agent-scaffold` CLI: 템플릿 `CLAUDE.md` + `.claude/{skills,commands,rules,agents}/`를
  대상 디렉터리에 복사합니다. `--force`를 주지 않으면 이미 있는 파일은 건너뜁니다.
- 템플릿 페이로드: 스켈레톤 `CLAUDE.md`와 빈 `.claude/skills/`, `.claude/commands/`,
  `.claude/rules/`, `.claude/agents/` 디렉터리(각각 이 리포 안의 `README.md`로
  포맷이 설명되어 있으며, 대상 프로젝트로는 복사되지 않습니다).
- CI 워크플로우(린트 + 테스트).
