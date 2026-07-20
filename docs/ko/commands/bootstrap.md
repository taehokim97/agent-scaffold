> 이 파일은 번역본입니다. 실제로 배포되는 원본:
> [source-structure의 영문 버전](../../../src/agent_scaffold/source-structure/common/.claude/commands/bootstrap.md)

---
description: Interview to bootstrap a freshly scaffolded project — fills in CLAUDE.md (overview, build/test, code style, and a new Git Workflow section for branch/commit conventions) and hands off into spec-driven-development for the first goal.
---

# /bootstrap

`agent-scaffold`로 프로젝트를 스캐폴딩한 직후(또는 `CLAUDE.md`가 아직
대부분 TODO 상태일 때 언제든) 한 번 실행한다. 빈 스켈레톤을 프로젝트의
실제 헌법으로 바꾸고, 이어서 처음으로 무엇을 만들지에 대한
`specs/<slug>/`를 새로 연다.

## 질문하기 전에

저장소가 이미 알려주는 정보부터 읽는다:

- 매니페스트 파일(`package.json`, `pyproject.toml`, `Cargo.toml`,
  `go.mod`, `Gemfile` 등)에서 설치/빌드/테스트/린트 명령을 확인한다.
- 린트/포맷 설정(`.eslintrc*`, `ruff.toml`/`[tool.ruff]`,
  `.prettierrc*`, `.editorconfig` 등)에서 이미 정해진 네이밍·포맷팅·
  스타일 컨벤션을 확인한다.
- 기존 소스 파일이 있다면 이미 쓰이고 있는 패턴을 확인한다.

스스로 알아낼 수 없었던 것, 또는 온전히 사용자의 판단이 필요한 것만
질문한다. 이미 찾아낸 내용을 다시 말하게 하지 않는다.

## 덮어쓰기 전에 확인

현재 `CLAUDE.md`를 읽는다. `Project Overview`, `Build & Test`,
`Code Style`에 이미 실제 내용이 채워져 있다면 — 배포판이 기본으로
제공하는 `<!-- TODO: ... -->` 자리표시자가 아니라면 — 그 사실을 알리고
계속 진행해서 덮어써도 되는지 확인한다. 기존 답변을 조용히 덮어쓰지
않는다.

## 인터뷰

한 번에 하나씩 질문한다. 저장소를 읽어서 이미 답을 찾은 질문은
건너뛴다 — 열린 질문으로 다시 묻는 대신 한 줄로 확인만 한다.

1. **프로젝트 정체성** — 한 문장으로: 이게 무엇이고, 누구를 위한
   것인가?
2. **빌드 & 테스트** — 에이전트가 실행해야 할 정확한 설치/빌드/테스트/
   린트 명령을 확인(또는 채워 넣기)한다.
3. **코드 스타일** — 포맷팅, 네이밍, 에러 처리 등 컨벤션을 확인(또는
   채워 넣기)한다.
4. **규모** — 혼자 하는 프로젝트/데모인가, 팀/프로덕션 코드베이스인가?
   (다음 질문의 기본 제안값을 결정할 뿐, 강제 규칙은 아니다.)
5. **브랜치 전략** — 정확히 두 가지 선택지:
   - `main`에 직접 커밋, PR 없음. 데모/혼자 하는 프로젝트에 기본 제안.
   - 피처 브랜치 + 머지 전 PR. 팀/프로덕션에 기본 제안.
   4번 답변이 무엇을 제안했든 사용자가 둘 중 아무거나 고를 수 있게
   한다.
6. **커밋 컨벤션** — 기본값으로 [Conventional
   Commits](https://www.conventionalcommits.org/)(`feat:`/`fix:`/
   `docs:`/`chore:`/`test:`/`ci:`, 명령형 제목 줄)를 권장한다. 사용자가
   거부하면 자유형식 설명 커밋을 명시적인 대안으로 제시한다 — 묻지도
   않은 세 번째 방식을 만들어내지 않는다.
7. **에이전트를 위한 메모** — 코드만 봐서는 알기 어려운, 에이전트가
   알아야 할 나머지 정보: 유의사항, 불변조건, 손대면 안 되는 영역.
8. **초기 목표** — 처음에 무엇을 만들 것인가?

## CLAUDE.md 작성

배포판 스켈레톤의 헤딩에 맞춰 제자리에 채워 넣는다:

- 맨 위의 한 줄 설명.
- `## Project Overview`
- `## Build & Test`
- `## Code Style`
- `## Notes for Agents`

그리고 스켈레톤에 없던 섹션 하나를 추가한다:

```markdown
## Git Workflow

- Branching: <5번 답변>
- Commits: <6번 답변>
```

## 첫 스펙으로 인계

`CLAUDE.md` 작성이 끝나면, 8번의 목표를 대상으로
`spec-driven-development` 스킬을 사용한다: 인터뷰를 통해
`specs/<slug>/README.md`와 `spec.md`를 만든다(slug는 목표에서
파생한다). 거기서 멈춘다 — `plan.md`/`tasks.md`는 아직 작성하지 않는다;
이는 스펙 자체가 합의된 뒤에 오는 단계이며, 해당 스킬이 별도의
단계로 다룬다.
