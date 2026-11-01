# B31 — Bounded Context invariant and failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and alternative were supported;
invariant and failure/recovery were partial. This lane binds the source-supported
parts of both dimensions to Fowler, Microsoft and Evans public pages and labels
the named arbiter and the expert-review-before-boundary-move rule as Tycho
guidance. The metadata patch was exercised in a detached scratch copy: preflight
passes 1/1, owner units, registry, cards, sources, book metadata, directory
migration, decomposition and enrichment pass. The patch is not in the lane
commit; promotion is not claimed or ready.

## Lane coordinates

- Parent HEAD: `316c905b39e2a8cd73d787c4e7634b160841f570` (`316c905b`).
- Branch: `b31-bounded-context`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b31-bounded-context`.
- Scope: the owner section `### Domain-Driven Design and Bounded Context` in
  the V02/C02 owner page and the inline V11/C01 card
  `### Domain-Driven Design / Bounded Context`. Single-entry lane; no other
  entry, shared owner page, promotion or generated file is changed.
- Owner path (concatenate the two lines):

      book/volumes/v02-application-boundaries-and-contracts/
      c02-domain-boundaries-data-ownership-and-contracts/domain-authority.md

- Card path:
  `book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md`.
- Card location: inline. No dedicated `bounded-context.md` exists. A split is
  an integrator decision; this lane does not create one.

## Candidate evaluation

- Fowler, "Bounded Context" (2015-01-15). Existing source
  `src.fowler-bounded-context` and record
  `read.fowler-bounded-context.2026-10-21`. Selected for the language-change
  driver, context map and polysemy. The article is a definition and boundary
  argument, not a full DDD reference.
- Microsoft, "Use domain analysis to model microservices". Selected for the
  co-created ubiquitous language, domain-expert participation, context map,
  negotiated contracts and iterative boundaries. The page does not name a single
  expert arbiter or prescribe an expert review before a boundary move.
- Evans, "DDD Reference" 2015-03 PDF. Existing source `src.ddd-reference`.
  Selected for the definitions of bounded context and ubiquitous language, the
  domain-expert objection rule and the language-model change rule. The PDF is a
  summary reference, not the full 2004 book and not a review gate.
- Microsoft, "Design a DDD-oriented microservice" (candidate, not selected).
  It correlates each bounded context with a microservice and adds no
  domain-expert review content. Its 1:1 correlation conflicts with the owner
  page's one-deployable/several-contexts framing. URL, revision and the exact
  conflicting passages are recorded below.
- No other candidate was selected. No selected page tests a boundary move, names
  a single arbiter or measures translation cost.

## Source binding

### Fowler — Bounded Context

- Source id: `src.fowler-bounded-context` (existing).
- Existing record: `read.fowler-bounded-context.2026-10-21`.
- URL: `https://martinfowler.com/bliki/BoundedContext.html`.
- Unit label: "Bounded Context — article"; unit type `article`; access date
  2026-10-21; re-read 2026-10-30.
- Recheck 2026-10-30: HTTP `Last-Modified` 2026-10-29T16:11:21Z; ETag
  `"4a04-65efcee2d9c40"`; served raw HTML SHA-256
  `5f6bbdd9567aeb45cb81d536a9e01a7636f2792ba41fa0abeff5603b74d46184`,
  equal to the record's `content_sha256`. Canonical extraction SHA-256 is
  `c3eb721b9a3614a615f8bffcd7c12a84d1875b3f7b8c64d7a1cd8902db7cf425`;
  the record revision is the raw digest, so bindings use `5f6bbdd9...`.
- Sections used: "Bounded Context", "Further Reading", "Notes".
- Exact quotes used:

      you need a different model when the language changes.

      Different contexts may have completely different models of common concepts
      with mechanisms to map between these polysemic concepts for integration.

- The existing mechanism and alternative bindings are unchanged. They use the
  "So instead DDD divides up a large system into Bounded Contexts..." and
  "Usually the dominant one is human culture..." quotes from the same record.
