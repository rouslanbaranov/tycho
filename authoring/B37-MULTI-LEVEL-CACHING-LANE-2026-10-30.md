# B37 — Multi-Level Caching invariant and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and failure/recovery were supported;
invariant and alternative were partial. This lane binds the source-supported
parts of both dimensions to Hazelcast Near Cache 5.6, Redis client-side
caching and AWS Well-Architected caching guidance, and labels the per-tier
synthesis, version-check example, promotion rule and local-only comparison as
Tycho guidance. A detached scratch metadata patch passes preflight and
owner-unit/source checks; the patch is not in the lane commit.

## Lane coordinates

- Parent HEAD: `255474fd9016a51d86041a952299c46f6171bcb4` (`255474fd`).
- Branch: `b37-multilevel`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b37-multilevel`.
- Scope: the owner section `### Multi-Level Caching` in the V06/C01 owner page
  and the inline V11/C05 card `### Multi-Level Caching`. Single-entry lane; no
  other entry, shared owner page, promotion or generated file is changed.
- Owner path (concatenate the three lines):

      book/volumes/v06-caching-indexing-and-retrieval/
      c01-local-and-distributed-caching/
      local-and-distributed-cache-design.md

- Card path:
  `book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md`.
- Path check: the parent brief named V11 (C05/C06). At this HEAD V11/C05 is
  caching and retrieval and contains the card at line 388; V11/C06 is database
  and storage and has no multi-level card. No C06 card was created.
- The card remains inline; the integrator owns any split and `card_path`
  registration.

## Candidate evaluation

- Hazelcast, "Near Cache", 5.6 (selected; existing source `src.hazelcast`;
  proposed record). Selected for the local-copy description, the explicit
  eventual-consistency and stale-read cost, the invalidation-loss statement,
  the loss-detection and fallback behavior, and the "high invalidation rates"
  cost. The page is versioned 5.6 and carries a warning that 5.7 is current.
- Redis, "Client-side caching introduction" (selected; existing source
  `src.redis`; proposed record). Selected for the local-cache latency benefit,
  the server-side tracking and invalidation-message description, the
  disconnect-flush behavior and the invalidation-overhead warning.
- AWS, "PERF03-BP05 Implement data access patterns that utilize caching"
  (selected; new source `src.aws-caching-guidance`; proposed record). Selected
  for the explicit client-side, remote and multi-level comparison, the
  duplicate/inconsistency cost of local copies, the remote-cache network-hop
  cost and the TTL invalidation step.
- Hazelcast, "Near Cache", existing `read.batch3-hazelcast-near.2026-10-21`
  (retained, not replaced). It covers the same page at an earlier
  representation and supports the existing mechanism and failure bindings; the
  new record binds the 2026-10-30 representation used by this lane.
- Redis, "Cache-aside" (examined, not selected). It supports application-owned
  fill and invalidation, not the local-versus-shared tier comparison.
- AWS, "Caching patterns" whitepaper URL (examined, not selected). The URL now
  redirects to an ElastiCache Memcached strategies page; mixing that page with
  the Well-Architected multi-level guidance would weaken the product and
  revision boundary.
- AWS, "Caching best practices" (examined, not selected). It carries TTL and
  cache-expiration guidance but no client-side/remote tier comparison.
- Redis, "CLIENT TRACKING" command reference (examined, not selected as a
  separate unit). The selected introduction page already carries the tracking
  and invalidation claims used here; the command reference is a candidate for
  a later protocol-level unit.

## Source binding

Quotes reproduce the served prose. Markdown bold/italic markers and page
navigation are not repeated; line breaks inside a quote are editorial wrapping.
The binding revision always identifies the exact representation: raw HTML
digest and article/main-text digest for Hazelcast and Redis, and the Markdown
alternate digest for AWS.

### Hazelcast — Near Cache 5.6

- Source id: `src.hazelcast` (existing).
- Proposed record: `read.hazelcast-near-cache.2026-10-30`.
- URL:
  `https://docs.hazelcast.com/hazelcast/5.6/cluster-performance/near-cache`.
