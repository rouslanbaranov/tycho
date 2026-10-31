# B54 Priority Queue split and metadata integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no promotion, owner acceptance or independent AI review is
claimed.

## Commit chain

- Parent: `65918d896c1dfdc4db39699c617fa6c29a1e0292` (`65918d89`).
- B54 book-binding cherry-pick: `7e3a381a` from source `a0e6f77a`
  (`docs(priority-queue): bind four dimensions to public sources`).
- This integration: dedicated card page, shared metadata, counters and tests.

The cherry-pick applied cleanly. It contains the B54 lane note, the V07/C05
owner edits and the expanded inline V11/C07 card.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c07-resilience/priority-queue.md`.
- Page identity: `tycho.page.e89c1693f295dde2349c93019fcd8a7f`.
- Page raw SHA-256:

      93a3f63ef7c916b9d4e81336cde7b4d6cc6976a25ae3fb06c238093fdfe3c2a8

- Historical-view SHA-256:

      1f9f28328eacfaafffbd26f53de4224b9f78759be340d2cdcfa02d20f137884c

- Body SHA-256:

      fad4e94a60017659638b29af2427ab2f058603a3c8f6b62941a437f27c3190d9

- README raw SHA-256:

      4b857991a548afc16657e05c3b67347e600472a92140fef18c77797f2b4f0d37

- README historical-view SHA-256:

      7fc3bb0e0c61db4c76cf115a38b7ad15e15e586d5cf11843fc093d9972d6004b

- Owner page raw SHA-256:

      d26824f46f210be58c78102e4f87d8a4226b670f5cdb8a27ae8689f286bb3f62

- Owner page historical-view SHA-256:

      2d7662a2e37342ad3a67ff7b8a313a6b276146549422ebea6f9310208710a484

- The card moved verbatim from the shared chapter page; the section heading
  becomes the page H1. The README keeps `### Priority Queue` and points to the
  dedicated card, so the owner backlink (`README.md#priority-queue`) and the
  card owner link both resolve. The moved card text is 63 body lines and 393
  words; the page is 121 lines with frontmatter and 532 words.
- The README drops the card-only `src.azure-service-bus-amqp` id, which now
  belongs to the dedicated page; the chapter source list keeps the ids used by
  other C07 cards.

## Applied metadata

- `sources/register.json`: 318 -> 319 sources. Added
  `src.azure-service-bus-amqp`; RabbitMQ, Microsoft Cloud Design Patterns and
  AWS SQS gain the 2026-10-31 representations, access dates and verification
  scopes. The source catalogue was regenerated.
- `edition/patterns/reading-ledger.v1.json`: 257 -> 262 records. The five new
  records are `read.rabbitmq-priority-queues.2026-10-31`,
  `read.microsoft-priority-queue-pattern.2026-10-31`,
  `read.azure-service-bus-amqp-message-mapping.2026-10-31`,
  `read.aws-sqs-queue-types.2026-10-31` and
  `read.aws-sqs-fair-queues.2026-10-31`. The retained
  `read.batch4-rabbit-priority.2026-10-21` record is marked
  `intentionally-unused` and parked as a foundation record because the card
  no longer cites it and the plan unit now points at the 2026-10-31 read.
- `edition/patterns/source-plan.v1.json`: 305/304/257 -> 309/308/262
  required/read/ledger; blocked stays 1. The existing RabbitMQ unit keeps its
  URL and section list and takes the new record; R2-R5 are appended in the
  lane order.
- `edition/patterns/registry.v1.json`: the entry gains four source units (five
  total); technical owner, atlas owner, technical coverage, decision coverage
  and overall coverage move to `partial-bounded`. Notes name the five
  bindings.
