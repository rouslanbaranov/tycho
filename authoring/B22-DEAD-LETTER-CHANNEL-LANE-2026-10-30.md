# B22 — Dead Letter Channel / DLQ invariant and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and failure/recovery were supported;
invariant and alternative were partial. This lane binds the invariant to three
public units and labels the alternative as Tycho guidance because those units do
not compare the listed alternatives. After the integrator metadata patch the
entry is 3/4: invariant supported, alternative still partial. Promotion is not
claimed or ready on the current preflight rule.

## Lane coordinates

- Parent HEAD: `83d4dd40eb9364848efdd5d0ec26256576f2fd02` ("feat(research):
  promote Idempotent Receiver").
- Branch: `b22-dlq`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b22-dlq`.
- Scope: the V04/C06 owner section `### Dead Letter Channel-DLQ` and the inline
  V11/C03 card `### Dead Letter Channel / DLQ` only.
- The card remains inline in the V11/C03 `README.md`; the integrator owns the
  split and the `card_path` registration.
- Single-entry lane; no other entry, shared owner page, promotion or generated
  file is changed.

## Candidate evaluation

- Enterprise Integration Patterns, Dead Letter Channel:
  `https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html`.
  The existing record `read.batch2-dlq.2026-10-21` covers the served Problem
  and Solution text, the Amazon SQS example and Kafka Connect. It is
  publisher-abridged. It states that a message the system "cannot or should not
  deliver" may move to a Dead Letter Channel, but it does not separate transient
  from permanent failure or compare quarantine with bounded retry, drop or a
  repair table/outbox.
- AWS, "Using dead-letter queues in Amazon SQS":
  `https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/` +
  `sqs-dead-letter-queues.html` (concatenate).
  Selected because it states the receive-count bound, retention guidance,
  redrive and diagnostic use. It describes SQS, not a vendor-neutral
  alternative comparison.
- Microsoft Learn, "Overview of Service Bus dead-letter queues":
  `https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues`.
  Selected because it states the DLQ purpose, the maximum-delivery-count
  transition, the dead-letter reason and description fields, application-level
  rejection of malformed or unauthenticated messages, and correction/resubmit.
  It describes Service Bus, not a vendor-neutral alternative comparison.
- No selected unit names bounded retry without quarantine, drop with a record or
  a repair table/outbox as a competing choice. The alternative dimension is not
  promoted to a source claim; the owner and card label it Tycho guidance.

## Source binding

### EIP (existing unit)

- Source id: `src.enterprise-integration`.
- Record: `read.batch2-dlq.2026-10-21`; access date 2026-10-21.
- Unit: Dead Letter Channel — pattern page.
- Revision in the ledger: `714f6babd327e622695d9be989c93c704d23b034cb2e0fcc1065a0eaa203a278`.
  This is the served raw-page SHA-256 in the existing record; the current
  canonical extracted-text SHA-256 is
  `dfa480fbec13efc811bfe8726f7b3112be1444f8c58eb9b623fe532ff106c03f`
  because the extraction includes navigation chrome. No new EIP record is
  created.
- Exact quote used in the owner section:

      When a messaging system determines that it cannot or should not deliver a
      message, it may elect to move the message to a Dead Letter Channel.

  The served text has one link-adjacent space before the terminal period
  ("Dead Letter Channel ."). The book quote normalizes that single space; it
  changes no word.
- Section: "Solution (unlabelled)".
- Limits: publisher-abridged; requeue, replay, ownership, retention and alerting
  are not stated.

### AWS SQS (new unit)

- Proposed source id: `src.aws-sqs-dlq`.
- Proposed record: `read.aws-sqs-dlq.2026-10-30`; access date 2026-10-30.
- URL:
  `https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/` +
  `sqs-dead-letter-queues.html` (concatenate).
- Unit label: `Using dead-letter queues in Amazon SQS — Amazon Simple Queue Service`.
- Unit type: `documentation-page`.
- Canonical text SHA-256:
  `c6142288904155bbd99a057145c632195aa76ab86aa939a38a9f0825f3c7e74b`.
- Raw HTML SHA-256:
  `de132a6ead70785842ddd73915323a5817260938c0792eddafb49fcb0f3b5be6`.
- Fetch check: two public HTTPS GETs on 2026-10-30 served identical 18,560-byte
  representations and produced the same canonical and raw hashes. The response
  reported `Last-Modified: Fri, 30 Oct 2026 01:54:13 GMT` and an ETag. The page
  publishes no version identifier; the canonical hash pins this representation.
- Sections read: "Using dead-letter queues in Amazon SQS", "Using policies for
  dead-letter queues" and "Understanding message retention periods for
  dead-letter queues".
- Sections not read or not used as evidence: linked child pages (configure a
  dead-letter queue, redrive, CloudWatch alarms), images, navigation chrome and
  code samples (none on the page).
- Exact quotes used in the owner or card:

      The maxReceiveCount is the number of times a consumer can receive a
      message from a source queue before it is moved to a dead-letter queue.

      To ensure that your system is resilient against errors, set the
      maxReceiveCount high enough to allow for sufficient retries.

      Move messages out of the dead-letter queue using dead-letter queue
      redrive.

      Thus, it is a best practice to always set the retention period of a
      dead-letter queue to be longer than the retention period of the original
      queue.

- Limits: SQS-specific behavior and configuration; no queue, redrive or alarm
  was executed; no general comparison of DLQ alternatives.

### Azure Service Bus (new unit)

- Proposed source id: `src.azure-service-bus-dlq`.
- Proposed record: `read.azure-service-bus-dlq.2026-10-30`; access date
  2026-10-30.
- URL:
  `https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues`.
- Unit label: `Overview of Service Bus dead-letter queues — Azure Service Bus`.
- Unit type: `documentation-page`.
- Canonical text SHA-256:
  `200c9ae3c042cab7a8852b33cda0214c14b5eab177a04f2bdcc02ae665005600`.
- Raw HTML SHA-256:
  `3253ad11305030fe4d021c3ad700162289865184cfe864af54582b52a65a95a7`.
- Fetch check: two public HTTPS GETs on 2026-10-30 served identical 67,574-byte
  representations and produced the same canonical and raw hashes. The page
  reports `ms.date` 2026-07-16, `updated_at` 2026-07-22 and
  `document_version_independent_id`
  `19d4a83e-55c8-8b9c-38a0-0e9a26ba2cdb`; it publishes no semantic version.
- Sections read: "The dead-letter queue", "Moving messages to the DLQ",
  "Maximum delivery count" and "Application-level dead-lettering".
- Sections not read or not used as evidence: path/transfer-path sections, DLQ
  message count, settlement, auto-forward and send-via scenarios, receive
  procedures, "Why did my message go to the dead-letter queue?", related
  content, linked child pages, images and sample code.
- Exact quotes used in the owner or card:

      The purpose of the dead-letter queue is to hold messages that can't be
      delivered to any receiver, or messages that couldn't be processed.

      When the delivery count exceeds the limit, the message is moved to the
      DLQ.

      The following two properties (dead-letter reason and dead-letter
      description) are added to dead-lettered messages.

      Unacceptable messages can include messages that can't be properly
      processed because of any sort of system issue, messages that hold
      malformed payloads, or messages that fail authentication when some
      message-level security scheme is used.

      An application might let a user correct issues and resubmit the message.

      There's no automatic cleanup of the DLQ. Messages remain in the DLQ until
      you explicitly retrieve them from the DLQ and complete the dead-letter
      message.

- Limits: Service Bus-specific behavior; no broker, repair or replay test was
  executed; no general comparison of DLQ alternatives.

## Book edits

### V04/C06 owner `workflow-failure.md#dead-letter-channel-dlq`

- Rewrites the bounded DLQ section around an explicit **Invariant** paragraph:
  retry exhaustion or permanent failure moves a message into a declared
  quarantine with diagnostic context. It quotes the EIP, AWS and Azure
  sentences above.
- Labels the transient/permanent/unknown classification as Tycho guidance.
- Keeps the existing retry, replay and ownership paragraph.
- Adds an **Alternative** paragraph that names bounded retry with audit, drop
  with a record and a repair table/outbox, quotes the AWS retry bound and the
  Azure reason/description and resubmit sentences, and labels the comparative
  choice and reversal condition as Tycho guidance.
- Adds a **Source boundary** paragraph with the three records, revisions,
  sections and limits.
- Frontmatter adds `src.aws-sqs-dlq` and `src.azure-service-bus-dlq`; advances
  `content_review.reviewed_at`, `updated_at` and `source_inspection_date` to
  2026-10-30; the reviewer becomes "Automated authoring agent".
- `### Dead Letter Channel-DLQ` moves from line 196 to line 198 because of the
  two added frontmatter source lines. The page is 253 lines.
- Raw SHA-256:
  `e73a238a31ffe248979326a59f4d1724fcb045e8dfc777311f0abc6c94c7e38c`;
  historical-view SHA-256:
  `4d6efa8ad6758d01869360771e4580e213f9f2aa9f4be7e684b03f59e9b3174f`.

### V11/C03 inline card `### Dead Letter Channel / DLQ`

- **Competing alternative** now names bounded retry with an audit record, drop
  with a recorded disposition and a repair table/outbox, and labels the
  comparison and reversal condition as Tycho guidance.
- **Failure and recovery** now names the Azure no-cleanup rule and AWS
  retention/redrive instead of only a generic warning.
- **Sources** adds the AWS and Azure records, sections, exact quotes,
  revisions and the public-documentation limit in addition to the existing EIP
  record.
- Frontmatter adds `src.aws-sqs-dlq` and `src.azure-service-bus-dlq`; the
  2026-10-30 review, update and inspection dates are already current.
- `### Dead Letter Channel / DLQ` moves from line 375 to line 377. The chapter
  page is 607 lines.
- Raw SHA-256:
  `6f659fbd215f0488079f1f0009715be5926bcb757c88f0bdd492afdf811e0068`;
  historical-view SHA-256:
  `6f7750d0dfe6a625f2143170a4c8b00eab447b461bf867e4a7dae077bf944238`.

No other book file, edition JSON, promotion or generated file is changed by this
lane.

## Metadata needs (integrator)

The following patch was exercised in a detached scratch copy of this worktree,
not in the lane commit. It produced the validation results in the next section.

### Source register `sources/register.json`

Add two source records and set `updated` to 2026-10-30.

- `src.aws-sqs-dlq`: title "Using dead-letter queues in Amazon SQS";
  category "messaging"; publisher "Amazon Web Services"; kind
  "official-docs"; URL and resolved URL as above; topics
  `["messaging", "integration", "failure"]`; priority "core"; planned use
  "Dead-letter queue retry bounds, retention, redrive and diagnostic evidence.";
  admission "admitted-for-research"; access "public-web-or-author-download";
  reading status "selected-sections-inspected"; version must name the
  2026-10-30 access, canonical hash, 2026-10-30 Last-Modified and no published
  version identifier; `access_checked` and `content_verified` 2026-10-30;
  license note "Public AWS documentation; cite short excerpts and paraphrase;
  do not mirror."; verification scope must name the three sections read and
  exclude linked pages, images and navigation; observed title
  "Using dead-letter queues in Amazon SQS - Amazon Simple Queue Service".
- `src.azure-service-bus-dlq`: title "Overview of Service Bus dead-letter
  queues"; category "messaging"; publisher "Microsoft Learn"; kind
  "official-docs"; URL and resolved URL as above; topics
  `["messaging", "integration", "failure"]`; priority "core"; planned use
  "Service Bus dead-letter purpose, delivery-count bound, diagnostic fields and
  application-level rejection."; admission "admitted-for-research"; access
  "public-web-or-author-download"; reading status
  "selected-sections-inspected"; version must name the 2026-10-30 access,
  canonical hash, `ms.date` 2026-07-16, `updated_at` 2026-07-22 and the
  document version id; `access_checked` and `content_verified` 2026-10-30;
  license note "Public Microsoft Learn documentation; cite short excerpts and
  paraphrase; do not mirror."; verification scope must name the four sections
  read and exclude linked pages, images and navigation; observed title
  "Service Bus Dead-Letter Queues - Azure Service Bus | Microsoft Learn".

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add two records and keep `updated` at 2026-10-30.

- `read.aws-sqs-dlq.2026-10-30`: source `src.aws-sqs-dlq`; URL and unit
  label as above; unit type `documentation-page`; access date 2026-10-30;
  access method names public HTTPS GET, `scripts/source_content_hash.py` and
  the two identical 18,560-byte fetches; `sections_read` is exactly the
  source-plan list below; `sections_not_read` names linked child pages,
  images/navigation and code samples; one tables/figures note says no table or
  figure was used; license note as above; `claims_supported` contains the four
  AWS quotes above plus the intro claim "Amazon SQS supports dead-letter queues
  (DLQs), which source queues can target for messages that are not processed
  successfully." and the log-diagnosis sentence "Examine logs for exceptions
  that might have caused messages to be moved to a dead-letter queue.";
  `claims_not_supported` names a general DLQ-alternative comparison,
  application behavior/throughput, linked pages/redrive implementation and
  independent reproduction; limitations names the living page, Last-Modified,
  hash pin and no execution; `content_sha256` is the canonical hash;
  `read_scope` names the three sections and excludes linked pages/images;
  reviewer "Automated authoring agent"; status "read".
- `read.azure-service-bus-dlq.2026-10-30`: source
  `src.azure-service-bus-dlq`; URL and unit label as above; unit type
  `documentation-page`; access date 2026-10-30; access method names public
  HTTPS GET, `scripts/source_content_hash.py` and the two identical
  67,574-byte fetches; `sections_read` is exactly the source-plan list below;
  `sections_not_read` lists the path/transfer, settlement, auto-forward,
  send-via, receive and why-did-it-go sections plus related content and linked
  pages/images; one tables/figures note says the dead-letter reason table was
  read in text form and not reproduced; license note as above;
  `claims_supported` contains the six Azure quotes above;
  `claims_not_supported` names a general DLQ-alternative comparison, a complete
  repair/outbox/drop policy, application behavior, linked pages/sample code and
  independent reproduction; limitations names the living page, dates,
  document version id and hash pin; `content_sha256` is the canonical hash;
  `read_scope` names the four sections and excludes linked pages/images;
  reviewer "Automated authoring agent"; status "read".

### Source plan `edition/patterns/source-plan.v1.json`

Append these two units to `tycho.pattern.dead-letter-channel-dlq`, after the
existing EIP unit and in this order:

- `src.aws-sqs-dlq`: unit "Using dead-letter queues in Amazon SQS — Amazon
  Simple Queue Service"; unit type `documentation-page`; URL above; sections
  `["Using dead-letter queues in Amazon SQS", "Using policies for dead-letter
  queues", "Understanding message retention periods for dead-letter queues"]`;
  status `read`; read record `read.aws-sqs-dlq.2026-10-30`; blocked reason
  null.
- `src.azure-service-bus-dlq`: unit "Overview of Service Bus dead-letter
  queues — Azure Service Bus"; unit type `documentation-page`; URL above;
  sections `["The dead-letter queue", "Moving messages to the DLQ", "Maximum
  delivery count", "Application-level dead-lettering"]`; status `read`; read
  record `read.azure-service-bus-dlq.2026-10-30`; blocked reason null.

Set `summary.required_units` 175 -> 177, `summary.read_units` 174 -> 176 and
`summary.ledger_records` 144 -> 146. `summary.planned_units` stays 0 and
`summary.blocked_units` stays 1. Set `updated` to 2026-10-30. Recompute
`registry_sha256` after saving the registry; the scratch serialization
produced `f5afa09496deacc630f079c99c1c7b53ad9aa999295ba50a3fef078e0ae96f21`,
but the authoritative value is the SHA-256 of the saved registry file.

### Registry `edition/patterns/registry.v1.json`

Entry `tycho.pattern.dead-letter-channel-dlq`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to `partial-bounded`;
  `coverage.decision` and `atlas_owner.state` stay `partial-bounded`.
- Append the two source units with the exact source-plan unit labels and status
  `read`.
- Replace the notes with: "Phase 3 C03 card; bounded owner section and backlink
  are self-checked, not independent-reviewed or sufficient. Invariant bound
  2026-10-30 to EIP, AWS SQS and Azure Service Bus; alternative remains partial
  because the pages do not compare drop/repair alternatives. Coverage
  partial-bounded."

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.dead-letter-channel-dlq`:

- Set `owner.line` to 198. Set
  `tycho.pattern.correlation-identifier.owner.line` to 174, because the shared
  page's frontmatter grew by two lines.
- Set `technical_evidence.invariant.state` to `supported`.
  - `quote`: "The maxReceiveCount is the number of times a consumer can
    receive a message from a source queue before it is moved to a dead-letter
    queue."
  - `binding`: `src.aws-sqs-dlq`, record
    `read.aws-sqs-dlq.2026-10-30`, section "Using policies for dead-letter
    queues", quote as above, revision
    `c6142288904155bbd99a057145c632195aa76ab86aa939a38a9f0825f3c7e74b`.
  - Add four supporting bindings: EIP "Solution (unlabelled)" with the
    cannot/should-not-deliver quote and revision
    `714f6babd327e622695d9be989c93c704d23b034cb2e0fcc1065a0eaa203a278`;
    Azure "The dead-letter queue" with the purpose quote; Azure "Maximum
    delivery count" with the delivery-count quote; Azure
    "Application-level dead-lettering" with the malformed-payload/auth quote.
    All Azure revisions are `200c9ae3c042cab7a8852b33cda0214c14b5eab177a04f2bdcc02ae665005600`.
  - `reason`: state that AWS supports the receive-count bound, EIP supports
    cannot/should-not-deliver, and Azure supports the purpose, delivery-count
    and malformed-payload/authentication cases; classifying each outcome as
    transient, permanent or unknown remains Tycho guidance.
- Set `technical_evidence.alternative.state` to `partial` (not supported).
  - `quote`: "To ensure that your system is resilient against errors, set the
    maxReceiveCount high enough to allow for sufficient retries."
  - Add the AWS binding at "Using policies for dead-letter queues" with
    revision `c6142288904155bbd99a057145c632195aa76ab86aa939a38a9f0825f3c7e74b`.
  - Add two Azure supporting bindings: "Moving messages to the DLQ" for the
    dead-letter reason/description sentence and "The dead-letter queue" for
    correction/resubmission; revision
    `200c9ae3c042cab7a8852b33cda0214c14b5eab177a04f2bdcc02ae665005600`.
  - `reason`: state that AWS supports a bounded retry count and Azure supports
    a diagnostic record and correction/resubmission inside the DLQ mechanism;
    neither page compares a DLQ with bounded retry without quarantine, drop
    with a record or a repair table/outbox, so those alternatives and the
    reversal condition remain Tycho guidance.
- Add `source_support.auxiliary` entries for both new records and revisions.
- Change `technical_coverage` from `partial` to `partial-bounded`.
- Set `decision_evidence.competing_alternative` to the exact new card field:
  "Bounded retry with backoff and an audit record, then alert and stop; drop
  with a recorded disposition or park the work in a repair table/outbox when
  failure is deterministic. The public DLQ pages describe retry limits and
  diagnostic fields, not these comparisons; the alternatives and the reversal
  condition are Tycho guidance. Reverse the choice when replay is frequent and
  needs automated policy."
- Replace `notes` with: "Poison-work subsection binds retry
  exhaustion/permanent failure to EIP, AWS SQS and Azure Service Bus; bounded
  retry and a diagnostic record are source-stated, while drop-with-record and
  repair-table/outbox alternatives remain Tycho guidance. Coverage
  partial-bounded; no promotion."
- In `shared_pages`, entry for the workspace owner path: set
  `bounded_entries` from 1 to 2. The shared-page decision stays `deepen`.
- Summary changes: `invariant_supported` 63 -> 64,
  `technical_partial_bounded` 22 -> 23, `technical_partial` 87 -> 86.
  No other counter changes; `alternative_supported` stays 63 and
  `technical_sufficient` stays 36.

### Card path `edition/patterns/card-batches.v1.json`

The card is still inline in the V11/C03 `README.md`, so the entry has no
`card_path` and preflight reports it missing. The integrator must either split
the card to a dedicated page and register its `card_path`, or explicitly
register the inline chapter path. A split card must keep both new source ids in
`evidence_scope.source_ids` and the 2026-10-30 dates. No split is performed by
this lane.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B22 dead-letter channel source binding".

- `directory_documents`:
  - Owner path, previous `d050a75f68a18dbfca34eb0a998da64a7076210f96cd6e22468da56d6160fdc1`
    (migration baseline), current
    `4d6efa8ad6758d01869360771e4580e213f9f2aa9f4be7e684b03f59e9b3174f`
    (historical-view text after link rewriting).
  - Card path, previous
    `6019fa28b483a027dc816d6797dd20564c2dc1c8665f1112c66fb34984a84c80`
    (migration baseline), current
    `6f7750d0dfe6a625f2143170a4c8b00eab447b461bf867e4a7dae077bf944238`
    (historical-view text after link rewriting).
- `enrichment_baselines`:
  - The manifest uses the pre-migration path
    `book/volumes/v04/c06/workflow-failure.md`, not the current path.
  - Previous `af17efd0504d1f80bdc828244a08f7f4cead6241a6a9eb69fc97359c40c3276d`,
    current
    `36bdc38a0359b8b376bf8b1339030d58c0727e340880b4dfcf8b0c2eb6f2da55`.
- Leave `source_blocks`, `enrichment_documents` and
  `enrichment_additions` empty. The addition hash is unchanged at
  `43b1a833e22e1d978ac621f12bbea820622a8deca1afc160e9692f47985b6039`
  and is already authorized by an earlier revision.

## Validation

At the parent HEAD:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still required.

After the two book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` - PASS; V11 prose <=100,
  145 exact owner-link exceptions.
- `python3 scripts/check_boundary.py` - PASS; independent-origin review still
  required.
- `python3 scripts/validate_pattern_sources.py` - PASS, 174 read and 144
  ledger records, because shared metadata is unchanged.
- `python3 scripts/validate_pattern_cards.py` - PASS.
- `python3 scripts/validate_pattern_registry.py` - PASS.
- `python3 scripts/validate_pattern_owner_units.py` - FAIL
  `owner-units-unit-ambiguous: Correlation Identifier` because the owner
  heading moved from line 172 to 174 and the metadata still points at 172.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.dead-letter-channel-dlq` - FAIL: invariant partial, alternative
  partial and card_path missing.
- `python3 scripts/validate_directory_migration.py` - FAIL
  `directory-baseline-payload-drift` until the content revision is applied.
- `python3 scripts/validate_enrichment.py` - FAIL
  `enrichment-baseline-altered` until the enrichment-baseline revision is
  applied.

In a detached scratch copy with the metadata patch above and a scratch-only
`card_path` pointing at the V11/C03 `README.md`:

    FAIL: tycho.pattern.dead-letter-channel-dlq
      - alternative: state 'partial', not supported
    0/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: source plan 145 entries; 176 read; 146 ledger records
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: 11 volumes, 82 chapters, 476 canonical documents
    PASS: enrichment explicit membership and byte conservation

The invariant now passes preflight. The alternative remains partial because no
selected public unit compares the listed alternatives. Do not mark it
`supported` without a source that does; the Tycho-guidance label is deliberate.
The scratch `card_path` is a check only; it is not a split or a real card
registration.

## Derived artifacts

The integrator must regenerate or refresh the artifacts affected by the two
book-file hashes: atlas manifest, inventory, route index, page census,
coverage/reverse maps, semantic audit, candidate and review packets, delivery
evidence and search indexes. The lane intentionally does not edit
`edition/atlas-manifest.json`, `edition/inventory.json`,
`generated/route-index.v1.json`, promotions or other generated state. Refresh
`edition/patterns/sufficient-candidates.v1.json` and
`sufficient-ready-plan.v1.json` only through their owning generation or batch
process; they still describe the pre-lane state.

## Limits

The binding covers two living vendor pages at two pinned canonical
representations plus the existing publisher-abridged EIP page. It supports
retry exhaustion, permanent-failure cases, the DLQ purpose, the diagnostic
reason/description fields, retention, redrive and correction/resubmission. It
does not support a general comparison of a DLQ with bounded retry without
quarantine, drop with a record or a repair table/outbox. Those alternatives and
the reversal condition are Tycho guidance. No broker, queue, redrive, replay,
retention or repair test was executed. Coverage remains
`partial-bounded`; alternative coverage remains partial; independent review,
promotion and owner acceptance are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- `book/volumes/v04-distributed-coordination-and-events/`
  `c06-messaging-families-and-delivery-contracts/workflow-failure.md`.
- `book/volumes/v11-pattern-atlas/c03-messaging-integration/README.md`.

No shared JSON, promotion or generated file is in the lane commit.
