# M9 E16-08 — Precise Dependencies on the Original Tycho Search and MCP Roadmap

**Snapshot examined:** 2026-10-19 · **Scope:** read-only reconnaissance of original M1–M8 issue and PR status; M9 does **not** modify those issues/branches or implement a second retrieval server.

## Graph-retirement supersession

The **accepted Tycho ADR retires curated knowledge graphs**. Earlier issue titles/dependency observations in the table below are historical and must **not** be interpreted as an M9 graph requirement. The only M9 deliverables are case pages, explicit Markdown cross-links, stable metadata/claim-to-source provenance, textual section search, and evidence-bound agent retrieval. Do not build or maintain graph infrastructure or block M9 acceptance on a graph feature. Operational MCP/search gates must be evaluated against graph-free contracts when available.

## Confirmed core dependencies

| Capability in original roadmap | Core GitHub item | Observed status | Required before M9 can claim a real integration evaluation |
|---|---|---|---|
| Deterministic snapshot/section index K18 | [E07-03 #49](https://github.com/rouslanbaranov/tycho/issues/49) | OPEN; [FTS5 pilot PR #188](https://github.com/rouslanbaranov/tycho/pull/188) under review at snapshot | Indexed M9 case sections with stable case IDs and a reported source/index snapshot |
| Ranked search and progressive reads K18/K20 | [E07-04 #50](https://github.com/rouslanbaranov/tycho/issues/50) | OPEN; depends on #49 | Ranked compact case candidates, filtering, bounded selected evidence reads and explicit missing/stale-source states |
| Evidence/provenance resolution K20 | [E07-05 #51](https://github.com/rouslanbaranov/tycho/issues/51) | OPEN; depends on #50, #46 and #29 | Case→claim→source/section provenance, with no curated graph edges, traversal or graph pipeline |
| Embeddings and hybrid retrieval K19 | [E08 #52–#55](https://github.com/rouslanbaranov/tycho/issues/9) | OPEN, staged after K18, including benchmark/adoption decision | Optional comparison to lexical baseline only when versioned embeddings/vector results actually exist |
| MCP protocol/transport design K21 | [E09-01 #56](https://github.com/rouslanbaranov/tycho/issues/56) | CLOSED, specification/compatibility decision, not live service | Stable definitions of transport, session/snapshot and client limitations |
| Read-only MCP retrieval adapter K21/K22 | [E09-02 #57](https://github.com/rouslanbaranov/tycho/issues/57) | OPEN; depends on #56 and #51 | Real MCP discover/search/read roundtrip with case refs, truncation and explicit non-hallucinated errors |
| MCP provenance + onboarding | [E09-03 #58](https://github.com/rouslanbaranov/tycho/issues/58), [E09-04 #59](https://github.com/rouslanbaranov/tycho/issues/59), [E09-05 #60](https://github.com/rouslanbaranov/tycho/issues/60) | OPEN | Real generic-client interoperability, navigable source evidence, onboarding and failure/unknown handling |

These are **issues and status at observation time**, not promises about which implementation will ship. A merged PR, a prototype and an open issue do not imply the associated production search/MCP capability is deployed.

## What M9 can measure without waiting

**Available and actually executed as bounded diagnostics:**

- Basic source / stable-ID / internal Markdown file-link checks against GitHub tree for the case and decision collection.
- Draft 2020-12 proposed record schema validation of two manually transferred examples, with explicitly limited provenance and negative-case checks; `scripts/validate_m9_cases.py` and its follow-up regressions still require full checkout execution to claim suite pass.
- **Offline document-level lexical candidate ranking**, 29 case drafts × 60 evidence/refusal query fixtures, published as [BM25 baseline](M9_BM25_CANDIDATE_BASELINE_2026-10-19.md), Hit@1 48/57 and Hit@3 55/57 on author-labelled relevance. This is **not** MCP or final-answer accuracy.
- **Q042 multi-hop facet proposal:** [composite agent+immutable shadow oracle](M9_Q042_MULTIHOP_RELEVANCE_REVIEW.md), proposed label file `tests/fixtures/m9-q042-evidence-facets.proposed.json` and owner-authored guardrails. It is not an independently approved gold label set.
- Case-by-case public source/technical review can continue in M9, provided author checks never masquerade as a qualified independent reviewer.

## Non-negotiable prerequisites for declaring a real 60-query retrieval test

When the owning core team exposes a usable pinned K18/K20/K21 service, run the **unchanged** `tests/fixtures/m9-case-queries.json` and separately record:

1. **Environment and identity:** build/commit SHA, collection `tycho-public`, source snapshot ID, index and optional embedding version (if implemented), MCP server/SDK/client/transport versions, relevant client request budget.
2. **Candidate retrieval:** case/section IDs and ranked positions at 1/3/5, evidence/decision coverage, explicitly excluded sources src.m9-n14/src.m9-st02, stale/missing snapshot cases.
3. **Claim verification:** resolved primary URL and source section, publication/observation date, reported vs measured vs synthetic inference and negative counterexamples, unsupported-company-claim rejection.
4. **Actual agent answer behavior:** citation fidelity, multi-hop evidence synthesis vs falsely attributing company work, refusal for 26 false-claim and 13 insufficient-evidence questions, with independent human adjudication of ambiguous labels.
5. **Cost and failure:** p50/p95 latency, per-query input/output/tool tokens, truncation, retries, response payload, 5xx/timeout and fallback reasons; never substitute document recall for token cost or correct final reasoning.
6. **Human acceptance:** reviewer identity, sampled/error claim references and signed verdicts from an authorized independent reviewer. Populating `status: independent_reviewed` metadata alone is not such a verdict.

**If core capabilities are not available:** the correct M9 result is `BLOCKED_BY_CORE_SERVICE`, with these specific issue links and missing runtime measurements. A human milestone owner may expressly accept a deferred integration gate and sign an exception, but an assistant must never infer that waiver from a closed issue, an author's pilot, or elapsed time. Do not close issue [#121](https://github.com/rouslanbaranov/tycho/issues/121) or Epic [#113](https://github.com/rouslanbaranov/tycho/issues/113) as independently accepted until the authorized decision and evidence exist.

## Parallel worker and corpus boundaries

This report is authored solely under M9. Do **not** edit the core worker lock `automation/tycho-core-worker-lock`, PR #188 or E07/E08/E09 issues. No changes to their schemas, commands, implementation schedule or CI policy are authorized here.

Tycho case data and tests remain a completely **public-source-only** collection. Adro data, employer code, private source paths and UBS-specific concepts are prohibited. Rocinante remains the single umbrella specialist agent; M9 does not create a second expert or duplicate search service.

**State:** dependency trace prepared; **independent review and genuine MCP evaluation still pending**.
