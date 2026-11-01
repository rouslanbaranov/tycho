# B23 — Two-Phase Commit failure/recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and invariant were supported;
failure/recovery and alternative were partial. This lane binds both dimensions
to public units and labels the remaining protocol-level framing as Tycho. The
entry is 4/4 on technical dimensions after the integrator metadata patch; the
scratch preflight passes 1/1. Promotion is not claimed or ready.

## Lane coordinates

- Parent HEAD: `379c6eba12f89ccc160bcb056056438b792a05b2`
  ("feat(research): promote Dead Letter Channel").
- Branch: `b23-2pc`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b23-2pc`.
- Scope: the V04/C03 owner section `### Two-Phase Commit (2PC)` in
  `invariants-isolation.md` and the inline V11/C04 card
  `### Two-Phase Commit (2PC)` in the V11/C04 `README.md`.
- Owner path (concatenate the two lines):

      book/volumes/v04-distributed-coordination-and-events/
      c03-consistency-and-distributed-transactions/invariants-isolation.md

- Card path:
  `book/volumes/v11-pattern-atlas/c04-consistency-events/README.md`.
- The card remains inline; the integrator owns any split and `card_path`
  registration.
- Single-entry lane; no other entry, shared owner page, promotion or generated
  file is changed.

## Candidate evaluation

- PostgreSQL 18, PREPARE TRANSACTION:
  `https://www.postgresql.org/docs/18/sql-prepare-transaction.html`.
  The existing `src.postgresql` source has a 2PC section record, but that
  section does not address coordinator crash, in-doubt outcomes, a decision
  record or held locks. The PREPARE TRANSACTION page does state the durable
  on-disk prepared state, crash-surviving committed state, held locks and the
  external transaction manager requirement.
- Oracle Database 26, "Distributed Transactions Concepts":
  `https://docs.oracle.com/en/database/oracle/oracle-database/26/admin/` +
  `distributed-transactions-concepts.html` (concatenate).
  Selected because it explicitly defines in-doubt transactions after a 2PC
  failure, prepared nodes waiting for the global coordinator, redo-log and
  commit-point records, data locked until resolution and a manual resolution
  path. It is product-specific Oracle behavior, not a portable algorithm.
- microservices.io, "Saga": `https://microservices.io/patterns/data/saga.html`.
  The existing record `read.batch2-saga.2026-10-21` is reused. It states that
  2PC is not an option in the pattern's context, defines a saga by local
  transactions and compensating actions, lists lack of automatic rollback and
  lack of isolation, and shows an order in a PENDING state.
- Microsoft Learn, "Saga distributed transactions pattern":
  `https://learn.microsoft.com/en-us/azure/architecture/patterns/saga`.
  The existing record `read.microsoft-saga-azure.2026-10-30` is reused for its
  statement that compensation can fail and leave an inconsistent state.

No selected unit presents a portable 2PC recovery algorithm. The coordinator-
crash framing and the "avoids prepared locks" comparison are therefore labelled
as Tycho readings in the owner section.

## Source binding

### PostgreSQL 18 PREPARE TRANSACTION

- Source id: `src.postgresql` (existing).
- Proposed record: `read.pg-prepare-transaction.2026-10-30`; access date
  2026-10-30.
- URL: `https://www.postgresql.org/docs/18/sql-prepare-transaction.html`.
- Unit label: `PREPARE TRANSACTION — PostgreSQL 18`.
- Unit type: `documentation-page`.
- Canonical text SHA-256:
  `8cf69b9a6e4e0d7f2318a05bb054f6ca67e6a486e564d892db4f858835aa0bd5`.
- Raw HTML SHA-256:
  `2a2fe0714e1b6c7d2c830918bb7c2b7df9e3bfd926d1c5d5675c298b727b649b`.
- Fetch check: two public HTTPS GETs on 2026-10-30 served identical 19,968-byte
  representations and produced the same canonical and raw hashes.
