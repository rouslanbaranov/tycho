# M9 case, claim, provenance and decision-retrieval contract

**Status:** **portable proposed v1 contract** for issue [E16-07 #120](https://github.com/rouslanbaranov/tycho/issues/120). Updated 2026-10-19. This document and accompanying `case-record.schema.json` are *interchange fixtures and a design proposal*, **not** completion of Tycho K10–K20 (generated frontmatter, production JSON Schema, lexical index, Graphify/curated graph, hybrid search or MCP). Those remain owned by existing original Tycho epics. Do not create a second server, graph implementation or indexer in M9.

## Invariants and identifiers

- `case_id`: stable lower-case `case.<company>.<slug>`; refers to one company's bounded, dated modernization event, NEVER a universal endorsed pattern. Current 22 cases have one stable ID each.
- `claim_id`: globally stable `claim.<company>.<case-slug>.<sequence>`, independently verifiable unit. Claim content must distinguish *direct article statement*, *company-reported measurement*, *author interpretation*, *independent Tycho analysis*, *unknown*.
- `source_id`: foreign key to a public-original-only source (N01–N20, U01–U06, A01, SH01–SH04, SP01–SP03, ST01–ST02, DI01–DI02, ME01–ME03, LI01, CF01). **Candidate register entries are NOT automatically admitted.**
- `legacy_state`, `target_state`: case-specific patterns and boundary descriptions, NOT a graph of the contemporary company unless dated primary sources demonstrate it.
- `selected_patterns`, `avoided_patterns`, `constraints`, `failure_modes`: canonical normalized tokens, indexable. `avoided_patterns` means 'contraindication for the synthetic use case' unless a primary source expressly says the company rejected it.
- `valid_from` and `valid_until`: historical claim observation (ISO dates) and uncertainty; unknown is null. NEVER infer `valid_until` from publication date.
- `publication_date` is distinct from `event_date` and `accessed_on`. A **2026 conference abstract describing a 2023 architecture is not a 2026 deployment observation**.
- `confidence` is claim-relative: `primary_statement`, `first_party_reported_measurement`, `independent_replication`, `analysis`, `insufficient_evidence`. Do not compute artificial confidence scores; independent replication must cite a real independently reproduced experiment.
- `review_status`: `draft`, `source_reviewed`, `mechanically_validated`, `independent_reviewed`, `rejected`. A machine-readable record is not automatically `independent_reviewed`.
- Every concrete numeric claim must include a unit, numerator/denominator where relevant, version/window, exact location in original publication and explicit comparison denominator. Unknown values remain unknown rather than invented.
- Contract is collection-specific: `collection = tycho-public`; **Adro/private corpus must not enter Tycho's metadata, source register, evaluation cache, graph or embeddings.**

## Proposed JSON Schema boundaries

- `case-record.schema.json` is a portable **Draft 2020-12 proposal**. The owning K11 implementation may promote/adapt it after compatibility review; until then this is not declared the book's canonical production schema.
- Fields `case_id`, `title`, `company`, `status`, `observed_on`, `legacy_state`, `target_state`, `source_refs`, `claims`, `patterns`, `constraints`, `failure_modes`, `review` must be present. Schema is strict about allowed fields.
- Individual claims require `source_ref_id`, source `section` or `timestamp`, source-reported vs synthesized `evidence_type`, `validity_window` and `qualification`. Unknown unsupported claims may be represented as `insufficient_evidence`, but never silently admitted.
- The contract describes logical, not physical index formats. No Elasticsearch/Lucene/vector embedding shape is mandated by M9.

## Proposed graph relations (K15/K16 owners implement only after review)

| From | Directed edge | To | Restriction |
|---|---|---|---|
| case | `documents-transition` | transition (legacy → target) | Temporal and public-source provenance |
| case | `responds-to` | constraint | Requirement+workload scoped |
| case | `reports-failure` | failure mode | Original source or explicitly labelled synthesis |
| case | `uses-pattern` | pattern | Never implies pattern is globally best |
| case | `contradicts-applicability-of` | decision card | Condition must be present; not company ranking |
| claim | `derived-from` | primary source anchor | Exact section / timestamp / revision |
| decision | `compares` | two or more cases | May not claim original companies considered each other |
| query fixture | `tests-answer` | case, claim | Must preserve temporal uncertainty, refusal, negative evidence |

Graph endpoint IDs must be stable, direction explicit, evidence-bound and versioned under K15/K16 semantics. If graph owner has not released its schema, these remain **proposed relationships**, not materialized graph edges.

## Retrieval and MCP compatibility (K12, K17–K23)

**Route:** match requirements/problem and legacy state (e.g. wide Cassandra partition, hot-key skew, no-downtime). Return candidate case IDs and decisions, not whole chapter text.

**Read:** bounded summary with source statement vs analysis, validity window, exact claim IDs and its countercases. Allow clients to request detail on demand.

**Verify:** resolve `claim_id → source_id → primary URL + section/revision`, and attach inaccessible/pending-reverify state. Never fabricate a quote or fetch restricted content.

**Cross-provider:** specialist Rocinante chooses the appropriate provider; Tycho results must visibly say `tycho-public` and must not resolve internal private sources. Do not implement a Tycho-specific duplicate agent.

**Versioning:** content revision, schema version, source snapshot ID and index build revision should be linked in future immutable snapshots (K24). If index is stale or missing, return explicit `not_indexed`, never a synthetic retrieval hit.

## Acceptance and evaluation

The sibling `tests/fixtures/m9-case-queries.json` contains 44 labelled queries covering answerable, uncertain, and false-claim rejection. It is a **fixture specification**, not 36 verified retrieval results or an executed MCP benchmark. A future production evaluator should run these against actual K18/K19/K20/MCP endpoints, record tool-token/latency/citation fidelity, p95 and policy/negative-truth detection, and fail on attribution, historical/date inversion, overconfident source extrapolation or cross-provider leakage. Until the retrieval platform exists, **do not label the evaluation executed**.

Companion records `authoring/cases/examples/case-records.json` instantiate two proposed case records drawn from admitted/practitioner primary sources. Their `status` remains `draft`; they do not grant copied source-text rights.

## Contradiction handling and admission

Netflix 2023 talk reporting ~2,800 Java apps (N02) and a 2026 JavaOne session summary referencing 3,000+ services (N03) are **dated source statements**, not a proof of one inventory or growth causality. N09 2024-04 plan and N10 2024-12 release are sequential evidence, not contradictory simultaneity. N05 generational ZGC/G1 and its separate Parallel-GC batch counterexample belong to distinct workloads. Without such qualifiers, the retrieval system must return `insufficient_evidence` and explain why.

Source admission and correctness review are still tracked by [#114](https://github.com/rouslanbaranov/tycho/issues/114) and [#121](https://github.com/rouslanbaranov/tycho/issues/121). Original case drafts: [book/cases](../../book/cases/README.md).
