# Research log

## 2026-10-18 — Bootstrap

Established the project charter, source-admissibility boundary, authoring rules, and initial roadmap. No technical research, source admission, or chapter completion is claimed. General methodology was independently expressed; no companion corpus or implementation was imported.

## 2026-10-18 — Public-source discovery

Created a canonical inventory of 169 public research entries, with separate access, admission, reading and version states. Built coverage and implementation maps spanning the requested architecture, data, execution, delivery, workload and observability areas. Public source entry pages/abstracts were inspected; paid book contents and full linked documentation trees were not read. Direct JEP retrieval limits and further evidence gaps remain explicit.

Added a deterministic catalogue renderer and structural/reference validator. Removed coding-assistant-specific instructions; research and authoring continue in the ChatGPT project. Next action: bounded pilot contracts and chapter plan, with source version/section pinning and deeper reading.

## 2026-10-18 — Architecture decision layer added to plan

Added a bounded work plan connecting requirements, workload, existing-system constraints, pattern applicability, alternatives, evidence, ADRs, experiments and migration. Separated target architecture from interim coexistence and transition states. Added four navigation routes and pilot acceptance criteria, including insufficient-evidence outcomes. Updated the roadmap, methodology pointer and next action. This records planned work; no decision models, templates, graph, evaluated selection engine or real-system modernization were implemented.

## 2026-10-18 — Complete knowledge-platform and MCP scope recorded

Expanded the roadmap from book-first optional delivery to a mandatory self-contained book plus external-agent knowledge service. Added a 30-capability status/acceptance matrix covering authoring, metadata/schema/index validation, reproducible public code evidence, two graph layers, ranked retrieval, semantic/hybrid evaluation, read-only MCP, onboarding, shared Rocinante integration, snapshots, independent deployment, access controls, observability and quality/cost evaluation. Removed the prior deferred-until-justified wording for MCP delivery. Tool/engine choices remain evidence-based; development is not delegated. No platform implementation or deployment was performed in this planning update.

The shared external specialist remains Rocinante. Tycho supplies provider-specific MCP/onboarding guidance and integration tests; no separate book-specific expert is planned. Multi-provider reasoning occurs outside the corpus, with source attribution and isolation, and creates no dependency on or ingestion of another knowledge collection.


## 2026-10-18 — TYCHO-17 requirements and workload profile (feature branch)

Started on `feature/TYCHO-17-requirements-and-workload-profile` from `main`; one issue per branch is now explicit in repository instructions, with PR branch-name validation. This planning convention does not by itself configure GitHub branch protection.

Authored `authoring/models/requirements-workload-profile.md`, `templates/requirements-workload-profile.md`, `examples/synthetic-workshop-registration.md`, and `authoring/contracts/TYCHO-17-research-contract.md`. The first defines required business outcomes, hard constraints versus preferences, quality-attribute scenarios, arrival/concurrency/mix/skew/growth dimensions, SLI/SLO measurement contracts and evidence gates. The second offers a reusable input contract. The third illustrates assumptions and arithmetic using a wholly fictional registration portal, not a benchmark or current-system observation.

Bounded source inspection: public arc42 Section 1 (§1.1/§1.2), Google SRE Workbook Chapter 2 (SLIs and their implementation), Grafana k6 open/closed arrival models, each read from official public pages on 2026-10-18. Full works were not read. The registered Little's Law paper remains discovery-only for this slice; no claim is attributed to unread paper contents. Source register remains discovery-level until section-level read states are supported by its validator.

Quality scope: independent-origin review of authored content, checks of example calculations and branch-name parsing, repository boundary checks, source inventory checks and PR workflow. These are mechanical validations and a bounded self-review, **not** a human-approved architecture, measured capacity, proven invariant or production-validated SLO.

Validation outcome: [PR #95](https://github.com/rouslanbaranov/tycho/pull/95) opened as draft; [branch convention CI](https://github.com/rouslanbaranov/tycho/actions/runs/39153497864) and [source boundary CI](https://github.com/rouslanbaranov/tycho/actions/runs/39153497829) both completed successfully. Local source-boundary scans also passed on the feature commits. No human approval or merge is claimed. Next: independent review and merge; issue remains open. Subsequent #18/#19 work is not implemented here.
