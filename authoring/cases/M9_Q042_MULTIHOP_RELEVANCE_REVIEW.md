# M9 / E16-08 — Ambiguous Retrieval Gold Labels: Agent-Generated Migration + Immutable Shadow Proof

**Evaluation item:** `m9-q042` · **Status:** structured relevance *proposal awaiting independent adjudication*. This is not a change to the frozen 60-query benchmark, not production search quality acceptance and not a claim that any one company implemented an end-to-end LLM+shadow-comparison pipeline.

## Why the current labels alone are insufficient

The original query asks how **immutable Big Data shadow comparisons** could gate an **agent-generated data migration**. The frozen query fixture names only Netflix Casspactor→Cassandra Analytics (src.m9-n11) and Stripe subscription storage migration (src.m9-st01). These are valuable correctness precedents but **neither is public evidence of the company using an AI coding agent for that particular migration**.

The executed [29-page BM25 baseline](M9_BM25_CANDIDATE_BASELINE_2026-10-19.md) ranked the named Netflix case **15th** and Stripe **11th**. It ranked Spotify Honk, LinkedIn Kafka audit and Meta ingestion shadow lifecycle at positions 1–3. The Spotify case actually covers **LLM-assisted migration PRs**; Meta's case covers **shadow / reverse-shadow validation of data ingestion**; LinkedIn provides a distinct stream auditing precedent. These results cannot be judged solely by whether Netflix/Stripe appear in top three. Conversely, Spotify + Meta + LinkedIn do **not** establish the exact two-sided immutable set comparison documented by Netflix.

## Required answer facets and company evidence

| Essential facet | Source-backed case | Can establish | Cannot establish |
|---|---|---|---|
| Agent-generated changes | [Spotify Honk (src.m9-sp03)](../../book/cases/spotify-honk-data-consumer-migration.md) | Real rollout of generated dbt/BigQuery Runner migration PRs; explicit ambiguous field-mapping rejection, missing tests and owner verification | That every automated migration passed semantic parity or all 1,800 downstream pipelines were migrated |
| Immutable snapshot/output proof | [Netflix Casspactor (src.m9-n11)](../../book/cases/netflix-casspactor-shadow-migration.md) | Comparison of **C−M** and **M−C** to detect missing/extra rows with controlled fallback | That Netflix generated this migration with an LLM coding agent |
| Human-defined oracle and rollout gate | Spotify src.m9-sp03 **plus** Netflix src.m9-n11 | Combine field-mapping/owner judgement and two-sided equivalence on comparable snapshot inputs | That either company's original product already combined both methods |

**Relevant but distinct contrasts:** [Meta ingestion (src.m9-me03)](../../book/cases/meta-ingestion-shadow-migration-lifecycle.md) used shadow and reverse-shadow migration with row-count/checksum/freshness/resource gates; [Stripe online migration (src.m9-st01)](../../book/cases/stripe-online-subscriptions-migration.md) demonstrates mutable dual writes, read comparison and authority handoff; [LinkedIn Kafka audit (src.m9-li01)](../../book/cases/linkedin-kafka-tiered-completeness.md) describes stream tier auditing. None alone answers the composite immutable+agent question.

## Safe proposed synthesis for a new, hypothetical legacy system

1. An agent proposes a bounded data transformation from a pinned source schema/revision, and annotates ambiguous fields for an owner (informed by **Spotify**, not claimed to be Netflix's process).
2. Old and candidate immutable outputs are generated from the same data snapshot/window. Compare missing/extra rows in **both directions**, and define timestamp/TTL/schema canonicalization; declare what cannot be proven by equality to an imperfect old implementation (informed by **Netflix**).
3. Require explicit owner-approved invariants and a controlled fallback. If a case lacks an oracle, the recommendation is **no automatic cutover**; this is Tycho synthesis, not a reproduced vendor release pipeline.
4. For a mutable target store, use the alternate staged read/write ownership model (**Stripe**) rather than incorrectly treating its online subscriptions as an immutable batch.

A useful future agent answer must cite **at least src.m9-sp03 and src.m9-n11**, identify them as distinct companies/periods, and disclose which steps are synthesized. It must reject a statement that any publisher independently proved autonomous AI migration correctness.

## Proposed secondary evaluation contract

A machine-readable **supplemental pilot** lives at [`tests/fixtures/m9-q042-evidence-facets.proposed.json`](../../tests/fixtures/m9-q042-evidence-facets.proposed.json). It captures three required *facets* and three related-but-not-sufficient comparators, preserving the original fixture's immutable `expected_case_ids` so published Hit@k results remain reproducible.

A future retrieval evaluator can use **facet coverage@k**: a facet is covered when at least one *direct_evidence* case supporting that facet appears in the top k. A complete answer additionally needs two distinct companies' source statements and correct synthesis/false-claim guards. The existing BM25 top three covers the agent-code facet but **not** the immutable set-comparison facet; this is different from saying all the retrieved pages are irrelevant. Facet labels are proposed by the same authors as the cases, so an independent relevance reviewer must approve or alter them before official evaluation.

## Negative controls for label gaming

- Do **not** silently add Spotify or Meta to the original `m9-q042.expected_case_ids` to raise the BM25 score.
- Do **not** claim a case is directly relevant merely because its title says “shadow”, “agent” or “migration”; tie each facet to a claim/source/period.
- Do **not** treat high BM25 Hit@k as evidence that the agent answered the multi-hop question safely. Refusal, provenance and authorization remain separate axes.
- Do **not** move this pilot into the canonical K18–K23 retrieval schema or invent an MCP endpoint in M9; it is a proposed annotation for a future independently judged evaluation set.

**Acceptance:** provisional reviewer aid only; #121 must remain open until actual independent semantic/source review and relevant runtime benchmarks or an explicit authorized exception.