- Sections read as evidence: Description and Notes. The Synopsis, Parameters,
  Examples and Compatibility sections and linked pages were not used.
- Exact quotes used in the owner section and metadata:

      After this command, the transaction is no longer associated with the
      current session; instead, its state is fully stored on disk, and there is
      a very high probability that it can be committed successfully, even if a
      database crash occurs before the commit is requested.

      Keep in mind also that the transaction continues to hold whatever locks
      it held.

      If you have not set up an external transaction manager to track prepared
      transactions and ensure they get closed out promptly, it is best to keep
      the prepared-transaction feature disabled by setting
      max_prepared_transactions to zero.

      It is unwise to leave transactions in the prepared state for a long time.

- Limits: one PostgreSQL 18 page; product-specific SQL behavior; no database,
  prepared transaction, crash or recovery test was executed.

### Oracle Database 26, Distributed Transactions Concepts

- Proposed source id: `src.oracle-distributed-transactions`.
- Proposed record: `read.oracle-distributed-transactions.2026-10-30`; access
  date 2026-10-30.
- Canonical URL (concatenate the two lines):
  `https://docs.oracle.com/en/database/oracle/oracle-database/26/admin/`
  `distributed-transactions-concepts.html`.
- Unit label: `Distributed Transactions Concepts — Oracle Database 26`.
- Unit type: `documentation-page`.
- Canonical text SHA-256:
  `509659faa90d9379b750679db38da26eb48e83428585e16f50247972f698ca25`.
- Raw HTML SHA-256:
  `355acefc2e541d3ba7a2d500d6cc0f91240d9ce0c8a1b61190ab4ea5fd03fe4e`.
- Fetch check: two public HTTPS GETs on 2026-10-30 served identical
  106,035-byte representations and produced the same canonical and raw hashes.
  The page reports Release 26, a content date of 2026-07-20 and the document
  identifier `GUID-C1B373BA-410E-4F38-8522-F72A74665919`.
- Sections read as evidence: "Two-Phase Commit Mechanism", "Commit Point Site",
  "Prepare Phase", "Commit Phase", "In-Doubt Transactions",
  "About In-Doubt Transactions", "Automatic Resolution of In-Doubt
  Transactions" and "Manual Resolution of In-Doubt Transactions".
- Exact quotes used in the owner section and metadata:

      A transaction becomes in-doubt if the two-phase commit mechanism fails.

      What happens if any of the three phases fails because of a system or
      network error? The transaction becomes in-doubt.

      A server system running Oracle Database software crashes

      Records information in the redo logs so that it can subsequently either
      commit or roll back the transaction, regardless of intervening failures

      The prepared nodes then wait until a COMMIT or ROLLBACK request is
      received from the global coordinator.

      The node guarantees that locks held for the transaction are able to
      survive a failure.

      Because the commit point log contains a record of the commit, the
      transaction is considered committed even though some participating nodes
      may still be only in the prepared state and the transaction not yet
      actually committed at these nodes.

      Until RECO can resolve the transaction, the data is locked for both reads
      and writes.

      If necessary, force a commit using the COMMIT FORCE statement or a
      rollback using the ROLLBACK FORCE statement.

- Limits: product-specific Oracle behavior, including RECO and commit-point
  roles. The page supports an in-doubt outcome after a failure, prepared nodes
  waiting for the coordinator, a durable redo/commit-point record, locked data
  and a resolution path. It does not establish a portable decision-log format
  or a universal coordinator-crash algorithm; those framings remain Tycho
  guidance. No database or recovery test was executed.

### microservices.io Saga (existing unit)

- Source id: `src.microservices-patterns` (existing).
- Record: `read.batch2-saga.2026-10-21`; access date 2026-10-21.
- Unit label: `Saga — pattern page`; unit type `pattern-page`.
- Recorded revision:
  `54805df89f619c8432fd280263a88670ed66fac6cbe0b5429a1ebdc5d4cd1047`.
  The existing record stores the raw served HTML digest. The current canonical
  text digest is
  `d6a4a989bf382419f6792d9afdf3baa49eabc0ab5879222ea1a5f2d2bae4814e`,
  but the owner-unit revision must match the record field above. Two fetches
  on 2026-10-30 returned the same raw HTML, so the page is unchanged.
