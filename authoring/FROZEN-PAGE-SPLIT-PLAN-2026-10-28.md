# Frozen page split plan — 2026-10-28

These chapter pages hold promotion-bound cards. Editing the page changes the card
hash and invalidates the promotion until the moved card receives a fresh external
review. Split one page at a time; do not batch pages that carry owner-accepted entries
without a new owner decision.

| Page | Promotion-bound card | Owner decision needed | Sequence |
|---|---|---|---|
| c01 README | Sidecar | no | 1 |
| c02 README | Async Request-Reply — **done** | no | 2 |
| c05 README | Cache Invalidation | yes (accepted) | 4 |
| c09 README | Static Content Hosting | yes (accepted) | 5 |
| c10 README | Dark Launching — **done** | no | 3 |
| c04 README | Transactional Outbox | yes (accepted) | 6 |

## Per-page procedure

1. Create a dedicated `<section>.md` page and move the card section verbatim.
2. Set `card_path` in `edition/patterns/card-batches.v1.json`.
3. Rebind the reciprocal owner backlink.
4. Update atlas, directory, identities, semantic audit, phase4.
5. Run `scripts/refresh_atlas_artifacts.py --authorize "..."`.
6. Suspend the promotion and set coverage to `partial-bounded`.
7. Run a fresh external review of the moved card.
8. Restore promotion and coverage only after `pass`.
9. If the entry is owner-accepted, obtain a new owner decision after the page change.

## Why one page at a time

A failed split can be reverted without touching the other five pages, and the
promotion/review evidence stays attributable to one page hash.

## Current state

- c11 fully split;
- c01 ACL split;
- c10 Parallel Run split;
- c04/c05/c09/c01 still carry promotion-bound cards listed above;
- c02 and c10 are split, with Async and Dark on their own pages and promotions restored.
