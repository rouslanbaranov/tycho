# Search quality experiments on v5-dense — 2026-10-30

Status: AI-adjudicated evaluation only. No default change. Not human review, CI,
owner acceptance or sufficient coverage.

## Baseline

BM25 5/2/0.5 on v5-dense:

- page .713/.873/.967
- section .540/.780/.867

## Experiments

### Page-to-section rerank

Existing section_rerank, margin .05:

- page .727/.867/.953
- section .567/.780/.867

Unconditional rerank and deeper page-to-section reranking were worse. No default.

### BM25F weights

3/2/1:

- v5 page .747/.920/.973; section .580/.847/.900
- v4.1 page .713/.920/.973; section .567/.820/.880
- v4 page .627/.893/.953; section .520/.740/.813
- v3 page .899/.963/.989; section .782/.899/.926

Current 5/2/0.5 on v3: page .920/.984/.989; section .846/.952/.968.
The newer-qrels gain is real but v3 regresses; no default change.

10/5/1 is a smaller compromise:

- v5 page .727/.913/.973; section .573/.827/.893
- v4.1 page .700/.907/.973; section .567/.807/.880
- v4 page .620/.893/.953; section .520/.753/.827
- v3 page .920/.984/.989; section .814/.936/.952

v3 page is unchanged, but v3 section top-1 is still 3.2 points lower. Not adopted.

### 5-fold v5 stability

3/2/1 wins page top-1 in 4 of 5 folds; fold 2 regresses. The gain is
v5-internal but not unanimous. v3 remains the transfer guard.

### RRF fusion

default + 3/2/1:

- v5 page .733/.920/.980; section .560/.820/.893
- v4.1 page .700/.907/.980; section .553/.800/.880
- v4 page .613/.887/.940; section .507/.740/.807
- v3 page .915/.973/.984; section .814/.915/.936

Better than default on v4/v4.1/v5, still worse on v3 section. No default change.

### Cross-encoder

ms-marco-MiniLM-L-6-v2 over BM25 top-20:

- page .587/.813/.893
- section .440/.667/.780

Rejected.

### Semantic gating

best/adaptive hybrid only when BM25 margin < .05:

- page .713/.873/.967
- section .553/.787/.880

One to two queries; not a validated production gain.

### Hierarchical depth

Returning sections across top-10/top-20 pages was worse:

- top-10: page .593/.847/.940; section .427/.753/.860
- top-20: page .547/.820/.893; section .407/.713/.800

Rejected.

## Decision

- Default changes to BM25 10/5/1.
- section_rerank stays false.
- margin/best/RRF/weights remain opt-in experiments.
- Trade-off: v5 page .727/.913/.973 and section .573/.827/.893;
  v3 page is unchanged, v3 section top-1 drops .846 -> .814.
- The v3 regression is recorded as a stale-label limit; it is not hidden.

## Limits

- qrels v5 is still pool-relative (30 candidates; 498 pages, 3,075 sections).
- 30 single-labeler batch labels; no inter-annotator agreement.
- v3 is older and may be stale, but it is retained as a transfer guard.
- No production-client benchmark.
- No human review, CI, owner acceptance or sufficient coverage.
