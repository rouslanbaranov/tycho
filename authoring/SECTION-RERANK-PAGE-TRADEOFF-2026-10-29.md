# Section rerank page tradeoff — 2026-10-29

Status: diagnostic on AI qrels v3. Not human review, independent review, CI or
owner acceptance.

## Result

Page-level hit rates:

| Split | n | BM25 hit@1/3/5 | section_rerank hit@1/3/5 |
|---|---:|---|---|
| v2 | 155 | .865/.948/.974 | **.929/.968/.974** |
| phase3 | 19 | .895/.947/.947 | **.789/.895/.947** |
| V12 | 14 | 1.000/1.000/1.000 | **.857/1.000/1.000** |
| all | 188 | .878/.952/.973 | .910/.963/.973 |

## Interpretation

- v2 improves by +6.4 points top-1 and +2.0 points top-3.
- phase3 loses 10.5 points top-1 and 5.3 points top-3.
- V12 loses 14.3 points top-1; accepted top-5 is unchanged.
- The aggregate +3.2 points is driven entirely by v2.

Section rerank is **not safe as a global default**. It must remain optional and
should be guarded or disabled for V12/phase3 until those splits have a
dedicated section review.

The section qrels improvement for phase3/V12 is therefore not a page-level win:
reranking sections can move the wrong page above the right one.

## Limits

- AI page labels and a candidate pool built from both modes.
- phase3/V12 samples are small.
- No human review, CI, owner acceptance or sufficient coverage.
