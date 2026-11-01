# B22 follow-up — Dead Letter Channel alternative source

Status: lane-local follow-up, self-checked on 2026-10-30. This note supersedes
the alternative status in `B22-DEAD-LETTER-CHANNEL-LANE-2026-10-30.md`. The
invariant work, source boundary and metadata needs in that note remain valid
except where this follow-up changes counts, hashes or the alternative state.
No shared edition metadata, promotion, generated artifact or owner acceptance
is included in this follow-up.

## Result

The parent asked for a public source that explicitly names or compares a DLQ
with at least one alternative: bounded retry without quarantine,
drop-with-record, a repair table/outbox or a parking-lot pattern. Hookdeck's
public guide "Alternatives to Dead-Letter Queues for Webhook Reliability"
explicitly frames alternatives to DLQs and compares database persistence, a
retry table and a transactional outbox with a DLQ. The alternative dimension is
now source-bound and supported. The entry is 4/4 on technical dimensions after
the integrator metadata patch; the scratch preflight passes 1/1.

The guide is webhook-specific vendor guidance. The drop-with-record variant and
the general transfer beyond webhooks remain Tycho guidance and are labelled as
such in the owner and card.

## Lane coordinates

- Parent HEAD: `83d4dd40eb9364848efdd5d0ec26256576f2fd02`.
- Branch: `b22-dlq`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b22-dlq`.
- Prior lane commit: `f0bdc23205214313decb5a2d6768a8ba2237beb0`.
- This follow-up changes the V04/C06 owner alternative and source boundary, the
  V11/C03 inline card alternative and sources, the prior lane note's status
  line and this note.
- No shared JSON, promotion or generated file is changed.

## Source binding

- Source id: `src.hookdeck-dlq-alternatives`.
- Proposed record: `read.hookdeck-dlq-alternatives.2026-10-30`; access date
  2026-10-30.
- Canonical page:
  `https://hookdeck.com/webhooks/guides/alternatives-to-dead-letter-queues`.
- Representation read: the publisher's Markdown alternate,
  `https://hookdeck.com/webhooks/guides/alternatives-to-dead-letter-queues.md`.
- Unit label:
  `Alternatives to Dead-Letter Queues for Webhook Reliability — Hookdeck`.
- Unit type: `engineering-article`.
- Raw Markdown SHA-256:
  `bd4ed76074e2d44f3eaa3e0b8b5f85fed27b00f6867b71e5ba21c439a239d1af`.
- Raw HTML SHA-256:
  `254af170075081977f458696138548eb26871d14caf2de9621c8d06cc6957179`.
- Fetch check: the HTML page and the Markdown alternate were fetched on
  2026-10-30. The HTML metadata reports `datePublished` and `dateModified`
  2026-01-28, canonical URL as above and a 2026 copyright notice. The page has
  no explicit reuse license; only short excerpts are cited and no text is
  mirrored.
- Sections read in the Markdown representation: Introduction (unlabelled),
  "The Database Persistence Pattern", "The Retry Table Pattern", "The Circuit
  Breaker Pattern", "The Transactional Outbox Pattern", "The Event Sourcing
  Approach", "The Saga Pattern", "Issue-Based Failure Management" and "Choosing
  the Right Approach".
- Exact quotes used in the owner and card:

      But DLQs aren't the only approach, and they come with operational
      overhead that many teams find burdensome.

      Instead of moving failed events to a separate queue, persist them
      directly to a database table.

      A variation of database persistence, the retry table pattern uses a
      dedicated table specifically for events that need reprocessing.

      After a maximum number of attempts, events move to a failed state for
      manual review.

      The transactional outbox pattern solves the dual-write problem: when you
      need to both update your database and send a message, failures can leave
      these out of sync.

      For high-scale systems with dedicated platform teams, traditional DLQs
      remain a solid choice.

- The guide supports database persistence, a retry table and a transactional
  outbox as explicit DLQ alternatives, plus a bounded-attempt/record path and a
  high-scale reversal. It is webhook-specific and is not a general messaging
  benchmark. It does not name drop-with-record or the parking-lot pattern.

## Book edits

### V04/C06 owner `workflow-failure.md#dead-letter-channel-dlq`

- The **Alternative** paragraph now quotes Hookdeck's database-persistence,
  retry-table, bounded-attempt and transactional-outbox sentences and the
  high-scale reversal. It states that the guide supports those alternatives and
  that the webhook-specific transfer and drop-with-record remain Tycho
  guidance.
- The **Source boundary** paragraph adds the Hookdeck Markdown hash, the four
  sections used and the vendor-guide limit; it changes "All three" to "All
  four" public sources.
- Frontmatter adds `src.hookdeck-dlq-alternatives`.
- `### Dead Letter Channel-DLQ` moves from line 198 to line 199 because of the
  added frontmatter source line. The page is 262 lines.
