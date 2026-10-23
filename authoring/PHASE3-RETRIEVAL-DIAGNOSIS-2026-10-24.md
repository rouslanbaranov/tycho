# Phase 3 retained-answerable retrieval diagnosis — 2026-10-24

Status: diagnostic only. No retrieval code change was merged. Human review of the
9-item sample remains pending.

## What was measured

Filtered phase-3 answerable set: 19 items.

| Split | Page hit@5 | Section hit@5 |
|---|---:|---:|
| Dev (T1-T3) | 11/13 | 7/13 |
| Held-out (T4-T6) | 4/6 | 3/6 |
| All | 15/19 | 10/19 |

Page retrieval is much better than exact H2 retrieval: most misses are
same-page or H3-support cases, not complete page misses.

## Diagnosed causes

- The FTS index contains only H2 sections. H3 owner notes are inside the H2
  body, so BM25 can dilute a short supporting passage.
- Search returns one best section per document; a second H2 on the same page is
  discarded before the user sees it.
- Several questions name an external source (Azure, ZooKeeper, MongoDB, Google
  SRE) while the accepted Tycho support is a generic mechanism section.
- Some accepted sections are owner-note H2s; question terms match a different
  page section more strongly.

## Experiments that did not ship

1. Passage reranking before dedupe, coverage-only:
   - alpha 0.25: qrels v2 held-out section hit@5 0.787 vs 0.800 baseline;
   - phase-3 held-out 0.667 vs 0.500, but the overall result regressed.
2. Heading-aware reranking (alpha 0.1-0.3): 70-71/94 versus 70/94 baseline;
   no meaningful gain.
3. Two sections per page: 71/94 versus 70/94; not enough to justify redundant
   results.

These are challenge-set experiments; none justify changing the default.

## Recommended next step

Implement an H3/passage index with an explicit parent-H2 mapping:

- index H3 passages for matching and ranking;
- return the parent H2 as the public citation/section;
- keep the H3 section_key for bounded reads;
- dedupe at the parent-H2 level without discarding the best H3 passage;
- evaluate on qrels v2 dev/held plus phase 3, without tuning the refusal gate.

Until that exists, do not tune the gate on phase 3 and do not claim that
retrieval is fixed.

## Limits

- 19 answerable items are a small diagnostic set.
- Phase 3 is agent-authored/agent-adjudicated, not human review.
- The 9-item human sample is pending, not passed.
- No CI, owner acceptance or sufficiency claim.
