# B73 — Aggregator failure/recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-11-01. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and invariant were supported;
failure/recovery and alternative were partial. This lane binds failure/recovery
to the existing Enterprise Integration Patterns Aggregator unit and the
alternative to the existing microservices.io API Composition unit, with the
comparison and reversal labelled Tycho synthesis. The entry is 4/4 on technical
dimension states after the integrator metadata patch; coverage remains
partial-bounded and promotion is not claimed. The promoted Scatter-Gather
section on the same page is byte-identical, but its page-level promotion hash
is invalidated by this sibling edit and needs a separate decision.

## Lane coordinates

- Parent HEAD: `ee90382356558fb70119020fbc2c7133fd4ff681` (`ee903823`,
  merged `feature/TYCHO-540-promotion-86-bookkeeping`).
- Lane label: Tycho.
- Branch: `feature/TYCHO-540-aggregator-2`; worktree:
  `/tmp/tycho-aggregator-2`.
- Scope: the owner section `### Aggregator` in V04/C06, the inline
  `### Aggregator` card in V11/C03, and this note. Single-entry lane; no other
  entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate the three lines):

      book/volumes/v04-distributed-coordination-and-events/
      c06-messaging-families-and-delivery-contracts/
      messaging-families-and-durable-workflows.md

- Card path:
  `book/volumes/v11-pattern-atlas/c03-messaging-integration/README.md`.
- The card remains inline; no split is performed. The integrator owns any
  split and the `card_path` registration.
- Exactly three files change: the owner page, the inline card host and this
  note.

## Baseline and gap

- Baseline owner page: 184 lines, SHA-256
  `1397ad303520df66900ae5046495473eb543a1d2ff64b29332506c3788938950`.
- Baseline `### Aggregator`: lines 119-138, 1,366 bytes, SHA-256
  `769ac9f3b9c659fcce93eb58ca29f6d729c1a4765d8e01703916cdd5b4c44d30`.
- Baseline `### Scatter-Gather`: lines 144-184, 2,867 bytes, SHA-256
  `ea18949ac86f863bd2e3a19cb6a0560aa4a7594650901da5fd71ce8d52677ab9`.
- Baseline card file: 518 lines, SHA-256
  `e62e4182bd52261118b428b57f9bc1564b9639dafea6a0cab46b77922627ac2c`.
- Baseline `### Aggregator` card: lines 298-336, 2,086 bytes, SHA-256
  `21cfe5abfe51801bfd9f254088f8aa15ab3a23d73bc8e23ca6cc4a9db65fd7a8`.
- `owner-units` records mechanism `supported`, invariant `supported`,
  failure/recovery `partial` and alternative `partial`: 2/4.
- Baseline preflight: FAIL `failure_recovery` partial, `alternative`
  partial and `card_path` missing.
- Baseline line-length and boundary checks pass.

## Candidate evaluation

- Enterprise Integration Patterns, "Aggregator":
  `https://www.enterpriseintegrationpatterns.com/patterns/messaging/`
  `Aggregator.html` (concatenate the two lines). Reused from
  `src.enterprise-integration` and
  `read.batch2-aggregator.2026-10-21`. It states that a single missing or
  delayed message prevents further processing of the whole aggregate, that the
  Wait-for-All strategy raises an error condition after a time-out period,
  that detecting a missing message is hard in loosely coupled asynchronous
  flows, that a missing message can be re-requested, and that the Time Out
  strategy may report an exception or retry. It does not support a general
  partial-result rule or cancellation; those remain Tycho guidance. It names
  Scatter-Gather only as a related pattern, not as an alternative.
- microservices.io, "API Composition":
  `https://microservices.io/patterns/data/api-composition.html`. Reused from
  `src.microservices-patterns` and
  `read.microservices-api-composition.2026-10-21`. It defines a query
  implementation in which an API Composer invokes the data-owning services and
  performs an in-memory join, and it notes that some queries would produce
  inefficient large in-memory joins. It does not compare API Composition with
  Aggregator. The alternative framing and reversal are therefore Tycho
  synthesis.
- Microsoft Azure Architecture Center, "Gateway Aggregation":
  `https://learn.microsoft.com/en-us/azure/architecture/patterns/`
  `gateway-aggregation` (concatenate the two lines). Considered as related
  naming only. It is not used as a binding for this entry because it describes
  gateway-side aggregation of back-end calls, not the EIP aggregator decision.
  The card lists it under Related entries only.
