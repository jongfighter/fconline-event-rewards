# FC Online Event Rewards

FC 온라인 공식 웹 이벤트, 웹상점, 멤버십 보상을 확인하고 수령하는 스킬 플러그인입니다. 이벤트 코인으로 진행하는 참참참·승부차기 같은 미니게임도 현재 조건과 보상 규칙을 확인해 진행합니다.

## 할 수 있는 일

- 로그인된 공식 사이트에서 이벤트 참여 현황을 갱신하고 받을 수 있는 보상을 확인합니다.
- 퀴즈와 방문 미션의 근거를 조사하고, 완료 여부를 다시 조회합니다.
- 공식 웹상점과 플레이어스·구매 멤버십 보상을 확인합니다.
- 이미 획득한 이벤트 전용 무료 코인으로 웹 미니게임을 진행하고 지급 완료 상태를 확인합니다.

이 플러그인은 브라우저, 웹 검색, 넥슨 로그인을 제공하지 않습니다. 호스트에 로그인된 브라우저와 검색 도구가 필요합니다. 계정 로그인이 필요하면 사용자가 직접 로그인해야 합니다. 게임 보관함 아이템 개봉과 쏠돌코인 사용은 이 플러그인의 범위가 아닙니다.

## 설치

### Codex

```text
codex plugin marketplace add jongfighter/fconline-event-rewards
```

Codex Plugins Directory에서 `FC Online Event Rewards`를 설치합니다.

### Claude Code

```text
claude plugin marketplace add jongfighter/fconline-event-rewards
claude plugin install fconline-event-rewards@fconline-event-rewards
```

설치 후 새 세션에서 FC 온라인 보상 수령을 요청하면 스킬이 적용됩니다.

## 범위

웹 이벤트와 웹상점에서 보상이 지급되면 사이트의 완료 메시지나 수령 완료 상태로 검증합니다. 게임 내 보관함으로 지급되는 아이템은 실제 게임 보관함에서 확인해야 합니다. 이벤트 미니게임의 성공 여부와 아이템팩 구성품은 확률에 따라 달라질 수 있습니다.

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
