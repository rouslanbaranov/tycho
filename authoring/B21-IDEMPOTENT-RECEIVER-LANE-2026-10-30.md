# B21 - Idempotent Receiver invariant and crash-window lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and alternative were supported;
invariant and failure/recovery were partial. This lane supplies source-bound
text for the two missing dimensions. Preflight still requires the metadata
patch and card registration described below. The lane commit edits only the two
book files and this note.

## Lane coordinates

- Parent HEAD: `502d3f69` ("feat(research): promote Saga").
- Branch: `b21-idempotent`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b21-idempotent`.
- Scope: the V04/C04 owner section `### Idempotent Receiver` and the inline
  V11/C03 card `### Idempotent Receiver` only.
- The card remains inline in the V11/C03 `README.md`; the integrator owns the
  split and the `card_path` registration.
- Single-entry lane; no other entry, shared owner page, promotion or generated
  file is changed.

## Candidate evaluation

- `microservices.io` Idempotent Consumer page:
  `https://microservices.io/patterns/communication-style/idempotent-consumer.html`.
  The existing record `read.batch2-idempotent-consumer.2026-10-21`
  (`src.microservices-patterns`) is assigned to
  `tycho.pattern.transactional-inbox`; its `claims_not_supported` list
  includes "crash-window ordering". The page supports the
  `(subscriberId, messageID)` primary-key duplicate insert inside a database
  transaction, but it does not describe marker-before/marker-after windows for
  an external effect or a repair procedure. It is not used as a new binding;
  the owner page keeps its existing mechanism link.
- AWS Prescriptive Guidance: I checked the current
  `cloud-design-patterns`, `patterns` and
  `modernization-integrating-microservices` guides and their
  `toc-contents.json` indexes and did not find an "idempotent consumer"
  page. The `transactional-outbox` page covers producer-side dual-write
  atomicity and duplicate delivery, not consumer marker windows. No AWS page is
  cited.
- Selected source: Microsoft Azure Architecture Center, Idempotent Consumer
  pattern,
  `https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer`.
  It is public, already admitted through `src.microsoft-cloud-patterns`, and
  states the atomic-marker rule, the store-level uniqueness rule, the
  consumer-scoped composite key, both crash-window directions and the
  in-progress/completed reconciliation rule. Only a new unit is added; no new
  source admission is requested.

## Source binding

- Source id: `src.microsoft-cloud-patterns`.
- New public unit: Idempotent Consumer pattern — Azure Architecture Center.
- Ledger record: `read.microsoft-idempotent-consumer.2026-10-30`.
- Access date: 2026-10-30.
- Canonical text SHA-256:
  `f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34`.
- Raw HTML SHA-256:
  `f335c4291771cc0421741e45761ca7810c11c980ddf9c163ae2fa91586e7594a`.
- Fetch check: the page was fetched twice on 2026-10-30. Both served
  representations were 68,045 bytes and produced the same raw and canonical
  hashes. The page is living Microsoft Learn documentation with no published
  version identifier; the canonical hash pins the 2026-10-30 representation.
- Sections read: "Choose a stable deduplication key", "Commit the processed key
  and the side effects atomically", "Guard against concurrent duplicates",
  "Handle side effects that can't join the transaction" and "Problems and
  considerations".
- Exact quotes used in the owner section and card:
  - "Avoid this failure window by writing the deduplication marker and the
    business side effects in the same transaction."
    ("Commit the processed key and the side effects atomically")
  - "Use a uniqueness constraint on the deduplication key such that two
    transactions can attempt to insert a key, but only one can succeed."
    ("Guard against concurrent duplicates")
  - "If the consumers share a deduplication store, key the records on a
    composite of the consumer identity and the message identity."
    ("Choose a stable deduplication key")
  - "A check-then-process flow has a failure window. If a consumer processes a
    message and then records the key in a separate step, a crash between the
    two operations leaves the side effects applied but the key unrecorded, so
    the consumer reprocesses the next redelivery."
    ("Commit the processed key and the side effects atomically")
  - "Record the key with an in-progress state, and then perform the external
    action. Update the record to completed and store the outcome. On
    redelivery, a completed record tells the consumer to skip repeating the
    call. An in-progress record signals that a previous attempt might be
    partially completed or is being processed by another consumer. The
    consumer should reconcile stale records or route unresolved cases for
    intervention before acknowledging redelivery."
    ("Handle side effects that can't join the transaction")
  - "If a consumer commits both operations together or not at all, upon
    redelivery it either finds the marker and skips the message, or finds no
    marker because the transaction didn't complete and safely reprocesses the
    message."
    ("Commit the processed key and the side effects atomically")
  - "Retain each record at least as long as the broker can still redeliver the
    original message."
    ("Problems and considerations")
  - "Set a time-to-live on deduplication records that exceeds this window, so
    that a late redelivery still finds its marker."
    ("Problems and considerations")
  - "Deduplication removes duplicates, but doesn't guarantee order."
    ("Problems and considerations")