- Sections used: Forces, Solution, Resulting context and
  "Example: Choreography-based saga".
- Exact quotes used in the owner section and metadata:

      2PC is not an option

      the changes made by the completed steps are undone by compensating
      transactions

      Lack of automatic rollback - a developer must design compensating
      transactions that explicitly undo changes made earlier in a saga rather
      than relying on the automatic rollback feature of ACID transactions

      Lack of isolation (the “I” in ACID) - the lack of isolation means that
      there’s risk that the concurrent execution of multiple sagas and
      transactions can use data anomalies.

      The Order Service receives the POST /orders request and creates an Order
      in a PENDING state

- Limits: public pattern description, not a benchmark or a recovery
  specification. It does not name prepared locks; the "avoids prepared locks"
  inference is Tycho guidance.

### Microsoft Learn, Saga distributed transactions pattern (existing unit)

- Source id: `src.microsoft-cloud-patterns` (existing).
- Record: `read.microsoft-saga-azure.2026-10-30`; access date 2026-10-30.
- Unit label:
  `Saga distributed transactions pattern — Azure Architecture Center`;
  unit type `pattern-page`.
- Recorded revision:
  `84fba1653e842f2af72959d9ac6c3d88821c179804049849e09431b5132069ca`.
- Sections used: Solution and Problems and considerations.
- Exact quotes used in the owner section and metadata:

      If a step fails, a series of compensating transactions undoes the changes
      that the completed steps made.

      Compensating transactions might not always succeed, which can leave the
      system in an inconsistent state.

- Limits: vendor pattern guidance; no benchmark or local execution.

## Book edits

### V04/C03 owner `invariants-isolation.md#two-phase-commit-2pc`

- Frontmatter adds `src.postgresql`, `src.oracle-distributed-transactions`,
  `src.microservices-patterns` and `src.microsoft-cloud-patterns` to
  `evidence_scope.source_ids`; sets the scope status to `source-linked`,
  review/update and inspection dates to 2026-10-30 and the reviewer to
  "Automated authoring agent".
- The existing mechanism paragraph is retained. The old failure sentence, saga
  alternative and limits paragraph are replaced with:
  - a **Failure and recovery** paragraph that quotes the Oracle in-doubt,
    waiting, redo-log, commit-point and lock sentences and the PostgreSQL
    on-disk, crash-survival, held-lock and external-transaction-manager
    sentences;
  - an **Alternative** paragraph that quotes the Saga compensation, lack of
    automatic rollback, lack of isolation and PENDING sentences and the Azure
    compensation-failure sentence, and labels the avoided-locks and
    local-transaction comparisons as Tycho guidance;
  - a **Limits** paragraph and a **Source boundary** paragraph with URLs,
    sections and canonical/recorded hashes;
  - an explicit Tycho label for the coordinator-crash framing.
- `### Two-Phase Commit (2PC)` moves from line 126 to line 130 because the
  frontmatter gains four source-id lines. The page is 172 lines.
- Raw SHA-256:
  `0a1320daac84db46f683e9af27dac84e8d272d41bfef480f2cae7655506eed02`.
- Historical-view SHA-256:
  `3f3eeacb4037f2f8b2e5b828a25a644c1a295b7b2f38375872111c6cd7941a13`.

### V11/C04 inline card `### Two-Phase Commit (2PC)`

- Frontmatter adds `src.oracle-distributed-transactions` to
  `evidence_scope.source_ids`.
- **Competing alternative** now names the public Saga pattern's "2PC is not an
  option" statement, its local-transaction/compensation mechanism, visible
  intermediate states and non-atomic outcomes, and keeps the reversal
  condition.
