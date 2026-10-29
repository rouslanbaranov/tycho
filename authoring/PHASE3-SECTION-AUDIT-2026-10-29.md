# Phase3 section-level audit — 2026-10-29

Status: diagnostic on the 19 answerable phase3 queries. Not human review,
independent review, CI or owner acceptance.

## Result

| Method | section hit@1/3/5 | page hit@1/3/5 |
|---|---|---|
| BM25 | .263/.368/.526 | .421/.632/.737 |
| best | .263/.421/.579 | .421/.684/.789 |

## Interpretation

- Section top-1 is only **26.3%** for both BM25 and best.
- Page top-1 is **42.1%**: in about 16 points, the right page is returned with
  the wrong section.
- Best improves section hit@3 by 5.3 points and hit@5 by 5.3 points, but not
  section top-1.
- Page-level qrels v3 overstate production precision because the search result
  is a section citation, not a page.

This is primarily a section-selection gap, not a semantic-recall gap. The next
improvement should target within-page section choice, not another embedding
model or default change.

## Limits

- 19 queries; small sample.
- phase3 labels are agent-adjudicated, not human.
- Section ids are exact; some accepted entries may be page-level.
- No owner acceptance, CI or sufficient coverage.
