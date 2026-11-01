# B24 — Scatter-Gather failure/recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and invariant were supported;
failure/recovery and alternative were partial. This lane binds both dimensions
to the existing public AWS Prescriptive Guidance unit and labels the
aggregator-alone alternative as Tycho synthesis. The entry is 4/4 on technical
dimension states after the integrator metadata patch; the scratch preflight
passes 1/1 with a scratch-only card pointer. Promotion is not claimed or ready.

## Lane coordinates

- Parent HEAD: `c7fae34b099a44aa429c0f0832f9c905813df728`
  ("feat(research): promote Two-Phase Commit").
- Branch: `b24-scatter-gather`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b24-scatter-gather`.
- Scope: the V04/C06 owner section `### Scatter-Gather` in
  `messaging-families-and-durable-workflows.md` and the inline V11/C03 card
  `### Scatter-Gather` in the V11/C03 `README.md`.
- Owner path (concatenate the three lines):

      book/volumes/v04-distributed-coordination-and-events/
      c06-messaging-families-and-delivery-contracts/
      messaging-families-and-durable-workflows.md

- Card path: `book/volumes/v11-pattern-atlas/c03-messaging-integration/README.md`.
- The card remains inline; the integrator owns any split and `card_path`
  registration.
- Single-entry lane; no other entry, shared owner page, promotion or generated
  file is changed.

## Candidate evaluation

- AWS Prescriptive Guidance, "Scatter-gather pattern":
  `https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/`
  `scatter-gather.html` (concatenate the two lines). Reused from
  `src.aws-scatter-gather`. It states that recipients can time out,
  that the implementation should tell the client the response is incomplete,
  that timed-out responses are ignored, that the aggregator combines partial
  responses and returns a final result, and that the aggregator is "another
  messaging pattern". It does not state that a standalone aggregator is an
  alternative to scatter-gather. The aggregator-alone decision and its
  reversal are therefore labelled Tycho synthesis.
- Enterprise Integration Patterns, "Scatter-Gather":
  `https://www.enterpriseintegrationpatterns.com/patterns/messaging/`
  `BroadcastAggregate.html` (concatenate the two lines). The existing
  `read.batch2-scatter.2026-10-21` record remains the mechanism
  and invariant binding. It is not re-read in this lane.
- No other candidate was selected. The existing AWS page already supports the
  timeout, incomplete-response, timeout-ignore and partial-return sentences
  that the owner section now quotes exactly.

## Source binding

### AWS Prescriptive Guidance, Scatter-gather pattern

- Source id: `src.aws-scatter-gather` (existing).
- Record: `read.aws-scatter-gather.2026-10-28`; access date 2026-10-28.
- URL:
  `https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/`
  `scatter-gather.html` (concatenate the two lines).
- Unit label: `Scatter-gather pattern — AWS Prescriptive Guidance`.
- Unit type: `documentation-page`.
- Canonical text SHA-256:
  `4b5c777b08c089f6753dc3f5743627d17a35720b7bc1e5fecaae69c31f64fda3`.
- Fetch check: one public HTTPS GET on 2026-10-30 served a 28,574-byte page
  whose canonical text digest equalled the ledger revision. The raw HTML
  digest observed that day was
  `4ad4a96051a67834d68931a90a467c6c55bb051c6b1916f4b15a273916a46b7f`;
  the ledger stores only the canonical digest. The revision is unchanged, so
  no new read record is required.
- Sections read as evidence: "Issues and considerations", "Scatter by
  distribution (overview)" and "Scatter by auction (overview)". The existing
  record's `sections_read` includes all three.
- Exact quotes used in the owner section and metadata:

      When requests are scattered to multiple recipients, some recipients can
      time out. In these cases, the implementation should communicate to the
      client that the response is incomplete.

      It can configure a timeout parameter to ignore responses that take too
      long.

      The responses that time out are ignored.

      The aggregator combines the partial responses and returns the final
      result to the client.

      Because the root controller isn't aware of the recipients, the gathering
      process uses an aggregator (another messaging pattern) to collect the
      responses and distill them into a single response message.

