> 이 파일은 번역본입니다. 실제로 배포되는 원본:
> [source-structure의 영문 버전](../../../src/agent_scaffold/source-structure/common/.claude/commands/thk-research.md)

---
description: Turn an open research question into a scoped brief (question, in/out of scope, stop condition) using the research-brief skill, before running or handing it off.
---

# /thk-research

`research-brief` 스킬로 가는 명시적인 정문이다. 스킬 파일은 브리프의
네 가지 항목이 이미 정해져 있다고 가정하는데, 이 커맨드가 실제로 그걸
한 번에 하나씩 물어서 이끌어낸다:

1. **질문** — 실제로 알아내고자 하는 것은 무엇인가?
2. **범위 안** — 무엇을 확인해야 하는가?
3. **범위 밖** — 흥미로워 보여도 쫓지 말아야 할 것은 무엇인가?
4. **중단 조건** — 시간 제한인가, 확인할 출처 개수인가, 아니면 확신에
   도달하는 것인가?

## 지금 하는가, 넘기는가?

명시적으로 묻는다: 이 조사를 지금 이 세션에서 바로 할 것인가, 아니면
길게 실행되거나 무인으로 도는 세션에 넘길 것인가? 넘기는 경우라면,
반드시 하나의 긴 세션으로 실행하거나 정상적인 권한 확인 프롬프트가
살아있는 하네스 자체의 스케줄링(예: 스스로 페이스를 조절하는 루프)으로
실행해야 하며, "진짜 무인"으로 보이게 하려고 권한을 상향하거나
우회해서 연결해서는 안 된다는 것을 분명히 말한다. 스킬은 이 규칙을
명시하고 있을 뿐이며, 이 커맨드는 그 규칙이 넘기기 전에 실제로
확인되는 지점이다 — 당연히 알고 있을 거라 가정하지 않는다.

## 그다음

위 네 가지 답변으로 `research/<kebab-case-slug>/findings.md`에 브리프
헤더 블록을 작성하고, 이후로는 `research-brief` 스킬이 문서화한 그대로
진행한다: 주장 하나당 발견 항목 하나, 모든 주장에는 출처, 추측 대신
`needs verification` 표시.