- Raw SHA-256:
  `79d3902dcc8c748a5c5da088bf86b5746e3326f00fed989f6440dd81a964c131`;
  historical-view SHA-256:
  `226b13187d26274dbcf41d85c0508fe29f7563f1fc5aac936f774ccb35fc634d`.

### V11/C03 inline card `### Dead Letter Channel / DLQ`

- **Competing alternative** now states that Hookdeck's guide explicitly
  compares a DLQ with database persistence, a retry table and a transactional
  outbox, and labels the webhook-specific transfer and drop variant as Tycho
  guidance.
- **Sources** adds the Hookdeck record, sections, exact quotes, revision and
  the vendor-guide limit.
- Frontmatter adds `src.hookdeck-dlq-alternatives`.
- `### Dead Letter Channel / DLQ` moves from line 377 to line 378. The chapter
  page is 620 lines.
- Raw SHA-256:
  `3748415299e486c360ab815dec8849542f5cdff04b2f08c12422ddc1f4fcefa5`;
  historical-view SHA-256:
  `bcd320685ba469073f8175903a75e72befa283d627667bd3238583ca7354a481`.

## Metadata needs (integrator)

These changes are on top of the metadata needs in the first lane note. The
first note's AWS/Azure and invariant values remain valid. The changes below
supersede its alternative state, counts and hashes.

### Source register `sources/register.json`

Add `src.hookdeck-dlq-alternatives` and keep `updated` at 2026-10-30.

- Title "Alternatives to Dead-Letter Queues for Webhook Reliability";
  category "messaging"; publisher "Hookdeck"; kind "engineering-article"; URL
  and resolved URL as the canonical HTML page above; topics
  `["messaging", "integration", "failure"]`; priority "supporting"; planned
  use "Explicit vendor guide comparison of DLQs with database persistence,
  retry table and transactional outbox."; admission "admitted-for-research";
  access "public-web-or-author-download"; reading status
  "full-public-page-inspected"; version names the 2026-01-28 publication and
  modification dates and the Markdown hash; `access_checked` and
  `content_verified` 2026-10-30; license note "Public vendor guide; no explicit
  reuse license found on the page; cite short excerpts and paraphrase; do not
  mirror."; verification scope names the complete Markdown alternate and
  excludes linked pages, images and the HTML rendering; observed title as
  above.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add `read.hookdeck-dlq-alternatives.2026-10-30`.

- Source `src.hookdeck-dlq-alternatives`; unit URL as the canonical HTML page;
  unit label and type as above; access date 2026-10-30; access method names
  the public Markdown alternate and raw-byte hashing; `sections_read` is the
  nine-section list above; `sections_not_read` names linked pages, images and
  the HTML rendering; one tables/figures note says the article is prose with
  lists; license note as above; `claims_supported` contains the six quotes
  above; `claims_not_supported` names drop-with-record, the parking-lot
  pattern, a general non-webhook comparison, linked pages/images and
  independent reproduction; limitations names the webhook-specific vendor
  scope, the Markdown representation and the absence of a benchmark or
  execution; `content_sha256` is the Markdown hash; `read_scope` is the
  complete Markdown alternate; reviewer "Automated authoring agent"; status
  "read".

### Source plan `edition/patterns/source-plan.v1.json`

Append one unit to `tycho.pattern.dead-letter-channel-dlq` after the EIP, AWS
and Azure units:

- `src.hookdeck-dlq-alternatives`: unit
  "Alternatives to Dead-Letter Queues for Webhook Reliability — Hookdeck";
  unit type `engineering-article`; URL as the canonical HTML page; sections
  the nine-section list above; status `read`; read record
  `read.hookdeck-dlq-alternatives.2026-10-30`; blocked reason null.

Set `summary.required_units` 177 -> 178, `summary.read_units` 176 -> 177 and
`summary.ledger_records` 146 -> 147. Set `updated` to 2026-10-30. Recompute
`registry_sha256` after saving the registry; the scratch serialization
produced `66bd7f4c2e02ccaca8ce89e51b143677711074d57e4398f535a1f095ecc4a097`,
but the authoritative value is the SHA-256 of the saved registry file.

### Registry `edition/patterns/registry.v1.json`

Entry `tycho.pattern.dead-letter-channel-dlq`:

- Append the Hookdeck source unit with the exact source-plan label and status
  `read`.
- Keep `technical_owner.state`, `coverage.technical` and `coverage.overall`
  at `partial-bounded`.