- Limits: one living AWS page; no benchmark, local execution or production
  observation. The page supports timeout handling, a client-visible incomplete
  response, ignoring timed-out responses, returning a combined result from
  partial responses and the aggregator-as-related-pattern comparison. It does
  not establish a bounded partial-result contract, a failure rule, a
  cancellation rule or a standalone-aggregator decision; those remain Tycho
  guidance.

## Book edits

### V04/C06 owner `messaging-families-and-durable-workflows.md#scatter-gather`

- Frontmatter adds `src.enterprise-integration` and
  `src.aws-scatter-gather` to `evidence_scope.source_ids`; sets the review
  status to `self-checked`, review/update and inspection dates to 2026-10-30
  and the reviewer to "Automated authoring agent".
- The existing mechanism paragraph is retained. The old failure/alternative
  paragraph is replaced with:
  - a **Failure and recovery** paragraph that quotes the AWS incomplete-response,
    timeout-parameter, timeout-ignore and partial-return sentences, then labels
    the bounded partial-result, failure and cancellation rules as Tycho
    guidance;
  - an **Alternative** paragraph that quotes the AWS aggregator-as-another-
    pattern sentence, states that this supports a message-aggregation comparison
    rather than a standalone alternative, and labels the aggregator-alone
    decision and reversal as Tycho synthesis;
  - a **Limits** paragraph and a **Source boundary** paragraph with the URL
    scope, sections and canonical hash.
- The frontmatter gains two source-id lines, so `### Scatter-Gather` moves
  from line 142 to line 144. The page is 184 lines.
- Raw SHA-256:
  `a407f00eb3ef31d1eab70e3e667274214d3281c31f69223414470e260da715a0`.
- Historical-view SHA-256:
  `3bb5dff1e57bd1030a281c257b7debe2556dff16a1a56e72d63d69f984600a9b`.
- The same two added lines move `### Aggregator` from line 117 to line 119.
  That is a metadata-only consequence; the Aggregator text is unchanged.

### V11/C03 inline card `### Scatter-Gather`

- Frontmatter is unchanged; `src.aws-scatter-gather` is already declared.
- **Competing alternative** now states the Tycho synthesis, says the AWS page
  supports only the aggregator-as-another-pattern comparison, and keeps the
  reversal condition.
- **Failure and recovery** now names the AWS timeout, incomplete-response,
  timeout-ignore and combined-result statements, then labels the bounded
  partial-result, failure and cancellation rules as Tycho guidance.
- **Sources** now names the "Issues and considerations" and
  scatter-by-auction sections; the existing record citation remains.
- `### Scatter-Gather` stays at line 338. The chapter page is 561 lines.
- Raw SHA-256:
  `a79ce25c2e8b8fc6d09b33a32a2ddaf34d67bbbdd6072818e0d3e4df56d5597d`.
- Historical-view SHA-256:
  `6d8c387fdeaf2d4e376d29d7b7329a44bfc111db0580c30e05c6120a169270f9`.

No other book file, edition JSON, promotion or generated file is changed by
this lane.

## Metadata needs (integrator)

