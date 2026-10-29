# B2-B6 accelerated pre-split batch - 2026-10-29

Status: split complete and review-ready. No external review, promotion or owner
acceptance was performed in this batch. Content is at the pre-split state below;
a fresh review is required before any promotion is restored.

## Parent and scope

- Parent HEAD: `4f111f25eb6fbccedaab78ddd9197fcf7ea54b8b`.
- One accelerated batch covering inventory B2, B3, B4, B5 and B6.
- Ten pages were added: four atlas cards and six dedicated owner notes.
- Eight promotions and their owner acceptances are suspended; all four dimensions
  remain supported and coverage remains `partial-bounded`.
- Paths below use the inventory shorthand: `vNN/cMM/file.md` names the cMM
  directory under the vNN volume.

## Moves

| Batch | Entry | Card page | Owner page |
|---|---|---|---|
| B2 | Transactional Outbox | v11/c04 | v04/c05 |
| B3 | Static Content Hosting | v11/c09 | v08/c08 |
| B4 | Self-Contained Service | v11/c01 | unchanged (card only) |
| B4 | Immutable Infrastructure | unchanged (candidate card) | v08/c03 |
| B5 | Controlled Cutover | v11/c10 | v10/c05 |
| B5 | Dark Launching / Shadow Traffic | dedicated card unchanged | v08/c04 |
| B6 | RBAC / ABAC | dedicated card unchanged | v09/c05 |

Each old section is replaced by a one-line index link; the six affected chapter
landings also list the new owner notes. Card and owner bodies moved verbatim; only
the technical-owner link path changed where an owner moved.

## Suspended promotions and acceptance

The suspended entries are Transactional Outbox, Static Content Hosting,
Self-Contained Service, Sidecar, Ambassador, Controlled Cutover,
Dark Launching / Shadow Traffic and RBAC / ABAC. Their promotion records and
acceptance entries were removed; every saved review report remains on disk.
Registry, owner-unit and ready-plan coverage is `partial-bounded`; no sufficient
claim, CI result or merge permission is implied.

### Transactional Outbox (B2)

- Card: `v11/c04/transactional-outbox.md`
- Card SHA-256: `d0e15060bb5d3a18abac64d8c784ca68c457bdcea52632f497194ad6f39317ca`
- Owner: `v04/c05/transactional-outbox.md`
- Owner SHA-256: `97be1479721f6492ef182a5bdbd08c5a5c6dcac2029b329b9c22f4bff94bc7ae`
- Moved card-body SHA-256: `d438fc70a32c3ff10b9afcb671687711848ff48ed07b698a800bdfc4c80e341f`
- Moved owner-body SHA-256: `5a6b0e30aab50ec8da29a9b910413a09881524b4281cd82d7511b407e29a71c9`

### Static Content Hosting (B3)

- Card: `v11/c09/static-content-hosting.md`
- Card SHA-256: `23a362f212f996b619fdac41b7b679653af9557e21bb6f3677d302b389207984`
- Owner: `v08/c08/static-content-hosting.md`
- Owner SHA-256: `1f3d9ebeb1aba3a23ddb19650e75fb8611c34d3e4c484a9dacef9955277f9c06`
- Moved card-body SHA-256: `dee73e557357188f73979c8b9a255e5c4f911e8ec7360b73829cb5187c969383`
- Moved owner-body SHA-256: `99fcdc1bcfa8b12a494da69c7112c5bfab7d046fd87a3741b08ec17bc7167949`

### Self-Contained Service (B4)

- Card: `v11/c01/self-contained-service.md`
- Card SHA-256: `1b7839e0a8ac2993cbfdd451fa7cf58bd1511dd1f731a949cb56dc3ae3f333c7`
- Owner: `v02/c04/service-independence.md`
- Owner SHA-256: `f343e82b6b2fb24904176c2652dfabfbc4c92aecb3e91feb478d3fc35e07fd48`
- Moved card-body SHA-256: `90628b705649cf76ea8e311a502e23ba4c761000a059bc1044647a94f2672b73`

### Sidecar (B4)

- Card: `v11/c01/sidecar.md`
- Card SHA-256: `d2169cf74651eac88b0a169f144a6a16bcfbc057778e81f798c4cca565112d7a`
- Owner: `v08/c03/static-stability.md`
- Owner SHA-256: `d18bf7cfbcc64c7aa2ceb1a087f51561fc48ace5d137b60d6bc1892e092ca5a3`
- Moved body: n/a; the owner section did not move.

### Ambassador (B4)

- Card: `v11/c01/ambassador.md`
- Card SHA-256: `e424421b7b483dcc541a96a4857eaf26b6c076489612391d60c547ab3d451fd0`
- Owner: `v08/c03/static-stability.md`
- Owner SHA-256: `d18bf7cfbcc64c7aa2ceb1a087f51561fc48ace5d137b60d6bc1892e092ca5a3`
- Moved body: n/a; the owner section did not move.

### Controlled Cutover (B5)

- Card: `v11/c10/controlled-cutover.md`
- Card SHA-256: `8e9b67fb18e148fe699d0658627d4c5eb05c6d1e572ed97f83688d2453565b7d`
- Owner: `v10/c05/controlled-cutover.md`
- Owner SHA-256: `b21931c6b6942f430ee16a8a432ee0290757970593f5894f12ae08e29c934840`
- Moved card-body SHA-256: `81ae1588a869caeca341b545a6791f63ff16c1189052a76a6e630eb6e3c7c433`
- Moved owner-body SHA-256: `cb9c8bd19b335a60b224b22a6289422a954fd9d59d3a80bba4eb537e882f0bb7`

