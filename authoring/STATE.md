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

The [architecture decision layer](architecture-decision-layer-plan.md) is now part of the roadmap: requirements/workload and legacy profiles, applicability cards, option comparison, ADRs, target/transition architecture and four decision-navigation routes. Only the plan is recorded; these models and their evaluation are not implemented.

## Required knowledge-service delivery

The [knowledge platform and MCP plan](knowledge-platform-and-mcp-plan.md) defines mandatory capabilities K01–K30: reproducible sources/provenance, automatic metadata and schemas, routing and validation, static code and curated graphs, ranked lexical retrieval, vector/hybrid evaluation, read-only MCP, generic onboarding, shared Rocinante integration, immutable snapshots, independent deployment, access controls, observability, quality/cost evaluation and maintenance. This is a plan, not a completed service. These capabilities are no longer deferred product scope.

## Not implemented

Technical chapters; approved table of contents; formal JSON Schema; chapter frontmatter/index/link/anchor validation; evidence-backed graph; retrieval benchmark; semantic search; MCP delivery.

## GitHub delivery tracking

Validated on 2026-10-18: [Program #1](https://github.com/rouslanbaranov/tycho/issues/1) owns 15 native epic sub-issues (#2–#16), which own all 78 work items (#17–#94). Eight GitHub milestones (M1–M8) cover the epic and work-item acceptance stages. All 112 declared issue dependencies have native \`blocked by\` relationships, without cycles or unknown targets. [The delivery map](GITHUB-DELIVERY-MAP.md) provides navigable milestone → epic → issue references and the M1 entry point. The [reconciliation workflow](https://github.com/rouslanbaranov/tycho/actions/workflows/reconcile-delivery-hierarchy.yml) completed successfully.

All 94 issues are open; this confirms a complete GitHub planning structure, **not** completed book research, code, retrieval, MCP or rollout. Due dates and assignees are intentionally unasserted.

## Next action

Start M1 with [#17 — Requirements and workload profile](https://github.com/rouslanbaranov/tycho/issues/17) (no prerequisites). Complete it before its dependents #18 and #19; follow the recorded native blocking links throughout M1. Define the models/templates in architecture-decision-layer-plan.md together with the knowledge, graph, retrieval and MCP contracts in knowledge-platform-and-mcp-plan.md. Then use sources/READING-PLAN.md and sources/COVERAGE.md to propose a question-driven book structure and three bounded pilot contracts that exercise architecture selection and modernization reasoning. Pin relevant versions and exact source sections, establish minimal chapter metadata contracts, then research the pilots. The inventory is not an instruction to read every linked corpus in full or generate the entire book.

## Review limits

The private remote repository is established. Branch protection has not been configured. Discovery and mechanical checks do not establish technical truth or independent human review.
