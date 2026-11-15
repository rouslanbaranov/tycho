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