- The page does not prescribe a complete repair algorithm, a post-expiry
  policy, tenant scoping or a specific ordering protocol beyond the ordering
  caveat. The marker-before/marker-after comparison, the cleanup owner, the
  post-expiry route and tenant/owner-scope details remain Tycho guidance and
  are labelled as such in both book files.

## Book edits

- V04/C04 owner `dedup-authority.md#idempotent-receiver`:
  - Adds the exact atomic-marker, store-uniqueness, consumer-composite,
    check-then-process, two-phase, retention/TTL and order quotes.
  - Labels key derivation, collision response, the marker-order comparison,
    cleanup ownership, post-expiry routing and tenant scope as Tycho guidance.
  - Adds a source-boundary paragraph with the canonical hash, section names and
    the page's limits.
  - Frontmatter adds `src.microsoft-cloud-patterns`; advances
    `content_review.reviewed_at`, `updated_at` and
    `source_inspection_date` to 2026-10-30; the reviewer becomes
    "Automated authoring agent".
  - The owner heading moves from line 103 to line 104 because of the added
    frontmatter source line. The page is 160 lines.
  - Raw SHA-256:
    `a45c3771d4e69622822a007e8e4598682b2e56c954421baa08da89d44aef0a96`;
    historical-view SHA-256:
    `4350d763e887b53d345d1976225611883687a443948bf3ea930048525a8d2c0c`.
- V11/C03 inline card `### Idempotent Receiver`:
  - **Failure and recovery** now names the marker-after duplicate window, the
    marker-before in-progress window and the reconcile-stale-records rule, and
    labels cleanup ownership, post-expiry routing and the order/version policy
    beyond the source caveat as Tycho guidance.
  - **Sources** adds the Microsoft record, sections, exact quotes and revision
    in addition to the existing primary record.
  - Frontmatter adds `src.microsoft-cloud-patterns`; advances
    `content_review.reviewed_at`, `updated_at` and
    `source_inspection_date` to 2026-10-30.
  - The card heading moves from line 439 to line 440. The chapter page is 624
    lines.
  - Raw SHA-256:
    `e5e8678e80f8473a48e91c9d9fbb7adaf7c47d57fedce28f5eb3dd40053d8076`;
    historical-view SHA-256:
    `2e0a1ac55e532c67453ac5793aa1633e79916f5452b4fdf0f77cb44124517202`.
- No other book file, edition JSON, promotion or generated file is changed by
  this lane.

## Full ledger record (integrator)

Add `read.microsoft-idempotent-consumer.2026-10-30` to
`edition/patterns/reading-ledger.v1.json` and set `updated` to
2026-10-30. The exact fields are:

