# Atlas card page granularity

Status: mandatory from 2026-10-27. Owner decision: atlas cards are split by pattern or family
so a promotion pinned to one card cannot freeze neighboring cards.

## Rule

1. A V11 atlas page owns one pattern card or one family of cards. It must not be a chapter
   index that also hosts unrelated cards.
2. New or changed cards go to a dedicated page under the owning V11 chapter directory.
3. A chapter `README.md` is an index and may hold the family landing text, not promotion-bound
   cards.
4. A promotion binds the card file hash, not a chapter page shared by other patterns.
5. Editing a card page invalidates every promotion that binds that file. Neighbor isolation is
   the reason for the split, not a side effect.

## Migration debt

The following existing cards still live on shared chapter pages and are grandfathered until
split. They must not be edited in place while any card on the same page is promotion-bound.

- `book/volumes/v11-pattern-atlas/c04-consistency-events/README.md`
- `book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md`
- `book/volumes/v11-pattern-atlas/c09-scalability/README.md`
- `book/volumes/v11-pattern-atlas/c11-security-operations/README.md`

Other chapter pages with multiple cards are migration candidates. A page with exactly one
`###` card heading is already compliant.

## Split procedure

1. Create one page per card under the chapter directory; keep the chapter README as an index.
2. Move the card section without rewriting its claims.
3. Update atlas metadata, route entries, inventory, semantic audit and card page paths.
4. Re-run the external review for the moved card before retaining its promotion.
5. Update the promotion record to the new card file hash.

## Gate

A promotion whose card lives on a shared page is migration debt. It is not evidence that the
shared page is an acceptable target. New promotions must use a dedicated page.