The following patch was exercised in a detached scratch copy of this worktree,
not in the lane commit. It produced the validation results in the next section.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.scatter-gather`:

- Set `owner.line` to 144 (was 142).
- Set `technical_evidence.failure_recovery.state` to `supported`.
  - `quote`: "When requests are scattered to multiple recipients, some
    recipients can time out. In these cases, the implementation should
    communicate to the client that the response is incomplete."
  - `binding`: AWS, record `read.aws-scatter-gather.2026-10-28`, section
    "Issues and considerations", quote as above, revision `4b5c777b...`.
  - Add supporting bindings, all AWS and revision `4b5c777b...`:
    "Scatter by distribution (overview)" for "It can configure a timeout
    parameter to ignore responses that take too long.", "The responses that
    time out are ignored." and "The aggregator combines the partial responses
    and returns the final result to the client."
  - `reason`: state that AWS supports recipient timeouts, a client-visible
    incomplete response, ignoring timed-out responses and returning a combined
    partial result; the bounded partial-result/failure rule and cancellation are
    Tycho guidance.
- Set `technical_evidence.alternative.state` to `supported`.
  - `quote`: "Tycho synthesis: an aggregator alone is the alternative when
    responses already exist and no broadcast is needed; reverse the choice when
    only already-produced responses must be combined."
  - `binding`: AWS, record `read.aws-scatter-gather.2026-10-28`, section
    "Scatter by auction (overview)", quote "Because the root controller isn't
    aware of the recipients, the gathering process uses an aggregator (another
    messaging pattern) to collect the responses and distill them into a single
    response message.", revision `4b5c777b...`.
  - `reason`: state that AWS describes the aggregator as another messaging
    pattern that collects and distills responses, supporting a message-
    aggregation comparison; the standalone aggregator alternative and reversal
    are Tycho synthesis, not a source statement.
- Add `source_support.auxiliary` entry for `src.aws-scatter-gather`, record
  `read.aws-scatter-gather.2026-10-28`, revision `4b5c777b...`.
- Set `decision_evidence.competing_alternative` to the exact new card field:
  "Tycho synthesis: a standalone aggregator fits when responses already exist
  and no broadcast is needed. The AWS page supports only the comparison: it
  calls the aggregator "another messaging pattern" that collects and distills
  responses, while scatter-gather adds the broadcast. Reverse the choice when
  only already-produced responses must be combined."
- Replace `notes` with: "Failure/recovery bound 2026-10-30 to AWS
  recipient-timeout, incomplete-response, timeout-ignore and partial-response
  return statements; alternative bound to the AWS aggregator-as-another-pattern
  comparison, with the standalone aggregator alternative and reversal labelled
  Tycho synthesis. Coverage partial-bounded; no promotion."
- Summary: `failure_recovery_supported` 54 -> 55 and
  `alternative_supported` 65 -> 66. `technical_partial_bounded` stays 21,
  `technical_partial` stays 86 and `technical_sufficient` stays 38. No other
  counter changes.
- Entry `tycho.pattern.aggregator`: set `owner.line` to 119 (was 117). No
  other Aggregator field changes.

### Source register `sources/register.json`

- Update `src.aws-scatter-gather`: set `access_checked` to 2026-10-30 and
  append "canonical digest reconfirmed 2026-10-30" to the version string.
  Keep `content_verified` 2026-10-28 and keep the existing URL, scope, license
  note and observed title. Regenerate `sources/CATALOG.md` with
  `python3 scripts/source_catalog.py` if the version string changes.

### Registry `edition/patterns/registry.v1.json`

Entry `tycho.pattern.scatter-gather`:

- Keep `technical_owner.state`, `coverage.technical`, `coverage.decision`
  and `coverage.overall` at `partial-bounded`; the entry is not promoted.
- Replace `notes` with the same text proposed for owner-unit `notes`.
- Set `updated_at` to 2026-10-30.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B24 scatter-gather source binding".

- `directory_documents`:
  - Owner path, previous
    `282bc7a5b163358f91b4b3bc49d82e52145fa79f61136c8b667855bef1bd28f5`
    (migration baseline), current
    `3bb5dff1e57bd1030a281c257b7debe2556dff16a1a56e72d63d69f984600a9b`
    (historical-view text after link rewriting).
  - Card path, previous
    `6019fa28b483a027dc816d6797dd20564c2dc1c8665f1112c66fb34984a84c80`
    (migration baseline), current
    `6d8c387fdeaf2d4e376d29d7b7329a44bfc111db0580c30e05c6120a169270f9`
    (historical-view text after link rewriting).
- Leave `source_blocks`, `enrichment_documents`, `enrichment_additions`
  and `enrichment_baselines` empty. The owner page is retained and
  `validate_enrichment.py` passes without a baseline revision.

### Card path `edition/patterns/card-batches.v1.json`

The card is still inline in the V11/C03 `README.md`, so the entry has no
`card_path` and preflight reports it missing. The integrator must either split
the card to a dedicated page and register its `card_path`, or explicitly
register the inline chapter path. A split card must keep
`src.enterprise-integration` and `src.aws-scatter-gather` in
`evidence_scope.source_ids` and the 2026-10-30 dates. No split is performed by
this lane. The scratch run used a temporary pointer to the V11/C03
`README.md`; that is a check only, not a real registration.

### Unchanged metadata

- `edition/patterns/source-plan.v1.json`: no change. Both source units are
  already listed and the existing record revision is unchanged.
- `edition/patterns/reading-ledger.v1.json`: no change. The 2026-10-30
  re-fetch reproduced the recorded canonical digest.

### Derived artifacts and tests

The scratch metadata patch changes two owner-unit counters and two owner lines
but does not regenerate derived atlas artifacts. Update or regenerate the
affected coverage, census, reverse-map and sufficient-workflow artifacts at
batch end. Run the complete suite once at batch end; any failure caused by a
stale derived count or hash is not a lane content failure.

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
  tycho.pattern.scatter-gather` - FAIL: failure_recovery partial, alternative
  partial and card_path missing, because shared metadata is unchanged.