~~~json
{
  "id": "read.microsoft-idempotent-consumer.2026-10-30",
  "source_id": "src.microsoft-cloud-patterns",
  "unit_url": "https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer",
  "unit_label": "Idempotent Consumer pattern — Azure Architecture Center",
  "unit_type": "pattern-page",
  "access_date": "2026-10-30",
  "access_method": "public HTTPS GET; canonical page text extracted with scripts/source_content_hash.py; extracted-text SHA-256 verified as f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34",
  "sections_read": [
    "Choose a stable deduplication key",
    "Commit the processed key and the side effects atomically",
    "Guard against concurrent duplicates",
    "Handle side effects that can't join the transaction",
    "Problems and considerations"
  ],
  "sections_not_read": [
    "Context and problem",
    "Solution",
    "When to use this pattern",
    "Idempotent processing beyond messaging",
    "Workload design",
    "Example",
    "Next step",
    "Related resources",
    "linked child pages and sample code",
    "navigation and unrelated chrome (included only in the digest)",
    "images and their interiors"
  ],
  "tables_figures": [
    "the workload-design table was outside the read scope; images and diagram interiors were not inspected"
  ],
  "license_notes": "Public Microsoft Learn documentation; cite short excerpts and paraphrase; do not mirror.",
  "claims_supported": [
    "Avoid this failure window by writing the deduplication marker and the business side effects in the same transaction.",
    "If a consumer commits both operations together or not at all, upon redelivery it either finds the marker and skips the message, or finds no marker because the transaction didn't complete and safely reprocesses the message.",
    "Use a uniqueness constraint on the deduplication key such that two transactions can attempt to insert a key, but only one can succeed.",
    "If the consumers share a deduplication store, key the records on a composite of the consumer identity and the message identity.",
    "A check-then-process flow has a failure window. If a consumer processes a message and then records the key in a separate step, a crash between the two operations leaves the side effects applied but the key unrecorded, so the consumer reprocesses the next redelivery.",
    "Record the key with an in-progress state, and then perform the external action. Update the record to completed and store the outcome. On redelivery, a completed record tells the consumer to skip repeating the call. An in-progress record signals that a previous attempt might be partially completed or is being processed by another consumer. The consumer should reconcile stale records or route unresolved cases for intervention before acknowledging redelivery.",
    "Retain each record at least as long as the broker can still redeliver the original message.",
    "Set a time-to-live on deduplication records that exceeds this window, so that a late redelivery still finds its marker.",
    "Deduplication removes duplicates, but doesn't guarantee order."
  ],
  "claims_not_supported": [
    "a complete repair algorithm or a post-expiry policy",
    "tenant scoping or a specific ordering protocol beyond the order caveat",
    "implementation behavior, throughput, latency or production outcomes",
    "linked pages, sample code and images",
    "independent reproduction, benchmark or local execution"
  ],
  "limitations": "One living Microsoft Learn page with no published version identifier; no benchmark, local execution or production observation. The canonical digest covers the full extracted page text including navigation chrome because the page has no recognized article-body marker; quoted sentences were checked against that extraction. The page does not prescribe a complete repair algorithm, a post-expiry policy, tenant scoping or a specific ordering protocol.",
  "content_sha256": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34",
  "read_scope": "selected public page text: Choose a stable deduplication key, Commit the processed key and the side effects atomically, Guard against concurrent duplicates, Handle side effects that can't join the transaction and Problems and considerations; linked pages, images and navigation excluded; digest covers the canonical extracted article text including chrome",
  "reviewer": "Automated authoring agent",
  "status": "read"
}
~~~

The record's `sections_read` must exactly equal the source-plan unit's
`sections` list. The `unit_label`, `unit_url` and `unit_type` must also
match the source-plan unit exactly.

## Registry and source-plan fields (integrator)

In `edition/patterns/registry.v1.json`, entry
`tycho.pattern.idempotent-receiver`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to
  `partial-bounded`; `coverage.decision` and `atlas_owner.state` stay
  `partial-bounded`.
- Append the source unit:
  `{"source_id": "src.microsoft-cloud-patterns", "unit": "Idempotent Consumer
  pattern - Azure Architecture Center", "status": "read"}`.
- Replace the notes with: "Phase 3 C03 card; bounded owner section and backlink
  are self-checked, not independent-reviewed or sufficient. Invariant and
  failure/recovery bound 2026-10-30 to the Microsoft Learn Idempotent Consumer
  page; all four technical dimensions supported; coverage partial-bounded."
- Set `updated_at` to 2026-10-30.

In `edition/patterns/source-plan.v1.json`, entry
`tycho.pattern.idempotent-receiver`, append the same unit with
`unit_type` `pattern-page`, the five sections above, `status` `read`,
`read_record_id` `read.microsoft-idempotent-consumer.2026-10-30` and
`blocked_reason` null. Update the summary to:

- `required_units`: 174 -> 175.
- `read_units`: 173 -> 174.
- `ledger_records`: 143 -> 144.
- `registry_sha256`: recompute after saving the registry. The patched value
  is `2552efa9667689c06316dd2fb5cd0d7695dcf086ad1c837f638bd00beed00f99`.
- `updated`: 2026-10-30.

The registry `source_units` array must equal the source-plan unit list for
this pattern, in the same order. The two unit records are:

~~~json
{
  "source_id": "src.microsoft-cloud-patterns",
  "unit": "Idempotent Consumer pattern — Azure Architecture Center",
  "status": "read"
}
~~~

