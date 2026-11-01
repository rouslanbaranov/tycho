# B9 — ready-lane integration and two card splits, 2026-10-29

Status: integrated and review-ready. No promotion, sufficient-coverage claim or
owner acceptance was added.

## Parent and lanes

- Parent HEAD: `0bbf500a`.
- Cherry-picked in order: Gatekeeper `ca6e3686` -> `f0775bc3`, Health
  `c55b4656` -> `73eb0a8a`, Multi-Leader `6b6f9688` -> `8f9d5b5c`.
- The three lanes edited six disjoint book files and no shared metadata. All
  shared metadata, derived artifacts and review records were applied once here.
- Coverage stays `partial-bounded` for all three entries; no promotion record
  was added and the existing 22 promotions remain unchanged.

## Card splits

- Gatekeeper:
  `book/volumes/v11-pattern-atlas/c02-api-communication/gatekeeper.md`,
  page id `tycho.page.e709abf2484148c4a0d0fe76321a09b6`, card SHA-256
  `6ce9d5a58ed646991c36686016b50d1e25a70d52b15687576ce29a4bd45a74b6`.
- Multi-Leader Replication:
  `book/volumes/v11-pattern-atlas/c06-database-storage/multi-leader-replication.md`,
  page id `tycho.page.1f0f0984036746779cc0bc96826db1e9`, card SHA-256
  `2fd84c096dfffa719d59a476b7efdd35baa0ce6562667e97cfbf7b97ef6f7165`.

- Both card sections moved verbatim; the chapter headings remain as stable
  `#gatekeeper` and `#multi-leader-replication` index anchors with one link.
- Moved-body SHA-256: Gatekeeper
  `8e2a16ff4c5d5bac17c2cf5009a6be9bd334d59847ff9686cd999c1e62d292e2`;
  Multi-Leader
  `7ea8bbd06c6100e5c067f3cd2934809bdd8d63ed0f01e2ef4d3890d518c71a88`.
- Post-split chapter README SHA-256: c02
  `794cbeb4ca02f9670435b6b961c93662a094012572f7d1a9d84292e7e563701e`;
  c06 `b45ce74d6c1cd08a3ed0e688e7eedc363ab95609f1f138c125d25ac14b1c3ca9`.
- The V02/C07 and V04/C02 owner backlinks now point to the dedicated pages.
- Registered in the atlas manifest, directory migration (469 canonical
  documents), document identities, semantic audit and `card_path`; the V11
  atlas carries 46 documents. The chapter result, navigation and limits
  sections remain on both READMEs.

## Sources and metadata

- Added ledger records `read.microsoft-health-endpoint.2026-10-29` for
  Microsoft's Health Endpoint Monitoring pattern (canonical text SHA-256
  `b5b302585c4e60a5d696b128b6a03d21c9629848e9fa2be23e6e1bc1751d1d61`,
  "When to use this pattern") and
  `read.postgresql-replication-solutions.2026-10-29` for PostgreSQL 18
  section 26.1 (canonical text SHA-256
  `7a5bc0622dd4ff65ca5e13a3b449c0e7d2855f3ad875305d1f7df1569d2604f9`,
  asynchronous and synchronous multi-master subsections).
- Source-plan and registry units were added for both records. The plan now
  reports 168 required units, 167 read units and 138 ledger records.
- Owner units: Gatekeeper `failure_recovery` is supported by the SPoF and
  redundant-instance advice in the existing gatekeeper record; Health and
  Multi-Leader `alternative` are supported by the new units. All three
  `decision_evidence.competing_alternative` values match the moved card text.
  Summary counts: 47 failure/recovery and 60 alternative supported entries.
- The ready plan moves all three entries to `awaiting-external-review`;
  candidate sources now include `src.microsoft-cloud-patterns` and
  `src.postgresql` where applicable.
- Historical review records for the three entries and for the other three
  patterns on the changed replication owner page pin their reviewed page
  hashes; no historical verdict was changed.

## Refresh and rebind

- One full `scripts/refresh_atlas_artifacts.py --authorize ...` run rebuilt
  the route index, section index, census, coverage, phase 4, inventory,
  candidates, reconciliation, review scope and packets.
- A follow-up format-only fix shortened one 101-character frontmatter question
  line in the new Gatekeeper page. The page hash, directory baseline and
  derived artifacts were rebound without changing the card body; the full
  refresh was not rerun.
- The same refresh rebound the two pre-existing format-only page wraps from
  `0bbf500a` (anti-corruption-layer and rbac-abac) in the inventory, atlas
  and semantic hashes; their canonical text is unchanged.
- `python3 scripts/book_change.py --plan`: clean after the rebind and the
  candidate/reconciliation regeneration.

## Packets

- 145 packets: 36 `page-changed-since-review`, 99
  `reviewed-by-independent-agent` and 10
  `awaiting-current-external-review`.
- Gatekeeper, Health and Multi-Leader are each
  `page-changed-since-review` with their historical page hash pinned and
  their new card and owner hashes recorded.
- All verdict templates remain blank; no reviewer, verdict or finding was
  filled. These packets are review hand-offs, not reviews.

## Verification

- Targeted atlas, card, coverage, owner-unit, phase 4, registry, semantic,
  source, delivery, directory, edition, enrichment, promotion, acceptance,
  pilot, metadata and corpus-qrels validators pass.
- `python3 scripts/check_boundary.py`: pass.
- `python3 scripts/check_markdown_line_length.py`: pass; 145 exact
  owner-link exceptions retained.
- `python3 scripts/validate_book_navigation.py`: the same four pre-existing
  missing-local-anchor findings in the dark-launching and RBAC pages.
- Full suite at batch end: `python3 -m unittest discover -s tests`, 688
  tests, OK, run once. One earlier full run found only a stale candidate
  matrix after review-record pinning; regeneration fixed it.

## Limits

- No entry reaches `sufficient`; no promotion, owner acceptance or
  independent review is claimed.
- The new source records cover only the sections named above; the digests
  cover canonical page text, not linked pages or figures.
- This record is a structural integration and hand-off, not proof of source
  truth, completeness or merge readiness.
