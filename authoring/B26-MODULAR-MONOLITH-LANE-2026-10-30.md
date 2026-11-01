# B26 — Modular Monolith invariant and failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and alternative were supported;
invariant and failure/recovery were partial. This lane binds the enforceable
parts of both dimensions to Spring Modulith 1.3.12 public pages and labels the
named owner, the single-deployable framing and the deployment blast radius as
Tycho analysis. The metadata patch was exercised in a detached scratch copy:
preflight passes 1/1, owner units, registry, cards, sources, book metadata,
directory migration and enrichment all pass. The patch is not in the lane
commit; promotion is not claimed or ready.

## Lane coordinates

- Parent HEAD: `e65664d4` ("feat(research): promote API Gateway").
- Branch: `b26-modular-monolith`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b26-modular-monolith`.
- Scope: the V02/C03 owner section `### Modular Monolith` and the inline
  V11/C01 card `### Modular Monolith`. Single-entry lane; no other entry,
  shared owner page, promotion or generated file is changed.
- Owner path (concatenate the three lines):

      book/volumes/v02-application-boundaries-and-contracts/
      c03-modular-monolith-and-internal-events/
      modular-monolith-and-internal-events.md

- Card path: `book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md`.
- The card remains inline; the integrator owns any split and `card_path`
  registration.

## Candidate evaluation

- `src.monolith-first`, record `read.monolith-first.2026-10-21`: the existing
  mechanism and alternative binding. It argues for modular design before
  distribution and warns about dependency tangles, but it does not define a
  named module owner, an allowed-call surface, a dependency test, synchronous
  cross-module call chains or a deployment blast radius. No new unit is read.
- Spring Modulith 1.3.12, `verification.html`: the verification rules reject
  module cycles, references to internal packages and, when configured,
  undeclared module dependencies. Selected for the dependency test and bypass.
- Spring Modulith 1.3.12, `fundamentals.html`: modules expose an API and hide
  internal implementation packages; the Java compiler alone cannot prevent
  illegal references. Selected for the allowed-call surface and bypass.
- Spring Modulith 1.3.12, `events.html`: event publication is synchronous by
  default, widens the transaction boundary and can lose an event when an
  asynchronous listener fails without a safety net. Selected for synchronous
  call chains and recovery.
- No selected page supports a named module owner, a single-deployable
  definition or an observed deployment blast radius. Those remain Tycho
  labels in the owner section and card.

## Source binding

### Spring Modulith — verification

- Existing source id: `src.spring-modulith`.
- Proposed record: `read.spring-modulith-verification.2026-10-30`.
- URL (concatenate the two lines):

      https://docs.spring.io/spring-modulith/reference/1.3/
      verification.html

- Unit label: "Verifying Application Module Structure".
- Unit type: `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-09-24T10:16:20Z;
  displayed version 1.3.12.
- Canonical text SHA-256:
  `c1ee41282edd5866877a4d2a09d4585196a4a2ac05a672416624e4b9eb117cd4`.
- Raw HTML SHA-256:
  `82edd76b7887a535999a412b6c0e22bafc289b183f0763ba7703733424411720`.
- Sections read: `Verifying Application Module Structure`.
- Exact quotes used:

      No cycles on the application module level — the dependencies between
      modules have to form a directed acyclic graph.

      Efferent module access via API packages only — all references to types
      that reside in application module internal packages are rejected.

      Explicitly allowed application module dependencies only (optional) — an
      application module can optionally define allowed dependencies via
      @ApplicationModule(allowedDependencies = …) . If those are configured,
      dependencies to other application modules are rejected.

- Limits: one versioned documentation page. It documents framework
  verification rules, not a universal enforcement guarantee, a local build or
  an implementation test.

### Spring Modulith — fundamentals

- Existing source id: `src.spring-modulith`.
- Proposed record: `read.spring-modulith-fundamentals.2026-10-30`.
- URL (concatenate the two lines):

      https://docs.spring.io/spring-modulith/reference/1.3/
      fundamentals.html

- Unit label: "Fundamentals".
- Unit type: `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-09-24T10:16:20Z;
  displayed version 1.3.12.
- Canonical text SHA-256:
  `6f45529855cf017220ca400ab72e87fc805cd31e044db44f47705a4ac16f95bd`.
- Raw HTML SHA-256:
  `7b3e065fe5de06348d9e5c06638bfa2e52570bed94f3085cd32c72472645eb0d`.
- Sections read: `Application Modules`, `Advanced Application Modules`,
  `Explicit Application Module Dependencies`, `Named Interfaces`.
- Exact quotes used:

      Code within those must not be referred to from other modules.

      In this case, the Java compiler is not of much use to prevent these
      illegal references.

- Limits: one versioned documentation page. It describes a framework package
  model, not every language's visibility rules or an executed build.