- Unit label: "Near Cache — Hazelcast documentation"; unit type
  `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET on 2026-10-30; served HTML 156,052 bytes; raw HTML
  SHA-256
  `3dafe42787ec7b957abf573e69f9ad506eb3a7cec4b1031372b9e7b506e1af7f`;
  article-region text 26,510 characters, SHA-256
  `7a90d5773194eebdc81c567da7a8eebf7550b0669e156cd9398ab0013486b70e`;
  HTTP Date 2026-10-30T19:40:14Z; no Last-Modified, ETag or published commit
  in the served headers. Version badge 5.6. The page's edit link names
  `hazelcast_versioned_docs/version-5.6/develop-and-build/best-practices/near-cache.mdx`;
  the latest GitHub commit touching that path is
  `b6b79177a352c465476aacd9f3c3e90a133dc488` (2026-10-26), recorded as a
  source-path revision, not a build identifier printed by the page. This is
  the binding revision.
- Sections used: "Near Cache", "Near Cache Invalidation", "Near Cache
  Consistency", "Eventual Consistency".
- Exact quotes used:

      Access to small-to-medium, read-mostly data sets may be sped up by
      creating a Near Cache. This cache maintains copies of distributed data
      in local memory for very fast access.

      Strong consistency is not maintained; you might read stale data.

      Near Caches are invalidated by invalidation events. Invalidation events
      can be lost due to the fire-and-forget fashion of the eventing system.
      If an event is lost, reads from Near Cache can indefinitely be stale.
      To solve this problem, Hazelcast provides eventually consistent behavior
      for IMap/JCache Near Caches by detecting invalidation losses. After
      detection of an invalidation loss, stale data is made unreachable and
      Near Cache's get calls to that data are directed to the underlying
      IMap/JCache to fetch the fresh data.

      High invalidation rates can outweigh the benefits of locality of
      reference.

- Limits: one versioned product page; no cache was run and no invalidation
  was exercised. The page states that 5.6 is not the latest version. The
  loss-detection/reconciliation behavior is a product mechanism, not a
  general requirement for every cache tier.

### Redis — client-side caching introduction

- Source id: `src.redis` (existing).
- Proposed record: `read.redis-client-side-caching.2026-10-30`.
- URL:
  `https://redis.io/docs/latest/develop/clients/client-side-caching/`.
