> 이 파일은 번역본입니다. 실제로 배포되는 원본:
> [source-structure의 영문 버전](../../../src/agent_scaffold/source-structure/common/.claude/commands/thk-ship.md)

---
description: Pre-flight the project's own build/test/lint, then classify the current change and draft a CHANGELOG entry using the release-versioning skill, before treating it as ready to ship.
---

# /thk-ship

`release-versioning` 스킬로 가는 명시적인 정문이며, 스킬이 다루지 않는
한 가지를 더한다: 사전 점검. 빌드가 깨진 상태로 체인지로그 항목이
초안 작성되는 일이 없도록 한다.

## 사전 점검

`CLAUDE.md`의 `## Build & Test` 섹션을 읽고 거기 명시된 것을
실행한다(명령을 하드코딩하지 않는다 — 프로젝트마다 다르다). 하나라도
실패하면 여기서 멈추고 무엇이 실패했는지 알린다. 자체 빌드나 테스트를
통과하지 못하는 변경에 대해 분류하거나 체인지로그 항목을 작성하지
않는다.

## 분류하고 초안 작성

사전 점검이 깨끗하면 `release-versioning` 스킬이 문서화한 그대로
따른다:

1. 변경 사항을 Semantic Versioning 기준(MAJOR / MINOR / PATCH)으로
   분류한다.
2. `CHANGELOG.md`의 `[Unreleased]` 항목을 Keep a Changelog 형식으로
   초안 작성한다.
3. 프로젝트가 번역된 CHANGELOG를 유지한다면 같은 항목을 그쪽에도
   반영한다.

## 최종화 전 확인

분류 결과와 작성한 항목을 알리고, 최종으로 확정하기 전에 사람의
확인을 구한다 — 이건 스킬 파일 자체에는 없는 단계다. 스킬은 워크플로우
중간에 실행된다고 가정할 뿐, 무언가를 출시할지에 대한 마지막 발언으로
쓰인다고 가정하지 않기 때문이다.