### Spring Modulith — working with application events

- Existing source id: `src.spring-modulith`.
- Proposed record: `read.spring-modulith-events.2026-10-30`.
- URL (concatenate the two lines):

      https://docs.spring.io/spring-modulith/reference/1.3/
      events.html

- Unit label: "Working with Application Events".
- Unit type: `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-09-24T10:16:20Z;
  displayed version 1.3.12.
- Canonical text SHA-256:
  `c15f574e8029e58e50346011402e03439590af4e3e6a3e15940fab2fa5472c6a`.
- Raw HTML SHA-256:
  `6d39cbac2cd2b461a549bff17e32998724c474c9c418625d8d97a5184c3e4735`.
- Sections read: `Working with Application Events`,
  `The Event Publication Registry`.
- Exact quotes used:

      As event publication happens synchronously by default, the
      transactional semantics of the overall arrangement stay the same as in
      the example above.

      but also for the bad as more triggered related functionality will widen
      the transaction boundary and potentially cause the entire transaction to
      fail, even if the functionality that is causing the error is not crucial.

      if the listener fails for whatever reason, the event publication is
      lost, unless each listener actually implements its own safety net.

- Limits: one versioned documentation page. It describes framework event
  handling, not a local event replay, a production failure or a benchmark.
  The mid-sentence quotations keep the source's lower-case openings.

### Monolith First — existing record

- Existing source id: `src.monolith-first`; record
  `read.monolith-first.2026-10-21`.
- URL (concatenate the two lines):

      https://martinfowler.com/bliki/
      MonolithFirst.html

- Recheck 2026-10-30: raw HTML digest
  `722d8d78beddd9e0f6ff3e856eec94dfa2b9fa3bebcaaf4c9e80ccdd3c0e1446`
  equals the record's `content_sha256`; HTTP `Last-Modified`
  2026-10-29T16:11:21Z. The `scripts/source_content_hash.py` digest is
  `9cb2a6797a8c41fabba65adcff1d5408c46814616d17e5430e1aac3ce491539f`
  because that script's fallback includes page chrome; this is not a content
  change. No new record is required.
- No new quote is bound from this source. The existing mechanism and
  alternative bindings are unchanged.

## Book edits

### V02/C03 owner section

- Frontmatter: `content_review.status` moves from `draft` to
  `self-checked`; `reviewed_at`, `updated_at` and
  `source_inspection_date` are 2026-10-30; the reviewer is
  "Automated authoring agent". `evidence_scope.source_ids` stays empty;
  its note now points to the body Source boundary instead of denying an
  inspection. The page still makes no claim-level source mapping there.
- The opening note now records the 2026-10-30 self-check instead of the
  decomposition-era draft state.
- The owner section keeps the existing definition and adds:
  - the Spring Modulith API-only access and allowed-dependency rules;
  - the internal-package rule and the Java compiler limit;
  - synchronous event publication, the widened transaction and the lost-event
    risk;
  - explicit Tycho labels for the named owner, the single-deployable framing
    and the deployment blast radius.
- The source boundary lists the existing Monolith First record and the three
  Spring Modulith 1.3.12 canonical revisions.
- Heading `### Modular Monolith` stays at line 121. The page is 167 lines.
- Raw SHA-256:
  `1c39f9803a7ce319a278168d697f927294661257d02f7e9f016f55465b4d41ad`.
- Historical-view SHA-256:
  `97d4b9b63427c73b2f69aaf4015b5edcc2d87a80d65864395db4aa784e3a2f24`.

### V11/C01 inline card

- Frontmatter adds `src.spring-modulith` to
  `evidence_scope.source_ids`. Review and inspection dates already read
  2026-10-30.
- **Failure and recovery** now names synchronous publication, the widened
  transaction, the dependency verification and the lost-event risk, and labels
  the deployment blast radius and "distributed monolith" as Tycho analysis.
- **Sources** retains the Monolith First record citation and names the three
  Spring Modulith 1.3.12 pages, pointing to the owner section for exact
  quotes, sections and revisions.
- `### Modular Monolith` moves from line 119 to line 120 because of the one
  added source id. The chapter page is 367 lines.
- Raw SHA-256:
  `3af48c7a4f514c3eb430cf37bc2ead03b9aab9db7521cda924f74759153f574e`.
- Historical-view SHA-256:
  `f89a587407423769d20271ca4028e35b5840a131588cd3dbd75adc093297e111`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was exercised in a detached
scratch copy of this worktree with the three Spring Modulith records, the
updated source register, registry, source plan, owner unit, card registration
and content revision. The scratch results are in the Validation section.

### Source register `sources/register.json`

Update the existing `src.spring-modulith` record; do not add a new source id.

- `reading_status`: `full-public-page-inspected`.
- `version`: record the three 1.3.12 page revisions and the 2026-10-30
  access check.
