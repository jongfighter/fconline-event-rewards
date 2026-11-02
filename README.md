# FC Online Event Rewards

FC 온라인 공식 웹 이벤트, 웹상점, 멤버십 보상을 확인하고 수령하는 스킬 플러그인입니다. 이벤트 코인으로 진행하는 참참참·승부차기 같은 미니게임도 현재 조건과 보상 규칙을 확인해 진행합니다. Codex, Claude Code, OpenCode에서 같은 스킬 파일(`plugins/fconline-event-rewards/skills/`)을 공유합니다.

## 할 수 있는 일

- 로그인된 공식 사이트에서 이벤트 참여 현황을 갱신하고 받을 수 있는 보상을 확인합니다.
- 퀴즈와 방문 미션의 근거를 조사하고, 완료 여부를 다시 조회합니다.
- 공식 웹상점과 플레이어스·구매 멤버십 보상을 확인합니다.
- 이미 획득한 이벤트 전용 무료 코인으로 웹 미니게임을 진행하고 지급 완료 상태를 확인합니다. 추가 코인을 위해 실제 공식경기가 필요하면 모드, 필요한 경기 수와 이어서 진행하는 방법을 안내합니다.

이 플러그인은 브라우저, 웹 검색, 넥슨 인증을 제공하지 않으며 실제 공식경기를 대신 플레이하지 않습니다. 호스트에 브라우저와 검색 도구가 필요합니다. 게임 보관함 아이템 개봉과 쏠돌코인 사용은 이 플러그인의 범위가 아닙니다.

## 로그인

보상 수령 요청에는 로그인 진행이 포함됩니다.

- 로그인 상태가 아니면 공식 페이지의 로그인 버튼을 눌러 넥슨 로그인 화면을 엽니다.
- 아이디와 비밀번호 입력란이 모두 채워져 있고 추가 인증이 없으면 `넥슨 ID 로그인`을 눌러 제출하고 성공 여부를 확인합니다.
- **아이디나 비밀번호가 비어 있으면 대신 입력하지 않고 멈춥니다.** 열려 있는 브라우저의 로그인 화면에 사용자가 직접 입력해야 하며, 입력을 마쳤다고 알리면 이어서 진행합니다. 아이디·비밀번호를 채팅으로 보낼 필요가 없고 보내서도 안 됩니다.
- 입력값은 읽어 내거나 복사·출력·기록하지 않고 채워졌는지만 확인합니다.
- CAPTCHA·2단계 인증·QR 로그인 등 추가 절차는 사용자가 그 단계만 완료합니다.
- 로그인 실패 메시지가 나오면 같은 입력으로 반복 제출하지 않고 사용자에게 다시 입력을 요청합니다.

## 설치

### Codex

```text
codex plugin marketplace add jongfighter/fconline-event-rewards
codex plugin add fconline-event-rewards@fconline-event-rewards
```

Codex Plugins Directory에서 `FC Online Event Rewards`를 설치해도 됩니다.

### Claude Code

```text
claude plugin marketplace add jongfighter/fconline-event-rewards
claude plugin install fconline-event-rewards@fconline-event-rewards
```

설치 후 새 세션에서 FC 온라인 보상 수령을 요청하면 스킬이 적용됩니다.

### OpenCode

OpenCode V2의 플러그인으로 설치합니다. 플러그인이 `fconline-event-rewards` 스킬을 등록합니다.

```text
opencode plugin add 'github:jongfighter/fconline-event-rewards#main::path:plugins/fconline-event-rewards'
```

- Git 하위 폴더 설치는 `::path:` 앞에 `#main` 같은 ref가 필요합니다. PowerShell에서는 전체를 작은따옴표로 감쌉니다. 특정 버전에 고정하려면 `main` 대신 태그나 전체 커밋 해시를 씁니다.
- 저장소를 내려받아 쓰려면 `opencode.jsonc`의 `plugins`에 플러그인 폴더 경로를 넣습니다.

  ```jsonc
  {
    "plugins": ["/absolute/path/to/fconline-event-rewards/plugins/fconline-event-rewards"]
  }
  ```

- 같은 ID(`fconline-event-rewards`)의 스킬이 `~/.config/opencode/skills`, `.opencode/skills`, `.claude/skills`, `.agents/skills`에 이미 있으면 그 스킬이 플러그인의 스킬보다 우선합니다. 플러그인으로 바꿀 때는 기존 스킬 폴더를 정리하세요.
- Git 플러그인은 서버 시작 시 백그라운드에서 설치되어 처음에는 몇 초 늦게 나타날 수 있습니다. 설치 후 `SKILL.md`만 고치면 바로 반영되지 않으니 OpenCode를 다시 불러옵니다(`/reload`).

## 업데이트

```text
codex plugin marketplace upgrade fconline-event-rewards
claude plugin marketplace update fconline-event-rewards
claude plugin update fconline-event-rewards@fconline-event-rewards
opencode plugin update
```

## 범위

웹 이벤트와 웹상점에서 보상이 지급되면 사이트의 완료 메시지나 수령 완료 상태로 검증합니다. 게임 내 보관함으로 지급되는 아이템은 실제 게임 보관함에서 확인해야 합니다. 이벤트 미니게임의 성공 여부와 아이템팩 구성품은 확률에 따라 달라질 수 있습니다.

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
