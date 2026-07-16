# agent-scaffold

**🇰🇷 한국어** | [🇺🇸 English](../../README.md)

Claude Code의 `CLAUDE.md` + `.claude/{skills,commands,rules,agents,hooks}/` 레이아웃을
현재 프로젝트에 추가하는 CLI입니다. **프로필**(`dev` 또는 `research`)을 선택해서
어떤 스킬/커맨드/룰/에이전트/훅이 채워질지 결정합니다.

## 설치 & 실행

별도 설치 과정 없이, [uv](https://docs.astral.sh/uv/)로 소스에서 바로 실행합니다:

```bash
uvx --from git+https://github.com/taehokim97/agent-scaffold agent-scaffold --profile dev
```

`--profile`은 필수입니다 — `dev` 또는 `research` 중 선택하세요. 현재 디렉터리에
스캐폴드를 복사합니다. 다른 경로를 지정하거나, 이미 있는 파일을 덮어쓰려면
`--force`를 사용하세요:

```bash
uvx --from git+https://github.com/taehokim97/agent-scaffold agent-scaffold path/to/project --profile research --force
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

`CLAUDE.md`와 빈 디렉터리 레이아웃 자체는 모든 프로필에서 동일합니다. `.claude/`
안에 실제로 어떤 스킬/커맨드/룰/에이전트/훅이 들어가는지는 선택한 `--profile`에
따라 다릅니다 — `dev`와 `research`는 서로 다른 콘텐츠를 담습니다 (무엇이 포함되고
어디서 왔는지는 Credits 참고).

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

이 스캐폴드는 아직 구체적인 스킬·커맨드·룰·에이전트·훅을 담고 있지 않습니다 —
`dev`/`research` 프로필은 현재 디렉터리 구조만 있고 비어 있습니다. 콘텐츠가
추가되면 여기에 `inspired by` 또는 `based on` 태그와 출처 링크로 함께 기록하겠습니다
(직접 제공받아 채택한 콘텐츠는 "제공: 사용자"로 표기).

## Contributing (기여하기)

[CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.

## License

[MIT](../../LICENSE)
