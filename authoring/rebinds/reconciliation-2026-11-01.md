# Reconciliation rebind record — 2026-11-01

Scope: link and metadata repairs only; no new promotion.

## Registry state correction

- Registry technical `sufficient` before: 92; after: 95.
- Promotion set before: 95; after: 95 (unchanged).
- The three coverage corrections are Hexagonal Architecture, Load Balancing and Zero Trust
  Architecture; all three were already in the promotion set. No entry was promoted by this
  change.
- Event Sourcing `review_status` changed from independent-reviewed to self-checked; this is a
  review-claim downgrade, not a coverage change.
- Six owner-unit `review_state` values were changed from independent-reviewed to self-checked.
  Their DeepSeek reports still exist and their hashes still match the promotion records; the
  downgrade is conservative and does not inflate any review claim.
- Event Sourcing `decision_evidence.competing_alternative` was rewritten to match the card.
  This is decision-metadata alignment, not new source evidence.

## Owner-page and card hashes

CQRS:

- owner page `d7119460b8ac5843eec139a367186955f3e0837798f662857b41082ac9097f48` unchanged;
- card `fef6aa079be778a5bcf3690934a657de1627684a6723f545cee65711cef9d166` ->
  `cbcf867e69c5a1c61aebb795b2c14288d27a951138152cd9f57b48def8bb2d50`;
- reason: Technical owner link rebased from the legacy `../../../distributed/...` target to
  `../../v04-distributed-coordination-and-events/...`.

Server-Side Discovery and Load Balancing share `discovery-balancing.md`:

- owner page `cf4454984da07c8a5f121df8bc281268970562114d1c65ca28e2b0cfb15c1bcf` ->
  `34b139c4294d752bd8a4d4eada4deac0eacdeaaacd0d21816f3c1e86566300ce`;
- reason: page-level Load Balancing atlas link gains `#load-balancing`, matching the card H1
  anchor used by the phase4 backlink dimension.
- cards unchanged.

These are link-target changes, not format-only rebinds. They require the normal delta review;
this record does not waive it.

Delta review: `authoring/ai-reviews/2026-11-01-reconciliation-delta-deepseek.md` (pass).

## Link verification

Six link edits across eight changed files were resolved on disk; every fragment matched a
heading slug on its target page (True/True for target file and anchor).

## H1 slugs

`Publish/Subscribe` and `Blue/Green Deployment` H1 headings were changed to hyphenated forms so
the Phase 4 section extractor can bind the card section. Inbound links to the retired slugs
`#publishsubscribe` and `#bluegreen-deployment`: 0.
