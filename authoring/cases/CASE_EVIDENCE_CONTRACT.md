# M9 case, claim, provenance and decision-retrieval contract

**Status:** **portable proposed v1 contract** for issue [E16-07 #120](https://github.com/rouslanbaranov/tycho/issues/120). Updated 2026-10-19. This document and accompanying `case-record.schema.json` are *interchange fixtures and a design proposal*, **not** completion of Tycho K10–K20 (generated frontmatter, production JSON Schema, lexical index, hybrid search or MCP). Those remain owned by existing original Tycho epics. Do not create a second server or indexer in M9. **Graph development, graph fixtures, graph versioning, traversal and maintenance are retired under the accepted Tycho ADR.**

## Invariants and identifiers

- `case_id`: stable lower-case `case.<company>.<slug>`; refers to one company's bounded, dated modernization event, NEVER a universal endorsed pattern. Current 22 cases have one stable ID each.
- `claim_id`: globally stable `claim.<company>.<case-slug>.<sequence>`, independently verifiable unit. Claim content must distinguish *direct article statement*, *company-reported measurement*, *author interpretation*, *independent Tycho analysis*, *unknown*.
- `source_id`: foreign key to a public-original-only source (src.m9-n01–src.m9-n20, src.m9-u01–src.m9-u06, src.m9-a01, src.m9-sh01–src.m9-sh04, src.m9-sp01–src.m9-sp03, src.m9-st01–src.m9-st02, src.m9-di01–src.m9-di02, src.m9-me01–src.m9-me03, src.m9-li01, src.m9-cf01). **Candidate register entries are NOT automatically admitted.**
- `legacy_state`, `target_state`: case-specific patterns and boundary descriptions, NOT a graph of the contemporary company unless dated primary sources demonstrate it.
- `selected_patterns`, `avoided_patterns`, `constraints`, `failure_modes`: canonical normalized tokens, indexable. `avoided_patterns` means 'contraindication for the synthetic use case' unless a primary source expressly says the company rejected it.
- `valid_from` and `valid_until`: historical claim observation (ISO dates) and uncertainty; unknown is null. NEVER infer `valid_until` from publication date.
- `publication_date` is distinct from `event_date` and `accessed_on`. A **2026 conference abstract describing a 2023 architecture is not a 2026 deployment observation**.
- `confidence` is claim-relative: `primary_statement`, `first_party_reported_measurement`, `independent_replication`, `analysis`, `insufficient_evidence`. Do not compute artificial confidence scores; independent replication must cite a real independently reproduced experiment.
- `review_status`: `draft`, `source_reviewed`, `mechanically_validated`, `independent_reviewed`, `rejected`. A machine-readable record is not automatically `independent_reviewed`.
- Every concrete numeric claim must include a unit, numerator/denominator where relevant, version/window, exact location in original publication and explicit comparison denominator. Unknown values remain unknown rather than invented.
- Contract is collection-specific: `collection = tycho-public`; **Adro/private corpus must not enter Tycho's metadata, source register, evaluation cache or embeddings.**

## Proposed JSON Schema boundaries

- `case-record.schema.json` is a portable **Draft 2020-12 proposal**. The owning K11 implementation may promote/adapt it after compatibility review; until then this is not declared the book's canonical production schema.
- Fields `case_id`, `title`, `company`, `status`, `observed_on`, `legacy_state`, `target_state`, `source_refs`, `claims`, `patterns`, `constraints`, `failure_modes`, `review` must be present. Schema is strict about allowed fields.
- Individual claims require `source_ref_id`, source `section` or `timestamp`, source-reported vs synthesized `evidence_type`, `validity_window` and `qualification`. Unknown unsupported claims may be represented as `insufficient_evidence`, but never silently admitted.
- **Two-layer date checks:** Draft 2020-12 + `FormatChecker` validates the syntax of `valid_from` and `valid_until` individually; it does **not** express their relative chronological ordering in this schema. The portable Python `validate_record` semantic check rejects `valid_from > valid_until` when both exist. Future K11 adapters MUST retain this distinct business invariant. Test classification: **nine invalid schema shapes + one semantically inverted date window**; reporting ten JSON Schema failures is wrong.
- The contract describes logical, not physical index formats. No Elasticsearch/Lucene/vector embedding shape is mandated by M9.

## Navigation and decision relationships without a graph

Case-to-pattern, case-to-case, claim-to-source, and decision-to-contrary-evidence relationships are represented through **stable document and claim identifiers**, explicit Markdown links, canonical metadata/section indexes and first-party source sections. This is not a graph edge vocabulary or a materialized graph model; no K15/K16 implementation or maintenance is expected. Requirements/contraindications are explained locally so an agent can validate the reasoning by reading the page and its source. For verified claims the bounded read path is case ID → claim ID → source reference → public publisher URL/section, with revision/date/unknown status preserved. Graph-dependent acceptance, APIs and adapters are removed from M9 scope.

## Retrieval and MCP compatibility (K12, K17–K23)

**Route:** match requirements/problem and legacy state (e.g. wide Cassandra partition, hot-key skew, no-downtime). Return candidate case IDs and decisions, not whole chapter text.

**Read:** bounded summary with source statement vs analysis, validity window, exact claim IDs and its countercases. Allow clients to request detail on demand.

**Verify:** resolve `claim_id → source_id → primary URL + section/revision`, and attach inaccessible/pending-reverify state. Never fabricate a quote or fetch restricted content.

**Cross-provider:** specialist Rocinante chooses the appropriate provider; Tycho results must visibly say `tycho-public` and must not resolve internal private sources. Do not implement a Tycho-specific duplicate agent.

**Versioning:** content revision, schema version, source snapshot ID and index build revision should be linked in future immutable snapshots (K24). If index is stale or missing, return explicit `not_indexed`, never a synthetic retrieval hit.

## Acceptance and evaluation

The sibling `tests/fixtures/m9-case-queries.json` contains 60 labelled queries covering answerable, uncertain, and false-claim rejection. It is a **fixture specification**, not 60 executed retrieval results or a completed MCP benchmark. A future production evaluator should run these against actual K18/K19/K20/MCP endpoints, record tool-token/latency/citation fidelity, p95 and policy/negative-truth detection, and fail on attribution, historical/date inversion, overconfident source extrapolation or cross-provider leakage. Until the retrieval platform exists, **do not label the evaluation executed**.

Companion records `authoring/cases/examples/case-records.json` instantiate two proposed case records drawn from admitted/practitioner primary sources. Their `status` remains `draft`; they do not grant copied source-text rights.

## Contradiction handling and admission

Netflix 2023 talk reporting ~2,800 Java apps (src.m9-n02) and a 2026 JavaOne session summary referencing 3,000+ services (src.m9-n03) are **dated source statements**, not a proof of one inventory or growth causality. src.m9-n09 2024-04 plan and src.m9-n10 2024-12 release are sequential evidence, not contradictory simultaneity. src.m9-n05 generational ZGC/G1 and its separate Parallel-GC batch counterexample belong to distinct workloads. Without such qualifiers, the retrieval system must return `insufficient_evidence` and explain why.

Source admission and correctness review are still tracked by [#114](https://github.com/rouslanbaranov/tycho/issues/114) and [#121](https://github.com/rouslanbaranov/tycho/issues/121). Original case drafts: [book/cases](../../book/cases/README.md).

## Expanded evaluation fixture wave — security identity, overload and ingestion

The fixture set now contains **60** deterministic questions (**21 answerable**, **26 false/unsupported claim rejections**, **13 insufficient-evidence outcomes**). Twelve extra questions test Netflix Data Projects identity/least-privilege proposals (src.m9-n17), Uber Cinnamon workload-specific overload-control (src.m9-u06), Meta ingestion shadow validation (src.m9-me03), contradiction against Stripe/Netflix alternatives, and correct refusal for **src.m9-n14/src.m9-st02 deferred primary texts**. These are **test definitions only**, not executed search/MCP or validated answers. Runtime integration still belongs to Tycho's existing K18–K23 implementation roadmap.

## QCon 2023 outgoing gRPC CPU-pool regression contrast

Source [src.m9-n02](https://www.infoq.com/presentations/netflix-java/) supports a small, unquantified **few-percent regression** after trying virtual threads on a CPU-intensive outgoing gRPC client worker pool. This must be distinguished from src.m9-n06's July 2024 carrier starvation incident and src.m9-n07's 2016 Zuul2 I/O connection scaling. Four extra evaluation fixtures (`m9-q057`–`m9-q060`) capture positive comparison, false equivalence rejection and refusal to invent an exact p99/percentage. Total is now 60 proposed, **not executed**, retrieval questions.
