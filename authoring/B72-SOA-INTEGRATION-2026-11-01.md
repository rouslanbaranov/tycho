# B72 SOA lane integration

Status: integrated and self-checked on 2026-11-01. Coverage remains
partial-bounded; no promotion, sufficient-coverage claim, independent review or
owner acceptance is claimed.

## Commit chain

- Parent HEAD: `79e12d633939f19ade1615dd1f87cecaaa66375a` (`79e12d63`).
- Lane commit: `4bb6c9fe980bab40f617dcd676a0fcc94cb89a53` (`4bb6c9fe`).
- Cherry-pick on this branch: `0ad68434`; same three lane files.
- This integration commit applies the shared register, ledger, source plan,
  registry and owner-unit metadata, the dedicated card split, content revisions,
  counters, protected baseline and generated artifacts.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c01-application-boundaries/service-oriented-architecture.md`.
- Page identity: `tycho.page.1a22dabeec74779dfeb28fadc98ade4a`.
- Page raw SHA-256:

      db166936aeed919c7a18a3425b7c2f6184422e6e9dcc36bbb23ee7845c715f05

- Page historical-view SHA-256:

      15d76bef62739ebe4cae65c5eb96421bf208e8bdcb8bdf41c8f8d0170e8f22f8

- Page body SHA-256 (heading plus card):

      c03e8a5b34e448d8eca44bb857e67709771099eeab851eb77881c01996f5e9f0

- Moved card body SHA-256 (the bytes lifted from the chapter page):

      61d10aa8dc16104e735ef3c347acd8fc35e35b6b11de6811c25a5fc0586cea3f

- README raw SHA-256:

      635b2d936eab8df90fbe67165b54691d33a03d4f68c0183c500478ebd5beb07a

- README historical-view SHA-256:

      2c52e5029bee07e26449911516109ac136b94733f4a5dcc7fa1999ec9e9e6d18

- Owner page raw SHA-256:

      7eb9e4733160bd8e4b57924801264171ae2a12eb1026fe2d4a69882d1073bb0b

- Owner page historical-view SHA-256:

      e97ee4a8c6cd60b7b8751f77bddcd8c1ea4201e820daf27386b1d103a8a5fe3f

- The card moved from the shared V11/C01 page; the section heading becomes the
  page H1. The README keeps `### Service-Oriented Architecture (SOA)` with a
  link to the dedicated card, so the owner backlink at
  `service-orientation-microservices-and-distribution.md#service-oriented-architecture-soa`
  resolves through the chapter anchor.
- The page is registered as an id, atlas-manifest document, directory record,
  document identity, semantic-audit page and card path. The chapter evidence
  scope gains `src.soa-model`, `src.microsoft-service-orientation` and
  `src.microsoft-dotnet-soa`.

## Applied metadata

- `sources/register.json`: 354 -> 356 records. Added
  `src.microsoft-service-orientation` and `src.microsoft-dotnet-soa`;
  `src.soa-model` was already registered and gains the 2026-11-01 reading
  status, version and verification scope. The catalogue was regenerated.
- `edition/patterns/reading-ledger.v1.json`: 349 -> 352 records. Added
  `read.soa-rm.2026-11-01`,
  `read.microsoft-service-orientation.2026-11-01` and
  `read.microsoft-dotnet-soa.2026-11-01`.
- `edition/patterns/source-plan.v1.json`: the SOA entry takes four units.
  Summary: 385 -> 388 required, 384 -> 387 read, 349 -> 352 ledger records;
  planned stays 0 and blocked stays 1.
- `edition/patterns/registry.v1.json`: four read source units; the technical
  owner, technical coverage and overall coverage move from partial to
  partial-bounded. Atlas and decision coverage stay partial-bounded.
- `edition/patterns/owner-units.v1.json`: invariant and failure/recovery are
  supported with primary and supporting bindings; mechanism and alternative
  stay unchanged. Technical coverage is partial-bounded. Counters: invariant
  97 -> 98, failure/recovery 95 -> 96, technical partial 50 -> 49 and technical
  partial-bounded 11 -> 12. The shared-page entry records one bounded unit.
- `edition/patterns/card-batches.v1.json`: the SOA entry gains the dedicated
  `card_path`; `read.microservices-article.2026-10-21` remains its
  card-level citation.
- `edition/content-revisions.json`: one issue-540 revision authorizes the
  owner-page and chapter historical-view changes.
- `edition/v12/protected-baseline.json`: updated the two page hashes and the
  registry, atlas-manifest and re-review-packet promotion-record hashes.
- Atlas, coverage and reverse maps, page census, phase 4, semantic audit,
  delivery evidence, route and section indexes, qrels, inventory, candidates
  and re-review packets were refreshed. Counts: 100 atlas documents, 523
  canonical pages, 356 sources and 352 ledger records.

## Deviations from the lane note

- The lane note describes three source units; only two are new register
  records. `src.soa-model` existed at the parent HEAD and is extended, so the
  register count moves 354 -> 356, not 354 -> 357.
- The lane page text used a semicolon after the failure/recovery owner quote.
  The integration restores the period so the existing owner-unit quote is
  verbatim; this is the only book-text change beyond the cherry-pick.
- The Microservices promotion is not rebound. Its promoted section and card are
  byte-identical (section 1,429 bytes, SHA-256
  `39df97e0273ee98c4ada05f666d57f06822190f1ab9cf77ea3e1f62e707fd1bf`;
  card SHA-256 `4316e6ec...`), but the owner-page hash changed. Per instruction
  the promotion record is left untouched pending review, so
  `validate_pattern_owner_units.py` reports the expected stale promotion hash
  and the four owner-unit tests cascade from it. No rebind or suspension is
  claimed.

## Verification

- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.service-oriented-architecture-soa`: PASS, 1/1 clean.
- PASS: sources (356), catalogue, source plan (388/387/352), registry (388
  units), cards (145), atlas (100 documents), coverage, owner units (apart
  from the stale Microservices promotion hash), delivery evidence, directory
  migration (523 documents), book metadata, edition, phase 4 (523 pages),
  semantic audit (523 pages), pattern census, V12 (31 documents), sufficient
  promotions (84), pilot, owner acceptance and AI review index.
- PASS: V11 prose line length with 145 exact owner-link exceptions; configured
  lexical boundary checks; `git diff --check`.
- Full suite run once: `python3 -m unittest discover -s tests -p
  'test_tycho*.py' -v` ran 776 tests. Six failures and two errors: four
  pre-existing qrels failures also present at `79e12d63` (phase-2 and phase-3
  verbatim support plus two V12 qrels snapshot checks) and four owner-unit
  results caused by the unrebound Microservices promotion hash.

## Limits

- Partial-bounded coverage only; no promotion, sufficient coverage, owner
  acceptance, CI result or production observation.
- No external AI content review was run for this integration; the book and
  atlas review gate remains outstanding and is not waived.
- The OASIS unit is a reference model; the Microsoft units are a 2010
  architecture-style guide and a short ebook excerpt. None states a contract
  language, bus failure measurement, failover procedure or recovery-time bound.
- The mandatory four-field contract metadata, consumer inventory,
  bottleneck/single-point framing, sizing and fallback remain Tycho synthesis.
