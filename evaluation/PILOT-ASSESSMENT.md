# Tycho pilot wave — methodology acceptance and evidence limits

Issue: [#41](https://github.com/rouslanbaranov/tycho/issues/41). Evaluation date: 2026-10-18. **This is an author-conducted structural and qualitative review, not independent expert acceptance or an AI-agent answer-quality benchmark.**

## Evaluation material and protocol

Three actual technical pilot pages form the current corpus:

| Owner | Page | Inspected primary-source anchors |
|---|---|---|
| Mechanism / #38 | [Queueing, Little's Law](../book/volumes/v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) | Kim & Whitt (2013) §§1–2.2; Grafana k6 open/closed scheduling; public SRE Handling Overload |
| End-to-end / #39 | [Outbox and idempotency](../book/distributed/transactional-outbox-and-idempotency.md) | Debezium 3.6 Outbox Event Router; PostgreSQL 17; RFC 9110 §9.2.2; AWS idempotent-API research essay |
| Recovery / #40 | [Safe rollout and recovery](../book/delivery/safe-rollout-and-recovery.md) | Kubernetes Deployments docs, Argo Rollouts Canary/BlueGreen, AWS DR reference, Google SRE Cascading Failures |

The [25-question evaluation set](pilot-questions.json) consists of **five factual, four synthesis, four trade-off, four failure, three change-impact, two contradiction and three unanswerable** questions. Each question names its canonical page, an expected-answer element, a primary evidence target, and a forbidden unsupported assertion. This is an **author-created question set**, not independent ground truth.

Evaluation distinguishes:

1. **Navigation:** does a cheap lexical route find the correct owner among these three pages?
2. **Evidence discipline:** do manuscript claims carry exact source/version/section and avoid fabricated experiments?
3. **Explanation sufficiency:** can the reader understand causal mechanism, boundary assumptions, normal and failure flows, alternatives and a missing-evidence verdict?
4. **Human/agent answer quality:** would an independent solver answer all 25 correctly with calibrated uncertainty and citations? **Not executed; no quality score claimed.**
5. **Maintenance/readiness:** could the content be versioned/indexed and revisited? Only rudimentary Markdown/links and manual evidence ledgers exist.

## Actual checks and observations

- **Structural:** three technical Markdown pages, their landing pages and source-to-claim tables exist in versioned GitHub history; original Mermaid diagrams are included with text alternatives. PR tests and public-source boundary checks for #38, #39 and #40 passed. This proves *configured checks*, not technical completeness.
- **Routing smoke:** executed a tiny deterministic token-overlap baseline on the three pages using the 25 prompts. **25/25 top-1 matching canonical owners** in the author-created, in-sample set. The reproducible script is [pilot_lexical_smoke.py](../scripts/pilot_lexical_smoke.py). There are only three documents, strongly topic-distinct questions and no negative out-of-corpus distractor pages; this **must not** be extrapolated to full-corpus search recall, ranking, cross-system analysis, total LLM tool cost or response quality.
- **Source-to-claim scope:** evidence anchors identify bounded public sections, but neither a universal pinned dependency manifest nor machine-enforced paragraph provenance exists. This is a material **review** and **freshness** gap.
- **Unanswerable-case checks:** the manuscript explicitly refuses exact instance/pool sizing from users/RPS/p99, external exactly-once payment guarantees from outbox alone, and RPO=0 from deployment success alone. These are valuable calibrated outcomes, but no independent AI inference test was conducted.
- **Contradiction coverage:** finite-window Little's Law and deployment-ready versus user-health conflicts are addressed; there is no systematic independently reviewed conflicting-source dataset or evaluation.
- **Mechanism/diagram clarity:** page narratives separately describe assumptions and diagrams. Native Mermaid source is editable. Actual renderer compatibility was not exhaustively tested across clients.

## Adopt / revise / reject

| Finding | Decision | Rationale and bounded next action |
|---|---|---|
| Question-first, three bounded pilots before whole-book backfill | **ADOPT** | All three produce material evidence-backed narrative, failure and explicit unknowns without forcing the full service stack first; reuse for E14 topic coverage |
| Mermaid-first with text alternatives where diagrams clarify flows | **ADOPT** | Versionable visuals illustrate causal boundaries; validate renderability and text equivalents in future page-validation tooling |
| Explicit local atomicity / external effect / data recovery separation | **ADOPT** | Three pilots contain falsifiable limitations; require same discipline when adding Kafka, databases, CI/CD and scaling |
| Unstructured manual section-level provenance | **REVISE** | Source-level register is discovery-oriented; implement validated stable section/claim anchors, revision locks, freshness and checkers in K02–K12 work |
| Page IDs, canonical ownership and cross-volume links | **REVISE** | Current volume/chapter labels are planning locators, not machine IDs; implement agreed frontmatter, references, link resolution and strict schema before high-volume publication |
| Evidence review as mechanical/author review only | **REVISE** | Require independent domain/human review where material correctness or security is high-stakes; do not relabel CI as review |
| In-sample 25/25 lexical smoke as proof of retrieval quality | **REJECT** | Trivial three-page classification does not validate relevance, unknown detection, graph retrieval, agent answer quality or scale; build blind questions and real retrieval evaluation after corpus expansion |
| "Green CI / deployment / test implies user SLA or zero loss" | **REJECT** | The pilot failure scenarios explicitly refute such inference; demand real health/invariant, DR and workload tests |
| Apply one universal architecture based on user-count/RPS thresholds | **REJECT** | Workload-specific evidence, resource constraints, contention and cost must be measured or explicitly unknown |

**Overall pilot-method verdict:** **ADOPT the bounded authoring and diagram/evidence discipline, REVISE machine contracts and independent review before broad release, REJECT unsupported claims of evaluated full-system decision support.** This is an **author self-assessment**, not a release acceptance or independent reviewer approval.

## Expansion readiness and release gate

The method is sufficient to **start the next small, evidence-backed chapter** in a feature branch. It is *not* sufficient to label Tycho complete or deploy a search/MCP service. Further chapter work should run alongside mandatory metadata/schema/provenance infrastructure, and each chapter should record its own exact public source reading.

Next corpus epic: [E14 — System Design technical coverage](https://github.com/rouslanbaranov/tycho/issues/15), beginning with [#79 — foundations, quality attributes and application architectures](https://github.com/rouslanbaranov/tycho/issues/79). Avoid automatic mass generation before bounded evidence inspection. A small publicly sourced, concrete addition with truthful scope is better than a large unreviewed outline.
