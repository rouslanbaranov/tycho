# Domain-tuned semantic retrieval — negative result, 2026-11-15

Status: domain tuning and hard-query attempts completed; none improved BM25.
No semantic/reranker path is enabled or merged.

## Baseline BM25 (v5-dense)

- page hit@1/3/5: 0.720 / 0.900 / 0.973; MRR 0.822
- section hit@1/3/5: 0.567 / 0.820 / 0.893; MRR 0.704

## Domain tuning

- domain cross-encoder trained on v2 (815 pairs): v5 page hit@1 0.433,
  section hit@1 0.313; worse than BM25.
- domain bi-encoder trained on 155 v2 query/positive pairs:
  semantic page hit@1 0.627, section hit@1 0.467; hybrid page hit@1 0.653;
  all worse than BM25.
- BGE-small, MiniLM and potion-8M/32M chunk retrieval: page hit@5 0.69-0.75,
  section hit@5 0.61-0.71; worse.

## Hard query set

Two 32-query sets were attempted:

1. paraphrases without source reading: BM25 page hit@5 0.188, semantic 0.062;
2. source-grounded paraphrases: BM25 page hit@5 0.125, semantic 0.000.

The failure shows the hard set was not answerable by the copied accepted
sections: the paraphrases drifted from the original information need, or the
accepted section did not support the new wording. These sets are invalid as
qrels, not evidence against semantic retrieval.

## Conclusion

A genuine semantic test needs a **human-validated lexical-mismatch qrels set**
(question, accepted sections, answerability) and a domain-tuned model with
more than 155 training pairs. Without that, the current evidence is:

- BM25 is strong on v5-dense;
- all available semantic/reranker variants are worse;
- AI-generated hard qrels are not reliable enough to prove a semantic gain.

No merge. The experimental code remains on
`feature/TYCHO-1077-domain-tuned-semantic-retrieval`.

## Source-grounded hard set

Twenty questions were written from exact H2 section text; accepted_section was
the section used to write the question. Mean query-term overlap with that
section was 0.483 (range 0.297-0.655), so this is not a purely lexical set.

| Method | page hit@1/3/5 | section hit@1/3/5 | MRR page/section |
|---|---|---|---|
| BM25 | 0.650/0.700/0.800 | 0.600/0.650/0.750 | 0.706/0.647 |
| domain MiniLM semantic | 0.450/0.600/0.650 | 0.450/0.550/0.650 | 0.556/0.531 |
| MiniLM semantic | 0.450/0.600/0.650 | 0.450/0.550/0.650 | 0.548/0.526 |
| potion-8M semantic | 0.150/0.250/0.400 | 0.150/0.250/0.400 | 0.253/0.249 |
| hybrid domain 0.25 | 0.550/0.650/0.800 | 0.500/0.550/0.700 | 0.630/0.555 |

BM25 remains better at every rank. The hybrid matches page hit@5 but loses
top-1 and section ranking. Twenty queries give wide confidence intervals; no
statistically defensible semantic gain is present.

Bootstrap 95% CIs (2000 resamples, 20 hard queries):

- BM25 page hit@1 0.65 (0.45-0.85), hit@5 0.80 (0.55-0.90), MRR 0.70 (0.49-0.88)
- domain semantic page hit@1 0.45 (0.25-0.65), hit@5 0.65 (0.45-0.85),
  MRR 0.554 (0.375-0.746)

The CIs overlap; no statistically defensible improvement.
