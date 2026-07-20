> 이 파일은 번역본입니다. 실제로 배포되는 원본:
> [source-structure의 영문 버전](../../../../src/agent_scaffold/source-structure/common/.claude/skills/release-versioning/SKILL.md)

---
name: release-versioning
description: 변경 사항을 배포할 준비가 됐을 때, 버전 상승 판단과
  CHANGELOG 항목 작성이 필요할 때 사용한다. Semantic Versioning 기준으로
  변경을 분류하고 Keep a Changelog 형식의 항목을 초안 작성한다.
---

# 릴리스 버전 관리

## 변경 분류하기

- **MAJOR** — 하위 호환이 깨지는 변경: 공개 API·CLI 플래그·설정 형식이
  제거되거나 비호환적으로 바뀜, 또는 프로젝트가 항상 포함하던 파일이
  제거됨.
- **MINOR** — 하위 호환되는 추가: 기존 동작을 바꾸지 않는 새 기능·
  플래그·파일.
- **PATCH** — 버그 수정, 또는 동작 변화 없는 문구·문서 수정.

"Breaking" 항목을 쓰기 전에, 되돌리려는 그 변경이 실제로 릴리스된 버전에
포함된 적이 있는지 먼저 확인한다. `[Unreleased]` 상태로만 존재했던
변경은 그걸 설치한 사람이 아무도 없으므로 깨뜨릴 대상이 없다 — 아직
나가지 않은 이력을 되돌리는 것뿐이지 MAJOR 상승이 아니다.

## 항목 작성하기

`CHANGELOG.md`의 `[Unreleased]` 섹션에, 해당하는 Keep a Changelog
표제(`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`)
아래에 추가한다. 변경 하나당 한 줄, 명령형으로, 구현 세부사항이 아니라
업그레이드 여부를 판단하는 사람을 위해 쓴다.

```markdown
## [Unreleased]

### Added

- 무엇이 왜 바뀌었는지, 사용자 관점에서 짧게.
```

번역된 CHANGELOG(예: `docs/ko/CHANGELOG.md`)를 유지하는 프로젝트라면
같은 항목을 거기에도 반영한다.

## 자기합리화 체크

| 생각 | 반박 |
|---|---|
| "이건 사소해서 changelog 항목은 생략하자" | 사용자에게 조금이라도 보이는 변경이면 changelog에 들어가야 한다 — "사소하다"는 생략할 이유가 아니라 항목을 짧게 쓸 이유다. |
| "다 Added로 적는 게 간단하다" | 잘못된 분류는 릴리스 시점에 changelog를 읽을 수 없게 만든다. Removed와 Changed는 이유가 있어서 존재한다. |
| "MAJOR인 게 확실하니 릴리스됐는지 확인 안 해도 됨" | 확인은 최근 릴리스된 버전의 changelog를 한 번 보는 것뿐이다. 아무도 의존한 적 없는 걸 MAJOR로 올리면 사람들이 당신의 MAJOR 상승을 무시하게 된다. |
