# Qrels v3 top-1 discordance — 2026-10-29

Status: diagnostic on AI-adjudicated qrels v3. Not human review, independent
review, CI or owner acceptance.

## Counts

- Discordant top-1: 16 of 188.
- Best-only correct: 12.
- BM25-only correct: 4.
- Best-only direct (grade 2): 7.
- BM25-only direct: 0.
- By split: v2 15, phase3 1, V12 0.

## Pattern

Best-only wins include atlas cards and integrated architecture pages:

- Q031 cache authority;
- Q072 index counterexamples;
- Q104 ports and adapters;
- Q111 messaging integration;
- Q119 durable workflow ownership;
- Q127 cache-first writes;
- Q154 concurrent old/new comparison.

BM25-only wins are all partial (grade 1), not direct:

- Q028, Q136, Q148, Q157.

Five best-only wins are only partial: Q001, Q041, Q043, Q133, T4-A04. Three of
the 16 were long-query reranker skips (Q001, Q072, T4-A04); one of those was
direct (Q072).

## Interpretation

The point estimate favors best mode, but 16 discordant pairs are too few for a
stable conclusion. The exact McNemar p is .0768 and the paired bootstrap CI
includes zero. This supports keeping BM25 as default and best mode optional.

## Artifacts

- [corpus-qrels.v3.json](../evaluation/corpus-qrels.v3.json)
- [qrels-v3-discordance.json](../evaluation/qrels-v3-discordance.json)
- [qrels_v3_discordance.py](../scripts/qrels_v3_discordance.py)

## Limits

- AI-adjudicated page labels.
- Page-level only; accepted sets are broad.
- 16 discordant cases are a diagnostic subset, not a random sample.
- No human review, CI, owner acceptance or sufficient coverage.