- No other source was selected. The Scatter-Gather section is not edited and
  its existing AWS binding is not re-read.

## Source binding

### Enterprise Integration Patterns, Aggregator

- Source id: `src.enterprise-integration` (existing).
- Record: `read.batch2-aggregator.2026-10-21`; access date 2026-10-21.
- URL:
  `https://www.enterpriseintegrationpatterns.com/patterns/messaging/`
  `Aggregator.html` (concatenate the two lines).
- Unit label: `Aggregator — pattern page`.
- Unit type: `pattern-page`.
- Sections read as evidence: `Aggregator`; the record also read both
  loan-broker examples.
- Raw HTML revision:
  `15d8640d5ad149a0e54a23c4cfe4a84c0abdcec421de2f9eb301daf21d708f58`.
- Fetch check: one public HTTPS GET on 2026-11-01 served a 31,645-byte page
  whose raw HTML SHA-256 equalled the recorded revision. The committed
  canonical-text extractor yields
  `e1c4a2c4cef8a220390b9bab78851e35d9d473bee3dd0c3e0e2f7f84e925c494`,
  so the ledger's `content_sha256` is a raw-representation hash, not the
  canonical-text digest. This lane reuses the recorded revision and reports
  the distinction; no new ledger record is proposed.
- Exact quotes used:

      A single missing or delayed message will prevent further processing of
      the whole aggregate.

      One way to deal with missing messages is to re-request the message.

      If no responses are received, the system may report an exception or retry.

      An incomplete order may not be meaningful. So if not all items are
      received within a certain time-out period an error condition should be
      raised by the Aggregator.

- The last quote appears in the served HTML with italic markup that inserts a
  space before the final period; the binding normalizes that punctuation
  spacing, as the existing record quote already did.
- Limits: one living, publisher-abridged page. It supports the failure mode,
  the timeout error, detection difficulty, re-request and retry/exception. It
  does not define a bounded partial-result contract or cancellation.

### microservices.io, API Composition

- Source id: `src.microservices-patterns` (existing).
- Record: `read.microservices-api-composition.2026-10-21`; access date
  2026-10-21.
- URL: `https://microservices.io/patterns/data/api-composition.html`.
- Unit label: `API Composition — pattern page`.
- Unit type: `pattern-page`.
- Sections read as evidence: `Solution` and `Resulting context`; the record
  read all nine served headings.
- Raw HTML revision:
  `7ec014c171b2421f216c3a82ddb60af0104a2f38e6bb3af93e93c8065f04750b`.
- Fetch check: one public HTTPS GET on 2026-11-01 served a 21,585-byte page
  whose raw HTML SHA-256 equalled the recorded revision. The committed
  canonical-text extractor yields
  `75fae4c75e4c6d5cc8084bd4a4ecec5fed6aaf9a1816437cecf4950e0d82b4b7`,
  so the same raw-versus-canonical distinction applies.
- Exact quotes used:

      Implement a query by defining an API Composer, which invoking the
      services that own the data and performs an in-memory join of the results.

      Some queries would result in inefficient, in-memory joins of large
      datasets.

- The first quote preserves the source's "which invoking" wording; link
  markup inserts a space before the comma in the served HTML, and the binding
  normalizes that spacing. The owner section paraphrases the sentence as an
  API Composer that invokes the services and quotes only
  "performs an in-memory join of the results."
- Limits: a living pattern page. It defines API Composition but does not
  compare it with Aggregator; the comparison and reversal are Tycho synthesis.

## Book edits

### V04/C06 owner `messaging-families-and-durable-workflows.md#aggregator`

- Frontmatter is intentionally unchanged in this lane: no source id, review
  status or date edit. The proposed evidence-scope addition is listed under
  metadata needs.
- The mechanism paragraph is unchanged so the existing mechanism and
  invariant owner quotes remain verbatim.
- The old failure/alternative paragraph is replaced with:
  - a **Failure and recovery** paragraph that quotes the EIP missing/delayed
    aggregate statement, paraphrases the Wait-for-All time-out error and the
    detection difficulty, quotes the re-request path and the Time Out
    exception-or-retry sentence, and labels the partial-result and cancellation
    rules as Tycho guidance;
  - an **Alternative** paragraph that labels API Composition as the alternative
    in Tycho synthesis, quotes the source's in-memory-join fragment, states
    that the source does not compare the two patterns, gives the reversal, and
    records Scatter-Gather as a related composite and Azure Gateway Aggregation
    as related naming only;
  - a **Limits** paragraph retained from the prior note;
  - a **Source boundary** paragraph with both URLs, sections and raw HTML
    revisions, and the Tycho-synthesis labels.
