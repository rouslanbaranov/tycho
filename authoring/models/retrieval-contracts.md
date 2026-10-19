# Transport-independent retrieval contracts, version 1

> E07-01 [issue #47](https://github.com/rouslanbaranov/tycho/issues/47), M4. Original design contract, 2026-10-19. These envelopes are **specified**, not deployed: no lexical engine, MCP endpoint, graph query service, measured token saving or production performance is claimed.

## Common envelope, errors and identity

The same request/response semantics apply to local CLI, Python harness and a future Rocinante MCP adapter. A transport adapter must never silently change a snapshot, widen security/coverage constraints or claim source verification from search relevance.

| Field | Meaning |
|---|---|
| `protocol_version` | Exact major integer `1`; unknown versions fail closed |
| `request_id` | Caller correlation identifier, not authentication |
| `operation` | `search`, `read`, `graph` or `evidence` |
| `snapshot_id` | Immutable published index/graph/book snapshot. Null is accepted only for *initial* discovery; returned ID pins all subsequent operations |
| `filters` | Exact document ID, kinds, topics, perspectives, source IDs, evidence statuses and optional section boundary |
| `limits` | `max_results`, `max_chars`, `max_evidence_items`, `max_depth` and timeout; validate positive finite bounded inputs per operation |
| `cursor` | Opaque continuation bound to snapshot ID, normalized query, filters, sort mode and limit. Tampering/staleness fails closed |
| `status` | `ok`, `partial`, `no-results`, `snapshot-mismatch`, `incomplete-coverage`, `invalid-request`, `not-available` |
| `coverage` | Indexed document and section scope, excluded/unbuilt areas and source/graph availability. A zero-hit result is not proof of system-wide absence |
| `warnings` | Specific missing evidence, unimplemented semantic features and recheck actions |

Every result repeats protocol version, request ID, *actual* snapshot, status, coverage and warnings; no errors are rendered as ordinary factual citations. A requested snapshot mismatch returns **no new-snapshot result payload** and includes both requested and current identifiers so the caller can restart deliberately.

## Search: route without expanding full documents

Request: `query` plus optional exact terms, filters, sort and small first-pass `limits`. Result: stable `document_id`, `section_id`, repository-relative canonical `path`, heading, exact anchor, bounded excerpt and citation; `score` includes `score_kind` and `ranker_version`. Similarity scores from different indexes/revisions must not be compared. Deterministic tiebreaker: stable IDs in a pinned snapshot.

Return actual matched terms, supported filter coverage, `source_ids`, `claim_ids`, declared `evidence_status`, `truncated` and next cursor only if a bounded continuation exists. Do not infer source inspection, architectural applicability or graph edges from lexical co-occurrence. A planned vector or hybrid ranker is **not** an implemented search capability.

## Read: bounded sections and exact offsets

Request: `document_id`, optionally `section_id`, exact snapshot, optional `expected_sha256`, UTF-8 *codepoint* offset and positive `max_chars`. Response: the same canonical ID/section, start/end offsets, actual character count, next offset or null, original total length if known, page/section SHA-256, explicit truncation and cited heading. Character and byte offsets must never be conflated. A stale document hash, old cursor or changed snapshot is `snapshot-mismatch`—never silently slice the latest page using an old offset.

An implementation may prefer paragraph-aligned splitting, but only if it preserves correctly reported offsets and requested budget. Truncated text cannot gain invented source line numbers. Read must not cause enrichment, external fetches, writes or automatic index rebuild.

## Graph: typed, directed, budget-limited neighbors

Request: start node IDs, `outgoing`/`incoming`/`both`, exact allowed relation types and node kinds, `max_depth`, `max_results`, snapshot, cursor. Result: explicit `edge_id`, `from`, `to`, kind, `plane` (code, curated, navigation), conditions, limitations, pinned source version and `evidence_claim_ids`. Use the [graph vocabulary](graph-vocabulary-and-shards.md). A traversal never manufactures transitive `supports`, `candidate_for` or `contradicts` relationships. Missing graph shards return `incomplete-coverage` or `not-available`, not plausible invented neighbors.

## Evidence: verification is separate from retrieval

Request: exact claim, source or document-section ID at the same snapshot. Result: the [typed source-claim relationship](../../sources/CLAIM-PROVENANCE.md), publisher/canonical URL, documented section, locked code revision/path/symbol where relevant, inspection status, source relation `supports`/`qualifies`/`contradicts`/`unavailable`, applicability, contradictory claims and editorial review state. A registered source is not a read source; a structurally valid citation is not an expert's determination of technical truth. A blocked primary source remains blocked; an accessible official companion is separately identified, never presented as the unavailable original.

## Route → Read → Verify (agent-facing)

1. **Route** from a concrete user question through scoped filters to short canonical section candidates. The initial few results are a token-saving heuristic, never an evidence ceiling.
2. **Read** selected sections in the SAME snapshot with bounded continuation, expanding when failure conditions, alternatives or source details demand more context.
3. **Verify** decision-critical assertions against exact source passages/revisions; separately check constraints and counterexamples using [decision navigation](decision-navigation.md). If insufficient, return `insufficient-evidence` with a finite measurement/source request. Do not force a technology recommendation.
4. **Continue or restart** only with explicit snapshot agreement. Give consumers the stable citation and recheck triggers; never merge evidence from different snapshots without labeling it.

## Example fixtures and acceptance boundaries

[Request/response fixtures](../../fixtures/retrieval-contract-v1.json) demonstrate one small search and one stale-snapshot refusal. They are **illustrative envelopes**, not working endpoints, and are intentionally sparse. Later retrieval #48–#51, graph #46 and MCP #57+ own actual engines, schema gates, adapters and evaluation. This specification does not promise that any engine can fulfill all operations today.

A strict future validator must enforce types/limits, required operation-specific fields, deterministic cursor ownership, source-ID resolution and no substantive payload on snapshot mismatch; integration tests must simulate changed snapshots, missing sections, partial coverage, truncation and contradictory evidence. Tests, independent technical review and production evaluation are **not** claimed here.
