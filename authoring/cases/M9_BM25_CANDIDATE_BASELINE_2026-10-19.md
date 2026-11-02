# M9 — First Executed Lexical Candidate Baseline (BM25)

**Executed against 29 GitHub-connected Tycho case drafts and 60 real fixture queries on 2026-10-19.** This is an **offline diagnostic only**, NOT the K18–K23 production lexical/hybrid index, MCP output, answer generation, citation fidelity, semantic relevance evaluation or an independent case review.

Inputs: `book/cases/*.md` (29 case pages), `tests/fixtures/m9-case-queries.json` (60 queries, Git blob `c0c3c5653a0aa512e64fea2048550a2fb8759125`). Each case ID was parsed from its original page; all gold expected case IDs resolved uniquely. Query tokens and document tokens: lower-case ASCII alphanumeric, length >=3, a fixed common stopword set; case IDs and URL destinations removed from indexed text. Standard **BM25 k1=1.2, b=0.75**, unique query terms, tie-break by ID.

## Measured candidate retrieval (not final answer quality)

| Slice | Queries | Queries with gold case(s) | Hit@1 | Hit@3 | Hit@5 | Hit@10 | MRR |
|---|---:|---:|---:|---:|---:|---:|---:|
| All behavior classes | 60 | 57 | 48 | 55 | 55 | 56 | 0.8993 |
| Answerable | 21 | 21 | 19 | 20 | 20 | 20 | 0.925 |
| False-claim rejection | 26 | 25 | 23 | 25 | 25 | 25 | 0.9533 |
| Insufficient-evidence | 13 | 11 | 6 | 10 | 10 | 11 | 0.7273 |

**Definition:** Hit@k means at least one fixture `expected_case_ids` case appears among the first k ranked pages; for fixtures with no expected case IDs this metric is intentionally undefined and excluded from the denominator. This is a weak *candidate discovery* criterion: it does not prove all supporting citations were found, nor that an agent refused an incorrect premise. Additional pair-level gold recall metrics and individual ranks are in the [machine-readable result](M9_BM25_CANDIDATE_BASELINE_2026-10-19.json).

**Answerable queries missing all gold in top 3:** 1. `m9-q042` (gold rank(s) 15/11).

## Architectural consequence for external-specialist/Tycho

This pilot demonstrates the starting ceiling/weak spots for a **document-level lexical-only** baseline. Workload terms and company/technology overlaps can rank the wrong company case above the right one. Do not use title/code IDs alone to claim retrieval correctness. Future K18–K23 evaluation should compare full-document lexical, chunked lexical, semantic/hybrid and evidence-based reranking **on exactly the same fixture set**, preserving source/version anchors, false-claim refusal and token-cost measurement. No live system was changed; this work does **not** create a second production indexer or MCP agent.

**Limitations:** Tests were computed in a connected-tool JS environment; no local Python script or complete Git checkout was run, corpus is only 29 case files (not whole Tycho). The index may have changed after the fetch. Retrieval does **not** perform language-model answering or source correctness verification. This report is a diagnostic input to the still-open #121 independent review, **not** acceptance of M9.

## Label-adjudication risk — do not game the benchmark

The main positive miss is **m9-q042** (agent-generated data migration with immutable Big Data shadow comparison). The current fixture labels require Netflix Casspactor and Stripe, ranking **15** and **11**; lexical BM25 instead surfaces Spotify Honk, LinkedIn Kafka audit and Meta ingestion shadow validation in its first three hits. Some of those *may be legitimate partial evidence* for the mixed agent/data/shadow question. Therefore this is both a **candidate-ranking gap relative to existing gold IDs** and a **possible incomplete gold-label problem**. Do not rewrite the original `expected_case_ids` simply to inflate measured recall. Independent case/evaluation reviewers should adjudicate which sources genuinely establish agent-specific and data-equivalence parts, add graded/multi-hop relevance judgments if justified, and rerun the same baseline and production retrieval with versioned labels.

The 60 fixtures were created by the Tycho authors and are **not an independent held-out relevance set**. Hit@k is best treated as a diagnostic indicator, not proof of generalizable enterprise-search accuracy. A second blind, adversarial query set should eventually be authored by a different reviewer; for unsupported claims, retrieval hit rate does not measure the correctness of refusing the false premise.

**Reproducibility:** `python3 scripts/evaluate_m9_case_bm25.py` is added by the same PR as a stdlib-only local re-run script, but **it was not executed in a checkout** in this conversation. The numeric result above comes from the fully executed connected-tool JavaScript diagnostic across the 29 GitHub case contents. The reported fields can be independently compared on a pinned local revision.
