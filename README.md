# FC Online Skills

FC 온라인 플레이를 돕는 스킬 플러그인 모음입니다. Codex·ChatGPT, Claude Code, OpenCode에서 같은 스킬 파일(`plugins/*/skills/`)을 공유합니다. 필요한 플러그인만 골라 설치할 수 있습니다.

> **운영정책 위험 경고 (`fconline-items-manager`)**
> `fconline-items-manager`는 실행 중인 FC ONLINE 창에 마우스·키 입력을 보내는 스크립트(`scripts/game_ui.py`)를 포함합니다. 게임 메모리나 패킷은 건드리지 않지만, 넥슨 운영정책의 자동 프로그램·매크로 규정에 해당할 수 있어 **계정이 제재받을 수 있습니다.** 사용 여부와 그 결과의 책임은 사용자에게 있습니다. 위험을 받아들일 때만 설치하세요. 나머지 두 플러그인은 게임 창에 입력을 보내지 않습니다.

이 저장소는 비공식 프로젝트이며 넥슨·EA와 무관합니다.

| 플러그인 | 하는 일 | 게임 입력 |
| --- | --- | --- |
| `fconline-event-rewards` | 공식 웹 이벤트·웹상점·멤버십 보상 확인과 수령, 이벤트 코인 미니게임 진행 | 없음 (브라우저) |
| `fconline-tactics-review` | 현재 스쿼드·전술·코치를 확인하고 개선안을 HTML 조언판으로 작성 | 없음 (브라우저) |
| `fconline-items-manager` | 게임 보관함 수령, 박스·카드 개봉, 재료 소진·BP 전환, 감독모드 시작 | **있음 (경고 참고)** |

이 플러그인들은 브라우저, 웹 검색, 넥슨 인증을 제공하지 않으며 실제 공식경기를 대신 플레이하지 않습니다. 호스트에 브라우저와 검색 도구가 필요합니다. 플러그인 자체는 스킬 문서와 스크립트만 포함하며 데이터를 수집하거나 외부로 전송하지 않고 계정 정보를 저장하지 않습니다.

## 로그인

보상 수령 요청에는 로그인 진행이 포함됩니다. 아래 동작은 `fconline-event-rewards`에 적용되며, 로그인이 필요한 `fconline-tactics-review`도 같은 원칙(직접 입력 요구, 값 비노출, 추가 인증은 사용자가 직접)을 따릅니다.

- 로그인 상태가 아니면 공식 페이지의 로그인 버튼을 눌러 넥슨 로그인 화면을 엽니다.
- 아이디와 비밀번호 입력란이 모두 채워져 있고 추가 인증이 없으면 `넥슨 ID 로그인`을 눌러 제출하고 성공 여부를 확인합니다.
- **아이디나 비밀번호가 비어 있으면 대신 입력하지 않고 멈춥니다.** 열려 있는 브라우저의 로그인 화면에 사용자가 직접 입력해야 하며, 입력을 마쳤다고 알리면 이어서 진행합니다. 아이디·비밀번호를 채팅으로 보낼 필요가 없고 보내서도 안 됩니다.
- 입력값은 응답·기록에 옮기지 않고 채워졌는지만 값 길이의 참·거짓으로 확인합니다. 브라우저 도구의 스냅샷·텍스트 찾기·네트워크 요청 본문 조회는 비밀번호 칸을 포함한 입력값을 그대로 돌려줄 수 있어(Playwright MCP로 확인), 로그인 폼이 열려 있는 동안에는 호출하지 않도록 스킬에 명시했습니다. 다만 Playwright MCP는 이동·클릭 뒤에 스냅샷을 `.playwright-mcp/page-*.yml`로 자동 저장하므로, 입력값이 DOM에 있으면 그 파일에 남을 수 있습니다. 호스트와 도구 설정에 따라 동작이 다를 수 있으니 이 점이 걱정되면 직접 로그인한 뒤 요청하고, 로그인 뒤에는 해당 폴더의 파일을 확인하세요.
- CAPTCHA·2단계 인증·QR 로그인 등 추가 절차는 사용자가 브라우저에서 직접 완료합니다. 인증번호를 채팅으로 보낼 필요가 없습니다.
- 로그인 실패 메시지가 나오면 같은 입력으로 반복 제출하지 않고 사용자에게 다시 입력을 요청합니다. 계정 잠금·보호조치 안내가 나오면 멈춥니다.