~~~json
{
  "source_id": "src.microsoft-cloud-patterns",
  "unit": "Idempotent Consumer pattern — Azure Architecture Center",
  "unit_type": "pattern-page",
  "url": "https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer",
  "sections": [
    "Choose a stable deduplication key",
    "Commit the processed key and the side effects atomically",
    "Guard against concurrent duplicates",
    "Handle side effects that can't join the transaction",
    "Problems and considerations"
  ],
  "status": "read",
  "read_record_id": "read.microsoft-idempotent-consumer.2026-10-30",
  "blocked_reason": null
}
~~~

## Owner-units metadata needs (integrator)

In `edition/patterns/owner-units.v1.json`, entry
`tycho.pattern.idempotent-receiver`:

- Set `owner.line` to 104.
- Replace `owner.unit_terms` with:
  `["processed message IDs", "atomic (consumer", "marker-before/marker-after",
  "business-key upsert"]`.
- Set `technical_evidence.invariant.state` to `supported`.
  - `quote`: the atomic-marker sentence above.
  - `binding.section`: "Commit the processed key and the side effects
    atomically".
  - Add supporting bindings for the uniqueness sentence ("Guard against
    concurrent duplicates") and the consumer-composite sentence ("Choose a
    stable deduplication key").
  - Reason: the page requires one transaction, a store-level uniqueness
    arbitration and a consumer-scoped composite key; key derivation and
    collision response remain Tycho guidance.
- Set `technical_evidence.failure_recovery.state` to `supported`.
  - `quote`: the two-phase record sentence above.
  - `binding.section`: "Handle side effects that can't join the
    transaction".
  - Add supporting bindings for the check-then-process sentence, the
    commit-both-or-neither sentence, and the retention, TTL and order
    sentences ("Problems and considerations").
  - Reason: the page supports the crash window, the in-progress/completed
    marker pair and stale-record reconciliation; the marker-order comparison,
    cleanup owner, post-expiry policy and tenant/order rules beyond the source
    caveat remain Tycho guidance.
- Add the auxiliary source:
  `{"source_id": "src.microsoft-cloud-patterns", "ledger_record":
  "read.microsoft-idempotent-consumer.2026-10-30", "revision":
  "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"}`.
- Change `technical_coverage` from `partial` to `partial-bounded`.
  The derivation rule uses mechanism plus invariant, not failure/recovery.
- Replace `notes` with the registry-style binding note.
- Update the summary:
  - `invariant_supported`: 62 -> 63.
  - `failure_recovery_supported`: 52 -> 53.
  - `technical_partial_bounded`: 22 -> 23.
  - `technical_partial`: 88 -> 87.
  - No other counter changes; `technical_sufficient` stays 35.

Every binding and supporting binding must name a source-plan unit whose
`read_record_id` matches the binding record. The ledger `content_sha256`
must equal the binding revision.

## Content revisions

Add one entry to `edition/content-revisions.json`:

- `issue`: 540.
- `authorized_at`: 2026-10-30.
- `authorization`: "B21 idempotent receiver source binding".
- `directory_documents`:
  - Owner path, `previous_sha256`
    `aef57346a04d94eb413aa354a167a36240aa95d5fcfd43ebb22519338a214876`
    (the `baseline_sha256` in `edition/directory-migration.json`),
    `current_sha256`
    `4350d763e887b53d345d1976225611883687a443948bf3ea930048525a8d2c0c`.
  - Card path, `previous_sha256`
    `6019fa28b483a027dc816d6797dd20564c2dc1c8665f1112c66fb34984a84c80`
    (the migration baseline), `current_sha256`
    `2e0a1ac55e532c67453ac5793aa1633e79916f5452b4fdf0f77cb44124517202`.
- Empty `source_blocks`, `enrichment_documents`, `enrichment_additions`
  and `enrichment_baselines`.

The previous values are migration baselines, not the latest revision's
current hash. `validate_directory_migration.py` compares the baseline to the
authorized current hash.

## Source register

`sources/register.json` already admits `src.microsoft-cloud-patterns`.
Update that record's `version`, `access_checked`, `content_verified` and
`verification_scope` to name the Idempotent Consumer page, its 2026-10-30
canonical hash and the sections read. This is an editorial source-record
update, not a new admission. The lane does not edit the shared register.

## Card registration and promotion

The card is still inline in the V11/C03 `README.md`. At the parent HEAD,
`edition/patterns/card-batches.v1.json` has no `card_path` for this entry,
so preflight reports `card_path missing or absent`. The integrator must split
the card to a dedicated page and register its `card_path`, or explicitly
register the inline chapter path. The split card must keep
`src.microsoft-cloud-patterns` in `evidence_scope.source_ids` and the
2026-10-30 dates.

No promotion is added or changed. `sufficient-promotions.v1.json` does not
name this pattern. The entry remains `partial-bounded`; all four technical
dimensions become supported, but technical and decision sufficiency,
independent review and owner acceptance are not claimed.

## Validation

At the parent HEAD:

    FAIL: tycho.pattern.idempotent-receiver
      - invariant: state 'partial', not supported
      - failure_recovery: state 'partial', not supported
      - card_path missing or absent
    0/1 entries preflight clean

After the two book edits in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` - PASS; V11 prose <=100,
  145 exact owner-link exceptions.
- `python3 scripts/check_boundary.py` - PASS; independent-origin review still
  required.
- `python3 scripts/validate_pattern_sources.py` - PASS, 173 read, 143 ledger
  records, because the shared metadata is unchanged.
- `python3 scripts/validate_pattern_registry.py` - PASS.
- `python3 scripts/validate_pattern_cards.py` - PASS.
- `python3 scripts/validate_pattern_owner_units.py` - FAIL
  `owner-units-unit-ambiguous: Idempotent Receiver` because the owner heading
  moved from line 103 to 104 and the metadata still points at 103.
- Targeted tests
  `test_tycho_pattern_owner_units`, `test_tycho_pattern_sources`,
  `test_tycho_pattern_cards` and `test_tycho_pattern_registry` run 62
  tests; 59 pass. The two expected failures and one error all come from the
  stale owner line; the metadata patch clears them.
- `validate_pattern_atlas.py` fails `atlas-document-sha`;
  `validate_pattern_semantic_audit.py` fails the owner page hash;
  `validate_directory_migration.py` fails
  `directory-baseline-payload-drift` until the content-revision entry is
  applied. These are derived or authorization artifacts, not content errors.
- `validate_pattern_coverage.py`, `validate_claim_references.py` and
  `validate_enrichment.py` pass in the lane worktree.

A detached scratch worktree at the parent HEAD with the two book files and the
metadata changes described above showed the expected preflight and validator
results. After correcting the `previous_sha256` values to the migration
baselines and pointing `card_path` temporarily at the V11/C03 `README.md`,
the scratch tree reported:

    PASS: tycho.pattern.idempotent-receiver
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: source plan 145 entries; 174 read; 144 ledger records
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: 11 volumes, 82 chapters, 475 canonical documents

That pointer is a scratch-only check; it does not split the card and does not
register a real `card_path`. The two targeted counter failures remain in the
scratch suite (`read_units` 173 vs 174 and registry `source_units` 174 vs
175); those hard-coded counters belong to the batch-end test update, not this
lane.

## Derived artifacts

The integrator must regenerate or refresh the artifacts affected by the two
book-file hashes: atlas manifest, inventory, route index, page census,
coverage/reverse maps, semantic audit, candidate and review packets, delivery
evidence, and search indexes. The lane intentionally does not edit
`edition/atlas-manifest.json`, `edition/inventory.json`,
`generated/route-index.v1.json`, promotions or other generated state. Refresh
`edition/patterns/sufficient-candidates.v1.json` and
`sufficient-ready-plan.v1.json` only through their owning generation or
batch process; they still describe the pre-lane 2/4 state.

## Limits

The binding covers one living Microsoft Learn page at one pinned canonical
representation. It supports the atomic marker, the store-level uniqueness
constraint, the consumer-scoped composite key, both crash-window directions,
the in-progress/completed repair discipline and the retention/TTL/order
caveats. It does not define a complete repair algorithm, a post-expiry policy,
tenant scoping or a specific ordering protocol. Those details, and the
comparative marker-before/marker-after framing, remain Tycho guidance. No
broker, database, crash, replay, reconciliation or concurrency test was
executed. Coverage remains `partial-bounded`; independent review, promotion
and owner acceptance are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- The V04/C04 owner file `dedup-authority.md`.
- The V11/C03 inline card file `README.md`.

No shared JSON, promotion or generated file is in the lane commit.