- Limits: one short author article; no implementation, benchmark or boundary
  review. It supports the language-change driver and explicit context maps; it
  does not name a single expert arbiter or prescribe a review gate.

### Microsoft — Use domain analysis to model microservices

- Proposed source id: `src.microsoft-ddd` (new).
- Proposed record: `read.microsoft-ddd.2026-10-30`.
- URL: `https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis`.
- Unit label: "Use domain analysis to model microservices — Azure Architecture
  Center"; unit type `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-08-24T17:31:52Z; ETag
  `"8wP13EysDBh15GT+PBUfheG99gg="`; displayed "Last updated on" 2026-02-25.
- Canonical text SHA-256:
  `62191a60e230bc6b1950ea8427f27d0c5a360c14d2e02353a38ab3d7d903cf60`.
- Raw HTML SHA-256:
  `286da0bf96cbbda99b27c6f1da1459f356937ccd0f87498ed17fcd22e7aea5f4`.
- Sections read: "Introduction", "Scenario: Drone delivery", "Analyze the
  domain", "Example: Drone delivery application", "Define bounded contexts".
- Exact quotes used:

      It's a shared vocabulary that developers and domain experts create
      together within each bounded context.

      This effort should involve domain experts, software architects, and other
      stakeholders.

      The teams negotiate the contract between them.

      DDD is an iterative, ongoing process, so service boundaries don't remain
      fixed.

      If a single team must own multiple unrelated bounded contexts, or a single
      bounded context requires coordination across many teams, revisit either
      the boundaries or the team structure.

      A bounded context defines the boundary within a domain where a specific
      domain model applies.

      Fabrikam identifies these interactions and creates a context map that
      documents the relationships between bounded contexts.

      A context map highlights integration points and helps teams clarify
      responsibilities.

- Limits: living Microsoft Learn page with no published version identifier.
  The canonical digest covers the full extracted page text including navigation
  chrome because the page has no recognized article-body marker. It describes
  strategic DDD practice; it does not test a boundary move, name a single
  arbiter or prescribe an expert review gate.

### Evans — DDD Reference (2015-03 PDF)

- Existing source id: `src.ddd-reference`.
- Proposed record: `read.ddd-reference-bounded-context.2026-10-30`.
- Landing URL: `https://www.domainlanguage.com/ddd/reference/`.
- PDF URL (concatenate the two lines):

      https://www.domainlanguage.com/wp-content/uploads/2016/05/
      DDD_Reference_2015-03.pdf

- Unit label: "DDD Reference — summary booklet (2015-03 PDF)"; unit type
  `book-chapter`; access date 2026-10-30.
- Access: public HTTPS download; HTTP `Last-Modified` 2016-05-12T14:24:03Z;
  ETag `"76291-532a5e8f646c0"`; 59 pages; 22,778 extracted words.
- Raw PDF SHA-256:
  `cf82dc7b4736bb24f4a1b69a3213c25cbd38aa98e37b99c2facfb94ff5cacb99`.
- Normalized text SHA-256:
  `9f9830a4a088e44b0c8024db64570edfaccf9f5a41f258abbb6903f5cd6dd8e2`.
- Sections read: "Definitions", "Bounded Context", "Ubiquitous Language".
- Exact quotes used:

      ubiquitous language A language structured around the domain model and used
      by all team members within a bounded context to connect all the activities
      of the team with the software.

      bounded context A description of a boundary (typically a subsystem, or the
      work of a particular team) within which a particular model is defined and
      applicable.

      Domain experts should object to terms or structures that are awkward or
      inadequate to convey domain understanding; developers should watch for
      ambiguity or inconsistency that will trip up design.

      Resolve confusion over terms in conversation, in just the way we come to
      agree on the meaning of ordinary words.

      Recognize that a change in the language is a change to the model.

      Explicitly set boundaries in terms of team organization, usage within
      specific parts of the application, and physical manifestations such as
      code bases and database schemas.

      Once a bounded context has been defined, we must keep it sound.

      Relentlessly exercise the ubiquitous language to hammer out a shared view
      of the model as the concepts evolve in different people’s heads.