- `### Aggregator` is now lines 119-162, 2,994 bytes, SHA-256
  `7e2a5b28a0f310dc463bdbf71b4fb64fdcc230c4e57d97e973154b14b14c492b`.
- The owner page is now 207 lines, SHA-256
  `11e049dd7203d592070f043161b583055b38244727b0166b81863e2ee124bb56`.
- `### Scatter-Gather` now starts at line 167 (was 144) because the
  Aggregator section grew. Its bytes are unchanged: 2,867 bytes and SHA-256
  `ea18949ac86f863bd2e3a19cb6a0560aa4a7594650901da5fd71ce8d52677ab9`
  before and after. The heading line shift is the only Scatter-Gather change.
- The Scatter-Gather promotion record problem is described below.

### V11/C03 inline card `### Aggregator`

- Frontmatter is intentionally unchanged in this lane; the proposed
  evidence-scope addition is listed under metadata needs.
- **Competing alternative** now states the Tycho synthesis for API Composition,
  says the microservices.io page defines the composer and in-memory join but
  does not compare it with Aggregator, keeps the reversal, and records
  Scatter-Gather as a related composite rather than the alternative.
- **Failure and recovery** now names the EIP Wait-for-All time-out error, the
  re-request path and the Time Out retry/exception choice, then labels the
  partial-result and cancellation rules as Tycho guidance.
- **Hard contraindications** is explicitly labelled Tycho guidance.
- **Sources** now cites the EIP and microservices.io records with their raw
  HTML revisions; the AWS scatter-gather citation is removed because this card
  no longer uses it.
- **Related entries** adds API Composition and Gateway Aggregation.
- `### Aggregator` card is now lines 298-345, 2,692 bytes, SHA-256
  `2d89c239988d3c423822eae5d9da500a80de029fab6659880307a7a113e2897b`.
- The chapter page is now 526 lines, SHA-256
  `607d84ec3d48c4b323743da830ddd94cc5607c39f1a196ea73039669493fbf02`.
- No other card is edited.

## Metadata needs (integrator)

