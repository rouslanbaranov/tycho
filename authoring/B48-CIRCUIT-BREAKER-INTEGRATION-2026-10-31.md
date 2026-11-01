# B48 Circuit Breaker split and metadata integration

Status: integrated and self-checked on 2026-10-31. Coverage remains
partial-bounded; no Circuit Breaker promotion, owner acceptance or independent
AI review is claimed.

## Commit chain

- Parent: `4f863e6b0fdaac72c6f3639ed46f5944f6e0bb3d` (`4f863e6b`).
- B48 book-binding cherry-pick: `e6ddb6d6`, source `fc91b5a5`.
- This integration: dedicated card page, shared metadata, counters and tests.

The cherry-pick applied cleanly. It contains the B48 lane note, the V07/C05
owner edits and the updated inline V11/C07 card.

## Card split

- Dedicated page:
  `book/volumes/v11-pattern-atlas/c07-resilience/circuit-breaker.md`.
- Page identity: `tycho.page.35c975574fa3b7088402ce5dd037c4f5`.
- Page raw SHA-256:

      91afba8f885efad3803e05ca045d28bb966d9ee843e925f96e34b46c4a5d0979

- Historical-view SHA-256:

      5ff52150a6a961ecd483a4acc2cda0caaf3bdfe96f328ee5c3eb10ab7849176c

- Body SHA-256:

      f911612dac1c16fa4c04ffe61697e74877986fd0fd9424f8f92c3440059f943e

- README raw SHA-256:

      b6e000bc832668169a0e5a16bc5771d872757b2e6858d381da6f090f81f213b9

- README historical-view SHA-256:

      4c0785bd167a0b1458cd6aeb0fecdaf3ef5415ca9ef877b973e0fa5eb6e5a846

- Owner page raw SHA-256:

      c27480285dd97b6196b3ef6a41882672861c9d4064b6721c17e26d76b42078ab

- Owner page historical-view SHA-256:

      fd00929782d5d988e23b5885e9c9eb5e21165954803b3f8237572a791841c5b7

- The README keeps `### Circuit Breaker` and points to the dedicated card.
  The owner backlink remains the README anchor and the card keeps the owner
  link. The owner section is level 3 at line 117; Bulkhead moves to line 200.

## Applied metadata

- `sources/register.json`: 306 sources; no new source id. Resilience4j,
  Microsoft and AWS gain their 2026-10-31 circuit-breaker scopes; SRE is
  unchanged. The source catalogue was regenerated and has no content diff.
- `edition/patterns/reading-ledger.v1.json`: 224 -> 226 records. The two new
  records are `read.microsoft-circuit-breaker.2026-10-31` and
  `read.aws-builders-timeouts-retries.2026-10-31`; the Resilience4j and SRE
  records are retained and revalidated.
- `edition/patterns/source-plan.v1.json`: 269/268/224 ->
  272/271/226 required/read/ledger; blocked stays 1. Three units are added:
  Microsoft, AWS and the retained SRE chapter.
- `edition/patterns/registry.v1.json`: source units 269 -> 272; technical
  owner and technical/overall coverage move to `partial-bounded`; decision
  coverage stays `partial-bounded`.
- `edition/patterns/owner-units.v1.json`: all four dimensions set to
  `supported` with primary and supporting bindings. Counters: mechanism
  114 -> 115, invariant 79 -> 80, failure/recovery 73 -> 74, alternative
  78 -> 79, technical partial-bounded 15 -> 16, technical partial 69 -> 68;
  sufficient stays 61.
- `edition/patterns/card-batches.v1.json`: the entry gains the dedicated
  `card_path` and the Microsoft record as its cited record.
- `edition/content-revisions.json`: one issue-540 revision for the owner page
  and README. The new page baseline is its historical-view hash, so it needs
  no separate authorization.
- `edition/atlas-manifest.json`, `edition/directory-migration.json`,
  `sources/document-identities.json` and
  `edition/patterns/semantic-audit.v1.json`: register the page, identity,
  baseline and atlas review entry.
- Route and section indexes, census, coverage/reverse maps, phase 4, delivery
  evidence, semantic summary, qrels, inventory, sufficient candidates and
  re-review packets were refreshed. Guards move to 503 pages, 80 V11
  documents, 272 registry units, 271 read units and 226 ledger records.
- The 2026-10-22 re-reviews for Circuit Breaker and Bulkhead now pin
  `reviewed_page_sha256`; reconciliation records both as
  page-changed-since-review. Packet counts move from 56 reviewed / 79 changed
  to 54 / 81.

## Deviations from the B48 note

- The note proposed two reading records and implied two units. The owner-unit
  validator and preflight require every bound source and record to exist in
  the source plan and registry; failure/recovery cites the retained SRE
  record, so the SRE unit is added too. Ledger records stay +2; source-plan
  and registry units are +3.
- The owner page keeps the lane's "Proposed records" wording as historical
  lane text. The dedicated card describes the records as applied. The shared
  ledger contains both new records.
- Owner line numbers changed after the frontmatter addition and the expanded
  section: Circuit Breaker 115 -> 117 and Bulkhead 133 -> 200. Unit terms and
  the shared-page bounded count were updated to match.
- The failure/recovery owner quote was lowercased to match the owner body
  verbatim for preflight.
- Microsoft binding sections were corrected to "Solution" after checking the
  pinned Markdown; the affected quotes are in the source's Solution section.
- A verification fetch of the AWS article returned a different raw HTML
  digest (`2da40244f7c8dc30aca7d491977a3efff489c30dd3fda9ccb3b6dcddc245fe30`,
  139,053 bytes) from the lane's recorded `d289c95d...`. The recorded
  revision is retained and no new hash is claimed. The article is living; it
  should be re-pinned before a future promotion.

## Validation

- `preflight_sufficient.py --pattern tycho.pattern.circuit-breaker`: PASS,
  1/1.
- Full suite: 688 tests pass. The first run found the historical re-review pin
  missing; after pinning both records the rerun passed.
- PASS: sources, registry, cards, owner units, atlas, directory migration,
  edition, coverage, census, phase 4, delivery evidence, semantic audit,
  source catalogue, claim references, AI reviews and sufficient promotions.
- PASS: line length (145 exact owner-link exceptions) and boundary checks.
- At parent HEAD `validate_book_navigation.py` already reports four missing
  local anchors in dark-launching and RBAC/ABAC pages; they are unchanged by
  this integration. `validate_knowledge.py --mode strict` fails on the same
  pre-existing navigation check; no new failure is introduced.

## Limits

- Partial-bounded coverage only; no Circuit Breaker promotion or owner
  acceptance.
- No external AI content review was run for this integration; the book/atlas
  review gate remains outstanding.
- The integrator applied the lane's recorded revisions. A verification fetch
  checked quote placement only and did not replace the recorded
  representations. No benchmark, production observation or runtime experiment
  is claimed.
- No new source id was added; linked pages and images remain outside the
  records.
