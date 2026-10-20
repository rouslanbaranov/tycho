# Tycho — GitHub delivery map

> **GitHub issue-map freshness:** the 2026-10-18 initial 15-epic/78-work-item/112-dependency and pilot ordering claims below are a historical discovery snapshot, **not today's authoritative count or open/closed matrix**. GitHub issues/milestones are authoritative. M9/E16 was added; #216 merged, #217 replaced, #218 open, E14/#213 and #214 open, M9 #121 closed. **Live state (2026-10-20, before merging PR #218):** M1–M9 integrated draft merged via PR #216; PR #217 closed/unmerged and replaced by open/non-draft **unmerged PR #218**. M9 #121 closed under scoped owner acceptance; #213/E14 and final edition #214 remain open. **69/69 primary chapter manuscripts deepened, 0/69 independently accepted for final-book completeness.** The 10-volume edition, hosted MCP and deployment do not exist. Reported 13/13 groups and 215/215 tests passed on prior manuscript SHA `d8d04e0e3c97e9f364607f640faa9f5aee4866f3`, **not** on the subsequently edited status documents. Visual rendering and live MCP were owner-cancelled, not PASSED. See [canonical current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).


> Generated planning snapshot, 2026-10-18. GitHub Issues, native hierarchy and milestones are the tracking system of record; this document is navigation, not a second backlog. Regenerate when scopes change.

**Verified GitHub structure (2026-10-18):** 15 epic links under Program #1, 78 native work-item links under the appropriate epics, and 112 native blocked-by relationships. [Reconciliation and verification succeeded](https://github.com/rouslanbaranov/tycho/actions/runs/39151315650). Issue #17 was completed and closed via PR #95; other work items remain planned. Book-first priority corrections for #18, #19, #23, #26 and #38 will be reconciled by the dedicated workflow after the #23 PR merges.

## Program