## 설치

마켓플레이스 이름은 `fconline-event-rewards`입니다. 아래에서 필요한 플러그인 이름(`fconline-event-rewards`, `fconline-tactics-review`, `fconline-items-manager`)만 골라 쓰세요.

### Codex · ChatGPT

```text
codex plugin marketplace add jongfighter/fconline-event-rewards
codex plugin add fconline-event-rewards@fconline-event-rewards
codex plugin add fconline-tactics-review@fconline-event-rewards
```

ChatGPT 데스크톱 앱은 같은 마켓플레이스 파일(`.agents/plugins/marketplace.json`)을 읽습니다. 앱의 Plugins Directory에 `FC Online Skills`가 보이면 거기서 설치해도 됩니다.

### Claude Code

```text
claude plugin marketplace add jongfighter/fconline-event-rewards
claude plugin install fconline-event-rewards@fconline-event-rewards
claude plugin install fconline-tactics-review@fconline-event-rewards
```

설치 후 새 세션에서 요청하면 스킬이 적용됩니다.

### OpenCode

OpenCode V2의 플러그인으로 설치합니다. 각 플러그인이 같은 이름의 스킬을 등록합니다.

```text
opencode plugin add 'github:jongfighter/fconline-event-rewards#main::path:plugins/fconline-event-rewards'
opencode plugin add 'github:jongfighter/fconline-event-rewards#main::path:plugins/fconline-tactics-review'
```

- Git 하위 폴더 설치는 `::path:` 앞에 `#main` 같은 ref가 필요합니다. PowerShell에서는 전체를 작은따옴표로 감쌉니다. 특정 버전에 고정하려면 `main` 대신 태그나 전체 커밋 해시를 씁니다.
- 저장소를 내려받아 쓰려면 `opencode.jsonc`의 `plugins`에 플러그인 폴더 경로를 넣습니다.

  ```jsonc
  {
    "plugins": ["/absolute/path/to/fconline-event-rewards/plugins/fconline-event-rewards"]
  }
  ```

- 같은 ID의 스킬이 `~/.config/opencode/skills`, `.opencode/skills`, `.claude/skills`, `.agents/skills`에 이미 있으면 그 스킬이 플러그인의 스킬보다 우선합니다. 플러그인으로 바꿀 때는 기존 스킬 폴더를 정리하고 OpenCode를 다시 시작하세요.
- Git 플러그인은 서버 시작 시 백그라운드에서 설치되어 처음에는 몇 초 늦게 나타날 수 있습니다. 설치 후 `SKILL.md`만 고치면 바로 반영되지 않으니 OpenCode를 다시 시작해야 합니다.

### fconline-items-manager 설치 (경고를 읽은 경우만)

위 경고를 이해하고 받아들였다면 같은 방식으로 `fconline-items-manager`를 설치합니다.

```text
codex plugin add fconline-items-manager@fconline-event-rewards
claude plugin install fconline-items-manager@fconline-event-rewards
opencode plugin add 'github:jongfighter/fconline-event-rewards#main::path:plugins/fconline-items-manager'
```

Windows와 Python, Pillow(`pip install pillow`)가 필요합니다. 게임 캡처는 기본적으로 `~/FCOnline/skill-ui-captures`에 저장되며 닉네임·보유 재화 등이 보일 수 있으니 공유 전에 확인하세요.

## 업데이트

```text
codex plugin marketplace upgrade fconline-event-rewards
claude plugin marketplace update fconline-event-rewards
claude plugin update <플러그인 이름>@fconline-event-rewards
opencode plugin update
```

## 범위

웹 이벤트와 웹상점에서 보상이 지급되면 사이트의 완료 메시지나 수령 완료 상태로 검증합니다. 게임 내 보관함으로 지급되는 아이템은 실제 게임 보관함에서 확인해야 합니다. 이벤트 미니게임의 성공 여부와 아이템팩 구성품은 확률에 따라 달라질 수 있습니다. 전술 분석은 설정에서 추정한 가설이며 승률을 보장하지 않습니다.

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