- Unit label: "Client-side caching introduction — Redis documentation"; unit
  type `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET on 2026-10-30; served HTML 129,232 bytes; raw HTML
  SHA-256
  `2fe5199edb619ef4fc3bc17d72312ba5b356ce061c0ca82b2950a10cae15561d`;
  main-region text 7,148 characters, SHA-256
  `cd9a01d947a7526971b77d903ae2b37845ad2cabf4115a26dd17dc5a26485f20`;
  HTTP Date 2026-10-30T19:40:14Z; Last-Modified 2026-10-30T10:29:51Z;
  `dateModified` 2026-09-29T16:29:37+01:00; `x-goog-generation`
  1793356191351775; MD5 `JLBJaABpn+4VP7jac3W2yw==`; no ETag or published
  version. The page's edit link names
  `content/develop/clients/client-side-caching.md`; the latest GitHub commit
  touching that path is
  `998b50d6573d1b9d0461214206f1688f0f116d72` (2026-09-29), which matches the
  declared `dateModified`. This is the binding revision. The URL is a rolling
  `latest` page; the digest and commit pin it.
- Sections used: "Client-side caching introduction", "Updating the cache when
  the data changes", "Usage recommendations".
- Exact quotes used:

      Client-side caching reduces network traffic between a Redis client and
      the server, which generally improves performance.

      When any client writes new data to a tracked key, the server sends an
      invalidation message to all clients that have accessed that key
      previously. This message warns the clients that their cached copies of
      the data are no longer valid and the clients will evict the stale data
      in response.

      If any connection from a client gets disconnected (including one from a
      connection pool), then the client will flush all keys from the
      client-side cache.

      Cache misses, tracking, and invalidation messages always add a slight
      performance penalty.

- Limits: one documentation page; no Redis server or client was run. The page
  describes server-assisted client-side caching; it does not define a
  deployment's authorization, eviction or failure policy.

### AWS — Well-Architected caching guidance

- Source id: `src.aws-caching-guidance` (new).
- Proposed record: `read.aws-caching-guidance.2026-10-30`.
- URL: the AWS Well-Architected
  `perf_data_access_patterns_caching.html` page under
  `https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/`.
- Markdown alternate: the
  `perf_data_access_patterns_caching.md` page under
  `https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/`.
- Unit label: "PERF03-BP05 Implement data access patterns that utilize
  caching — AWS Well-Architected"; unit type `documentation-page`; access
  date 2026-10-30.
- Access: public HTTPS GET of the Markdown alternate on 2026-10-30; 7,404
  bytes; SHA-256
  `2a8596fad95cec9fcea60751e31a9190a76fcb0f773ee83c1c51d8775ff83ceb`;
  HTTP Date 2026-10-30T19:40:19Z; Last-Modified 2026-10-30T15:49:50Z; ETag
  `"bhrgUNnmIr/OXJkhVOqh60xI2Ic="`; no published version identifier. The
  HTML representation is 26,884 bytes, SHA-256
  `2f5070e63c27e48a5f779f6348d43cc4a7cc7f717bec4a63a057cfdabf9ed55b`,
  HTTP Last-Modified 2026-10-30T15:49:32Z, ETag
  `"nVU0RzAriohMDhejGCOoeGQOhXQ="`. This is the binding revision.
- Sections used: "Implementation guidance", "Client-side caching", "Remote
  caching", "Implementation steps".
- Exact quotes used:

      Data can be cached at multiple levels in the application, such as within
      the application making remote calls, known as client-side caching, or by
      using a fast secondary service for storing the data, known as remote
      caching.

      This pattern allows each client to store data in the closest location
      possible (the client itself), resulting in the lowest possible latency.

      One disadvantage of this approach is that when multiple clients are
      involved, they may store the same cached data locally. This results in
      both duplicate storage usage and data inconsistency between those
      clients.

      This strategy allows for more consistent responses between clients,
      better efficiency in stored data, and a higher volume of cached data
      because the storage space scales independently of clients.

      The disadvantage of a remote cache is that the overall system may see a
      higher latency, as an additional network hop is required to check the
      remote cache. Client-side caching can be used alongside remote caching
      for multi-level caching to improve the latency.

      Configure a cache invalidation strategy, such as a time-to-live (TTL),
      for all data that balances freshness of data and reducing pressure on
      backend datastore.

- Limits: one living guidance page; no cache was configured, no latency was
  measured and no TTL experiment was run. The page is general Well-Architected
  guidance, not a product implementation contract or a benchmark.

## Book edits

### Owner section

- Frontmatter: only `updated_at` moves from 2026-10-20 to 2026-10-30.
  `evidence_scope`, `content_review`, `source_inspection_date` and
  `content_verified_at` remain byte-identical; the new sources are proposed
  records and supporting bindings, not new `evidence_scope` ids.
- The mechanism paragraph names the Hazelcast local-copy and eventual-
  consistency statements and the Redis local-cache and invalidation-penalty
  statements. It keeps the existing local-tier-in-front-of-shared-tier
  definition.
- The invariant paragraph is labelled **Tycho synthesis**. It binds the
  Hazelcast invalidation-loss, loss-detection and fallback statements, the
  Redis write-invalidation and disconnect-flush statements, and the AWS TTL
  invalidation step. It labels the per-tier disjunction, the version-check
  example and the "every tier" scope as Tycho guidance; no selected source
  states a per-tier version check.
- The failure/recovery paragraph keeps the existing supported owner quote
  verbatim and binds the same Hazelcast/Redis/AWS recovery paths.
- The alternative paragraph is labelled **Tycho synthesis**. It binds the AWS
  remote-cache consistency/storage-efficiency and network-hop statements, the
  AWS client-side latency/duplication statements and the AWS multi-level
  statement. It labels the measurement threshold, the local-only fallback and
  the promotion rule as Tycho guidance.
- A limits paragraph and a three-item source list name the proposed records,
  raw hashes and article/main/Markdown digests.
- Raw SHA-256:
  `06745a814b5456fe11dd6c535613151b6892cc2e0f3272ff43676d956cc7c5e9`.
- Historical-view SHA-256:
  `8ae81dcb777e6ec91a1cf41b301b5e9c5bfbcc39bc839e07402d6398cc5f240a`.
- The owner heading stays at line 194; the page is 270 lines. The later
  `### Distributed Cache` heading moves from line 210 to line 255.

### V11/C05 inline card

- Frontmatter is unchanged. The 2026-10-30 review, update and inspection dates
  already exist; `content_verified_at` stays `null`.
- **Good-fit conditions** now require a named freshness bound per tier and a
  detected missed invalidation or TTL bound, in addition to owned promotion and
  invalidation.
- **Hard contraindications** now include an untestable staleness bound.
- **Competing alternative** now compares a single shared remote cache with a
  local-only cache and states the consistency-versus-network-hop and
  duplication costs.