The following patch was exercised in a detached scratch copy of this worktree,
not in the lane commit. It produced the validation results in the next section.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.aggregator`:

- Keep `owner.line` at 119.
- Replace `owner.unit_terms` with:
  `["fans in related results", "per-participant timeout",
  "partial-failure policy", "API composition is the alternative"]`.
- Set `technical_evidence.failure_recovery.state` to `supported`.
  - `quote`: "The source states: \"A single missing or delayed message will
    prevent further processing of the whole aggregate.\""
  - `binding`: EIP, record `read.batch2-aggregator.2026-10-21`, section
    `Aggregator`, quote "A single missing or delayed message will prevent
    further processing of the whole aggregate.", revision
    `15d8640d5ad149a0e54a23c4cfe4a84c0abdcec421de2f9eb301daf21d708f58`.
  - `supporting_bindings`, all EIP, same record, section `Aggregator`, same
    revision:
    - "An incomplete order may not be meaningful. So if not all items are
      received within a certain time-out period an error condition should be
      raised by the Aggregator."
    - "One way to deal with missing messages is to re-request the message."
    - "If no responses are received, the system may report an exception or
      retry."
  - `reason`: state that EIP supports the missing/delayed aggregate failure,
    the timeout error and the re-request and retry/exception recovery paths;
    the partial-result and cancellation rules are Tycho guidance.
- Set `technical_evidence.alternative.state` to `supported`.
  - `quote`: "Tycho synthesis: API composition is the alternative when the
    caller can invoke the data-owning services and join their responses at
    query time."
  - `binding`: microservices.io, record
    `read.microservices-api-composition.2026-10-21`, section `Solution`,
    quote "Implement a query by defining an API Composer, which invoking the
    services that own the data and performs an in-memory join of the results.",
    revision
    `7ec014c171b2421f216c3a82ddb60af0104a2f38e6bb3af93e93c8065f04750b`.
  - `supporting_bindings`: microservices.io, same record, section
    `Resulting context`, quote "Some queries would result in inefficient,
    in-memory joins of large datasets.", same revision.
  - `reason`: state that microservices.io defines API Composition and notes
    the large-join cost, but does not compare it with Aggregator; the
    comparison and reversal are Tycho synthesis.
- Add `source_support.auxiliary`:
  `{"source_id": "src.microservices-patterns",
  "ledger_record": "read.microservices-api-composition.2026-10-21",
  "revision": "7ec014c171b2421f216c3a82ddb60af0104a2f38e6bb3af93e93c8065f04750b"}`.
- Set `decision_evidence.competing_alternative` to the exact squashed card
  text:

      Tycho synthesis: API composition is the alternative when the caller can
      invoke the data-owning services and join their responses at query time.
      The microservices.io page defines the API Composer and in-memory join but
      does not compare it with aggregator; reverse the choice when related
      results already arrive as messages and completion must trigger the
      combined result. Scatter-gather is a related composite, not this
      alternative.

- Replace `notes` with: "Failure/recovery bound 2026-11-01 to EIP
  missing/delayed aggregate, timeout error, re-request and retry/exception
  statements; alternative bound to the microservices.io API Composition
  definition, with the comparison and reversal labelled Tycho synthesis.
  Coverage partial-bounded; no promotion." (400-character limit respected.)
- Keep `technical_coverage` and `decision_coverage` at
  `partial-bounded`; no promotion record is added.
- Summary: `failure_recovery_supported` 97 -> 98 and
  `alternative_supported` 98 -> 99. No other counter changes.

Entry `tycho.pattern.scatter-gather`:

- Set `owner.line` to 167 (was 144) because the Aggregator section grew. The
  section text and its SHA-256 are unchanged.
- Do not change its technical evidence, coverage or promotion record as part
  of this lane.

### Registry `edition/patterns/registry.v1.json`

Entry `tycho.pattern.aggregator`:

- Add source unit `{"source_id": "src.microservices-patterns",
  "unit": "API Composition — pattern page", "status": "read"}`.
- Replace `notes` with the same text proposed for the owner-unit `notes`.
- Keep `technical_owner.state`, `atlas_owner.state` and all three coverage
  values at `partial-bounded`; no promotion is claimed.

### Source plan `edition/patterns/source-plan.v1.json`

Entry `tycho.pattern.aggregator`:

- Add one required unit for `src.microservices-patterns`: unit
  `API Composition — pattern page`, type `pattern-page`, URL
  `https://microservices.io/patterns/data/api-composition.html`, sections
  `Pattern: API Composition`, `Context`, `Problem`, `Solution`,
  `Example`, `Resulting context`, `Related patterns`, `See also`,
  `Learn more`, status `read`, read record
  `read.microservices-api-composition.2026-10-21`, no blocked reason.
- Summary: `required_units` 390 -> 391 and `read_units` 389 -> 390. The
  `ledger_records` count does not change; no new reading record is added.
- After the registry edit, recompute `source-plan.registry_sha256` as the
  SHA-256 of `edition/patterns/registry.v1.json`; the scratch value is
  `ac0132ec34535904469dcfb44a2e1ab989143d5fc238483e1227312cc5ce096a`.
  Keep `route_index_snapshot` unless the route index changes.

### Card batch `edition/patterns/card-batches.v1.json`

Entry `tycho.pattern.aggregator`:

- The card is still inline, so it has no `card_path`. Register the inline
  host explicitly, `book/volumes/v11-pattern-atlas/c03-messaging-integration/
  README.md`, or split the card in a later reviewed change. Preflight fails
  with `card_path missing or absent` until one of these is done.
- If the card remains inline, add `src.microservices-patterns` to the
  V11/C03 chapter frontmatter `evidence_scope.source_ids`. The chapter
  frontmatter is shared by 20 cards and is intentionally unchanged in this
  lane.

### Owner page and card frontmatter

- If the evidence scope is refreshed, add `src.microservices-patterns` to the
  owner page `evidence_scope.source_ids` and to the V11/C03 chapter
  `evidence_scope.source_ids`.
- The owner page and card frontmatter dates are intentionally unchanged in this
  lane. Any date change must preserve
  `content_review.reviewed_at >= source_inspection_date`.

### Content revisions and derived artifacts

- The owner page and the card host changed; add an issue-540 content revision
  with the historical-view hashes for both paths. This lane does not edit
  `edition/content-revisions.json`.
