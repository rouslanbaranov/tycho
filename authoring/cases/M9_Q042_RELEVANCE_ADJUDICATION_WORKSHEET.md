# E16-08 — M9-Q042 Search Relevance Adjudication Worksheet

**Status:** author-generated **proposed** review rubric, **NOT independent gold-label acceptance**. Based on existing 2026-10-19 M9 corpus and [executed baseline](M9_BM25_CANDIDATE_BASELINE_2026-10-19.md). Current query fixture [`m9-q042`](../../tests/fixtures/m9-case-queries.json) asks: *How can immutable Big Data shadow comparisons be used to gate an agent-generated data migration?*

## Why this is a multi-evidence question, not a one-company keyword lookup

The query joins three requirements no one source necessarily supports together:

1. **Agent-generated transformation safety:** metadata/semantic mapping, untestable changes, human signoff and partial automation.
2. **Immutable/batch output comparison:** use comparable input snapshots and semantic old-vs-new set differences, instead of row-count equality alone.
3. **Gate and rollback policy:** define the trusted oracle, cohort selection, failed-validation behavior and authoritative cutover/rollback before automation.

A retrieved document can be directly relevant to one axis and irrelevant to another. Merely appearing in BM25 top 3 is **not** evidence of a complete answer or a model refusal. The historical gold set contains two case IDs (Netflix Casspactor src.m9-n11 and Stripe online data src.m9-st01), while the lexical results rank them **15th** and **11th**; Spotify Honk, LinkedIn Kafka audit and Meta ingestion shadow were ranked first through third.

## Proposed graded per-case evidence, pending separate reviewer

| Candidate case | Agent automation axis | Immutable/batch equivalence axis | Safe gate / fallback axis | Why grade must be justified |
|---|---|---|---|---|
| [Netflix Casspactor](../../book/cases/netflix-casspactor-shadow-migration.md) src.m9-n11 | **Not reported as an LLM-agent migration** | **High** — two-sided output sets C−M and M−C on comparable backup inputs | **High** — shadow check, cohort Decider/fallback | Direct evidence for snapshot/shadow oracle, not automatic code generation |
| [Spotify Honk dataset PRs](../../book/cases/spotify-honk-data-consumer-migration.md) src.m9-sp03 | **High** — background coding agent and bounded PR pipeline with failed/unsupported framework cohorts | **Not established** — the publication does not demonstrate immutable Casspactor-like output-set equality | **Medium** — owner verification, ambiguous mappings left unchanged; no general independent correctness oracle | Direct agent-process evidence with limited tests, **not** immutable-data proof |
| [Meta ingestion](../../book/cases/meta-ingestion-shadow-migration-lifecycle.md) src.m9-me03 | **Not reported as LLM-agent coding migration** | **Medium** — row-count and checksum comparisons for CDC partitions (not necessarily immutable batch equality) | **High** — shadow → reverse shadow, partition quarantine, backfill/rollback | Evidence for cutover/rollback orchestration under mutable CDC; not proof for immutable jobs |
| [Stripe subscriptions](../../book/cases/stripe-online-subscriptions-migration.md) src.m9-st01 | **Not LLM-agent authored** | **Low** for immutable batch: online mutable subscription schema, Scientist read comparison | **High** — dual write → verified reads → new writes → retirement | Good countercase for a **different data-authority problem**, not a direct batch equivalence witness |
| [LinkedIn Kafka completeness](../../book/cases/linkedin-kafka-tiered-completeness.md) src.m9-li01 | **Not agent-code-migration evidence** | **Low** — historical pipeline count/audit can mask canceling dropped+duplicate messages | **Context only** — relevant as warning that count equality alone is weak | Search result is topically related but does not answer the combined migration question |

**These values are preliminary, author-assessed evidence-axis descriptions; NOT true relevance grades or independent approvals.** A reviewer should open the exact cited primary-source sections, reject any assertion unsupported by the primary source, decide how to weigh the axes and record explicit reviewer identity/date.

## Suggested decision answer once the primary evidence is confirmed

A safe response could **combine**, without falsely attributing the combination to any one company:

1. **Design transformations:** narrow agent work to schema/field mappings with explicit testable contracts and permitted ambiguity/owner escape paths (Spotify src.m9-sp03).
2. **Define the data oracle:** pin source snapshot/revision, compare immutable outputs in both set-difference directions, and inspect extra/missing records, schema and temporal semantics (Netflix src.m9-n11). If data is mutable CDC rather than a single immutable batch, also enforce per-partition timestamp/landing and checksum consistency (Meta src.m9-me03).
3. **Gate rollout:** dry-run/shadow and test representative outliers, hold ambiguous or testless cohorts for human review, then canary with fallback that preserves old authority until verified. Reverse shadow/partition rollback (Meta) and Scientist read comparison (Stripe) are **alternatives conditional on different execution semantics**, not instructions to run all mechanisms blindly.
4. **Say what cannot be concluded:** none of the cited original company stories independently validates that one integrated AI-agent + immutable-output migration harness was deployed or achieved a universal defect escape rate. If the user's system cannot supply an oracle, return **insufficient evidence**, not an invented test result.

This is a **Tycho-derived synthesis** from independent company historical accounts, not something Netflix, Spotify, Stripe or Meta jointly evaluated.

## Independent adjudication and scoring protocol

- Preserve the original `m9-q042` gold labels in `tests/fixtures/m9-case-queries.json` until a second reviewer independently accepts a revision. Never optimize labels based on the benchmark top 3.
- Ask an independent reviewer to label each candidate **0 (no supporting evidence), 1 (context/counterexample), 2 (direct evidence for one required axis), 3 (sufficient for complete multi-axis answer)**, and cite exact source sections and limitations for every grade. A single-page grade **3** is not expected by default.
- Evaluate **set coverage**, e.g. whether a top-k *combination* covers mandatory agent-process + immutable oracle + fallback axes, in addition to conventional any-gold Hit@k and pair-recall. A one-document Hit@k is structurally ill-suited to this conjunctive question.
- Require two reviewer-authored adversarial paraphrases and one deliberately false claim about automatically proven equality. Verify that ranking does not manufacture correctness or unsupported AI success.
- If gold changes are approved, store an immutable **new** relevance-judgment revision and rerun the original baseline before comparing with hybrid/semantic retrieval. Never retroactively edit the 2026-10-19 baseline numbers.

## Reviewer acceptance

**Not completed:** independent source-level judgments, graded-gold artifact, real K18–K23 ranked search, MCP answers, provenance fidelity, token/latency metrics. This worksheet is a preparation deliverable for still-open #121, not M9 acceptance.