- Limits: the 2015-03 PDF is a summary reference derived from the 2004 book; it
  is not the full book and does not prescribe a review gate. The normalized text
  hash covers an extraction with normalized spacing and ligatures, not the PDF
  layout. The landing page states CC BY 4.0.

### Microsoft .NET page — considered, not selected

- URL (concatenate the two lines):

      https://learn.microsoft.com/en-us/dotnet/architecture/microservices/
      microservice-ddd-cqrs-patterns/ddd-oriented-microservice

- Access 2026-10-30: HTTP `Last-Modified` 2026-08-24T13:25:49Z; ETag
  `"WGzCkt+Xhgnnohy10hW3WeKRTa4="`; raw HTML SHA-256
  `3bfa96722b62c2c99730b68e98466556ec297fe57a5f5cc06d3ca7adc7a85af2`;
  canonical text SHA-256
  `2818d88d7519f49d250d4cbe65ebafd6fed59e225151c7e3fc524f7f23b48e5c`.
- Exact conflicting passages:

      It describes independent problem areas as Bounded Contexts (each Bounded
      Context correlates to a microservice), and emphasizes a common language to
      talk about these problems.

      Where to draw the boundaries is the key task when designing and defining
      a microservice.

- No ledger record or binding is added. The 1:1 correlation conflicts with the
  owner page's statement that one deployable can host several contexts and one
  context can span services; the page also adds no domain-expert review content.

## Book edits

### Owner section

- Frontmatter: `content_review.reviewed_at` and `updated_at` move to 2026-10-30;
  the reviewer is "Automated authoring agent"; `evidence_scope.notes` points to
  the body Source boundary. `source_inspection_date` stays `null`: the
  decomposition plan does not declare fresh sources for this page, and setting a
  date would fail `validate_decomposition.py` with
  `fabricated-question-verification`. `content_verified_at` stays `null`.
- The mechanism paragraph and the existing unit terms are retained. The
  invariant paragraph now names the Microsoft co-creation sentence, the Evans
  domain-expert objection rule and the Tycho label for co-ownership, the single
  named arbiter and the resolution record.
- The context-map paragraph now names Microsoft's context-map and integration
  language. The deployment paragraph keeps the one-deployable/several-contexts
  rule and labels the no-microservice-synonym rule as guidance rather than a
  definition.
- The failure/recovery paragraph now names the Evans language-model change rule,
  the Microsoft iterative-boundary sentence and Fowler's language-change
  sentence, and labels the sequenced expert review as Tycho governance.
- A Source boundary list records the three records and their revisions. The
  heading stays at line 126; the page is 173 lines.
- Raw SHA-256:
  `82330a277d33b7e0a611c5fcd62f389b7932e6053ceb0991c6d8ef9be098c708`.
- Historical-view SHA-256:
  `8e331bf5ee73263ba9b714cc7a8e546dc666268098ef3545f7eccb8c3a6c80e5`.

### V11/C01 inline card

- Frontmatter adds `src.ddd-reference` and `src.microsoft-ddd` to
  `evidence_scope.source_ids`. The card review, update and inspection dates are
  already 2026-10-30.
- **Good-fit conditions** now names co-created vocabulary and the ability to
  challenge terms that hide different meanings.
- **Failure and recovery** now names the Evans model-change rule, the Microsoft
  iterative-boundary sentence and the expert-review step, and labels the
  sequenced review as Tycho guidance.
- **Sources** names the existing Fowler record and the proposed Microsoft and
  Evans records with their revisions.
- The heading moves from line 206 to line 208 because of the two added source
  ids. The chapter page is 305 lines.
- Raw SHA-256:
  `3dde80eb009652d6430d2e5c7891621dcee685b391999bb8055780b53634ee9f`.
- Historical-view SHA-256:
  `0a53f86004797f84f314ba58ac494d53b693f2b8dbf35e87178dacd9cd85735e`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was exercised in a detached