- Replace the notes with: "Phase 3 C03 card; bounded owner section and backlink
  are self-checked, not independent-reviewed or sufficient. All four technical
  dimensions bound 2026-10-30: invariant EIP/AWS/Azure, alternative Hookdeck
  database persistence/retry table/outbox, failure/recovery EIP SQS example.
  Coverage partial-bounded."

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.dead-letter-channel-dlq`:

- Set `owner.line` to 199. Set
  `tycho.pattern.correlation-identifier.owner.line` to 175, because the shared
  page has one more frontmatter source line than the first lane note assumed.
- Keep the invariant block from the first lane note: AWS primary binding,
  EIP/Azure supporting bindings, state `supported`.
- Change `technical_evidence.alternative.state` from `partial` to
  `supported`.
  - `quote`: "Instead of moving failed events to a separate queue, persist
    them directly to a database table."
  - `binding`: `src.hookdeck-dlq-alternatives`, record
    `read.hookdeck-dlq-alternatives.2026-10-30`, section "The Database
    Persistence Pattern", quote as above, revision
    `bd4ed76074e2d44f3eaa3e0b8b5f85fed27b00f6867b71e5ba21c439a239d1af`.
  - Add supporting bindings for the retry-table description and the
    maximum-attempts sentence ("The Retry Table Pattern"), the transactional
    outbox sentence ("The Transactional Outbox Pattern") and the high-scale
    reversal ("Choosing the Right Approach"). Add the existing AWS retry-bound
    and Azure reason/description bindings as supporting alternatives. All
    Hookdeck bindings use the revision above.
  - `reason`: state that Hookdeck explicitly compares a DLQ with database
    persistence, a retry table and a transactional outbox and states the
    high-scale reversal; AWS supports the bounded retry setting and Azure the
    diagnostic record; the guide is webhook-specific and drop-with-record plus
    general transfer remain Tycho guidance.
- Add `source_support.auxiliary` for the Hookdeck record and revision.
- Set `decision_evidence.competing_alternative` to the exact new card field:
  "Bounded retry with backoff and an audit record, then alert and stop; drop
  with a recorded disposition or park the work in a repair table/outbox when
  failure is deterministic. Hookdeck's alternatives guide explicitly compares
  a DLQ with database persistence, a retry table and a transactional outbox;
  the guide is webhook-specific, so the drop variant and general transfer are
  Tycho guidance. Reverse the choice when replay is frequent and needs
  automated policy."
- Replace `notes` with: "All four technical dimensions are source-bound:
  invariant EIP/AWS/Azure, alternative Hookdeck database persistence/retry
  table/outbox, failure/recovery EIP SQS example. Drop-with-record and general
  webhook transfer remain Tycho guidance. Coverage partial-bounded; no
  promotion."
- In `shared_pages`, entry for the workspace owner path: keep
  `bounded_entries` at 2.
- Summary: `alternative_supported` 63 -> 64. The first lane note's changes
  remain: `invariant_supported` 64, `technical_partial_bounded` 23,
  `technical_partial` 86. No other counter changes.

### Content revisions `edition/content-revisions.json`

Update the issue-540 revision's hashes:

- Owner current historical-view
  `226b13187d26274dbcf41d85c0508fe29f7563f1fc5aac936f774ccb35fc634d`.
- Card current historical-view
  `bcd320685ba469073f8175903a75e72befa283d627667bd3238583ca7354a481`.
- Enrichment baseline old path `book/volumes/v04/c06/workflow-failure.md`,
  previous
  `af17efd0504d1f80bdc828244a08f7f4cead6241a6a9eb69fc97359c40c3276d`,
  current
  `0c35908899bb3250c2ef0da98813f9c0a4817b34614908d9981a6889bea8e253`.
- The addition hash is unchanged at
  `43b1a833e22e1d978ac621f12bbea820622a8deca1afc160e9692f47985b6039`
  and is already authorized.
- The directory previous values remain the migration baselines in the first
  lane note.

### Card path

The card remains inline and `card_path` is still missing. The scratch
preflight below uses a temporary pointer to the V11/C03 `README.md`; that is
not a split or a real registration. The integrator must split or explicitly
register the inline path.

## Validation

After these book edits only, the lane worktree still has the expected shared
metadata failures: owner units see stale lines, source plan/ledger lack the
new units and preflight sees the stale metadata. The line and boundary checks
remain:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still required.

In a detached scratch copy with the full metadata patch, including the first
lane note's AWS/Azure/invariant changes and this follow-up's Hookdeck
alternative, and a scratch-only `card_path` pointing at the V11/C03
`README.md`:

    PASS: tycho.pattern.dead-letter-channel-dlq
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: source plan 145 entries; 177 read; 147 ledger records
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: 11 volumes, 82 chapters, 476 canonical documents
    PASS: enrichment explicit membership and byte conservation

Derived atlas, coverage and semantic-audit artifacts still need regeneration
because their hashes were not refreshed. The scratch `card_path` is a check
only.

## Limits

Hookdeck is a vendor engineering guide focused on webhook reliability, not a
general messaging standard or a benchmark. Its comparison supports database
persistence, a retry table and a transactional outbox as DLQ alternatives, a
bounded-attempt/record path and a high-scale reversal. The webhook-specific
transfer, drop-with-record and any parking-lot generalization remain Tycho
guidance. No broker, queue, retry, outbox, replay or repair behavior was
executed. Coverage remains `partial-bounded`; independent review, promotion
and owner acceptance are not claimed.

## Commit scope

The follow-up commit contains this note, the prior lane note's status notice,
and the two book files. No shared JSON, promotion or generated file is in the
commit.