- [#1 — Tycho book and MCP knowledge platform](https://github.com/rouslanbaranov/tycho/issues/1)
- 15 epics, 78 implementation/research issues, 8 milestones. These are planned tasks; issue creation does not imply implementation or verification.

## Milestones, epics and work items

### [M1 — Product, decision models and book design](https://github.com/rouslanbaranov/tycho/milestone/1)

**[E01 — Architecture decision models and modernization](https://github.com/rouslanbaranov/tycho/issues/2)** (#2)

- [#17 — Requirements and workload profile](https://github.com/rouslanbaranov/tycho/issues/17)
- [#18 — Legacy baseline and modernization profile](https://github.com/rouslanbaranov/tycho/issues/18) — depends on [#39](https://github.com/rouslanbaranov/tycho/issues/39)
- [#19 — Pattern applicability and contraindication cards](https://github.com/rouslanbaranov/tycho/issues/19) — depends on [#38](https://github.com/rouslanbaranov/tycho/issues/38)
- [#20 — Candidate comparison and evidence-backed ADR template](https://github.com/rouslanbaranov/tycho/issues/20) — depends on [#18](https://github.com/rouslanbaranov/tycho/issues/18), [#19](https://github.com/rouslanbaranov/tycho/issues/19)
- [#21 — Target and transition architecture templates](https://github.com/rouslanbaranov/tycho/issues/21) — depends on [#20](https://github.com/rouslanbaranov/tycho/issues/20)
- [#22 — Decision navigation and insufficient-evidence behavior](https://github.com/rouslanbaranov/tycho/issues/22) — depends on [#21](https://github.com/rouslanbaranov/tycho/issues/21)

**[E02 — Book structure and authoring contracts](https://github.com/rouslanbaranov/tycho/issues/3)** (#3)

- [#23 — Define audience and question-driven book hierarchy](https://github.com/rouslanbaranov/tycho/issues/23) — depends on [#17](https://github.com/rouslanbaranov/tycho/issues/17)
- [#24 — Define editorial, navigation and page templates](https://github.com/rouslanbaranov/tycho/issues/24) — depends on [#23](https://github.com/rouslanbaranov/tycho/issues/23)
- [#25 — Define bounded research, deepening and readiness workflow](https://github.com/rouslanbaranov/tycho/issues/25) — depends on [#24](https://github.com/rouslanbaranov/tycho/issues/24)
- [#26 — Specify three pilot research contracts](https://github.com/rouslanbaranov/tycho/issues/26) — depends on [#25](https://github.com/rouslanbaranov/tycho/issues/25)

### [M2 — Reproducible knowledge foundation](https://github.com/rouslanbaranov/tycho/milestone/2)

**[E03 — Public evidence and reproducible sources](https://github.com/rouslanbaranov/tycho/issues/4)** (#4)

- [#27 — Resolve public-source access and licensing gaps](https://github.com/rouslanbaranov/tycho/issues/27) — depends on [#26](https://github.com/rouslanbaranov/tycho/issues/26)
- [#28 — Implement public repository lock and read-only clone tooling](https://github.com/rouslanbaranov/tycho/issues/28) — depends on [#27](https://github.com/rouslanbaranov/tycho/issues/27)
- [#29 — Implement precise claim and source reference model](https://github.com/rouslanbaranov/tycho/issues/29) — depends on [#27](https://github.com/rouslanbaranov/tycho/issues/27)
- [#30 — Implement admitted document acquisition and change detection](https://github.com/rouslanbaranov/tycho/issues/30) — depends on [#28](https://github.com/rouslanbaranov/tycho/issues/28), [#29](https://github.com/rouslanbaranov/tycho/issues/29)
- [#31 — Integrate research register, reading scope and checkpoint updates](https://github.com/rouslanbaranov/tycho/issues/31) — depends on [#29](https://github.com/rouslanbaranov/tycho/issues/29)

**[E04 — Metadata, routing index and validation](https://github.com/rouslanbaranov/tycho/issues/5)** (#5)

- [#32 — Specify document metadata and identity semantics](https://github.com/rouslanbaranov/tycho/issues/32) — depends on [#24](https://github.com/rouslanbaranov/tycho/issues/24), [#29](https://github.com/rouslanbaranov/tycho/issues/29)
- [#33 — Implement strict metadata and source JSON Schemas](https://github.com/rouslanbaranov/tycho/issues/33) — depends on [#32](https://github.com/rouslanbaranov/tycho/issues/32)
- [#34 — Implement automatic frontmatter generation and normalization](https://github.com/rouslanbaranov/tycho/issues/34) — depends on [#33](https://github.com/rouslanbaranov/tycho/issues/33)
- [#35 — Implement deterministic routing index and route command](https://github.com/rouslanbaranov/tycho/issues/35) — depends on [#34](https://github.com/rouslanbaranov/tycho/issues/34)
- [#36 — Implement local links, anchors, navigation and page validation](https://github.com/rouslanbaranov/tycho/issues/36) — depends on [#35](https://github.com/rouslanbaranov/tycho/issues/35)
- [#37 — Unify knowledge validation in CLI and CI](https://github.com/rouslanbaranov/tycho/issues/37) — depends on [#36](https://github.com/rouslanbaranov/tycho/issues/36)

### [M3 — Evidence-backed pilot corpus](https://github.com/rouslanbaranov/tycho/milestone/3)

**[E05 — Pilot corpus and evidence-grounded quality baseline](https://github.com/rouslanbaranov/tycho/issues/6)** (#6)

- [#38 — Research and author the mechanism pilot](https://github.com/rouslanbaranov/tycho/issues/38) — depends on [#26](https://github.com/rouslanbaranov/tycho/issues/26)
- [#39 — Research and author the end-to-end pilot](https://github.com/rouslanbaranov/tycho/issues/39) — depends on [#38](https://github.com/rouslanbaranov/tycho/issues/38)
- [#40 — Research and author the recovery and transition pilot](https://github.com/rouslanbaranov/tycho/issues/40) — depends on [#39](https://github.com/rouslanbaranov/tycho/issues/39)
- [#41 — Curate 20–30 questions and accept the pilot methodology](https://github.com/rouslanbaranov/tycho/issues/41) — depends on [#40](https://github.com/rouslanbaranov/tycho/issues/40)

### [M4 — Graphs and ranked retrieval baseline](https://github.com/rouslanbaranov/tycho/milestone/4)

**[E06 — Static code and curated knowledge graphs](https://github.com/rouslanbaranov/tycho/issues/7)** (#7)

- [#42 — Define graph vocabulary, provenance and shard ownership](https://github.com/rouslanbaranov/tycho/issues/42) — depends on [#32](https://github.com/rouslanbaranov/tycho/issues/32), [#22](https://github.com/rouslanbaranov/tycho/issues/22)
- [#43 — Implement version-pinned static code graph extraction](https://github.com/rouslanbaranov/tycho/issues/43) — depends on [#28](https://github.com/rouslanbaranov/tycho/issues/28), [#42](https://github.com/rouslanbaranov/tycho/issues/42)
- [#44 — Populate curated graph for the pilot corpus](https://github.com/rouslanbaranov/tycho/issues/44) — depends on [#41](https://github.com/rouslanbaranov/tycho/issues/41), [#42](https://github.com/rouslanbaranov/tycho/issues/42)
- [#45 — Implement graph schema, integrity validation and assembly](https://github.com/rouslanbaranov/tycho/issues/45) — depends on [#43](https://github.com/rouslanbaranov/tycho/issues/43), [#44](https://github.com/rouslanbaranov/tycho/issues/44)
- [#46 — Implement bounded direction-aware graph queries](https://github.com/rouslanbaranov/tycho/issues/46) — depends on [#45](https://github.com/rouslanbaranov/tycho/issues/45)

**[E07 — Ranked lexical retrieval and reusable knowledge core](https://github.com/rouslanbaranov/tycho/issues/8)** (#8)

- [#47 — Specify retrieval requests, responses and section boundaries](https://github.com/rouslanbaranov/tycho/issues/47) — depends on [#35](https://github.com/rouslanbaranov/tycho/issues/35), [#22](https://github.com/rouslanbaranov/tycho/issues/22)
- [#48 — Benchmark and select the lexical engine](https://github.com/rouslanbaranov/tycho/issues/48) — depends on [#41](https://github.com/rouslanbaranov/tycho/issues/41), [#47](https://github.com/rouslanbaranov/tycho/issues/47)
- [#49 — Implement deterministic section indexing and updates](https://github.com/rouslanbaranov/tycho/issues/49) — depends on [#48](https://github.com/rouslanbaranov/tycho/issues/48)
- [#50 — Implement ranked search and progressive reads](https://github.com/rouslanbaranov/tycho/issues/50) — depends on [#49](https://github.com/rouslanbaranov/tycho/issues/49)
- [#51 — Integrate safe evidence and graph resolution in retrieval core](https://github.com/rouslanbaranov/tycho/issues/51) — depends on [#50](https://github.com/rouslanbaranov/tycho/issues/50), [#46](https://github.com/rouslanbaranov/tycho/issues/46), [#29](https://github.com/rouslanbaranov/tycho/issues/29)

### [M5 — Hybrid evaluation and MCP delivery](https://github.com/rouslanbaranov/tycho/milestone/5)

**[E08 — Semantic and hybrid retrieval evaluation](https://github.com/rouslanbaranov/tycho/issues/9)** (#9)

- [#52 — Define chunk, embedding and vector-index version contracts](https://github.com/rouslanbaranov/tycho/issues/52) — depends on [#49](https://github.com/rouslanbaranov/tycho/issues/49)
- [#53 — Build a bounded semantic retrieval prototype](https://github.com/rouslanbaranov/tycho/issues/53) — depends on [#52](https://github.com/rouslanbaranov/tycho/issues/52)
- [#54 — Evaluate hybrid fusion and reranking](https://github.com/rouslanbaranov/tycho/issues/54) — depends on [#53](https://github.com/rouslanbaranov/tycho/issues/53), [#51](https://github.com/rouslanbaranov/tycho/issues/51)
- [#55 — Record vector/hybrid production decision and integration path](https://github.com/rouslanbaranov/tycho/issues/55) — depends on [#54](https://github.com/rouslanbaranov/tycho/issues/54)

**[E09 — Read-only MCP and generic onboarding](https://github.com/rouslanbaranov/tycho/issues/10)** (#10)

- [#56 — Verify MCP versions, clients and transport design](https://github.com/rouslanbaranov/tycho/issues/56) — depends on [#47](https://github.com/rouslanbaranov/tycho/issues/47)
- [#57 — Implement MCP capabilities, search and read adapter](https://github.com/rouslanbaranov/tycho/issues/57) — depends on [#56](https://github.com/rouslanbaranov/tycho/issues/56), [#51](https://github.com/rouslanbaranov/tycho/issues/51)
- [#58 — Expose graph, evidence and decision-method lookup via MCP](https://github.com/rouslanbaranov/tycho/issues/58) — depends on [#57](https://github.com/rouslanbaranov/tycho/issues/57), [#46](https://github.com/rouslanbaranov/tycho/issues/46)
- [#59 — Implement canonical onboarding and discoverable entry](https://github.com/rouslanbaranov/tycho/issues/59) — depends on [#57](https://github.com/rouslanbaranov/tycho/issues/57)
- [#60 — Test generic-client interoperability and manual fallback](https://github.com/rouslanbaranov/tycho/issues/60) — depends on [#58](https://github.com/rouslanbaranov/tycho/issues/58), [#59](https://github.com/rouslanbaranov/tycho/issues/59)

### [M6 — Shared Rocinante integration](https://github.com/rouslanbaranov/tycho/milestone/6)

**[E10 — Shared Rocinante specialist integration](https://github.com/rouslanbaranov/tycho/issues/11)** (#11)

- [#61 — Define Tycho provider contract for the shared Rocinante agent](https://github.com/rouslanbaranov/tycho/issues/61) — depends on [#60](https://github.com/rouslanbaranov/tycho/issues/60)
- [#62 — Generate compact versioned provider guidance](https://github.com/rouslanbaranov/tycho/issues/62) — depends on [#61](https://github.com/rouslanbaranov/tycho/issues/61)
- [#63 — Test routing, attribution and provider isolation](https://github.com/rouslanbaranov/tycho/issues/63) — depends on [#62](https://github.com/rouslanbaranov/tycho/issues/62)
- [#64 — Evaluate shared-specialist answer quality and global token cost](https://github.com/rouslanbaranov/tycho/issues/64) — depends on [#63](https://github.com/rouslanbaranov/tycho/issues/63), [#55](https://github.com/rouslanbaranov/tycho/issues/55)

### [M7 — Operational release and end-to-end acceptance](https://github.com/rouslanbaranov/tycho/milestone/7)

**[E11 — Immutable snapshots and reproducible deployment](https://github.com/rouslanbaranov/tycho/issues/12)** (#12)

- [#65 — Specify snapshot manifest and compatibility rules](https://github.com/rouslanbaranov/tycho/issues/65) — depends on [#51](https://github.com/rouslanbaranov/tycho/issues/51), [#45](https://github.com/rouslanbaranov/tycho/issues/45)
- [#66 — Implement deterministic snapshot packaging and verification](https://github.com/rouslanbaranov/tycho/issues/66) — depends on [#65](https://github.com/rouslanbaranov/tycho/issues/65), [#55](https://github.com/rouslanbaranov/tycho/issues/55)
- [#67 — Build service container and independent deployment automation](https://github.com/rouslanbaranov/tycho/issues/67) — depends on [#66](https://github.com/rouslanbaranov/tycho/issues/66), [#60](https://github.com/rouslanbaranov/tycho/issues/60)
- [#68 — Implement atomic activation, health and rollback runbook](https://github.com/rouslanbaranov/tycho/issues/68) — depends on [#67](https://github.com/rouslanbaranov/tycho/issues/67)
- [#69 — Exercise deployment smoke tests and release packaging](https://github.com/rouslanbaranov/tycho/issues/69) — depends on [#68](https://github.com/rouslanbaranov/tycho/issues/68), [#64](https://github.com/rouslanbaranov/tycho/issues/64)

**[E12 — Service access, safety, observability and capacity](https://github.com/rouslanbaranov/tycho/issues/13)** (#13)

- [#70 — Define audience, authentication and authorization policy](https://github.com/rouslanbaranov/tycho/issues/70) — depends on [#56](https://github.com/rouslanbaranov/tycho/issues/56)
- [#71 — Implement read-only resolution and hostile-input protections](https://github.com/rouslanbaranov/tycho/issues/71) — depends on [#70](https://github.com/rouslanbaranov/tycho/issues/70), [#58](https://github.com/rouslanbaranov/tycho/issues/58)
- [#72 — Implement query/output limits and overload behavior](https://github.com/rouslanbaranov/tycho/issues/72) — depends on [#71](https://github.com/rouslanbaranov/tycho/issues/71)
- [#73 — Implement metrics, safe audit events and alerting](https://github.com/rouslanbaranov/tycho/issues/73) — depends on [#72](https://github.com/rouslanbaranov/tycho/issues/72), [#67](https://github.com/rouslanbaranov/tycho/issues/67)
- [#74 — Measure multi-client capacity and document deployment sizing](https://github.com/rouslanbaranov/tycho/issues/74) — depends on [#73](https://github.com/rouslanbaranov/tycho/issues/73), [#68](https://github.com/rouslanbaranov/tycho/issues/68)

**[E13 — End-to-end release quality and cost acceptance](https://github.com/rouslanbaranov/tycho/issues/14)** (#14)

- [#75 — Expand the benchmark toward 50–100 service and agent tasks](https://github.com/rouslanbaranov/tycho/issues/75) — depends on [#41](https://github.com/rouslanbaranov/tycho/issues/41), [#64](https://github.com/rouslanbaranov/tycho/issues/64)
- [#76 — Run end-to-end quality, citation and total-cost comparisons](https://github.com/rouslanbaranov/tycho/issues/76) — depends on [#75](https://github.com/rouslanbaranov/tycho/issues/75), [#74](https://github.com/rouslanbaranov/tycho/issues/74)
- [#77 — Verify release safety, compatibility and recovery gates](https://github.com/rouslanbaranov/tycho/issues/77) — depends on [#76](https://github.com/rouslanbaranov/tycho/issues/76), [#69](https://github.com/rouslanbaranov/tycho/issues/69)
- [#78 — Complete release review and publish operational acceptance record](https://github.com/rouslanbaranov/tycho/issues/78) — depends on [#77](https://github.com/rouslanbaranov/tycho/issues/77)

### [M8 — Book coverage and maintenance baseline](https://github.com/rouslanbaranov/tycho/milestone/8)

**[E14 — System Design book coverage waves](https://github.com/rouslanbaranov/tycho/issues/15)** (#15)

- [#79 — Author foundations, quality attributes and application architecture styles](https://github.com/rouslanbaranov/tycho/issues/79) — depends on [#41](https://github.com/rouslanbaranov/tycho/issues/41)
- [#80 — Author distributed systems, transactions and idempotency](https://github.com/rouslanbaranov/tycho/issues/80) — depends on [#79](https://github.com/rouslanbaranov/tycho/issues/79)
- [#81 — Author integration, messaging, Kafka and stream processing](https://github.com/rouslanbaranov/tycho/issues/81) — depends on [#80](https://github.com/rouslanbaranov/tycho/issues/80)
- [#82 — Author Java concurrency, reactive execution and virtual threads](https://github.com/rouslanbaranov/tycho/issues/82) — depends on [#79](https://github.com/rouslanbaranov/tycho/issues/79)
- [#83 — Author PostgreSQL, database engines and data-model alternatives](https://github.com/rouslanbaranov/tycho/issues/83) — depends on [#80](https://github.com/rouslanbaranov/tycho/issues/80)
- [#84 — Author sharding, pooling and distributed/local caching](https://github.com/rouslanbaranov/tycho/issues/84) — depends on [#82](https://github.com/rouslanbaranov/tycho/issues/82), [#83](https://github.com/rouslanbaranov/tycho/issues/83)
- [#85 — Author lexical, vector, ANN, hybrid and graph retrieval](https://github.com/rouslanbaranov/tycho/issues/85) — depends on [#83](https://github.com/rouslanbaranov/tycho/issues/83)
- [#86 — Author workload-driven architecture and high-load resilience](https://github.com/rouslanbaranov/tycho/issues/86) — depends on [#81](https://github.com/rouslanbaranov/tycho/issues/81), [#84](https://github.com/rouslanbaranov/tycho/issues/84)
- [#87 — Author deployment topology, multi-region and disaster recovery](https://github.com/rouslanbaranov/tycho/issues/87) — depends on [#86](https://github.com/rouslanbaranov/tycho/issues/86)
- [#88 — Author CI/CD, GitOps, rollout and database evolution](https://github.com/rouslanbaranov/tycho/issues/88) — depends on [#87](https://github.com/rouslanbaranov/tycho/issues/87)
- [#89 — Author metrics, logs, tracing, lineage and audit architecture](https://github.com/rouslanbaranov/tycho/issues/89) — depends on [#86](https://github.com/rouslanbaranov/tycho/issues/86)
- [#90 — Author security, synthesis and architecture decision examples](https://github.com/rouslanbaranov/tycho/issues/90) — depends on [#85](https://github.com/rouslanbaranov/tycho/issues/85), [#88](https://github.com/rouslanbaranov/tycho/issues/88), [#89](https://github.com/rouslanbaranov/tycho/issues/89)

**[E15 — Freshness, maintenance and regression operating baseline](https://github.com/rouslanbaranov/tycho/issues/16)** (#16)

- [#91 — Implement source-to-claim/page/graph/index change impact](https://github.com/rouslanbaranov/tycho/issues/91) — depends on [#30](https://github.com/rouslanbaranov/tycho/issues/30), [#45](https://github.com/rouslanbaranov/tycho/issues/45), [#49](https://github.com/rouslanbaranov/tycho/issues/49)
- [#92 — Implement stale-state review and re-verification closure](https://github.com/rouslanbaranov/tycho/issues/92) — depends on [#91](https://github.com/rouslanbaranov/tycho/issues/91)
- [#93 — Automate incremental checks and retrieval regression runs](https://github.com/rouslanbaranov/tycho/issues/93) — depends on [#92](https://github.com/rouslanbaranov/tycho/issues/92), [#77](https://github.com/rouslanbaranov/tycho/issues/77)
- [#94 — Document maintenance ownership, upgrade and release playbooks](https://github.com/rouslanbaranov/tycho/issues/94) — depends on [#93](https://github.com/rouslanbaranov/tycho/issues/93)

## Execution entry point — M1

Requirements baseline [#17](https://github.com/rouslanbaranov/tycho/issues/17) was delivered. Prioritize [#23 — Book structure](https://github.com/rouslanbaranov/tycho/issues/23), then #24 → #25 → #26 → evidence-backed pilot chapters #38–#40. Source and content validation are required, but full tooling (#27–#37) is not a blanket blocker for the first authored material. Refine broad #18/#19 decision-layer deliverables against researched content. Do not bulk-generate unresearched chapters.

## Tracking rules

- Native GitHub parent/sub-issue links represent ownership; native blocked-by relationships mirror the explicit Dependencies section in executable issues.
- All nine milestones describe acceptance outcomes, not fabricated due dates.
- Keep all issues open until deliverables have actually passed their individual acceptance criteria; update source/version evidence and the current state after completion.
- This map is safe to regenerate from GitHub and must never drive an unsolicited change to the corpus.


## M9 — Real-World Architecture Modernization: Case Studies and Decision Transfer

[Native milestone](https://github.com/rouslanbaranov/tycho/milestone/9) → [Epic E16 #113](https://github.com/rouslanbaranov/tycho/issues/113).

| Issue | Work | Dependency |
|---|---|---|
| #114 | Source verification/admission | Existing public-source policy |
| #115 | Netflix Java, Spring and reactive evolution | #114 |
| #116 | JVM concurrency and performance failures | #114 |
| #117 | Cloud, storage and resilience transitions | #114 |
| #118 | Cross-industry counterexamples | #114 |
| #119 | Comparative decision and migration playbooks | #115–#118 |
| #120 | Case provenance and portable search/graph fixtures | #114; stable owning contracts for actual adapters |
| #121 | Independent review and milestone acceptance | #115–#120 |
| #122 | Native milestone and hierarchy setup | Epic #113 |

See [program acceptance and start-readiness](REAL_WORLD_CASE_STUDY_PROGRAM.md). Closed duplicates #123–#130 are excluded; no due date is asserted.