scratch copy of this worktree with the two book files plus the source register,
ledger, source plan, registry, owner units, card batches, content revisions and
catalogue updates. The scratch results are in the Validation section; no scratch
file is part of the lane commit.

### Source register `sources/register.json`

Add one source record, written as `src.` + `microsoft-ddd`, with title "Use
domain analysis to model microservices"; category "architecture"; publisher
"Microsoft Learn"; kind "official-docs"; the Microsoft URL above; topics
`["application-architecture", "domain-models", "architecture-decisions"]`;
priority "core"; planned use "Bounded public page for domain analysis, bounded
contexts, ubiquitous language and context maps."; admission
"admitted-for-research"; access "public-web-or-author-download"; reading status
"full-public-page-inspected"; version with the 2026-10-30 access, canonical
revision `62191a60...`, raw revision `286da0bf...`, HTTP Last-Modified
2026-08-24T17:31:52Z, displayed Last updated 2026-02-25 and no published version
identifier; `access_checked` and `content_verified` 2026-10-30; license note
"Public Microsoft Learn documentation; cite short excerpts and paraphrase; do not
mirror."; verification scope naming the full page and excluding linked pages,
images and navigation; observed title "Use Domain Analysis to Model Microservices
- Azure Architecture Center | Microsoft Learn".

Update the existing `src.ddd-reference` record: set `resolved_url` to the PDF URL
above; set planned use to "Domain boundaries and tactical design vocabulary,
including the 2015-03 summary PDF."; set reading status
"full-public-page-inspected"; set version to "DDD Reference, 2015-03 PDF, accessed
2026-10-30; raw PDF SHA-256 `cf82dc7b...`; normalized text SHA-256
`9f9830a4...`; 59 pages; PDF Last-Modified 2016-05-12T14:24:03Z; no later edition
identified."; set `access_checked` and `content_verified` to 2026-10-30; set the
license note to "CC BY 4.0 per the Domain Language landing page; cite short
excerpts and paraphrase; do not mirror the PDF."; set verification scope to
"Definitions, Bounded Context and Ubiquitous Language sections read in full from
the 2015-03 PDF; the remaining pattern summaries, linked pages and the full 2004
book were not read. Raw PDF and normalized text revisions recorded."

The source count moves from 287 to 288. Keep `updated` at 2026-10-30. Regenerate
`sources/CATALOG.md` with `python3 scripts/source_catalog.py`.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add two records. Set `updated` to 2026-10-30. Records move from 163 to 165.

- `read.microsoft-ddd.2026-10-30` — source `src.microsoft-ddd`; unit label
  "Use domain analysis to model microservices — Azure Architecture Center";
  type `documentation-page`; access date 2026-10-30; access method records the
  canonical and raw revisions, HTTP Last-Modified, ETag and displayed date;
  sections `Introduction`, `Scenario: Drone delivery`, `Analyze the domain`,
  `Example: Drone delivery application` and `Define bounded contexts`;
  `content_sha256` `62191a60...`; status `read`; reviewer "Automated authoring
  agent".
- Claims supported: the bounded-context definition; the co-created ubiquitous
  language; domain-expert participation in domain analysis; context maps and
  integration points; iterative boundaries and boundary/team-structure
  revisiting; negotiated customer-supplier contracts.
- Claims not supported: a single named domain-expert arbiter; a required expert
  review before every boundary move; implementation behavior, local execution or
  production observation; linked pages and other Microsoft guidance.
- Limits: one living Microsoft Learn page with no published version identifier;
  the canonical digest includes page chrome because the page has no recognized
  article-body marker; the page describes strategic DDD practice, not a measured
  boundary review.
- `read.ddd-reference-bounded-context.2026-10-30` — source
  `src.ddd-reference`; unit label "DDD Reference — summary booklet (2015-03
  PDF)"; type `book-chapter`; access date 2026-10-30; access method records the
  raw PDF and normalized text revisions, HTTP Last-Modified, ETag, page count and
  word count; sections `Definitions`, `Bounded Context` and
  `Ubiquitous Language`; `content_sha256` `cf82dc7b...`; status `read`;
  reviewer "Automated authoring agent".
