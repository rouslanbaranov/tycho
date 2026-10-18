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

A complete multi-volume book corpus; finalized table of contents; formal JSON Schema; chapter frontmatter/index/link/anchor validation; evidence-backed graph; retrieval benchmark; semantic search; MCP delivery.

## GitHub delivery tracking

Originally validated on 2026-10-18: [Program #1](https://github.com/rouslanbaranov/tycho/issues/1) owns 15 native epic sub-issues (#2–#16), which own all 78 work items (#17–#94). Eight GitHub milestones (M1–M8) cover the epic and work-item acceptance stages. The initial dependency tree was revised for book-first delivery on 2026-10-18. The scoped revision of native GitHub dependencies completed successfully in the book-first workflow linked from Issue #23. The original count of 112 is superseded and should not be assumed to be the current count. [The delivery map](GITHUB-DELIVERY-MAP.md) provides navigable milestone → epic → issue references and the M1 entry point. The historical [hierarchy reconciliation run](https://github.com/rouslanbaranov/tycho/actions/runs/39151315650) completed successfully. The old reconciliation workflow is retired to prevent unnecessary or unsafe reruns.

The original 94 issues formed the initial plan; #17, #23–#26 and #38–#41 were closed after bounded deliverables were merged. Issue #104 independently tracks milestone-only CI. The remaining backlog is not completed book research, code, retrieval, MCP or rollout. Due dates and assignees are intentionally unasserted.

## Completed bounded work / current book priority

- [#17](https://github.com/rouslanbaranov/tycho/issues/17) closed after [PR #95](https://github.com/rouslanbaranov/tycho/pull/95) was merged and configured CI passed. A requirements/workload model, template, original fictional illustration and bounded research contract now exist. K30 as a whole is **not** complete.
- Branch convention `feature/TYCHO-<issue-number>-<task-desc-slug>` remains mandatory. Per-PR CI is retired in favor of local pre-merge checks and one milestone-close verification. Administrative branch protection has not been established by this work.
- Book structure [#23](https://github.com/rouslanbaranov/tycho/issues/23) was delivered as a **proposal** through [PR #96](https://github.com/rouslanbaranov/tycho/pull/96) and closed; the five adjusted GitHub issue dependencies passed verification. Issues #24 and #25 were delivered and closed through PRs #97 and #98. Editorial templates and a bounded research workflow exist, while #26 formally scopes the first three source-reading pilots. Neither the outline nor the templates constitutes a researched technical chapter.
- #18/#19 decision-support development should be refined from researched pilot content rather than treated as a precondition for beginning the book. Manual evidence checks remain mandatory during pilots while full validators are developed in parallel.

## Milestone-only CI policy (Issue #104)

Only the [milestone verification workflow](../.github/workflows/boundary.yml) remains active. GitHub Actions now runs only when a **milestone is closed with zero open issues**. Normal commits and PRs incur no GitHub-hosted CI run; pre-merge checks run locally via [premerge_check.py](../scripts/premerge_check.py). See [the policy](MILESTONE-CI.md). This is a configuration change, **not** a claim that a milestone-wide verification has already passed.

## Next action

Editorial templates #24 and research workflow #25 have been merged and closed. Issue #26 is closed after PR #99 merged the [three bounded pilot contracts](PILOT-WAVE-01.md). First technical pilot #38 is merged and closed via PR #100; the [queueing chapter](../book/performance/queueing-littles-law.md) is now in main. Pilots #38 and #39 are merged and closed through PRs #100/#101; researched [queueing](../book/performance/queueing-littles-law.md) and [outbox/idempotency](../book/distributed/transactional-outbox-and-idempotency.md) chapters are in main. Pilot #40 was merged through PR #102 and closed; [rollout and recovery](../book/delivery/safe-rollout-and-recovery.md) joins [queueing](../book/performance/queueing-littles-law.md) and [outbox](../book/distributed/transactional-outbox-and-idempotency.md) as the first three source-grounded technical pages. Issue #41 now evaluates these pilots against a [25-question set](../evaluation/pilot-questions.json) and [bounded methodology assessment](../evaluation/PILOT-ASSESSMENT.md). This does not imply whole-volume or whole-book completion. Run existing independent-source and structural checks; perform exact manual source/claim verification while comprehensive validators (#27–#37) are built in parallel. Only then ground broad applicability and legacy-modernization cards in real researched findings (#18/#19). No implicit full-book generation or unverified technical claims.

## Immediate expansion path

Run the pilot methodology check in Issue #41 (author-only review and tiny in-sample retrieval smoke, not LLM answer acceptance). Then begin [#79 foundational architecture research](https://github.com/rouslanbaranov/tycho/issues/79) in its own feature branch. Full source pinning, structured metadata/validation, lexical/hybrid search and MCP are still required. The corpus is not complete.

## Foundations corpus expansion — Issue #79

Three original source-grounded pages now describe [quality-driven architecture views](../book/application/quality-drivers-and-architecture-views.md), [module and service styles](../book/application/architecture-styles-and-module-boundaries.md), and [architecture evolution](../book/application/architecture-evolution-and-extraction.md). A [navigation landing](../book/application/README.md) links them. These are bounded research chapters with original Mermaid diagrams and explicit limitations, not a complete System Design corpus, measured case study or independently reviewed architecture. Issue-level GitHub Actions checks are no longer triggered; verification is batched at milestone closure per [the current CI policy](MILESTONE-CI.md).

## Distributed-system corpus — Issue #80

Added three original source-grounded chapters on [causality and consensus](../book/distributed/causality-ordering-and-consensus.md), [transaction isolation and sagas](../book/distributed/transaction-isolation-and-sagas.md), and [CQRS/event sourcing](../book/distributed/cqrs-event-sourcing-and-projections.md). They extend the existing [outbox/idempotency chapter](../book/distributed/transactional-outbox-and-idempotency.md) without duplicating its canonical mechanisms. The [landing page](../book/distributed/README.md) routes questions among the four sources. All examples are synthetic; no production tests or independent domain review claimed. Full GitHub CI still runs **only at milestone acceptance**.

**Next corpus issue:** [#81 — Integration, messaging, Kafka and stream processing](https://github.com/rouslanbaranov/tycho/issues/81). The present pages do not constitute the entirety of the distributed-systems volume.

## Integration and stream-processing corpus — Issue #81

Three new independently grounded [integration pages](../book/integration/README.md) now cover [Kafka 4.1 partition/replication/transaction contracts](../book/integration/kafka-partitions-replication-and-contracts.md), [RabbitMQ/NATS/Pulsar messaging families and durable workflow boundaries](../book/integration/messaging-families-and-durable-workflows.md), and [stateful Kafka Streams, Flink checkpointing and CDC](../book/integration/stateful-stream-processing-and-cdc.md). Each page has original Mermaid diagrams, failure/repair paths and a bounded public-source ledger; all numerical examples are synthetic. Version scope (including archived Flink 2.1 docs) is explicit. No running broker, benchmark or independent human review has been performed.

Milestone-only CI remains the sole GitHub Actions trigger; issue PRs do **not** run automated GitHub pipelines. The next content issue is [#82](https://github.com/rouslanbaranov/tycho/issues/82). Full book coverage and shared Rocinante/MCP remain incomplete.

## Review limits

The private remote repository is established. Branch protection has not been configured. Discovery and mechanical checks do not establish technical truth or independent human review.