- `access_checked` and `content_verified`: 2026-10-30.
- `verification_scope`: three versioned public reference pages read in full;
  no local build, module verification run, implementation behavior or
  benchmark.
- Keep the title, publisher, URL, topics, priority, admission, access and
  license notes.

The source count stays 285 and `sources/CATALOG.md` does not need a
regeneration for an existing-record update; `validate_sources.py` passes in
the scratch.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add three read records with the existing schema fields:

- `read.spring-modulith-verification.2026-10-30` — canonical revision
  `c1ee41282edd5866877a4d2a09d4585196a4a2ac05a672416624e4b9eb117cd4`;
  section `Verifying Application Module Structure`.
- `read.spring-modulith-fundamentals.2026-10-30` — canonical revision
  `6f45529855cf017220ca400ab72e87fc805cd31e044db44f47705a4ac16f95bd`;
  sections `Application Modules`, `Advanced Application Modules`,
  `Explicit Application Module Dependencies`, `Named Interfaces`.
- `read.spring-modulith-events.2026-10-30` — canonical revision
  `c15f574e8029e58e50346011402e03439590af4e3e6a3e15940fab2fa5472c6a`;
  sections `Working with Application Events`,
  `The Event Publication Registry`.

Each record needs the versioned unit URL, unit label, `unit_type` of
`documentation-page`, access date 2026-10-30, access method, sections not
read, license note, claims supported and not supported, limitations, read
scope, reviewer and `status: "read"`. Keep
`read.monolith-first.2026-10-21` unchanged.

### Source plan `edition/patterns/source-plan.v1.json`

Add the three units above to
`tycho.pattern.modular-monolith.required_units`, each with its
`source_id`, unit label, versioned URL, section list, `status: "read"`,
`read_record_id` and `blocked_reason: null`. Keep the Monolith First unit.
Replace the entry notes with the bounds text proposed for the owner unit.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.modular-monolith`:

- Set `technical_owner.state` and `coverage.technical` to
  `partial-bounded`; the owner-unit technical derivation becomes
  `partial-bounded` once invariant is supported.
- Keep `atlas_owner.state` and `coverage.decision` at
  `partial-bounded`; set `coverage.overall` to `partial-bounded`.
- Add a `source_units` entry for `src.spring-modulith` with status
  `read`.
- Replace `notes` with: "Invariant and failure/recovery bound 2026-10-30 to
  Spring Modulith 1.3.12 verification, fundamentals and events pages plus the
  existing Monolith First record; named owner, single-deployable framing and
  blast radius remain Tycho analysis. Coverage partial-bounded; no
  promotion."
- Keep `review_status` `self-checked`. The registry pattern entry has no
  `updated_at` field in the current schema; do not add one.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.modular-monolith`:

- Keep `owner.line` at 121 and the unit terms unchanged.
- Invariant:
  - `state`: `supported`.
  - `quote`: "The deployable is one unit, but each module has a named owner,
    an allowed-call surface and a dependency test that fails a bypass."
  - `reason`: "Spring Modulith documents API-only access, declared allowed
    dependencies and a verification that rejects undeclared dependencies and
    cycles. The named owner and single-deployable framing are Tycho
    definitions."
  - `binding`: `src.spring-modulith`, record
    `read.spring-modulith-verification.2026-10-30`, section
    "Verifying Application Module Structure", quote "all references to types
    that reside in application module internal packages are rejected",
    revision `c1ee4128...`.
  - Supporting bindings: the same record and section quote "dependencies to
    other application modules are rejected."; the fundamentals record section
    "Advanced Application Modules" quotes "Code within those must not be
    referred to from other modules." and "the Java compiler is not of much use
    to prevent these illegal references.".
- Failure/recovery:
  - `state`: `supported`.
  - `quote`: "Synchronous call chains across modules and one deployment
    blast radius are the operational risk".
  - `reason`: "Spring Modulith documents synchronous event publication,
    widened transactions and lost asynchronous events; the deployment blast
    radius is Tycho inference from the single-deployable definition."
  - `binding`: `src.spring-modulith`, record
    `read.spring-modulith-events.2026-10-30`, section
    "Working with Application Events", quote "As event publication happens
    synchronously by default", revision `c15f574e...`.
  - Supporting bindings: the same record and section quotes "will widen the
    transaction boundary and potentially cause the entire transaction to
    fail" and "if the listener fails for whatever reason, the event
    publication is lost, unless each listener actually implements its own
    safety net."; the verification record and section quote "all references
    to types that reside in application module internal packages are
    rejected".
- `source_support.auxiliary`: add the three Spring Modulith record/revision
  tuples. Do not add the Monolith First record to the new auxiliary list; its
  primary mechanism/alternative bindings remain.