- Claims supported: the bounded-context and ubiquitous-language definitions; the
  domain-expert objection rule; language change as model change; resolving term
  confusion in conversation; setting boundaries in terms of team organization,
  usage and physical manifestations.
- Claims not supported: a single named domain-expert arbiter; a required expert
  review before every boundary move; implementation behavior or a measured
  boundary review; the rest of the reference and linked book material.
- Limits: the 2015-03 PDF is a summary reference derived from the 2004 book; it
  is not the full book and does not prescribe a review gate; the normalized text
  hash covers an extraction with normalized spacing and ligatures, not the PDF
  layout.

### Source plan `edition/patterns/source-plan.v1.json`

Append two units to `tycho.pattern.domain-driven-design-bounded-context`:

- `src.microsoft-ddd`: unit "Use domain analysis to model microservices — Azure
  Architecture Center", type `documentation-page`, the Microsoft URL, the five
  sections above, status `read`, record `read.microsoft-ddd.2026-10-30`.
- `src.ddd-reference`: unit "DDD Reference — summary booklet (2015-03 PDF)",
  type `book-chapter`, the PDF URL, the three sections above, status `read`,
  record `read.ddd-reference-bounded-context.2026-10-30`.

Replace the entry notes with: "Bounded-context focus using Fowler’s article,
Microsoft’s domain-analysis page and the Evans 2015-03 summary. Microsoft and
Evans support co-created vocabulary, domain-expert objection, context maps and
iterative boundaries; a single named arbiter and expert review before a boundary
move remain Tycho guidance."

Set `updated` to 2026-10-30. Summary: `required_units` 200 -> 202; `read_units`
199 -> 201; `ledger_records` 163 -> 165. Recompute `registry_sha256` after saving
the registry; the scratch serialization produced
`ddd2dc45a8041c4f5c649b44769c408f82da3e3370dd7d2a39787138068c378e`, but the
authoritative value is the SHA-256 of the saved registry file.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.domain-driven-design-bounded-context`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to `partial-bounded`. Keep
  `atlas_owner.state` and `coverage.decision` at `partial-bounded`.
- Replace `source_units` with, in order: the existing Fowler "Bounded Context —
  article"; Microsoft "Use domain analysis to model microservices — Azure
  Architecture Center"; and Evans "DDD Reference — summary booklet (2015-03
  PDF)". All three have status `read`.
- Replace `notes` with: "Invariant and failure/recovery bound 2026-10-30 to
  Fowler’s Bounded Context article, Microsoft’s domain-analysis page and the
  Evans 2015-03 summary; a single named arbiter and expert review before a
  boundary move remain Tycho guidance. Coverage partial-bounded; no promotion."
- Keep `review_status` `self-checked`. The registry pattern entry has no
  `updated_at` field in the current schema; do not add one.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.domain-driven-design-bounded-context`:

- Keep `owner.line` at 126, the heading and the four `unit_terms` unchanged.
- Invariant:
  - `state`: `supported`.
  - `quote`: "A named domain expert co-owns that vocabulary and arbitrates
    disputed meanings."
  - `reason`: "Microsoft says the vocabulary is one that developers and domain
    experts create together within each bounded context; Evans says domain
    experts should object to terms or structures that are awkward or inadequate
    to convey domain understanding. The words 'co-owns' and 'arbitrates', the
    single named arbiter and the resolution record are Tycho operational
    guidance."
  - `binding`: `src.microsoft-ddd`, record `read.microsoft-ddd.2026-10-30`,
    section `Introduction`, quote "It's a shared vocabulary that developers and
    domain experts create together within each bounded context.", revision
    `62191a60...`.
  - Supporting bindings: Evans `Ubiquitous Language` quote "Domain experts
    should object to terms or structures that are awkward or inadequate to
    convey domain understanding; developers should watch for ambiguity or
    inconsistency that will trip up design."; Evans `Ubiquitous Language` quote
    "Resolve confusion over terms in conversation, in just the way we come to
    agree on the meaning of ordinary words."; Microsoft `Analyze the domain`
    quote "This effort should involve domain experts, software architects, and
    other stakeholders.".