- **Failure and recovery** now names in-doubt state, locked prepared data, the
  commit-point log and external transaction manager, and automatic or forced
  resolution.
- **Sources** adds the PostgreSQL PREPARE TRANSACTION, Oracle, Saga and Azure
  records and sections; the existing PostgreSQL 2PC record remains cited.
- `### Two-Phase Commit (2PC)` moves from line 458 to line 459 because the
  frontmatter gains one source-id line. The chapter page is 526 lines.
- Raw SHA-256:
  `a01c2a24e954d29ed8fdc8622ebb343e5da957f3927a5a64e47829d199d7e75a`.
- Historical-view SHA-256:
  `c0961ea30bebf8575739676ac3eaeb66f4f7d14475a965933b75c14c78cb6f60`.

No other book file, edition JSON, promotion or generated file is changed by
this lane.

## Metadata needs (integrator)

The following patch was exercised in a detached scratch copy of this worktree,
not in the lane commit. It produced the validation results in the next section.

### Source register `sources/register.json`

- Add `src.oracle-distributed-transactions`: title "Distributed Transactions
  Concepts"; category "databases"; publisher "Oracle"; kind "official-docs";
  URL and resolved URL as above; topics
  `["databases", "distributed-transactions", "recovery", "locking"]`;
  priority "supporting"; planned use "Two-phase commit in-doubt state,
  redo-log and commit-point records, prepared locks and resolution.";
  admission "admitted-for-research"; access "public-web-or-author-download";
  reading status "full-public-page-inspected"; version names Release 26, the
  2026-07-20 content date and canonical hash `509659...`; access and content
  verification 2026-10-30; license note "Public Oracle documentation; cite
  short excerpts and paraphrase; do not mirror."; verification scope names the
  eight sections above and excludes other sections, linked pages, images and
  any execution; observed title "Distributed Transactions Concepts".
- Update `src.postgresql`: append the PREPARE TRANSACTION canonical hash
  `8cf69b...` and 2026-10-30 access to its version string; append the
  Description/Notes reading scope and the no-database-test limit to
  `verification_scope`; set `access_checked` to 2026-10-30. Keep
  `content_verified` null.
- Set `updated` to 2026-10-30 and regenerate `sources/CATALOG.md` with
  `python3 scripts/source_catalog.py`. The scratch run reports 283 source
  records.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add two records and keep `updated` at 2026-10-30.

- `read.pg-prepare-transaction.2026-10-30`: source `src.postgresql`; URL,
  label and type as above; access date 2026-10-30; access method names two
  identical 19,968-byte public HTTPS GETs, the canonical hash and the raw
  hash; `sections_read` is exactly `["PREPARE TRANSACTION", "Description",
  "Notes"]`; `sections_not_read` names Synopsis, Parameters, Examples,
  Compatibility, linked pages and navigation; one tables/figures note says no
  table or figure was used; license note as above; `claims_supported`
  contains the four PostgreSQL quotes above; `claims_not_supported` names a
  coordinator crash-recovery algorithm, other versions and execution;
  limitations say one page and no test; `content_sha256` is `8cf69b...`;
  `read_scope` names Description and Notes; reviewer "Automated authoring
  agent"; status "read".
- `read.oracle-distributed-transactions.2026-10-30`: source
  `src.oracle-distributed-transactions`; URL, label and type as above; access
  date 2026-10-30; access method names two identical 106,035-byte public HTTPS
  GETs, the canonical hash and the raw hash; `sections_read` is exactly the
  eight-section list above; `sections_not_read` names the other page sections,
  linked pages, images and navigation; one tables/figures note says tables
  were read in text form and not reproduced; license note as above;
  `claims_supported` contains the nine Oracle quotes above;
  `claims_not_supported` names a product-neutral decision-log format, a
  universal coordinator-crash rule, linked pages/images and execution;
  limitations name the living product page, RECO-specific behavior and no
  test; `content_sha256` is `509659...`; `read_scope` names the selected
  sections; reviewer "Automated authoring agent"; status "read".

