# FC Online Event Rewards Plugin — Design

Date: 2026-10-22
Status: Approved conversational design; awaiting written-spec review.

## Goal

Package the existing Korean FC Online web-reward workflow as one public GitHub project that users can install from both Codex and Claude Code. The same skill content must serve both hosts so event steps and corrections do not drift.

## Approved scope and constraints

- Repository: jongfighter/fconline-event-rewards, public.
- Plugin and skill identifier: fconline-event-rewards.
- Support Codex plugin marketplaces and Claude Code plugin marketplaces from the same repository.
- Retain the current five official event paths, current season-event discovery, refresh-before-eligibility checks, quiz research, visit verification, reward receipt verification, and separation from in-game item consumption.
- Remove local-history references that point to files on the author's computer.
- State that the skill uses browser automation and web search tools available in the host; the package itself does not install a browser, provide Nexon authentication, or contain credentials.
- Use MIT licensing, as proposed and accepted during design.
- Publish the GitHub repository and its marketplace manifests only. Do not submit to the OpenAI or Anthropic public plugin directories as part of this task.

## Approaches considered

1. One shared plugin with host-specific manifests and marketplace catalogs (selected). Keep the skill and references in one plugin folder, with Codex and Claude Code manifests around the same content. This avoids duplicated instructions and supports each host's marketplace installer.
2. Separate plugin folders for each host. This would permit host-specific skill text but duplicates the workflow and makes later event corrections prone to drift.
3. Publish only a standalone skill. This is smaller, but does not satisfy the request for an installable plugin and would leave users to copy files manually.

## Repository layout

    fconline-event-rewards/
    ├── .agents/plugins/marketplace.json       # Codex repository marketplace
    ├── .claude-plugin/marketplace.json        # Claude Code marketplace
    ├── LICENSE                                # MIT
    ├── README.md                              # Korean install and capability guide
    └── plugins/
        └── fconline-event-rewards/
            ├── plugin.json                    # Portable Agent Plugins manifest for Codex
            ├── .claude-plugin/plugin.json     # Claude Code plugin manifest
            └── skills/
                └── fconline-event-rewards/
                    ├── SKILL.md
                    ├── agents/openai.yaml     # Codex presentation metadata
                    └── references/event-ui.md

Both marketplace entries point to ./plugins/fconline-event-rewards. Codex discovers the portable manifest and skill from the plugin root. Claude Code reads its .claude-plugin/plugin.json and discovers the skill under skills/. Claude Code may ignore agents/openai.yaml; it is metadata for Codex only and is not needed for the skill workflow.

## Workflow portability

The bundled SKILL.md and event-ui.md remain the single source of workflow behavior. Replace wording that assumes a specific host's Playwright implementation with host-neutral instructions to use the currently available authenticated browser and search tools. If those tools are missing, the agent must report which step is blocked, continue independent event checks where possible, and never claim the mission or reward completed without observed confirmation.

Do not include local event audit files, browser profiles, screenshots, account identifiers, or secrets. Historical event instructions remain explicitly subject to rechecking current pages and dates.

## Installation and distribution

The README explains how to add the GitHub marketplace in each tool:

- Codex: run codex plugin marketplace add jongfighter/fconline-event-rewards, then install the plugin from the Plugins Directory.
- Claude Code: run claude plugin marketplace add jongfighter/fconline-event-rewards, then install with claude plugin install fconline-event-rewards@fconline-event-rewards.

The README scopes Claude support to Claude Code marketplace installs. Publishing to Claude's consumer plugin directory or OpenAI's universal directory would require separate submission and review and is outside this GitHub-sharing request.

## Validation

- Parse all JSON manifests and verify their names and relative paths agree.
- Run the Codex quick_validate.py skill validator on the packaged skill.
- Run claude plugin validate on both the plugin directory and Claude marketplace.
- Exercise Codex marketplace discovery using an isolated Codex configuration so the user's normal plugin settings are not changed.
- Review the final tree for local paths, browser data, credentials, and user-specific event history before publishing.

## Success criteria

The public repository contains one maintainable skill source, valid Codex and Claude Code manifests and marketplaces, documented install commands for both hosts, and a passing validation result for each available CLI. The final report links the public repository and states any runtime tool prerequisites clearly.