- Failure/recovery:
  - `state`: `supported`.
  - `quote`: "Model behavior changes are reviewed with the domain expert before
    a boundary moves."
  - `reason`: "Evans says to recognize that a change in the language is a change
    to the model; Microsoft says DDD is iterative and service boundaries do not
    remain fixed, and advises revisiting boundaries or team structure when
    ownership misaligns; Fowler says a different model is needed when the
    language changes. The sequenced review by a named expert before a boundary
    move is Tycho governance."
  - `binding`: `src.ddd-reference`, record
    `read.ddd-reference-bounded-context.2026-10-30`, section
    `Ubiquitous Language`, quote "Recognize that a change in the language is a
    change to the model.", revision `cf82dc7b...`.
  - Supporting bindings: Evans `Ubiquitous Language` quote "Relentlessly
    exercise the ubiquitous language to hammer out a shared view of the model as
    the concepts evolve in different people’s heads."; Microsoft `Introduction`
    quote "DDD is an iterative, ongoing process, so service boundaries don't
    remain fixed."; Microsoft `Analyze the domain` quote "If a single team must
    own multiple unrelated bounded contexts, or a single bounded context
    requires coordination across many teams, revisit either the boundaries or
    the team structure."; Fowler `Bounded Context` quote "you need a different
    model when the language changes.".
- `source_support`: primary Fowler record
  `read.fowler-bounded-context.2026-10-21`; add auxiliary Microsoft
  `read.microsoft-ddd.2026-10-30` and Evans
  `read.ddd-reference-bounded-context.2026-10-30` with revisions
  `62191a60...` and `cf82dc7b...`.
- `technical_coverage`: `partial-bounded`.
- `notes`: "Invariant and failure/recovery bound 2026-10-30 to Fowler’s
  Bounded Context article, Microsoft’s domain-analysis page and the Evans
  2015-03 summary; the single named arbiter and the expert review before a
  boundary move remain Tycho guidance. Coverage partial-bounded; no promotion."

Summary counters: `invariant_supported` 67 -> 68;
`failure_recovery_supported` 60 -> 61; `technical_partial_bounded` 19 -> 20;
`technical_partial` 82 -> 81. No other counter changes. The owner page is not a
shared page in `shared_pages`, so no shared record changes.

### Card registration `edition/patterns/card-batches.v1.json`

Add `card_path`:
`book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md` to the
`tycho.pattern.domain-driven-design-bounded-context` entry. Keep `ledger_record`
`read.fowler-bounded-context.2026-10-21`. The card remains inline; no split is
performed.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B31 bounded-context invariant and failure/recovery source binding; no promotion
or owner acceptance." The historical-view hashes are:

- Owner path previous `5d57b682...` (migration baseline), current
  `8e331bf5...`.
- Card path previous `0c5c2641...` (migration baseline), current
  `0a53f860...`.

Leave `source_blocks`, `enrichment_documents`, `enrichment_additions` and
`enrichment_baselines` empty. The owner page is retained and no split is
performed.

### Derived artifacts and review metadata

The book edit changes one canonical page and one atlas chapter. Before the content
revision, `validate_directory_migration.py` fails
`directory-baseline-payload-drift` and `validate_pattern_atlas.py` fails
`atlas-document-sha`. With the content revision and metadata patch,
`validate_edition.py` fails `edition-index-stale` and
`validate_pattern_atlas.py` fails `atlas-registry-hash`. These are derived-hash
refreshes for batch end: the affected route index, atlas coverage/census,
reverse-map, sufficient-workflow and semantic-audit artifacts are regenerated
once. Do not treat a stale derived hash as a lane content failure.

`edition/patterns/sufficient-candidates.v1.json` records the 2026-10-25 agent
review with page hash `60978a1f...`. That review predates this edit and no longer
covers the changed owner page (`82330a27...`) or card bytes. The book/atlas
independent review gate applies; do not update the recorded hash without a fresh
review. The prior review is historical evidence, not acceptance of this lane.