- **Failure and recovery** now points to the lost-invalidation,
  disconnect-flush and TTL bounds.
- **Sources** adds the 2026-10-30 Hazelcast, Redis and AWS bindings and states
  that the new records and the AWS source are proposed, not registered.
- The heading stays at line 388; the chapter page is 459 lines.
- Raw SHA-256:
  `4b842489f1d37efcb5efd2f7990d4456821922718276ae2235b5b809d10e8733`.
- Historical-view SHA-256:
  `08c45aecd650de85529cdd0ecabbe43b959a11f54a3563dfc37e2767faf42b2e`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was exercised in a detached
scratch copy of this worktree. The scratch results are in the Validation
section. The patch must not be merged until the book/atlas independent review
gate is satisfied.

### Source register `sources/register.json`

Add one source record; set `updated` to 2026-10-30. The source count moves from
296 to 297.

- `src.aws-caching-guidance` — title "AWS Well-Architected caching guidance";
  category "caching"; publisher "Amazon Web Services"; kind "official-docs";
  URL and resolved URL the HTML page; topics
  `["performance-engineering", "data-architecture"]`; priority "core";
  planned use "Client-side, remote and multi-level caching
  latency/consistency trade-offs and TTL invalidation for the Multi-Level
  Caching entry."; admission "admitted-for-research"; access
  "public-web-or-author-download"; reading status
  "full-public-page-inspected"; version records the Markdown alternate
  7,404 bytes with its SHA-256, Last-Modified and ETag, and the HTML
  26,884 bytes with its SHA-256, Last-Modified and ETag, plus "no published
  version identifier"; `access_checked` and `content_verified` 2026-10-30;
  license note "Public AWS documentation; cite short excerpts and paraphrase;
  do not mirror."; verification scope names the four sections and excludes
  linked pages; observed title "PERF03-BP05 Implement data access patterns
  that utilize caching - Performance Efficiency Pillar".

The existing `src.hazelcast` and `src.redis` entries do not need a new
identity. If the integrator wants their `version` fields to carry the exact
2026-10-30 representations, add the five-line digest metadata there; do not
rewrite their URLs or admission state.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add three records; set `updated` to 2026-10-30. Records move from 183 to 186.
Each is `status: read`, `reviewer: "Automated authoring agent"`, unit type
`documentation-page`, and uses the exact URL, sections and
`content_sha256` below.

- `read.hazelcast-near-cache.2026-10-30` — `src.hazelcast`; sections
  "Near Cache", "Hazelcast Data Structures with Near Cache Support",
  "Configuring Near Cache", "Near Cache Configuration Examples", "Near Cache
  Example for IMap", "Near Cache Example for JCache Clients", "Example for
  Near Cache with High-Density Memory Store", "Near Cache Eviction", "Near
  Cache Expiration", "Caching of null values", "Near Cache Invalidation",
  "Near Cache Consistency", "Eventual Consistency", "Locally Initiated
  Changes", "Near Cache Preloader"; raw HTML digest
  `3dafe427...`.
- `read.redis-client-side-caching.2026-10-30` — `src.redis`; sections
  "Client-side caching introduction", "Updating the cache when the data
  changes", "Usage recommendations"; raw HTML digest `2fe5199e...`.
- `read.aws-caching-guidance.2026-10-30` — `src.aws-caching-guidance`;
  sections "Implementation guidance", "Client-side caching", "Remote caching",
  "Implementation steps"; Markdown digest `2a8596fa...`.

Claims supported, claims not supported and limitations stay bounded to the
selected sections; no implementation behavior, independent reproduction or
deployment configuration is claimed. The existing
`read.batch3-hazelcast-near.2026-10-21` record remains unchanged.

### Source plan `edition/patterns/source-plan.v1.json`

