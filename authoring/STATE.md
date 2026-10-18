# Current state

Updated: 2026-10-18.

## Implemented

- Independent English charter and source-admissibility boundary, without employer names or abbreviations.
- Repository-wide agent instructions. Work is conducted in the ChatGPT project; GitHub is the book's versioned repository. No coding-assistant delegation is configured.
- Initial authoring methodology, research contract, roadmap and checkpoint.
- Curated public-source inventory, generated catalogue, topic coverage and implementation maps, reading priorities and explicit gaps.
- Workload-to-architecture research dimensions and proposed pilot questions.
- Structural inventory/reference checks, catalogue freshness checks, limited local-link boundary scan and CI workflow.

## Evidence state

Discovery/entry-page inspection is complete for the first inventory pass. Commercial books remain bibliography-only. Canonical pages that could not be fully fetched remain pending-content-access, with accessible official companions recorded. No full-book reading, source-code inspection, benchmark execution, production validation or domain/human review is claimed.

## Planned decision layer

The [architecture decision layer](architecture-decision-layer-plan.md) is now part of the roadmap: requirements/workload and legacy profiles, applicability cards, option comparison, ADRs, target/transition architecture and four decision-navigation routes. Only the requirements/workload model (#17) is implemented as a bounded authoring method. Legacy/applicability and the evaluated architecture-selection workflow remain unimplemented.

## Required knowledge-service delivery

The [knowledge platform and MCP plan](knowledge-platform-and-mcp-plan.md) defines mandatory capabilities K01–K30: reproducible sources/provenance, automatic metadata and schemas, routing and validation, static code and curated graphs, ranked lexical retrieval, vector/hybrid evaluation, read-only MCP, generic onboarding, shared Rocinante integration, immutable snapshots, independent deployment, access controls, observability, quality/cost evaluation and maintenance. This is a plan, not a completed service. These capabilities are no longer deferred product scope.

## Not implemented

Technical chapters; approved table of contents; formal JSON Schema; chapter frontmatter/index/link/anchor validation; evidence-backed graph; retrieval benchmark; semantic search; MCP delivery.

## GitHub delivery tracking

Originally validated on 2026-10-18: [Program #1](https://github.com/rouslanbaranov/tycho/issues/1) owns 15 native epic sub-issues (#2–#16), which own all 78 work items (#17–#94). Eight GitHub milestones (M1–M8) cover the epic and work-item acceptance stages. The original 112 declared issue dependencies had native `blocked by` relationships without cycles. A book-first dependency revision is planned under #23 and must be validated again before this count is treated as current. [The delivery map](GITHUB-DELIVERY-MAP.md) provides navigable milestone → epic → issue references and the M1 entry point. The [reconciliation workflow](https://github.com/rouslanbaranov/tycho/actions/workflows/reconcile-delivery-hierarchy.yml) completed successfully.

The initial 94 issues were created as open planning items; #17 is now closed after the bounded model was delivered. The remaining backlog is not completed book research, code, retrieval, MCP or rollout. Due dates and assignees are intentionally unasserted.

## Completed bounded work / current book priority

- [#17](https://github.com/rouslanbaranov/tycho/issues/17) closed after [PR #95](https://github.com/rouslanbaranov/tycho/pull/95) was merged and configured CI passed. A requirements/workload model, template, original fictional illustration and bounded research contract now exist. K30 as a whole is **not** complete.
- Branch convention `feature/TYCHO-<issue-number>-<task-desc-slug>` and PR-time checks are implemented. Administrative branch protection remains unconfigured.
- Book structure [#23](https://github.com/rouslanbaranov/tycho/issues/23) was delivered as a **proposal** through [PR #96](https://github.com/rouslanbaranov/tycho/pull/96) and closed; the five adjusted GitHub issue dependencies passed verification. Issue #24 now adds the [minimal editorial contract](EDITORIAL-CONTRACT.md) and page templates in a feature branch. Neither the outline nor the templates constitutes a researched technical chapter.
- #18/#19 decision-support development should be refined from researched pilot content rather than treated as a precondition for beginning the book. Manual evidence checks remain mandatory during pilots while full validators are developed in parallel.

## Next action

Complete the remaining minimal authoring/pilot contracts (#24–#26), then prioritize writing the first three **evidence-backed** technical chapters (#38–#40). Run existing independent-source and structural checks; perform exact manual source/claim verification while comprehensive validators (#27–#37) are built in parallel. Only then ground broad applicability and legacy-modernization cards in real researched findings (#18/#19). No implicit full-book generation or unverified technical claims.

## Review limits

The private remote repository is established. Branch protection has not been configured. Discovery and mechanical checks do not establish technical truth or independent human review.
