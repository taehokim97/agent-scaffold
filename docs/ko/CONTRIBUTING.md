# Contributing (기여하기)

**🇰🇷 한국어 | [🇺🇸 English](../../CONTRIBUTING.md)**

## 개발 환경 설정

```bash
git clone https://github.com/taehokim97/agent-scaffold
cd agent-scaffold
uv sync --dev
```

## 검사 실행

```bash
uv run pytest
uv run ruff check .
```

PR을 올리기 전에 두 명령 모두 통과해야 합니다.

## 커밋 컨벤션

커밋은 [Conventional Commits](https://www.conventionalcommits.org/)를 따릅니다:
`feat`, `fix`, `docs`, `chore`, `test`, `ci` 중 하나로 시작하는 짧은 명령형 제목을
사용하세요 (예: `feat: add --dry-run flag`). 커밋 하나에는 논리적으로 하나의
변경만 담으세요.

## 버전 관리

이 프로젝트는 [시맨틱 버저닝(Semantic Versioning)](https://semver.org/lang/ko/)을
따릅니다:

- **MAJOR** — 하위 호환이 깨지는 변경: CLI 플래그/서브커맨드 제거·이름 변경,
  또는 템플릿이 항상 포함하던 파일 제거.
- **MINOR** — 하위 호환되는 추가: 템플릿에 새 스킬/커맨드 추가, 새 CLI 플래그/서브커맨드
  추가.
- **PATCH** — 버그 수정, 또는 동작 변화 없는 문구·문서 수정.

사용자에게 보이는 변경을 만들 때는 `CHANGELOG.md`(Keep a Changelog 형식)도 함께
갱신하세요.

## 템플릿에 스킬·커맨드·룰·서브에이전트 추가하기

다른 프로젝트에서 가져와 적용하는 경우, 해당하는
`src/agent_scaffold/source-structure/.claude/{skills,commands,rules,agents}/`
디렉터리 아래에 추가하세요. 해당 디렉터리의 `README.md`에 설명된 포맷을 따르고
(이 파일 자체는 대상 프로젝트로 복사되지 않습니다 — `_template.py` 참고), 이
프로젝트의 `README.md` Credits 섹션에 `inspired by` 또는 `based on` 태그와 출처
링크로 함께 기록하세요.

## 브랜치 전략

초기 단계의 작은 변경은 `main`에 바로 반영될 수 있습니다. 프로젝트가 커지면
`main`에 직접 푸시하는 대신 기능 브랜치 + PR을 통해 기여해야 합니다.
