> 이 파일은 번역본입니다. 실제로 배포되는 원본:
> [source-structure의 영문 버전](../../../src/agent_scaffold/source-structure/common/.claude/commands/thk-spec.md)

---
description: Open (or resume) a specs/<slug>/ folder for a piece of work using the spec-driven-development skill, as an explicit entry point instead of relying on the skill auto-triggering.
---

# /thk-spec

`spec-driven-development` 스킬로 가는 명시적인 정문이다. Claude Code가
스킬의 description을 알아서 매칭해줄 거라 믿지 않을 때 쓴다 — 그 매칭은
확률적일 뿐 보장되지 않으며, 프로젝트 로컬 스킬일수록 더 그렇다.

## 먼저 재개 여부 확인

이 작업이 무엇에 대한 것인지 물은 뒤, 해당 작업에 대해
`specs/<slug>/progress.md`가 이미 있는지 확인한다. 있다면
`progress.md`만이 아니라 `specs/<slug>/` 폴더 전체를 먼저 읽고, 인터뷰를
처음부터 다시 시작하는 대신 거기서부터 이어간다.

## 새로 시작하는 경우

넓은 탐색은 직접 하지 말고 위임한다. 인터뷰 전에, 코드베이스나 작업
영역이 크거나 낯설다면 서브에이전트를 이용해 관련 기존 코드와
컨벤션을 조사시키고, 좋은 질문을 하는 데 필요한 것만 가져온다. 스킬의
"스스로 사실을 탐색하라"는 단계는 사람이 이미 아는 걸 다시 설명하지
않게 하려는 것이지, 파일 단위로 넓게 훑은 결과로 정작 자신의
컨텍스트를 채우라는 뜻이 아니다.

그 이후로는 `spec-driven-development` 스킬이 문서화한 그대로 따른다:
한 번에 하나씩 질문하는 인터뷰 → `README.md`(왜) → `spec.md`(무엇을) →
스펙이 합의된 뒤 `plan.md`와 `tasks.md`. 이 커맨드는 그 순서를 바꾸지
않는다 — 그 흐름으로 들어가는 명시적인 트리거일 뿐이다.