### Source plan `edition/patterns/source-plan.v1.json`

Append four units to `tycho.pattern.two-phase-commit-2pc`, after the existing
PostgreSQL 2PC unit and in this order. The `sections` list must equal the
record's `sections_read` exactly.

- `src.postgresql`, unit `PREPARE TRANSACTION — PostgreSQL 18`, type
  `documentation-page`, URL above, sections `["PREPARE TRANSACTION",
  "Description", "Notes"]`, status `read`, record
  `read.pg-prepare-transaction.2026-10-30`, blocked reason null.
- `src.oracle-distributed-transactions`, unit `Distributed Transactions
  Concepts — Oracle Database 26`, type `documentation-page`, URL above,
  sections as the eight-section record list, status `read`, record
  `read.oracle-distributed-transactions.2026-10-30`, blocked reason null.
- `src.microservices-patterns`, unit `Saga — pattern page`, type
  `pattern-page`, URL `https://microservices.io/patterns/data/saga.html`,
  sections exactly the existing record's `sections_read` (Pattern: Saga,
  Context, Problem, Forces, Solution, Example: Choreography-based saga,
  Example: Orchestration-based saga, Resulting context, Related patterns,
  Learn more, Example code), status `read`, record
  `read.batch2-saga.2026-10-21`, blocked reason null.
- `src.microsoft-cloud-patterns`, unit `Saga distributed transactions
  pattern — Azure Architecture Center`, type `pattern-page`, URL
  `https://learn.microsoft.com/en-us/azure/architecture/patterns/saga`,
  sections exactly the existing record's `sections_read` (Solution, Key
  concepts in the Saga pattern, Problems and considerations), status `read`,
  record `read.microsoft-saga-azure.2026-10-30`, blocked reason null.

Set `summary.required_units` 178 -> 182, `summary.read_units` 177 -> 181 and
`summary.ledger_records` 147 -> 149. `planned_units` stays 0 and
`blocked_units` stays 1. Set `updated` to 2026-10-30. Recompute
`registry_sha256` after saving the registry; the scratch value is the
SHA-256 of the saved registry file, not a supplied constant.

### Registry `edition/patterns/registry.v1.json`

Entry `tycho.pattern.two-phase-commit-2pc`:

- Append the four source units with the exact source-plan labels and status
  `read`.
- Keep `technical_owner.state`, `coverage.technical`, `coverage.decision`
  and `coverage.overall` at `partial-bounded`; the entry is not promoted.
- Replace the notes with: "Phase 3 C04 card; bounded owner section and backlink
  are self-checked, not independent-reviewed or sufficient. Failure/recovery
  bound 2026-10-30 to Oracle in-doubt/redo-log/lock statements and PostgreSQL
  prepared-state/lock statements; alternative bound to microservices.io Saga
  and Microsoft Azure Saga compensation. Coverage partial-bounded."
