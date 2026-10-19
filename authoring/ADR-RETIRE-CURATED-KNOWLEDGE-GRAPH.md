# ADR — Retire Tycho's curated knowledge graph

> **Decision accepted as a project-scope direction, 2026-10-19.** The decision removes a proposed **internal curated concept/decision graph** from Tycho's mandatory architecture and roadmap. It does **not** assert experimental evidence that graphs are generally ineffective, nor does it delete prior research or modify independent projects.

## Context and decision

Tycho is a self-contained System Design book serving agent consumers through structured metadata, ranked section search, immutable snapshots and evidence/provenance. Prior planning added a manually curated graph linking patterns, concepts, requirements, architecture decisions, constraints and sources (capabilities K15/K16). Its independent benefit over the existing metadata, pattern cards, ADRs and typed `claim → source` evidence records has **not been demonstrated**.

**Decision: do not build, populate, validate, deploy, index, serve or maintain a curated graph for Tycho.** Do not require graph shards, typed traversal, graph-aware MCP tools, graph-derived change impact, or a graph-success gate in any release/milestone.

### Scope boundary

| Area | Project status after decision |
|---|---|
| Stable document IDs, page/chapter metadata and navigation | **Retained**, authoritative |
| Claim-to-source provenance, explicit evidence limits, contradictory/unavailable sources | **Retained**, authoritative |
| Architecture applicability cards, requirement profiles, ADRs and decision methods | **Retained**, canonical documents, not replicated graph nodes |
| Lexical SQLite FTS5 sections and bounded read | **Retained**, implement and evaluate independently |
| Vector/hybrid retrieval evaluation | **Retained**, evidence-based production choice |
| Route → Read → Verify, MCP retrieval/lookup/onboarding, Rocinante specialist integration | **Retained**, with no graph traversal prerequisite |
| Curated concept/decision relationship graph, sharded graph assembly, graph query API | **Excluded** |
| Static code relationships over approved, version-locked public examples | **Optional experimental research only**, not required for Tycho product or release |
| Educational chapters about graph databases, graph algorithms and graph retrieval | **Retained** as System Design content; unrelated to product graph tooling |

### Existing work is history, not a hidden requirement

- [#42](https://github.com/rouslanbaranov/tycho/issues/42) previously delivered an illustrative vocabulary contract. Keep its original artifacts as archived design history; do not treat their examples as production graph input.
- [#43](https://github.com/rouslanbaranov/tycho/issues/43) and [draft PR #181](https://github.com/rouslanbaranov/tycho/pull/181) retain a limited syntactic code-import pilot only as deferred research; no mandatory extractor or runtime code graph.
- [#44](https://github.com/rouslanbaranov/tycho/issues/44), [#45](https://github.com/rouslanbaranov/tycho/issues/45) and [#46](https://github.com/rouslanbaranov/tycho/issues/46) are closed as **not planned**, not claimed completed.
- E07's evidence lookup, E09's MCP evidence/decision lookup, E11's immutable snapshot manifest and E15's freshness pipeline depend on **canonical provenance, metadata and indexed sections**, not graph assembly.

## Rationale, trade-offs and safeguards

The potential benefit of curated edges is additional cross-topic navigation, but this duplicates canonical concept descriptions and claim references. It introduces ongoing edge ownership, contextual correctness checks, ambiguity across architecture alternatives, stale relationship maintenance and synchronization whenever chapters and evidence change. No measured agent task improvement or source precision supports that additional maintenance yet.

Costs avoided: new graph schemas/validators and assembly pipelines, review of every manual relationship, graph version/compatibility management, cross-shard dependency tracking, graph query endpoints and separate benchmark/operations burden.

Risks accepted: some multi-hop conceptual journeys may take more retrieval steps. Mitigate by improving stable metadata routing, cross-referenced canonical sections, direct claim/provenance resolution, bounded lexical search, negative/unknown outcomes and agent evaluation. Do not replace a graph with fabricated implicit dependency relations in search snippets or heuristics.

## Revisit criteria — only with independent justification

Reconsider **as a new, separately approved experiment**, not as silently revived roadmap acceptance, only if representative real agent tasks show:
1. A repeatable class of relevant architecture questions that metadata + search + evidence retrieval cannot answer to the required quality;
2. A reproducible, source-grounded graph prototype improves factual correctness, citation precision or end-to-end token/latency cost beyond baseline, including adversarial/contradictory cases;
3. Material graph-edge curation, drift, review, licensing and serving costs are measured and acceptable; and
4. The graph does not become a competing source of technical truth.

Until then, the mandatory knowledge product is the **book plus versioned metadata, provenance and retrieval**, without curated graph infrastructure.

**No actual agent-search benchmark has been performed to establish graph value or disvalue.** This is a scope prioritization decision. Book content, approved code evidence and other provider architecture remain independent.
