# agent-scaffold

**🇰🇷 한국어** | [🇺🇸 English](../../README.md)

Claude Code의 `CLAUDE.md` + `.claude/{skills,commands,rules,agents,hooks}/` 레이아웃을
현재 프로젝트에 추가하는 CLI입니다.

## 설치 & 실행

별도 설치 과정 없이, [uv](https://docs.astral.sh/uv/)로 소스에서 바로 실행합니다:

```bash
uvx --from git+https://github.com/taehokim97/agent-scaffold agent-scaffold
```

현재 디렉터리에 스캐폴드를 복사합니다. 다른 경로를 지정하거나, 이미 있는
파일을 덮어쓰려면 `--force`를 사용하세요:

```bash
uvx --from git+https://github.com/taehokim97/agent-scaffold agent-scaffold path/to/project --force
```

## 생성되는 결과물

```
.
├── CLAUDE.md          # 스켈레톤: 개요, 빌드/테스트, 코드 스타일, 에이전트를 위한 메모
└── .claude/
    ├── skills/        # 스킬 포맷은 이 리포의 소스에 문서화되어 있음
    ├── commands/      # 슬래시 커맨드 포맷은 이 리포의 소스에 문서화되어 있음
    ├── rules/         # 프로젝트 룰 포맷은 이 리포의 소스에 문서화되어 있음
    ├── agents/        # 서브에이전트 포맷은 이 리포의 소스에 문서화되어 있음
    └── hooks/         # 훅 스크립트 — .claude/settings.json에 별도로 등록됨
```

실행할 때마다 동일한 내용이 복사됩니다 (무엇이 포함되고 어디서 왔는지는
Credits 참고).

이 리포에서 각 디렉터리에 있는 포맷 설명 문서(`README.md`)는 프로젝트로 복사되지 않습니다.

## 로드맵

지금 당장은 Claude Code만 대상으로 합니다 — 제가 평소에 쓰는 에이전트가 그것뿐이라,
두 번째로 실제 필요한 사례가 생기기 전에 일반화할 이유가 없습니다. 필요해지면
`--agent codex|claude` 플래그로 Claude Code의 네이티브 레이아웃과 범용 `AGENTS.md`
표준 출력 중 선택할 수 있게 할 계획입니다.

## Credits (참고한 곳)

`CLAUDE.md` + `.claude/{skills,commands,rules,agents,hooks}/` 레이아웃은
[Claude Code](https://docs.claude.com/en/docs/claude-code) 자체의 프로젝트 메모리,
스킬, 슬래시 커맨드, 룰, 서브에이전트, 훅 컨벤션을 그대로 따릅니다 — 이 스캐폴드는
그 설정을 자동화해줄 뿐입니다.

- **`reproducible-debugging`** 스킬 — [mattpocock/skills](https://github.com/mattpocock/skills)의
  `diagnosing-bugs`가 쓰는 재현 게이트 디버깅 루프, 그리고
  [obra/superpowers](https://github.com/obra/superpowers)가 여러 스킬에서 쓰는
  자기합리화 체크 표 기법에서 영감을 받았습니다. 파일을 그대로 복사하지 않고
  처음부터 다시 썼습니다. 한글 번역은
  [`docs/ko/skills/reproducible-debugging/`](skills/reproducible-debugging/SKILL.md)에
  있습니다(참고용 — CLI가 실제로 설치하는 건 영문 버전입니다).
- **`spec-driven-development`** 스킬 —
  [obra/superpowers](https://github.com/obra/superpowers)의
  `subagent-driven-development`가 쓰는 재개 원장과 `writing-plans` 스킬,
  그리고 [mattpocock/skills](https://github.com/mattpocock/skills)의
  `grill-with-docs → to-spec` 인터뷰 체인에서 영감을 받았습니다. 처음부터
  다시 썼습니다. 한글 번역:
  [`docs/ko/skills/spec-driven-development/`](skills/spec-driven-development/SKILL.md).
- **`release-versioning`** 스킬 — 제공: 사용자. 외부 저장소를 각색한 게
  아니라 이 프로젝트 자체의 [CONTRIBUTING.md](CONTRIBUTING.md) 버저닝
  정책을 재사용 가능한 스킬로 옮긴 것입니다. 한글 번역:
  [`docs/ko/skills/release-versioning/`](skills/release-versioning/SKILL.md).
- **`research-brief`** 스킬 —
  [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)의
  `to_human/` 진행 리포트 관행과
  [wanshuiyin/ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)의
  protocol-lock 원칙에서 영감을 받았습니다. 처음부터 다시 썼고 — 함께
  조사했던 다른 리서치 스킬 저장소에서 봤던, 권한을 우회하는 무인 자동화
  패턴은 의도적으로 배제했습니다. 한글 번역:
  [`docs/ko/skills/research-brief/`](skills/research-brief/SKILL.md).

## Contributing (기여하기)

[CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.

## License

[MIT](../../LICENSE)