- Set `updated_at` to 2026-10-30.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.two-phase-commit-2pc`:

- Set `owner.line` to 130 (was 126).
- Set `technical_evidence.failure_recovery.state` to `supported`.
  - `quote`: "A transaction becomes in-doubt if the two-phase commit
    mechanism fails."
  - `binding`: Oracle, record
    `read.oracle-distributed-transactions.2026-10-30`, section
    "In-Doubt Transactions", quote as above, revision `509659...`.
  - Add supporting bindings: Oracle "About In-Doubt Transactions" for the
    system/network failure question and for "data is locked for both reads and
    writes"; Oracle "Prepare Phase" for the redo-log sentence, the
    prepared-nodes-wait sentence and the lock-survival sentence; Oracle
    "Commit Point Site" for the commit-point log sentence; Oracle "Manual
    Resolution of In-Doubt Transactions" for the COMMIT FORCE/ROLLBACK FORCE
    sentence; PostgreSQL "Description" for the on-disk/crash sentence and
    "Notes" for the held-lock and external-transaction-manager sentences. All
    Oracle bindings use `509659...`; all PostgreSQL bindings use
    `8cf69b...`.
  - `reason`: state that Oracle supplies the in-doubt, waiting, redo-log,
    commit-point, lock and resolution statements and PostgreSQL supplies the
    durable prepared-state, crash-survival, held-lock and external-manager
    statements; the coordinator-crash framing is a Tycho reading of the
    documented roles and no portable algorithm is claimed.
- Set `technical_evidence.alternative.state` to `supported`.
  - `quote`: "the changes made by the completed steps are undone by
    compensating transactions".
  - `binding`: microservices.io Saga, record
    `read.batch2-saga.2026-10-21`, section "Solution", quote as above,
    revision `54805...`.
  - Add supporting bindings: Saga "Resulting context" for the lack of
    automatic rollback sentence and the lack of isolation sentence; Saga
    "Example: Choreography-based saga" for the PENDING sentence; Azure
    "Solution" for the compensating-transactions sentence and "Problems and
    considerations" for the inconsistent-state sentence. Saga bindings use
    `54805...`; Azure bindings use `84fba...`.
  - `reason`: state that the Saga page frames 2PC as not an option, defines
    compensation, lists the rollback/isolation drawbacks and shows a PENDING
    state, and Azure states that compensation can fail and leave an
    inconsistent state; the avoided-locks and local-transaction comparisons
    remain Tycho guidance.
- Add `source_support.auxiliary` entries for the two new records and the two
  reused records, with the revisions above.
- Set `decision_evidence.competing_alternative` to the exact new card field:
  "Saga/compensation or one local transaction. The public Saga pattern says
  "2PC is not an option" in its context and replaces atomic commit with local
  transactions and compensating actions, accepting visible intermediate states
  and non-atomic outcomes. Reverse the choice when blocking and coordinator
  complexity exceed atomicity benefit."
- Replace `notes` with: "Failure/recovery bound 2026-10-30 to Oracle
  in-doubt, redo-log, commit-point and lock statements plus PostgreSQL
  prepared-state and lock statements. Alternative bound to the microservices.io
  Saga compensation/PENDING text and Microsoft Azure compensation-failure text.
  Coordinator-crash framing and 'avoids prepared locks' remain Tycho guidance.
  Coverage partial-bounded; no promotion."
- Summary: `failure_recovery_supported` 53 -> 54 and
  `alternative_supported` 64 -> 65. `technical_partial_bounded` stays 22,
  `technical_partial` stays 86 and `technical_sufficient` stays 37. No
  other counter changes.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B23 two-phase commit source binding".

- `directory_documents`:
  - Owner path, previous
    `b07eaf66ade3d69b87eaa4b7a1dc0d5c82129c89af7135f14829956acd7f2066`
    (migration baseline), current
    `3f3eeacb4037f2f8b2e5b828a25a644c1a295b7b2f38375872111c6cd7941a13`
    (historical-view text after link rewriting).
  - Card path, previous
    `4b78177af1e1f2bf96c7488ebf4e0a0512e0bb2a1f35a1e52408720fba3df22d`
    (migration baseline), current
    `c0961ea30bebf8575739676ac3eaeb66f4f7d14475a965933b75c14c78cb6f60`
    (historical-view text after link rewriting).
- Leave `source_blocks`, `enrichment_documents`,
  `enrichment_additions` and `enrichment_baselines` empty. The owner page is
  retained and `validate_enrichment.py` passes without a baseline revision.

### Card path `edition/patterns/card-batches.v1.json`

The card is still inline in the V11/C04 `README.md`, so the 2PC entry has no
`card_path` and preflight reports it missing. The integrator must either split
the card to a dedicated page and register its `card_path`, or explicitly
register the inline chapter path. A split card must keep all five source ids in
`evidence_scope.source_ids` and the 2026-10-30 dates. No split is performed by
this lane. The scratch run used a temporary pointer to the V11/C04
`README.md`; that is a check only, not a real registration.

### Derived artifacts and tests

The scratch metadata patch changes source-plan and owner-unit counters but does
not regenerate derived atlas artifacts. The pattern unit tests in the scratch
tree fail on stale hardcoded counts/hashes (for example source units 178 vs
182, read units 177 vs 181) and on a stale coverage-map registry hash. Update
or regenerate the affected derived files and hardcoded test expectations at
batch end; do not treat the scratch pattern-test failures as lane content
failures.

## Validation

At the parent HEAD:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still required.

After the two book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` - PASS; V11 prose <=100,
  145 exact owner-link exceptions.