- `technical_coverage`: `partial-bounded`.
- `notes`: "Invariant and failure/recovery bound 2026-10-30 to Spring
  Modulith 1.3.12 verification, fundamentals and events pages plus the
  existing Monolith First record; named owner, single-deployable framing and
  blast radius remain Tycho analysis. Coverage partial-bounded; no
  promotion."

Summary counters: `invariant_supported` 65 -> 66;
`failure_recovery_supported` 56 -> 57; `technical_partial_bounded`
20 -> 21; `technical_partial` 85 -> 84. No other counter changes from this
entry. The owner page is not a shared page in `shared_pages`, so no shared
record changes.

### Card registration `edition/patterns/card-batches.v1.json`

The entry has no `card_path`. Register the inline chapter path
`book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md`.
Keep `ledger_record` `read.monolith-first.2026-10-21`. A later split must
keep the new source id, the 2026-10-30 dates and the owner anchor
`modular-monolith`. No split is performed by this lane.

### Frontmatter source id

The lane already adds `src.spring-modulith` to the V11/C01 chapter
`evidence_scope.source_ids`. After the register update this is the only
frontmatter source addition required. Do not add source ids to the owner
page; its `evidence_scope` stays empty and the body Source boundary is the
binding record. A future owner-page source-id addition must move
`### Modular Monolith` and recompute the owner content-revision hash.

### Content revisions `edition/content-revisions.json`

Add an issue-540 revision with `authorized_at` 2026-10-30 and
authorization "B26 modular monolith source binding".

- `directory_documents`:
  - owner path previous
    `70564b9464196128a8e264967c50e5672d893ef300b0f9bdb36b45c2d27e5e44`
    (migration baseline), current
    `97d4b9b63427c73b2f69aaf4015b5edcc2d87a80d65864395db4aa784e3a2f24`
    (historical-view text after the edit).
  - card path previous
    `0c5c26415aaa4a9d7744579492125d53f10e844bc85e90a881674c28310fed3f`
    (migration baseline), current
    `f89a587407423769d20271ca4028e35b5840a131588cd3dbd75adc093297e111`
    (historical-view text after the source id is added).
- Leave `source_blocks`, `enrichment_documents`, `enrichment_additions`
  and `enrichment_baselines` empty. The owner page is retained and no page
  split is performed.

### Review-state and derived artifacts

The lane does not update `sufficient-candidates.v1.json`,
`sufficient-ready-plan.v1.json` or the review reconciliation records. They
remain historical review-state evidence until the independent review and the
batch-end decision. Derived route, atlas coverage, census, reverse-map and
semantic-audit artifacts must be regenerated once at batch end; do not treat a
stale derived count or hash as a lane content failure.

## Validation

At the parent HEAD:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

After the two book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS; V11 prose <=100,
  145 exact owner-link exceptions.
- `python3 scripts/check_boundary.py` — PASS; independent-origin review still
  required.
- `python3 scripts/validate_book_metadata.py` — PASS; 480 canonical
  documents.
- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_sources.py` — PASS; 285 source records.
- `python3 scripts/validate_pattern_registry.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_owner_units.py` — PASS; 145 entries,
  145 units, 30 shared pages.
- `python3 scripts/validate_directory_migration.py` — FAIL
  `directory-baseline-payload-drift` until the content revision is applied.
- `python3 scripts/validate_enrichment.py` — PASS; explicit membership and
  byte conservation.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.modular-monolith` — FAIL: invariant partial, failure/recovery
  partial and `card_path` missing; all three are integrator metadata work.

In the detached scratch copy with the metadata patch above:

    PASS: tycho.pattern.modular-monolith
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: 480 canonical documents
    PASS: 285 source records, mandatory IDs, cross-references and catalogue
    freshness
    PASS: directory migration; 480 canonical documents, 339 moved documents,
    12 post-migration directories
    PASS: enrichment; explicit membership and byte conservation

The full unit suite is not run; batch-end tests remain with the integrator.
The quote-to-source check in the scratch verified every new binding quote
against the fetched canonical page text.

## Limits

The binding uses three versioned public documentation pages and the existing
Monolith First record. The pages describe a framework's verification and event
semantics; they do not test a local module verifier, a production event flow,
a bypass path or a deployment blast radius. The owner section and card label
those consequences as Tycho analysis. The named owner and the single-deployable
definition are Tycho framing, not source claims.

Coverage remains partial-bounded after the proposed metadata patch.
Independent review, promotion, owner acceptance, CI and merge permission are
not claimed. The prior independent review of this entry was recorded against
the earlier page hash and does not cover this text.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer
  should check quote-to-claim fit for the invariant and for each failure mode,
  the Tycho labels for the named owner, single-deployable framing and blast
  radius, the three 1.3.12 revisions, the metadata patch and the absence of a
  sufficient claim.
- The reviewer must use read-only repository access and must not run tests.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path above;
- `book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