### Dark Launching / Shadow Traffic (B5)

- Card: `v11/c10/dark-launching.md`
- Card SHA-256: `c4d0cb689a82700bbca460b5ec22367b0956b302c9a3ea5ead3961d3788f6984`
- Owner: `v08/c04/dark-launching-shadow-traffic.md`
- Owner SHA-256: `4cadc13e42d1973371b640432d9d50b95028cdb9cc4ada5a8965ac8a1c62d87d`
- Moved owner-body SHA-256: `9dff8bad30c9ee47a237c07927fab3d4ea44ad86df4a58a9278d8c7492534906`

### RBAC / ABAC (B6)

- Card: `v11/c11/rbac-abac.md`
- Card SHA-256: `8ce0024163783f49ca38d632be37513e3906f475979db28def48c06fc0c88cee`
- Owner: `v09/c05/rbac-abac.md`
- Owner SHA-256: `18e84b34a990496905215537493f177e445b1c6eaf8c1b33380b7d47d75c6c68`
- Moved owner-body SHA-256: `71e2173e88c977c4d820757ba06cdc1da2f7127efef5c083329f57948b9b7d33`

## Registration

- Atlas manifest: four new V11 card pages; 42 documents, 145 patterns.
- Directory migration: 10 new page records; canonical documents 459.
- Document identities, semantic audit and page census: 10 new pages, 459 total.
- Enrichment manifest: six split owner pages registered with `origin_page` and no
  new source-inspection claim.
- Card batches, registry and owner units rebind the new card and owner paths.
- The source plan, coverage, reverse map, phase 4, route index, delivery evidence,
  inventory, qrels snapshots and rereview packets were refreshed once.

## Moved-body hashes

- B2 card: `d438fc70a32c3ff10b9afcb671687711848ff48ed07b698a800bdfc4c80e341f`
- B2 owner: `5a6b0e30aab50ec8da29a9b910413a09881524b4281cd82d7511b407e29a71c9`
- B3 card: `dee73e557357188f73979c8b9a255e5c4f911e8ec7360b73829cb5187c969383`
- B3 owner: `99fcdc1bcfa8b12a494da69c7112c5bfab7d046fd87a3741b08ec17bc7167949`
- B4 card: `90628b705649cf76ea8e311a502e23ba4c761000a059bc1044647a94f2672b73`
- B4 owner: `ed3f719417e2a2e53f873d34fdf01318736c361b3d40064c4ea8e52a45c56534`
- B5 card: `81ae1588a869caeca341b545a6791f63ff16c1189052a76a6e630eb6e3c7c433`
- B5 owner: `cb9c8bd19b335a60b224b22a6289422a954fd9d59d3a80bba4eb537e882f0bb7`
- B5 dark owner: `9dff8bad30c9ee47a237c07927fab3d4ea44ad86df4a58a9278d8c7492534906`
- B6 owner: `71e2173e88c977c4d820757ba06cdc1da2f7127efef5c083329f57948b9b7d33`

## Verification

- `python3 scripts/book_change.py --plan`: clean after refresh.
- Structural validators: atlas, cards, coverage, owner units, phase 4, registry,
  semantic audit, sources, delivery evidence, directory migration, edition,
  enrichment, promotions, acceptance, pilot inputs and book metadata pass.
- `python3 scripts/check_boundary.py`: pass.
- `python3 scripts/check_markdown_line_length.py`: the same three pre-existing
  V11 failures remain (two c01 lines and one c11 RBAC card line).
- Full suite at batch end: `python3 -m unittest discover -s tests`, 608 tests,
  OK after correcting one moved qrels path exposed by the first run.
- Verbatim check: every moved card or owner body is a contiguous substring of its
  new page; card bodies match after normalizing the owner-link path only.

## Review packets needed

One fresh external AI review per suspended entry at the review HEAD, using the
card and owner hashes above. Use a different vendor/harness, or a fresh read-only
DeepSeek Reviewer not derived from this conversation. Reviewers must:

1. Work read-only; do not edit, commit, push, open a PR or change configuration.
2. Not run tests; the authoring parent already ran the suite once.
3. Read the exact card and owner section, verify the moved body bytes against the
   hashes above, and check all four dimensions and stated limits.
4. Return verdict, evidence, findings by severity with exact paths and limits;
   use a bounded schema and state `sufficient: 0` until a separate promotion
   commit exists. Do not claim owner acceptance.

Packet grouping: B2 one entry, B3 one, B4 three (Self-Contained Service,
Sidecar, Ambassador), B5 two (Controlled Cutover, Dark Launching / Shadow
Traffic), B6 one. Save each raw report under `authoring/ai-reviews/` and add its
SHA-256 to the index only after the review is complete. Owner acceptance is
recorded once after the planned batch set, not per batch.

## Limits

This record does not prove correctness, sufficient coverage, independent review,
CI or merge readiness. It records a structural split and its review hand-off.
Review HEAD is the commit that contains this record; run `git rev-parse HEAD`.