- `python3 scripts/validate_pattern_owner_units.py` - FAIL
  `owner-units-unit-ambiguous: Aggregator` because the owner headings moved by
  two lines and the metadata is unchanged.
- `python3 scripts/validate_directory_migration.py` - FAIL
  `directory-baseline-payload-drift` until the content revision is applied.
- `python3 scripts/validate_pattern_cards.py` - PASS.
- `python3 scripts/validate_pattern_registry.py` - PASS.
- `python3 scripts/validate_sources.py` - PASS; 283 source records.
- `python3 scripts/validate_book_metadata.py` - PASS; 478 canonical documents.
- `python3 scripts/validate_enrichment.py` - PASS.

In a detached scratch copy with the metadata patch above and a scratch-only
`card_path` pointing at the V11/C03 `README.md`:

    PASS: tycho.pattern.scatter-gather
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: pattern registry 145 entries, 11 families
    PASS: 283 source records, mandatory IDs, cross-references and catalogue
    freshness
    PASS: 478 canonical documents

    directory migration: PASS; 478 canonical documents, 339 moved documents,
    12 post-migration directories
    enrichment: PASS; explicit membership and byte conservation

Derived atlas, coverage and semantic-audit artifacts still need regeneration
because their hashes and counters were not refreshed. The scratch `card_path`
is a check only.

## Limits

The binding is one AWS Prescriptive Guidance page. It describes recipient
timeouts, a client-visible incomplete response, ignoring timed-out responses
and the aggregator's role in returning a combined result, but it does not
define a bounded partial-result contract, a failure rule, cancellation or a
standalone-aggregator alternative. Those are Tycho guidance and are labelled in
the owner section and card. No timeout, partial response, cancellation,
benchmark or production behavior was executed or observed.

Coverage remains `partial-bounded`; independent review, promotion, owner
acceptance and merge permission are not claimed. The historical record that this
entry was 2/4 and that both dimensions were partial is retained in the pilot
batch records; this note records the lane-local change, not a promotion.

## Review needs

- Request a fresh external review under the book/atlas gate. The historical
  Scatter-Gather reviews predate this text; this lane is self-checked only.
- The reviewer should check the AWS quote-to-claim fit, the Tycho labels for the
  aggregator-alone decision and bounded partial-result policy, the section and
  revision, the two owner-line shifts and the inline-card boundary.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- `book/volumes/v04-distributed-coordination-and-events/`
  `c06-messaging-families-and-delivery-contracts/`
  `messaging-families-and-durable-workflows.md` (concatenate the three lines).
- `book/volumes/v11-pattern-atlas/c03-messaging-integration/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