- Regenerate the page census, coverage map, reverse map, phase 4, semantic
  audit, sufficient-ready/candidate/reconciliation packets and any route or
  index artifact that pins the owner-page or card hashes. Those derived
  artifacts are not lane-local.
- Do not update the Scatter-Gather promotion hash without the decision
  described below.

## Validation

At the parent HEAD:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

After the two book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` - PASS; V11 prose <=100,
  145 exact owner-link exceptions.
- `python3 scripts/check_boundary.py` - PASS; independent-origin review still
  required.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.aggregator` - FAIL: failure/recovery partial, alternative
  partial and `card_path` missing, because shared metadata is unchanged.
- `python3 scripts/validate_pattern_owner_units.py` - FAIL
  `owner-units-term-missing: tycho.pattern.aggregator: Scatter-gather is the
  alternative` because the proposed `unit_terms` change is not applied.
- `python3 scripts/validate_pattern_cards.py` - PASS.
- `python3 scripts/validate_pattern_registry.py` - PASS.
- `python3 scripts/validate_sources.py` - PASS; 357 source records.
- `python3 scripts/validate_book_metadata.py` - PASS; 555 canonical
  documents.

In a detached scratch copy with the metadata patch above, the
Scatter-Gather `owner.line` update and a scratch-only
Scatter-Gather promotion-hash substitution:

    PASS: tycho.pattern.aggregator
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: pattern registry 145 entries, 11 families
    PASS: 357 source records, mandatory IDs, cross-references and catalogue
    freshness
    PASS: 555 canonical documents

The promotion-hash substitution in the scratch copy was used only to exercise
the remaining structural checks. It is not proposed for the lane commit and is
not a valid promotion rebind. Without it, `validate_pattern_owner_units.py`
fails `owner-units-promotion-owner-hash: tycho.pattern.scatter-gather`.

## Scatter-Gather promotion impact

- Section bytes and SHA-256 are identical before and after:
  `ea18949ac86f863bd2e3a19cb6a0560aa4a7594650901da5fd71ce8d52677ab9`,
  2,867 bytes. The heading moved from line 144 to line 167.
- The page-level SHA-256 moved from
  `1397ad303520df66900ae5046495473eb543a1d2ff64b29332506c3788938950`
  to
  `11e049dd7203d592070f043161b583055b38244727b0166b81863e2ee124bb56`.
- `edition/patterns/sufficient-promotions.v1.json` records the
  Scatter-Gather `owner_page_sha256` as the old page hash
  `1397ad30...`; it is now stale.
- Rule 35 does not authorize a raw hash update: this is a content edit in a
  sibling section, not a formatting-only change.
- Options for the integrator and owner:
  (a) re-review Scatter-Gather on the new page;
  (b) obtain an owner-authorized section-identity rebind that records the
  unchanged section hash, the new page hash and the review basis;
  (c) split the Aggregator owner note to a separate page in a later structural
  change. A split is outside this lane.
- Until one option is recorded, do not claim that the Scatter-Gather promotion
  is currently valid.

## Limits

- Two living public pages; no benchmark, execution or production observation.
- The API Composition comparison and reversal are Tycho synthesis. The source
  defines API Composition but does not compare it with Aggregator.
- The partial-result and cancellation rules are Tycho guidance, not EIP
  statements.
- Azure Gateway Aggregation is related naming only and is not a dimension
  binding.
- The entry remains `partial-bounded` with no promotion, independent review,
  owner acceptance, CI result or merge permission.
- The 2026-10-21 records store raw HTML SHA-256 values in the
  `content_sha256` field. The 2026-11-01 re-fetch matched both raw hashes; the
  committed canonical-text extractor produced different digests for both
  pages. This lane reuses the recorded revisions and does not add ledger
  records.

## Review needs

- Request a fresh external review under the book/atlas gate.
- The reviewer should check the EIP quote-to-claim fit, the timeout-error
  paraphrase, the API Composition comparison and Tycho labels, the
  raw-versus-canonical revision semantics, the owner/card/owner-unit
  alignment, the source-plan and registry additions, and the
  Scatter-Gather promotion decision.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- `book/volumes/v04-distributed-coordination-and-events/`
  `c06-messaging-families-and-delivery-contracts/`
  `messaging-families-and-durable-workflows.md` (concatenate the three lines).
- `book/volumes/v11-pattern-atlas/c03-messaging-integration/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