## Validation

Checker output in the lane worktree after the two book edits:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_registry.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_sources.py` — PASS; 199 read; 163 ledger
  records.
- `python3 scripts/validate_pattern_owner_units.py` — PASS; 145 entries.
- `python3 scripts/validate_book_metadata.py` — FAIL unknown source ID for the
  card's new `src.microsoft-ddd`; integrator register work.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.domain-driven-design-bounded-context` — FAIL: invariant and
  failure/recovery still partial and `card_path` missing; all three are
  integrator metadata work.
- `python3 scripts/validate_directory_migration.py` — FAIL
  `directory-baseline-payload-drift` until the content revision is applied.
- `python3 scripts/validate_edition.py` — FAIL
  `directory-baseline-payload-drift` in the lane tree; the scratch tree with
  the content revision reaches `edition-index-stale`.
- `python3 scripts/validate_pattern_atlas.py` — FAIL `atlas-document-sha` in
  the lane tree; the scratch tree with the metadata patch reaches
  `atlas-registry-hash`.
- `python3 scripts/validate_decomposition.py` — PASS; 739 preserved source
  blocks and 174 new question pages.
- `python3 scripts/validate_enrichment.py` — PASS; explicit membership and byte
  conservation.
- `python3 scripts/validate_sources.py` — PASS in the pre-note tree; after this
  note is added it fails `unknown source reference` for `src.microsoft-ddd`
  because the proposed register record is not in the lane commit. That is
  integrator work, not a lane content failure.

In the detached scratch copy with the metadata patch above:

    PASS: tycho.pattern.domain-driven-design-bounded-context
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: source plan 145 entries; 201 read; 165 ledger records
    PASS: 288 source records, mandatory IDs, cross-references and catalogue
    freshness
    PASS: 484 documents, structural metadata and registry references
    PASS: directory migration; 484 canonical documents, 339 moved documents,
    12 post-migration directories
    PASS: decomposition; 739 preserved source blocks, 174 new question pages
    PASS: enrichment; explicit membership and byte conservation
    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks.

The scratch tree still fails `validate_edition.py` (`edition-index-stale`) and
`validate_pattern_atlas.py` (`atlas-registry-hash`); these are derived-hash
refreshes for batch end, not lane content failures. The full unit suite is not
run; batch-end tests remain with the integrator.

## Limits

The binding uses two public pages and one public summary PDF. The sources
describe co-created vocabulary, domain-expert objection, context maps and
iterative boundaries; they do not test a boundary move, name a single arbiter or
measure translation cost. The owner section and card label those unsupported
parts as Tycho guidance. The `invariant` state is `supported` only because the
claim separates the source-supported co-creation and objection evidence from the
Tycho co-ownership, named-arbiter and resolution-record framing; a reviewer that
requires every word to be source-quoted should treat the dimension as partial
instead. The
`failure_recovery` state is `supported` only because the claim separates the
source-supported language-change and boundary-revisit context from the Tycho
sequenced-review rule; a reviewer that requires the review gate itself to be
source-quoted should treat the dimension as partial instead.

The Microsoft and Evans pages are living or summary documents. The Microsoft
canonical digest includes navigation chrome because the page has no recognized
article-body marker. The Evans normalized text hash covers an extraction with
normalized spacing and ligatures, not the PDF layout. The Microsoft .NET page is
recorded as a considered contradiction but is not a binding unit.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer should
  check quote-to-claim fit for each dimension, the Tycho labels for the named
  arbiter and the review-before-boundary-move rule, the three revisions, the
  Microsoft .NET contradiction, the metadata patch and the absence of a
  sufficient or promotion claim.
- The reviewer must use read-only repository access and must not run tests.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path (concatenate the two lines):

      book/volumes/v02-application-boundaries-and-contracts/
      c02-domain-boundaries-data-ownership-and-contracts/domain-authority.md

- the card path
  `book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
