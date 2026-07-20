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

## 템플릿에 스킬·커맨드·룰·훅·서브에이전트 추가하기

템플릿 페이로드는 전부 `src/agent_scaffold/source-structure/common/` 아래에
있습니다: `CLAUDE.md`와 `.claude/{skills,commands,rules,agents,hooks}/`
카테고리 디렉터리입니다. 각 카테고리 디렉터리에는 포맷 설명 문서
`README.md`도 있는데, 이 파일 자체는 대상 프로젝트로 복사되지 않습니다 —
`_template.py` 참고.

새 콘텐츠는 해당하는
`common/.claude/{skills,commands,rules,agents,hooks}/` 디렉터리 아래에,
그 카테고리의 `README.md`에 설명된 포맷을 따라 추가하세요. 훅은 예외입니다:
스크립트만 있어서는 아무 동작도 하지 않고, `common/.claude/settings.json`에도
함께 등록해야 합니다 (두 부분 구조는 `common/.claude/hooks/README.md` 참고).

다른 프로젝트에서 가져와 적용하는 경우, 이 프로젝트의 `README.md` Credits
섹션에 `inspired by` 또는 `based on` 태그와 출처 링크로 함께 기록하세요. 먼저
라이선스를 확인하세요 — 카피레프트나 라이선스 미표기 콘텐츠를 채택하기 전에
해당 카테고리 PR/이슈의 라이선스 검토 노트를 참고하세요.

## 브랜치 전략

모든 작업은 기능 브랜치 + PR을 통해서만 진행합니다 — `main`에 직접 푸시하지
않습니다. 논리적으로 하나의 작업 단위마다 브랜치 하나를 사용하세요 (예: 구조
변경 하나, 또는 `feat/skills-from-public-repos`처럼 카테고리 하나의 콘텐츠
전체). 서로 다른 카테고리를 한 브랜치에 섞지 마세요 — 한 브랜치가 라이선스
검토로 막히더라도 다른 브랜치가 거기에 발이 묶이지 않아야 하기 때문입니다.
로컬에서 `uv run pytest`와 `uv run ruff check .`가 모두 통과한 뒤에 PR을
여세요.