- `edition/patterns/owner-units.v1.json`: all four dimensions are
  `supported`, with one primary binding plus supporting bindings each. The
  owner line moves 179 -> 187, and `decision_evidence.competing_alternative`
  is rebased to the edited card text. `source_support.ledger_record` is the
  new RabbitMQ record; the other four records are auxiliary. Counters:
  mechanism 119 -> 120, invariant 84 -> 85, failure/recovery 79 -> 80,
  alternative 84 -> 85, technical partial-bounded 15 -> 16 and technical
  partial 63 -> 62. Decision partial-bounded stays 78 and sufficient stays 67.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and the new RabbitMQ ledger citation.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner page, README historical-view changes and the owner enrichment
  baseline/addition hashes.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page, identity,
  baseline and atlas review entry. Directory documents move to 509 and V11
  documents to 86.
- Route and section indexes, census, coverage/reverse maps, phase 4, delivery
  evidence, semantic summary, qrels, inventory, sufficient candidates and
  re-review packets were refreshed. Guards move to 509 pages, 86 V11
  documents, 309 registry units, 308 read units and 262 ledger records.
  Delivery counters move to 62 technical partial and 16 technical
  partial-bounded; decision partial-bounded stays 78.
- `edition/patterns/sufficient-review-records.v1.json` and
  `sufficient-candidates.v1.json` pin `reviewed_page_sha256` to the recorded
  `68181cf...` page, so re-review packets report
  `page-changed-since-review` rather than silently treating the changed owner
  page as reviewed. Packet counts move to 48 reviewed and 87 page-changed.

## Deviations from the B54 note

- The note leaves the card inline. The task and the card granularity policy
  require a dedicated page, so the card moves verbatim and the README keeps a
  stub link at the stable anchor.
- The note advances the owner `source_inspection_date` to 2026-10-31. The page
  is a decomposition question page, and `validate_decomposition.py` requires a
  null inspection date for pages without `fresh_source_ids`. The integration
  restores null; the 2026-10-31 inspection remains recorded in the shared
  ledger, the owner-unit bindings and the dedicated card.
- The note gives owner raw hash `4441a437...`; the null inspection date
  changes only frontmatter, so the final owner raw hash is
  `d26824f4...` and the historical-view hash is `2d7662a2...`.
- The note leaves the card-batch registration without a `card_path`. The
  integration adds it, as the task requires.
- The note quotes raw card and owner hashes for `content-revisions`. The
  repository authorizes historical-view hashes, so the revision stores
  `7fc3bb0e...` and `2d7662a2...`.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.priority-queue`: PASS, 1/1.
- PASS: sources (319), source catalogue, registry (309 units), atlas
  (86 documents), coverage, cards, owner units, source plan (308 read,
  262 records), directory migration (509 documents), edition, enrichment,
  decomposition, semantic audit (509 pages), phase 4 (509 pages), delivery
  evidence, sufficient promotions, sufficient pilot, owner acceptance, AI
  reviews, claim references, corpus qrels and page census.
- PASS: V11 prose line length, 145 exact owner-link exceptions.
- PASS: configured lexical boundary checks; independent-origin review remains
  required.
- PASS: `git diff --check` (no whitespace errors).
- `book_change.py --plan`: clean, no changed pages, missing revisions or stale
  artifacts.
- Full suite: 688 tests pass (688 OK). An earlier run failed one stale packet
  counter assertion (49 reviewed and 86 page-changed); the guard was updated to
  48 reviewed and 87 page-changed and the suite was rerun clean.

## Limits

- Partial-bounded coverage only; no Priority Queue promotion, sufficient
  coverage or owner acceptance.
- No external AI content review was run for this integration; the book/atlas
  review gate remains outstanding and the existing sufficient review is stale
  for the changed owner page.
- The integrator applied the lane's recorded revisions. No source was
  re-fetched, and no broker, queue, subscription, filter or consumer was run.
- All five units are living public documentation pages, not benchmarks,
  standards or production observations. Their digests pin the 2026-10-31
  representations, not future revisions.
- The moved card is a verbatim decomposition move plus frontmatter; the
  README stub, owner page and new page are self-checked, not independently
  reviewed.