- `python3 scripts/check_boundary.py` - PASS; independent-origin review still
  required.
- `python3 scripts/validate_pattern_sources.py` - PASS, 177 read and 147
  ledger records, because shared metadata is unchanged.
- `python3 scripts/validate_pattern_registry.py` - PASS.
- `python3 scripts/validate_pattern_cards.py` - PASS.
- `python3 scripts/validate_pattern_owner_units.py` - FAIL
  `owner-units-unit-ambiguous: Two-Phase Commit (2PC)` because the owner
  heading moved from line 126 to 130 and the metadata is unchanged.
- `python3 scripts/validate_directory_migration.py` - FAIL
  `directory-baseline-payload-drift` until the content revision is applied.
- `python3 scripts/validate_enrichment.py` - PASS.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.two-phase-commit-2pc` - FAIL: failure_recovery partial,
  alternative partial and card_path missing.
- `python3 scripts/validate_sources.py` - FAIL
  `Unknown source reference in authoring/B23-TWO-PHASE-COMMIT-LANE-2026-10-30.md`
  because the new `src.oracle-distributed-transactions` id is not registered yet;
  the scratch tree passes with 283 records.

In a detached scratch copy with the metadata patch above and a scratch-only
`card_path` pointing at the V11/C04 `README.md`:

    PASS: tycho.pattern.two-phase-commit-2pc
    1/1 entries preflight clean

    PASS: source plan 145 entries; 181 read; 149 ledger records
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: 283 source records, mandatory IDs, cross-references and catalogue freshness
    PASS: V11 prose <=100; 145 exact owner-link exceptions

    directory migration: PASS; 477 canonical documents, 339 moved documents,
    12 post-migration directories
    enrichment: PASS; explicit membership and byte conservation

Derived atlas, coverage and semantic-audit artifacts still need regeneration
because their hashes and counters were not refreshed. The scratch `card_path`
is a check only.

## Limits

The failure binding is product-specific: Oracle's in-doubt and RECO behavior
and PostgreSQL's prepared-transaction SQL behavior. Neither page is a
protocol-neutral recovery specification, and no coordinator crash, prepared
transaction, lock wait or forced resolution was executed. The alternative
binding is a public pattern description plus vendor guidance, not a benchmark
or proof that a saga preserves any particular business invariant. The Tycho
labels in the owner section mark the coordinator-crash framing, the
"avoids prepared locks" comparison and the single-local-transaction preference
as guidance rather than source claims.

Coverage remains `partial-bounded`; independent review, promotion, owner
acceptance and merge permission are not claimed. The historical record that
this entry was 2/4 and that both dimensions were partial is retained in the
pilot batch records; this note records the lane-local change, not a promotion.

## Review needs

- Request a fresh external review under the book/atlas gate. The historical
  2PC reviews predate this text; this lane is self-checked only.
- The reviewer should check the Oracle/PostgreSQL quote-to-claim fit, the
  Tycho labels for the coordinator-crash and saga-comparison inferences, the
  source revisions, and the inline-card/owner-link boundary.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- `book/volumes/v04-distributed-coordination-and-events/`
  `c03-consistency-and-distributed-transactions/invariants-isolation.md`
  (concatenate the two lines).
- `book/volumes/v11-pattern-atlas/c04-consistency-events/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