Append three units to `tycho.pattern.multi-level-caching` after the existing
Hazelcast unit, in the order used by the registry below. Use the same source
ids, labels, URLs, unit types, section lists, status `read` and record ids as
the Source binding section. Set `updated` to 2026-10-30. Summary:
`required_units` 220 -> 223; `read_units` 219 -> 222; `ledger_records`
183 -> 186. Replace the entry notes with: "The 2026-10-30 Hazelcast, Redis and
AWS units support invalidation, loss detection, disconnect flush and TTL
bounds; per-tier scope, version check, promotion rule and local-only
comparison remain Tycho guidance." Recompute `registry_sha256` after saving
the registry and refresh `route_index_snapshot` from the rebuilt route index.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.multi-level-caching`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to `partial-bounded`;
  keep `coverage.decision` at `partial-bounded`.
- Replace `source_units` with, in order: the existing Near Cache unit; the
  Near Cache 5.6 2026-10-30 revision; Redis client-side caching; AWS
  Well-Architected caching. All four have status `read`.
- Replace `notes` with: "Invariant and alternative bound 2026-10-30 to
  Hazelcast Near Cache 5.6, Redis client-side caching and AWS Well-Architected
  caching; per-tier scope, version check, promotion rule and local-only
  comparison remain Tycho guidance. Coverage partial-bounded; no promotion."
- Keep `review_status` `self-checked` and `atlas_owner` at V11/C05.
- Set `updated_at` to 2026-10-30.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.multi-level-caching`:

- Keep `owner.line` at 194, the heading, document id and unit terms unchanged.
- Invariant: `state: supported`; `quote: "Every tier must receive the
  invalidation, or it must detect a missed invalidation and bound how long a
  stale copy can be served."`; reason separates the Hazelcast, Redis and AWS
  statements from the Tycho per-tier disjunction and version-check example;
  primary binding `src.hazelcast`, record
  `read.hazelcast-near-cache.2026-10-30`, section "Eventual Consistency",
  revision `3dafe427...`; supporting bindings for Redis disconnect flush and
  AWS TTL.
- Alternative: `state: supported`; use the exact owner sentence:

      A remote cache avoids duplicate local copies and gives "more consistent
      responses between clients, better efficiency in stored data"; its cost is
      "higher latency, as an additional network hop is required to check the
      remote cache."

  The reason separates the AWS remote/local comparison and Hazelcast/Redis
  local-tier costs from the Tycho decision threshold, local-only fallback and
  promotion rule; primary binding `src.hazelcast`, record
  `read.hazelcast-near-cache.2026-10-30`, section "Near Cache", revision
  `3dafe427...`; supporting bindings for AWS remote caching/multi-level and
  Redis local-cache latency.
- Keep mechanism and failure/recovery states, quotes and bindings unchanged.
- `source_support`: keep the existing
  `read.batch3-hazelcast-near.2026-10-21` primary record and add auxiliary
  records for the three new records with their revisions. Set
  `technical_coverage` to `partial-bounded`; set `notes` to the registry
  notes above.
- Set `decision_evidence.competing_alternative` to the new card text:
  "Single shared remote cache or local-only cache. A shared cache gives more
  consistent responses at the cost of a network hop; a local tier lowers
  latency but duplicates data. Reverse the choice when coordination and
  invalidation cost exceeds the latency benefit."
- Set the `### Distributed Cache` entry's `owner.line` from 210 to 255.
- Shared-page entry for the owner path: `bounded_entries` 0 -> 1.
- Summary counters: `invariant_supported` 72 -> 73;
  `alternative_supported` 69 -> 70; `technical_partial_bounded` 19 -> 20;
  `technical_partial` 76 -> 75. No other counter changes.

### Card registration `edition/patterns/card-batches.v1.json`

Add `card_path`:
`book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md` to the
`tycho.pattern.multi-level-caching` entry. This is the same file as the
chapter, not a split. Keep `ledger_record`
`read.batch3-hazelcast-near.2026-10-21`.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B37 Multi-Level Caching invariant and alternative source binding; no promotion
or owner acceptance." Because the patch does not change frontmatter, these
lane-state historical-view hashes are also the final values for the patch:

- Owner path, previous (current authorized record):
  `d53ebae643a6cb6e4c0d364073960aba20a48406ce1f6f48b6a27ec34cebafea`;
  current:
  `8ae81dcb777e6ec91a1cf41b301b5e9c5bfbcc39bc839e07402d6398cc5f240a`.
  Add under `directory_documents` for the canonical owner path.
- Card path, previous:
  `320dc69b1bb944358f7138ee8b387750f4190b6b560ba8b4d08083c725159365`;
  current:
  `08c45aecd650de85529cdd0ecabbe43b959a11f54a3563dfc37e2767faf42b2e`.
  Add under `directory_documents` for the V11/C05 README key.

