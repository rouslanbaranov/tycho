# B50 Transactional Inbox split and metadata integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, owner acceptance or independent AI review is
claimed.

## Commit chain

- Parent: `a888c887eb8777386a10cb0e30fa53877dcbb38e` (`a888c887`).
- B50 book-binding cherry-pick: `5cc4a2f2e228b85a1917f43561c84685b4b93fcb`
  (`5cc4a2f2`), source `a2dc83009e3c472d523fee116a89021e4fb3bffb`.
- This integration: dedicated card page, shared metadata, counters and tests.

The cherry-pick applied cleanly. It contains the B50 lane note, the V04/C05
owner edits and the updated inline V11/C04 card.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c04-consistency-events/transactional-inbox.md`.
- Page identity: `tycho.page.c934153c2f6c4adc9d73a32c997be89a`.
- Page raw SHA-256:

      535a5df15ef3120109c5d3d6f89c55abd93d4b8af64a87ffd42a3b112d9a6371

- Historical-view SHA-256:

      cba5b761cef2d484767d58600bfad3db16510fa222b8fa9f92b197d31502aa1f

- Body SHA-256:

      c9bd63d2cf09d9f7cc09d5314067600e818f2f9f1a59eb01afaef65b282815e1

- README raw SHA-256:

      de0c0133203d74cbbcebb36e2e6ee5b6e65e4d5ceea68578bed65ee8d25216e8

- README historical-view SHA-256:

      82b304635925f918e12d601f8865f96c1e521a1c857ca3529ec93d58b7ec0ffc

- Owner page raw SHA-256:

      57717a5e279902f08bdd4cb58ce3cdcfc42486af260f577cdd99319ccf2f7c47

- Owner page historical-view SHA-256:

      dd36d014220aa613f42e0cb8a7f7a2e275a8f14f105d96c1e6d53cb74e683aec

- The README keeps `### Transactional Inbox` and points to the dedicated
  card. The owner backlink remains the README anchor and the card keeps the
  owner link. The owner section is level 2 at line 50.

## Applied metadata

- `sources/register.json`: 307 sources; no new source id. Microsoft,
  Kafka, PostgreSQL and Debezium gain their 2026-10-31 inbox/outbox scopes.
  The source catalogue was regenerated and has no content diff.
- `edition/patterns/reading-ledger.v1.json`: 231 -> 235 records. The four new
  records are `read.microsoft-transactional-outbox-cosmos.2026-10-31`,
  `read.kafka41-design-exactly-once.2026-10-31`,
  `read.postgresql-select-locking.2026-10-31` and
  `read.debezium-outbox-binding.2026-10-31`. The Microsoft Inbox record is
  retained unchanged.
- `edition/patterns/source-plan.v1.json`: 278/277/231 ->
  283/282/235 required/read/ledger; blocked stays 1. Five units are appended:
  the retained Microsoft Inbox unit, the Cosmos outbox guide, Kafka 4.1
  Design, PostgreSQL SELECT and Debezium Outbox Event Router.
- `edition/patterns/registry.v1.json`: six source units; the technical owner
  and technical/overall coverage move to `partial-bounded`; decision coverage
  stays `partial-bounded`.
- `edition/patterns/owner-units.v1.json`: all four dimensions are
  `supported` with one primary binding and supporting bindings each; the
  source support names the Microsoft Inbox record as primary and five
  auxiliary records. Counters: mechanism 116 -> 117, failure/recovery
  75 -> 76, alternative 80 -> 81, technical partial-bounded 15 -> 16 and
  technical partial 67 -> 66; invariant and sufficient stay unchanged.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path`; the retained idempotent-consumer record remains the primary
  cited record.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner page and README historical-view changes, plus the changed section 3
  source block. The new page baseline is its historical-view hash, so it
  needs no separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page, identity,
  baseline, documents count 505 and atlas review entry.
- Route and section indexes, census, coverage/reverse maps, phase 4, delivery
  evidence, semantic summary, qrels, inventory, sufficient candidates and
  re-review packets were refreshed. Guards move to 505 pages, 82 V11
  documents, 283 registry units, 282 read units and 235 ledger records.
- `edition/patterns/sufficient-review-records.v1.json` pins the historical
  re-review page hash for this entry, so its packet moves from
  `reviewed-by-independent-agent` to `page-changed-since-review`. Packet
  counts move to 53 reviewed and 82 page-changed.

## Deviations from the B50 note

- The note says the card remains inline; the owner request requires a dedicated
  page. The card body moves verbatim, the README keeps its stable anchor, and
  the card path is registered.
- The note proposes advancing the owner `evidence_scope` and
  `source_inspection_date`; the decomposition plan pins this page to
  `src.idempotent-consumer-pattern` and 2026-10-20. The integration keeps that
  plan-bound frontmatter so `validate_decomposition.py` and
  `validate_edition.py` pass. The four new sources remain recorded in the
  dedicated card, the ledger and the owner-unit bindings.
- Because the plan-bound frontmatter is four lines shorter than the lane
  proposal, the owner heading is at line 50, not 54. The heading text and
  anchor are unchanged.
- The content-revision hashes are the historical-view digests that
  `validate_directory_migration.py` compares, not the raw file digests shown
  in the lane note. A `source_blocks` revision authorizes the changed
  section 3 payload.
- `schemas/pattern-phase4.v1.schema.json` and
  `schemas/pattern-semantic-audit.v1.schema.json` move the page bound to 505;
  `schemas/pattern-delivery-evidence.v1.schema.json` moves the ledger count
  to 235. `delivery-evidence.v1.json` records 16 partial-bounded and 66
  partial technical entries.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.transactional-inbox`:
  PASS, 1/1.
- PASS: sources (307), source catalogue, registry, atlas (82 documents),
  coverage, cards, owner units, source plan (282 read, 235 records), directory
  migration (505 documents), edition, semantic audit (505 pages), phase 4
  (505 pages), delivery evidence, claim references, sufficient promotions,
  sufficient pilot, owner acceptance, AI reviews, page census, markdown line
  length (145 exact owner-link exceptions) and the boundary check.
- `validate_book_navigation.py` still reports four missing local anchors in
  untouched dark-launching and RBAC/ABAC pages; they are unchanged by this
  integration.
- Full suite: 688 tests pass (688 OK). An initial run found the historical
  re-review pin for this page missing; after pinning it the suite passed.

## Limits

- Partial-bounded coverage only; no Transactional Inbox promotion or owner
  acceptance.
- No external AI content review was run for this integration; the book/atlas
  review gate remains outstanding.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no benchmark, production observation or runtime experiment
  is claimed.
- The Microsoft pages publish no version identifier; Kafka is pinned to the
  4.1 Design page; PostgreSQL is the current 18 documentation; Debezium is the
  living stable page.
