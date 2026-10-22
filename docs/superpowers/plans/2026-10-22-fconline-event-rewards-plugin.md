# FC Online Event Rewards Plugin Implementation Plan

> For agentic workers: REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Publish one FC Online web-reward plugin source that can be installed from Codex and Claude Code marketplaces.

**Architecture:** Keep the existing reward workflow once under plugins/fconline-event-rewards/skills/fconline-event-rewards. Add a portable Codex plugin manifest, a Claude Code plugin manifest, and separate marketplace catalogs that both point to the same plugin directory.

**Tech Stack:** Markdown skill and documentation, JSON manifests, Python skill validator, Codex CLI, Claude Code CLI, GitHub CLI.

**Spec:** docs/superpowers/specs/2026-10-22-fconline-rewards-plugin-design.md

## Global Constraints

- Repository: jongfighter/fconline-event-rewards, public.
- Plugin and skill identifier: fconline-event-rewards.
- Keep one shared skill source for Codex and Claude Code.
- Keep both marketplace entries pointed at ./plugins/fconline-event-rewards.
- Retain the five official event paths and current season-event discovery.
- Use browser automation and web search tools available in each host; do not claim that the plugin installs or authenticates them.
- Remove local-history paths and do not publish browser data, screenshots, account identifiers, or secrets.
- Use MIT licensing.
- Publish the GitHub repository only; do not submit to the OpenAI or Anthropic public plugin directories.

## Review Focus

- Browser or search tools are unavailable: the skill reports the blocked step and continues independent checks; validate by reviewing the skill's tool-prerequisite instructions.
- Quiz evidence is inconclusive: the skill does not guess and keeps processing other events; validate against a representative uncertain-quiz scenario.
- A visit link opens but progress does not update: the skill returns to the event, refreshes status, and does not report completion without evidence; validate against a no-status-change scenario.
- An event refresh fails or a fixed event has ended: the skill records uncertainty or expiry, checks current official listings, and continues other events; validate against a partial-failure scenario.
- Public package accidentally includes personal data: final pre-publish scan finds no local audit paths, browser profiles, account identifiers, screenshots, or secrets.

---

### Task 1: Bundle and port the reward skill

**Files:**
- Create: plugins/fconline-event-rewards/skills/fconline-event-rewards/SKILL.md
- Create: plugins/fconline-event-rewards/skills/fconline-event-rewards/agents/openai.yaml
- Create: plugins/fconline-event-rewards/skills/fconline-event-rewards/references/event-ui.md
- Source: the installed local Codex skill folder named fconline-event-rewards.

**Inputs:** The existing local skill folder and the approved design spec.

**Outputs:** One self-contained, host-neutral skill directory preserving the established event-reward workflow.

- [ ] Copy SKILL.md, agents/openai.yaml, and references/event-ui.md from the existing skill into the package layout.
- [ ] Update browser and web-search wording so it names available host tools generically; say the package does not supply those tools or Nexon authentication.
- [ ] Remove the local event-audit file paths from references/event-ui.md while preserving the warning not to treat old status data as current.
- [ ] Run the skill creator's quick_validate.py against the packaged skill directory; expected result: validation passes.
- [ ] Manually review the five Review Focus scenarios against the skill instructions and confirm each has the expected stop/continue behavior.
- [ ] Commit the skill bundle with message: docs: package FC Online reward skill.

### Task 2: Add dual-host manifests, marketplaces, and install documentation

**Files:**
- Create: .agents/plugins/marketplace.json
- Create: .claude-plugin/marketplace.json
- Create: plugins/fconline-event-rewards/plugin.json
- Create: plugins/fconline-event-rewards/.claude-plugin/plugin.json
- Create: README.md
- Create: LICENSE

**Inputs:** Task 1's plugin directory and the approved design spec.

**Outputs:** A public-ready repository that each host can discover and install from the same plugin files.

- [ ] Add the portable Agent Plugins manifest with the stable name, initial version 0.1.0, description, author, repository URL, MIT license, and OpenAI interface metadata.
- [ ] Add the Claude Code plugin manifest with the same stable name, version, description, and author.
- [ ] Add the Codex marketplace entry with the required installation policy, authentication policy, category, and local source path ./plugins/fconline-event-rewards.
- [ ] Add the Claude Code marketplace entry with owner metadata and source path ./plugins/fconline-event-rewards.
- [ ] Write a Korean README with tool prerequisites, scope, and install steps: codex plugin marketplace add jongfighter/fconline-event-rewards followed by installation in the Codex Plugins Directory; claude plugin marketplace add jongfighter/fconline-event-rewards followed by claude plugin install fconline-event-rewards@fconline-event-rewards.
- [ ] Add the standard MIT license text and verify the portable manifest declares MIT.
- [ ] Parse each JSON file with Python's JSON parser and verify all plugin names and relative source paths agree; expected result: every file parses and both marketplace paths resolve to the plugin directory.
- [ ] Commit the manifests and documentation with message: feat: add Codex and Claude Code plugin packaging.

### Task 3: Validate host discovery and package contents

**Files:**
- Verify: all files created in Tasks 1 and 2.

**Inputs:** The complete local plugin repository.

**Outputs:** Recorded validation results and a clean, publishable tree.

- [ ] Run claude plugin validate plugins/fconline-event-rewards; expected result: Validation passed.
- [ ] Run claude plugin validate . from the repository root; expected result: marketplace validation passes.
- [ ] Set a task-specific temporary CODEX_HOME, add the local repository with codex plugin marketplace add, and run codex plugin marketplace list; expected result: the local Codex marketplace resolves without changing the user's normal Codex settings.
- [ ] Scan the package for local user paths, browser profile names, event-audit filenames, credentials, and screenshots; expected result: no personal artifacts are present.
- [ ] Check git status and review the final manifest paths and README commands; expected result: only intended plugin files are tracked and every referenced path exists.
- [ ] Commit any validation-driven corrections with a focused message.

### Task 4: Publish the approved package to GitHub

**Files:**
- Publish: the complete repository at jongfighter/fconline-event-rewards.

**Inputs:** Passing Task 3 validation and the user's explicit request for a public GitHub repository.

**Outputs:** A public GitHub repository with the default branch pushed.

- [ ] Confirm the final branch has no uncommitted changes and repeat the personal-data scan.
- [ ] Create jongfighter/fconline-event-rewards as a public repository and push the default branch with GitHub CLI.
- [ ] Query GitHub for the repository visibility and URL; expected result: visibility is PUBLIC and the URL resolves.
- [ ] Confirm both marketplace manifests and the installation README are visible in the public repository.