Raw file hashes for reference:
`06745a814b5456fe11dd6c535613151b6892cc2e0f3272ff43676d956cc7c5e9`
(owner) and
`4b842489f1d37efcb5efd2f7990d4456821922718276ae2235b5b809d10e8733`
(card). Leave `source_blocks`, `enrichment_additions` and
`enrichment_baselines` empty.

### Frontmatter and evidence scope

The lane and the proposed metadata patch leave the owner page's
`evidence_scope` and `source_inspection_date`, and the V11/C05 frontmatter,
unchanged. The new Redis and AWS sources are supporting bindings and proposed
records, not new `evidence_scope` ids. If the integrator wants
`src.redis` and `src.aws-caching-guidance` in `evidence_scope.source_ids`,
treat it as a separate change: add the inspection entries to
`sources/enrichment-inspections-2026-10-20.json`, update the owner
`edition/enrichment-manifest.json` record's source ids, inspection date and
`sha256`, add the source ids to the card frontmatter, and recompute the
owner/card historical-view hashes and content revision values. Do not reuse
the `8ae81dcb...` or `08c45aec...` values after that change.

### Derived artifacts

The book edit changes one canonical owner page and one atlas chapter. The
source register gains one record, so regenerate `sources/CATALOG.md` (scratch
count 297). The registry, card, source-plan and owner-unit changes make the
route index, atlas registry hash, edition inventory and the coverage, census
and reverse-map artifacts stale. Refresh them once at batch end; do not treat
a stale derived hash as a lane content failure. The atlas manifest must record
the new V11/C05 chapter SHA-256
`4b842489f1d37efcb5efd2f7990d4456821922718276ae2235b5b809d10e8733`,
the new owner page SHA-256
`06745a814b5456fe11dd6c535613151b6892cc2e0f3272ff43676d956cc7c5e9`
and the new registry SHA-256. The coverage map and reverse map must record the
new registry hash and route snapshot. The prior review recorded in
`edition/patterns/sufficient-candidates.v1.json` predates this edit and no
longer covers the changed owner page or card bytes. The book/atlas independent
review gate applies; do not update the recorded hash without a fresh review.
The prior review is historical evidence, not acceptance of this lane.

## Validation

Checker output in the lane worktree after the two book edits, before the
metadata patch:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_pattern_cards.py` — PASS, 11 batches, 145 entries.
- `python3 scripts/validate_book_metadata.py` — PASS, 490 documents.
- `python3 scripts/validate_sources.py` — expected FAIL on
  `Unknown source reference in
  authoring/B37-MULTI-LEVEL-CACHING-LANE-2026-10-30.md` because this note names
  `src.aws-caching-guidance` before the register and catalogue patch. The book
  edits alone add no unknown source reference and the book-only scan passed
  296 records before the note was added.
- `python3 scripts/validate_pattern_owner_units.py` — expected FAIL on
  `owner-units-unit-ambiguous: Distributed Cache` because the later heading
  moved from line 210 to 255; the owner-units JSON is unchanged in the lane.
- `python3 scripts/validate_enrichment.py` — PASS.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.multi-level-caching` — expected FAIL on invariant state
  `partial`, alternative state `partial` and `card_path`.

In the detached scratch copy with the metadata patch (including the
shared-page bounded count and source catalogue regeneration):

    PASS: tycho.pattern.multi-level-caching
    1/1 entries preflight clean
    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: 297 source records, mandatory IDs, cross-references and catalogue
    freshness
    490 documents, coverage complete (book metadata)

The scratch tree was not used to claim review, promotion or owner acceptance.
The full unit suite is not run; batch-end tests remain with the integrator.
The scratch patch did not regenerate the route index or the atlas/coverage
artifacts, so their validators were not run there.

## Limits

The binding uses three public sources: a versioned Hazelcast 5.6 page, a
rolling Redis `latest` page pinned by digest and commit, and a living AWS
Well-Architected page pinned by Markdown digest and HTTP metadata. None of the
selected sources reports a deployment test, an invalidation measurement or a
latency benchmark. The per-tier disjunction, the version-check example, the
promotion rule, the measurement threshold and the local-only fallback are Tycho
synthesis; the invariant and alternative states are `supported` only because
the owner section separates those Tycho additions from the source-supported
statements. A reviewer that requires every word of the owner quote to be
source-quoted should treat the dimensions as partial instead.

No independent AI review, owner acceptance, promotion or production
observation is claimed. The card remains inline in V11/C05, not V11/C06; this
lane did not create a second card.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- the card path `book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
