# B71 — Cache-Aside invariant and failure/recovery lane

Status: lane-local book edit, self-checked on 2026-11-01. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and alternative were supported;
invariant and failure/recovery were partial. This lane binds the two partial
dimensions to three public sources: the Microsoft Azure Cache-Aside pattern,
AWS ElastiCache best practices (the best-practices hub and its caching-strategies
child) and the Redis cache-aside page. It labels the stale-fill, version-gate,
tombstone and durable-invalidation rules as Tycho synthesis. The card is inline
in V11/C05 and this lane edits that block.

## Lane coordinates

- Parent HEAD: f176e40e536406b3340f4dabaf5c90db5638f268 (f176e40e).
- Lane label: Tycho.
- Branch: b71-cache-aside; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b71-cache-aside.
- Scope: the owner section "4. Cache-aside is a sequence, not a consistency
  theorem" in V06/C01, the inline "Cache-Aside / Lazy Loading" card in V11/C05,
  and this note. Single-entry lane; no other entry, shared JSON, promotion or
  generated file is changed.
- Owner path (concatenate):

      book/volumes/v06-caching-indexing-and-retrieval/
      c01-local-and-distributed-caching/refresh-semantics.md

- Inline card path:
  book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md.
- Exactly three files change: the owner page, the inline card host and this
  note.
- Existing source ids: src.aws-caching-strategies, src.microsoft-cloud-patterns
  and src.redis-cache-aside. No new source id is proposed.
- New ledger records proposed: four, listed below.
- Retained historical record: read.batch3-aws-caching.2026-10-21, kept as the
  card's original citation and not re-inspected on 2026-11-01.
- Owner-page frontmatter: only updated_at moves from 2026-10-20 to 2026-11-01.
  The decomposition-protected evidence_scope, content_review, authored_at,
  source_inspection_date and content_verified_at are byte-identical.
- Baseline and final line-length and boundary checks pass.

## Card location

The registry records atlas_section cache-aside-lazy-loading under V11/C05;
card-batches.v1.json records no card_path for this pattern, and the C05 chapter
landing already contains the card body. This lane edits the inline block rather
than creating a dedicated page. Baseline card lines 116-150 (the block plus its
separating blank line); final card lines 116-160. The chapter frontmatter is
unchanged; the proposed evidence_scope update is left for the integrator because
that field is decomposition-protected. Precedent: B38, B53, B59, B60, B61, B62,
B63 and B64 edited inline card hosts and left the chapter metadata to
integration.

## Baseline and gap

edition/patterns/owner-units.v1.json records mechanism supported, invariant
partial, failure/recovery partial and alternative supported. The recorded
reasons for the two partial dimensions are:

- invariant: "Source has no fill precondition tied to a competing update."
- failure_recovery: "Source has no stale-authorization or
  revocation-sensitive recovery rule."

The entry records technical_coverage partial, decision_coverage partial-bounded
and review_state self-checked. It carries no separate external-review verdict,
so this lane does not claim one.

Baseline, recomputed from f176e40e:

- Page: 8,830 bytes, 157 lines, 1,156 words, SHA-256
  d0152c2ce2b7f35a061cdb5bdf0c31c3120c73847ba710990e27032bfc0399b2.
- Owner section (lines 70-117): 3,010 bytes, 460 words, SHA-256
  978b6354b532a7acbe6e49781dd386714c6b825c222bff381260da2eb81ee1ba.
- Promoted TTL section (lines 132-157): 1,610 bytes, 275 words, SHA-256
  36fd06833870349d7baa126a4dcc319707bedf3f31148281c9fd8c60fd1a22f2.
- Inline card block (lines 116-150, including the separating blank line):
  1,778 bytes, 200 words, SHA-256
  a7085edbc80d5c736af7c552fb4efacce1a0c86af5144c9c2425d96b27b35cdb.
- Chapter landing: 365 lines, 1,720 words, SHA-256
  65ede6e8ab99cf99525bf1dece018e83ab33bbe2527733228a4d64a9e605acd8.

Final:

- Page: 11,822 bytes, 195 lines, 1,596 words, SHA-256
  070c60881e28cc2dfb40df2984458f874c1a68c42baa12e1e3c585544c2f2e7f.
- Owner section (lines 70-155): 6,002 bytes, 900 words, SHA-256
  3a99de2efcb1cffac85acd5be6dadfe8bf4ef0f1a37a018feb4bf2138191c411.
- Promoted TTL section (lines 170-195): 1,610 bytes, 275 words, SHA-256
  36fd06833870349d7baa126a4dcc319707bedf3f31148281c9fd8c60fd1a22f2,
  byte-identical before and after.
- Inline card block (lines 116-160, including the separating blank line):
  2,772 bytes, 339 words, SHA-256
  a30b8696a931846a7411ed50c383ecfb6a605d5b6cca0ad2023d4aecacc419d6.
- Chapter landing: 375 lines, 1,859 words, SHA-256
  a8ff592d4ff92e66151dc9de05d983e40170da6f32a4ec04b2130e107fe97475.

The gap was evidential. The owner page already stated the stale-fill race, the
version gate, the tombstone distinction and the invalidation outbox as Tycho
guidance, but no exact public quote, section and representation hash bound those
claims. Shared metadata still shows 2/4 and partial-bounded until the integrator
applies the proposals below.

The lane narrows the claims. First, the Azure pattern page states the
consistency limit and the sensitive-data contraindication; it does not prescribe
a version gate or an outbox. Second, the AWS caching-strategies page states the
miss-only-fill staleness, node-failure continuity and TTL limits; it is titled
for Memcached and carries general strategy statements, not cache-aside
consistency proof. Third, the Redis page states the TTL bound, write-invalidate
and stampede mitigation; it is a vendor use-case page and does not define an
authorization model or a cache-outage fallback.

## Candidate evaluation

- Microsoft, "Cache-Aside pattern" (selected; existing source
  src.microsoft-cloud-patterns). States the read-miss-fill-invalidate sequence,
  the consistency limit, the staleness window after writes, the invalidation
  ordering hazard, the sensitive-data contraindication, the cache-malfunction
  fallback and the write-through alternative. Primary source for the invariant
  and the revocation-sensitive contraindication.
- AWS, "ElastiCache best practices and caching strategies" (selected; existing
  source src.aws-caching-strategies). Confirms the best-practices entry point and
  lists the caching-strategies child. Supporting source for the AWS route only;
  the landing page carries no cache-aside mechanism.
- AWS, "Caching strategies for Memcached" (selected; same source). States lazy
  loading, the stale miss-only fill, write-through plus TTL, node-failure
  continuity, the three-trip miss penalty and the TTL freshness limit. Primary
  AWS evidence for the invariant and failure/recovery. The former whitepaper
  caching-patterns.html URL now redirects to this page.
- Redis, "Redis cache-aside" (selected; existing source src.redis-cache-aside).
  States read fallback, primary write plus invalidation, TTL-bounded staleness,
  in-process invalidation limits and atomic mutex or probabilistic early
  refresh. Primary evidence for the mechanism and stampede mitigation.
- Retained AWS record read.batch3-aws-caching.2026-10-21 (historical). Its
  revision 72856742... describes the older whitepaper representation; it stays
  the card's original citation and the historical example only.
- AWS Well-Architected PERF03-BP05 (considered, not bound). It is already read
  for Multi-Level Caching; it gives general client-side/remote and TTL guidance
  but not cache-aside-specific consistency or recovery statements.
- Redis "Distributed locks" (considered, not bound). It defines lock safety and
  failover limits, not the cache-aside read path or invalidation intent.
- Vendor tutorials and third-party summaries (considered, not bound). They
  restate the same patterns and would add unverified claims.

No cache, origin, node failure, stampede or revocation path was exercised.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-11-01 (UTC), twice per
representation, with Accept-Encoding: identity; the two raw bodies matched for
every selected representation. Raw bytes are the served body. Canonical text for
the Microsoft Learn page is the div.content article region under main#main: drop
script, style, nav, footer, header, aside, form and button elements and chrome
containers (feedback, additional resources, metadata, breadcrumb, outline,
actions); convert block elements to lines; decode entities; normalize
non-breaking spaces, typographic quotes and dashes to ASCII; collapse space runs
and blank lines; strip; cut at the Feedback heading. Canonical text for a
Markdown alternate: decode UTF-8; LF line endings; strip trailing whitespace;
normalize non-breaking spaces, typographic quotes and dashes to ASCII; collapse
three or more newlines to two; strip; end with one newline. Word counts split on
whitespace; character counts include spaces and newlines. Quoted fragments below
remove Markdown link targets, emphasis markers and backticks, and reflow line
breaks; the words themselves are unchanged.

### R1 — Microsoft Azure Cache-Aside pattern

- Record: read.azure-cache-aside-pattern.2026-11-01 (proposed).
- Source: src.microsoft-cloud-patterns (existing; extend).
- URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside
- Label/type: "Cache-Aside pattern"; official documentation, design pattern;
  the page carries the product tag "Azure Managed Redis".
- Representation: HTTP/2 200 at 2026-11-01T10:47:58Z and 10:47:59Z; 60,812-byte
  HTML both times; ETag "+nEuQdqh/wQeBSsBPQVNWDA16h0="; Last-Modified Wed, 05
  Aug 2026 07:31:51 GMT; ms.date 2025-09-11T00:00:00Z; updated_at
  2025-12-09T06:03:00Z; git_commit_id
  cb69919fc6c9ebe8c3e3c389020e29a0ede6c941; raw HTML SHA-256
  e80c50b99fd589c53951d3794ef06fb4d5097220b9bbf4b85482432ab81f04f4. An
  earlier fetch without Accept-Encoding: identity was 60,436 bytes and differed
  only in page chrome; its canonical article text was identical.
- Canonical: 12,798 characters / 1,940 words / 171 lines; SHA-256
  f59a403f79981ad106f0c7c9a9aa1760d26e4cbdc6d591da947bfcafda97f841.
- Sections read: "Context and problem"; "Solution"; "Problems and
  considerations", including "Consistency", "Staleness after writes" and "Local
  caching"; "When to use this pattern"; "Workload design" Reliability row;
  "Example" and its two notes; "Related resources".
- Sections not read: linked pages (caching guidance, data-consistency primer,
  semantic-cache tutorial), images, code beyond the displayed example; no cache
  was deployed.
- Claims supported: read-miss-fill-invalidate sequence; consistency not
  guaranteed; stale read between a write and the next read; invalidate-before-
  update ordering hazard; sensitive data should come from the primary source;
  cache-malfunction fallback; write-through alternative.
- Limits: living pattern documentation; intended application behavior, not a
  benchmark or a tested cache-aside implementation.

### R2 — AWS ElastiCache best practices

- Record: read.aws-elasticache-best-practices.2026-11-01 (proposed).
- Source: src.aws-caching-strategies (existing; extend).
- URL: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.html
- Markdown alternate: the same path with BestPractices.md.
- Label/type: "ElastiCache best practices and caching strategies — Amazon
  ElastiCache"; official documentation.
- Representation: HTTP/1.1 200 at 2026-11-01T10:46:56Z on both fetches;
  6,142-byte Markdown both times; Last-Modified Sat, 31 Oct 2026 03:32:54 GMT;
  ETag "D6ogJDk639KHJYbWq6g3zIEJGFo="; raw Markdown SHA-256
  cca778f340946a3102c77a2fbfddfc4e139370e3c33c556cbd672a8dd562cbf4.
- Canonical: 6,138 characters / 840 words / 96 lines; SHA-256
  9186ee013a7ccf99d0a8ff03056222a60fa0b7df639f39b3fdf30827eae68d16.
- Sections read: the landing page, including the Topics list and the inline
  "TLS enabled dual stack ElastiCache clusters" section.
- Sections not read: the linked child pages, except the caching-strategies unit
  in R3; images.
- Claims supported: the hub is the recommended best-practices entry point for
  ElastiCache and lists "Caching strategies for Memcached".
- Limits: mostly a hub; it carries no cache-aside sequence, staleness or failure
  semantics.

### R3 — AWS Caching strategies for Memcached

- Record: read.aws-caching-strategies.2026-11-01 (proposed).
- Source: src.aws-caching-strategies (existing; extend).
- URL: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html
- Markdown alternate: the same path with Strategies.md.
- Label/type: "Caching strategies for Memcached — Amazon ElastiCache"; official
  documentation. The older whitepaper caching-patterns.html URL now redirects to
  this page.
- Representation: HTTP/1.1 200 at 2026-11-01T10:47:03Z on both fetches;
  10,199-byte Markdown both times; Last-Modified Sat, 31 Oct 2026 03:33:09 GMT;
  ETag "3hphMp6rLIHNl4HMLpA7XXBmAS8="; raw Markdown SHA-256
  1545d654b3ba951387ec1f77f05d9cd96da9212c21b1a352f1260140c306ffc3.
- Canonical: 10,164 characters / 1,452 words / 225 lines; SHA-256
  9382d8a93498e13e46b5b5b51252b87a4e2c3cd0dccc8f713cd8c82328cb78ca.
- Sections read: "Lazy loading" and its advantages/disadvantages; "Write-through"
  and its advantages/disadvantages; "Adding TTL"; the topic list and lead
  paragraphs.
- Sections not read: "Read replicas"; pseudocode not analyzed beyond the quoted
  prose; linked pages and images.
- Claims supported: lazy-loading sequence; miss-only fill leaves the cache
  stale; write-through and TTL are the stated remedies; node failure is
  survivable with a miss penalty; TTL does not guarantee freshness.
- Limits: product strategy documentation; the title names Memcached and the
  statements are general caching-strategy claims, not a consistency proof. No
  node failure, TTL expiry or stampede was exercised.

### R4 — Redis cache-aside

- Record: read.redis-cache-aside.2026-11-01 (proposed).
- Source: src.redis-cache-aside (existing; extend from landing inspection to a
  full read).
- URL: https://redis.io/docs/latest/develop/use-cases/cache-aside/
- Markdown alternate:
  https://redis.io/docs/latest/develop/use-cases/cache-aside/index.html.md
- Source path: content/develop/use-cases/cache-aside/_index.md in
  redis/docs at commit 87a7babb3752f4b4912b577a43cd90c19ec2525d
  (2026-09-16T15:50:30Z); the source-path revision, not a build identifier
  printed by the page.
- Label/type: "Redis cache-aside — Redis docs"; official documentation.
- Representation: HTTP/2 200 at 2026-11-01T10:48:05Z and 10:48:06Z; 6,706-byte
  Markdown both times; ETag "73eac54c1ee8399adb7603f676671bdb";
  Last-Modified Mon, 10 Aug 2026 13:46:19 GMT; raw Markdown SHA-256
  03008bbc239b95ddec24bb6690f6082790a7b604e7e852a8ac821ebf3fa62539.
- Canonical: 6,697 characters / 677 words / 99 lines; SHA-256
  392854e0c638038095f356216f4838cc6a4caa8e73a893fb6367b112d7920745.
- Sections read: all six: "When to use Redis cache-aside"; "Why the problem is
  hard"; "What you can expect from a Redis solution"; "How Redis supports the
  solution"; "Ecosystem"; "Code examples to build your own Redis cache-aside".
- Sections not read: linked command references, ecosystem guides and code
  examples; no Redis server was run.
- Claims supported: read fallback to the primary on a miss; write the primary
  then invalidate the key; TTL bounds staleness; an in-process cache cannot be
  invalidated consistently; popular-key expiry can stampede; atomic mutex or
  probabilistic early refresh mitigates it.
- Limits: vendor use-case page; its latency figures are not reproduced. It does
  not define an authorization model or a cache-outage fallback, and it does not
  prescribe a version gate.

## Selected exact quotes

Quotes reproduce the normalized prose described above. Twenty-three named
fragments are listed; the page uses all 23 and the card uses a subset (the Q6,
Q7, Q8, Q14, Q17, Q19 and Q21 wording). All 23 were checked against the three
canonical representations on 2026-11-01, and 25/25 checked strings used in the
page and card, including two repeated fragments, were present. A wider set of
33 candidate passages from the four units was checked with 33/33 present; the
unused candidates are not carried into the book.

### Mechanism

- Q1, R1, section "Solution":

      writes the change to the data store and then invalidates the
      corresponding item in the cache

- Q2, R3, section "Lazy loading":

      If the data doesn't exist in the cache or has expired, your application
      requests the data from your data store

- Q3, R4, section "How Redis supports the solution":

      falls back to the primary on a miss, and writes the result back to Redis

- Q4, R4, section "How Redis supports the solution":

      writes the primary and invalidates the cache key

### Invariant

- Q5, R1, section "Problems and considerations", "Consistency":

      doesn't guarantee consistency between the data store and the cache

- Q6, R1, section "Problems and considerations", "Staleness after writes":

      Between the write and the next read, a reader can experience a cache miss
      or briefly see stale data

- Q7, R3, section "Advantages and disadvantages of lazy loading", "Stale data":

      no updates to the cache when data is changed in the database

- Q8, R3, same section:

      data in the cache can become stale

- Q9, R3, section "Adding TTL":

      doesn't guarantee that a value isn't stale

- Q10, R3, section "Adding TTL":

      keeps data from getting too stale

- Q11, R4, section "How Redis supports the solution":

      a TTL that bounds how long stale data can be served

- Q12, R1, section "Example", note after UpdateEntityAsync:

      a small window of time when a client might fetch the item before the data
      store is updated

- Q13, R1, same note:

      This sequence leads to stale data in the cache

### Failure and recovery

- Q14, R1, section "Workload design", Reliability row:

      If the cache malfunctions, the workload can fall back to the origin data
      store.

- Q15, R1, section "Workload design", Reliability row:

      In limited ways, it can preserve the availability of frequently accessed
      data if the origin data store becomes temporarily unavailable.

- Q16, R3, section "Advantages and disadvantages of lazy loading", advantage:

      Node failures aren't fatal for your application

- Q17, R3, same advantage:

      though with increased latency

- Q18, R3, section "Advantages and disadvantages of lazy loading",
  disadvantage "cache miss penalty":

      three trips

- Q19, R1, section "When to use this pattern":

      sensitive or security related

- Q20, R1, same section:

      might be inappropriate

- Q21, R1, same section:

      from the primary source

### Alternative

- Q22, R1, section "Problems and considerations", "Staleness after writes":

      read-heavy paths need read-after-write freshness

- Q23, R3, section "Advantages and disadvantages of lazy loading", "Stale
  data":

      Write-through and Adding TTL strategies

## Dimension mapping

- Mechanism. Keep state supported. Primary binding remains the retained record
  read.batch3-aws-caching.2026-10-21, source src.aws-caching-strategies, sections
  "Caching patterns", "Cache-Aside (Lazy Loading)" and "Write-Through",
  revision 7285674270bc8c142038380b991124a33538c4eecef644b40539cb32a8902c4b.
  Supporting: Q1-Q4 and Q11. Tycho reading: cache-aside is a read-miss-fill-
  invalidate sequence with a TTL-bound fill, not a consistency mechanism.
- Invariant. State supported. Claim quote: "A cache-aside read is a freshness
  claim bounded by the fill revision, the invalidation path and the TTL, not a
  consistency theorem." Primary binding: Q5, record
  read.azure-cache-aside-pattern.2026-11-01, source src.microsoft-cloud-patterns,
  section "Problems and considerations", subsection "Consistency", revision
  f59a403f79981ad106f0c7c9a9aa1760d26e4cbdc6d591da947bfcafda97f841. Supporting:
  Q6-Q11, Q12-Q13 and Q23. Tycho rule: the freshness claim is bounded by the
  fill revision, the invalidation path and the TTL.
- Failure and recovery. State supported, narrowed. Claim quote: "A write can
  commit while its delete fails; the invalidation intent must be durable at
  commit time and retried." Primary binding: Q14, record
  read.azure-cache-aside-pattern.2026-11-01, section "Workload design",
  Reliability row, revision f59a403f.... Supporting: Q15-Q18, Q12-Q13 and Q6.
  The sources state fallback, node-failure continuity, miss cost and stampede
  mitigation; none states a durable invalidation outbox, fencing rule or version
  gate, so those write-path rules are Tycho guidance.
- Alternative. State supported. Claim quote: "When the read budget allows,
  serving from the source or a shorter TTL with retried invalidation is the
  alternative." Primary binding: Q22, record
  read.azure-cache-aside-pattern.2026-11-01, section "Problems and
  considerations", subsection "Staleness after writes", revision f59a403f....
  Supporting: Q23, Q11 and Q1-Q4. Tycho choice rule: reverse when fill and
  invalidation logic duplicates.
- Retention and coverage. The lane proposes mechanism, invariant,
  failure/recovery and alternative all supported; technical_coverage sufficient
  and decision_coverage sufficient as a self-check. The card split,
  promotion gate, owner acceptance and independent review remain integrator and
  owner decisions; this lane claims none of them.

## Proposed shared metadata

The following changes are proposals only. No shared JSON is edited in this lane.

### sources/register.json

Extend src.microsoft-cloud-patterns; append to version "Cache-Aside pattern page
fetched 2026-11-01; 60,812-byte HTML; ETag +nEuQdqh/wQeBSsBPQVNWDA16h0=;
Last-Modified 2026-08-05T07:31:51Z; ms.date 2025-09-11; updated_at
2025-12-09T06:03:00Z; git_commit_id
cb69919fc6c9ebe8c3e3c389020e29a0ede6c941; raw HTML SHA-256 e80c50b9...;
canonical text 12,798 characters / 1,940 words, SHA-256 f59a403f...; two
fetches byte-identical; no published version identifier."; append to
verification_scope "The Cache-Aside pattern page was read in full on 2026-11-01
for the solution sequence, consistency, staleness after writes, local caching,
sensitive-data contraindication, workload reliability fallback and example
ordering note; linked pages, images and code beyond the displayed example were
not read." access_checked and content_verified are already 2026-11-01 after the
Geodes re-read.

Extend src.aws-caching-strategies: reading_status
full-public-page-inspected; access_checked and content_verified 2026-11-01;
append to version "ElastiCache best-practices hub fetched 2026-11-01; Markdown
alternate 6,142 bytes, SHA-256 cca778f3..., Last-Modified 2026-10-31T03:32:54Z,
ETag D6ogJDk639KHJYbWq6g3zIEJGFo=; canonical text 6,138 characters / 840 words,
SHA-256 9186ee01.... Caching strategies for Memcached fetched 2026-11-01;
Markdown alternate 10,199 bytes, SHA-256 1545d654..., Last-Modified
2026-10-31T03:33:09Z, ETag 3hphMp6rLIHNl4HMLpA7XXBmAS8=; canonical text 10,164
characters / 1,452 words, SHA-256 9382d8a9.... The older caching-patterns.html
whitepaper URL now redirects to the strategies page; the 2026-10-21 record
remains historical."; append to verification_scope "The best-practices hub and
the caching-strategies page were read on 2026-11-01 for lazy loading, the stale
miss-only fill, write-through and TTL remedies, node-failure continuity, the
miss penalty and the TTL freshness limit; the read-replicas section, pseudocode,
linked pages and images were not read."

Extend src.redis-cache-aside: reading_status full-public-page-inspected;
access_checked and content_verified 2026-11-01; version "Markdown alternate
fetched 2026-11-01; 6,706 bytes, ETag 73eac54c1ee8399adb7603f676671bdb,
Last-Modified 2026-08-10T13:46:19Z; canonical text 6,697 characters / 677 words,
SHA-256 392854e0...; source path content/develop/use-cases/cache-aside/_index.md
at redis/docs commit 87a7babb3752f4b4912b577a43cd90c19ec2525d dated
2026-09-16."; verification_scope "The full cache-aside use-case page was read on
2026-11-01 for the read/fallback/invalidate sequence, TTL-bounded staleness,
in-process invalidation limits and atomic stampede mitigation; linked commands,
ecosystem guides and code examples were not read, and no Redis server was run."

### reading-ledger.v1.json

Add four records. All use access_date 2026-11-01, access_method "public HTTP
fetch; served HTML or Markdown inspected", reviewer "Automated authoring agent"
and status "read".

- read.azure-cache-aside-pattern.2026-11-01
  - source: src.microsoft-cloud-patterns
  - unit_url: the Azure URL in R1
  - unit_label: Cache-Aside pattern
  - unit_type: documentation-page
  - sections_read: Context and problem; Solution; Problems and considerations,
    including Consistency, Staleness after writes and Local caching; When to use
    this pattern; Workload design; Example; Related resources
  - sections_not_read: linked pages; images; code beyond the displayed example
  - content_sha256: f59a403f79981ad106f0c7c9a9aa1760d26e4cbdc6d591da947bfcafda97f841
  - characters/words: 12,798 / 1,940
  - claims_supported: Q1, Q5-Q6, Q12-Q15, Q19-Q22
  - claims_not_supported: version gates, tombstones, durable invalidation,
    benchmarks, deployed-cache behavior
  - limitations: living pattern documentation; no cache deployed.
- read.aws-elasticache-best-practices.2026-11-01
  - source: src.aws-caching-strategies
  - unit_url: the BestPractices URL in R2
  - unit_label: ElastiCache best practices and caching strategies
  - unit_type: documentation-page
  - sections_read: landing page, Topics list, TLS dual-stack section
  - sections_not_read: linked child pages except the strategies unit; images
  - content_sha256: 9186ee013a7ccf99d0a8ff03056222a60fa0b7df639f39b3fdf30827eae68d16
  - characters/words: 6,138 / 840
  - claims_supported: the best-practices entry point and the caching-strategies
    route
  - claims_not_supported: cache-aside mechanism, staleness, failure recovery
  - limitations: hub page; no cache configured.
- read.aws-caching-strategies.2026-11-01
  - source: src.aws-caching-strategies
  - unit_url: the Strategies URL in R3
  - unit_label: Caching strategies for Memcached
  - unit_type: documentation-page
  - sections_read: Lazy loading; advantages and disadvantages; Write-through;
    advantages and disadvantages; Adding TTL
  - sections_not_read: Read replicas; pseudocode; linked pages; images
  - content_sha256: 9382d8a93498e13e46b5b5b51252b87a4e2c3cd0dccc8f713cd8c82328cb78ca
  - characters/words: 10,164 / 1,452
  - claims_supported: Q2, Q7-Q10, Q16-Q18, Q23
  - claims_not_supported: cache-aside consistency proof, version gates,
    authorization semantics, benchmark
  - limitations: product strategy documentation; no node failure or expiry test.
- read.redis-cache-aside.2026-11-01
  - source: src.redis-cache-aside
  - unit_url: the Redis page URL in R4
  - unit_label: Redis cache-aside
  - unit_type: documentation-page
  - sections_read: all six sections listed in R4
  - sections_not_read: linked commands, ecosystem guides, code examples
  - content_sha256: 392854e0c638038095f356216f4838cc6a4caa8e73a893fb6367b112d7920745
  - characters/words: 6,697 / 677
  - claims_supported: Q3-Q4, Q11
  - claims_not_supported: authorization semantics, cache-outage fallback,
    benchmark, local reproduction
  - limitations: vendor use-case page; no Redis server run.

### Source plan edition/patterns/source-plan.v1.json

Replace the one required unit for tycho.pattern.cache-aside-lazy-loading with
the four units below. Keep the existing schema fields (source_id, unit,
unit_type, url, sections, status, read_record_id, blocked_reason: null). URLs
are the exact ones recorded in R1-R4. Proposed notes: "Three public sources
across four representations bound on 2026-11-01: the Azure Cache-Aside pattern,
the AWS ElastiCache best-practices hub and its caching-strategies child, and the
Redis cache-aside page. The 2026-10-21 AWS whitepaper record remains historical."

- src.microsoft-cloud-patterns — "Cache-Aside pattern"; documentation-page;
  URL as in R1; sections "Solution", "Problems and considerations", "When to use
  this pattern", "Workload design"; status read; record
  read.azure-cache-aside-pattern.2026-11-01.
- src.aws-caching-strategies — "ElastiCache best practices and caching
  strategies"; documentation-page; URL as in R2; sections "Topics", "TLS enabled
  dual stack ElastiCache clusters"; status read; record
  read.aws-elasticache-best-practices.2026-11-01.
- src.aws-caching-strategies — "Caching strategies for Memcached";
  documentation-page; URL as in R3; sections "Lazy loading", "Write-through",
  "Adding TTL"; status read; record read.aws-caching-strategies.2026-11-01.
- src.redis-cache-aside — "Redis cache-aside"; documentation-page; URL as in R4;
  full page; status read; record read.redis-cache-aside.2026-11-01.

### Owner units edition/patterns/owner-units.v1.json

Keep the document id, path, heading, anchor, level and owner.line 71; the
heading remains at line 71. Keep unit_kind dedicated. Consider adding
unit_terms "consistency", "stale data" and "origin data store".

Technical evidence:

- mechanism: keep state supported. Claim quote unchanged. Reason: the Azure and
  AWS pages state the read-miss-fill-invalidate sequence, and Redis states the
  read fallback and write invalidation. Add supporting bindings for Q1-Q4 and
  Q11; keep read.batch3-aws-caching.2026-10-21 as the primary historical
  binding.
- invariant: state supported. Claim quote: "A cache-aside read is a freshness
  claim bounded by the fill revision, the invalidation path and the TTL, not a
  consistency theorem." Reason: Azure states the pattern does not guarantee
  consistency and shows stale reads after writes; AWS states a miss-only fill
  leaves the cache stale; Redis bounds staleness with a TTL. Primary binding:
  Q5, record read.azure-cache-aside-pattern.2026-11-01, section "Problems and
  considerations", subsection "Consistency", revision f59a403f.... Supporting:
  Q6-Q11, Q12-Q13 and Q23. Tycho rule: bound the freshness claim by the fill
  revision, the invalidation path and the TTL.
- failure_recovery: state supported, narrowed. Claim quote: "A write can commit
  while its delete fails; the invalidation intent must be durable at commit time
  and retried." Reason: Azure states the cache-malfunction fallback; AWS
  states node-failure continuity and the miss penalty; Redis states atomic
  stampede mitigation. Primary binding: Q14, record
  read.azure-cache-aside-pattern.2026-11-01, section "Workload design",
  Reliability row, revision f59a403f.... Supporting: Q15-Q18, Q12-Q13 and Q6.
  Narrowing: no selected unit states an outbox, fencing rule or version gate;
  those are Tycho guidance, not source claims.
- alternative: state supported. Claim quote unchanged. Reason: Azure recommends
  write-through for read-after-write freshness; AWS names write-through and TTL;
  Redis bounds staleness with a TTL. Primary binding: Q22, record
  read.azure-cache-aside-pattern.2026-11-01, section "Problems and
  considerations", subsection "Staleness after writes", revision f59a403f....
  Supporting: Q23, Q11 and Q1-Q4. Tycho choice rule: reverse when fill and
  invalidation logic duplicates.

Other owner-units fields:

- technical_coverage "sufficient"; decision_coverage "sufficient";
  review_state "self-checked".
- notes: "Two partial dimensions bound 2026-11-01 to the Azure Cache-Aside
  pattern, AWS ElastiCache best practices and caching strategies, and Redis
  cache-aside; the Azure page limits the consistency claim and contraindicates
  sensitive data, AWS states miss-only-fill staleness and node-failure
  continuity, and Redis states the TTL bound and stampede mitigation. The
  stale-fill algorithm, version gate, tombstone rule and durable invalidation
  are Tycho synthesis; no cache, node failure, stampede or revocation path was
  exercised; coverage is self-checked, not independently reviewed."
- source_support: primary ledger_record
  read.azure-cache-aside-pattern.2026-11-01, source_id
  src.microsoft-cloud-patterns, unit_type documentation-page, status read,
  card_citation true; auxiliary entries for read.aws-elasticache-best-practices,
  read.aws-caching-strategies, read.redis-cache-aside and the retained
  read.batch3-aws-caching.2026-10-21.
- decision_evidence.competing_alternative: keep the existing text; decision_state
  applicable-under-conditions; card_components 10; atlas_section
  cache-aside-lazy-loading.

### Registry, card batches and derived artifacts

The registry currently records technical_owner.state partial, atlas_owner.state
partial-bounded and coverage partial. After the owner-units proposal is applied,
regenerate those fields from owner-units rather than editing them by hand. The
proposed state is technical_owner.state sufficient, atlas_owner.state
sufficient and coverage technical/decision/overall sufficient, confidence
high. source_units should list the four units above. The registry notes should
state that the dimensions are self-checked and that promotion is not part of
this lane.

card-batches.v1.json needs no card_path while the card remains inline; if the
integrator splits it into a dedicated page, register the page identity, card
path, atlas manifest, directory migration, document identity and semantic-audit
entries, and update the chapter card block to a link.

### Content revisions, V12 baseline and generated artifacts

One issue-540 revision authorizes the changed section-4 source block
(source_blocks). One decomposition_metadata revision is needed only if the
integrator updates the owner-page evidence_scope or the chapter frontmatter
source_ids and notes; this lane leaves both unchanged and proposes the binding
through the ledger and owner units. Historical-view revisions authorize the
owner-page and chapter changes. Then refresh edition/content-revisions.json,
edition/atlas-manifest.json, edition/patterns/card-batches.v1.json,
edition/v12/protected-baseline.json (the refresh-semantics.md hash changes) and
the generated route, section, census, coverage, reverse-map, phase-4, delivery,
qrels, inventory and sufficient-review artifacts. No promotion or owner
acceptance is authored here.

## Verification

Commands run in /Users/rbaranov/Projects/tycho-worktrees/b71-cache-aside:

- python3 scripts/check_markdown_line_length.py
  Result: PASS: V11 prose <=100; 145 exact owner-link exceptions.
- python3 scripts/check_boundary.py
  Result: PASS: 1 hash-pinned reviewed media file(s) skipped;
  independent-origin review still required.
- Added-line scan: every added owner and card line is <=100 characters. The
  retained "Text alternative" line and the pre-existing frontmatter,
  navigation, Caffeine-link and pattern-atlas lines exceed 100; they are
  unchanged and outside this lane.
- Quote check: 25/25 strings used in the page and card are present after the
  documented quote normalization; 33/33 wider candidate passages are present.
- python3 scripts/validate_pattern_cards.py: PASS, 145 entries.
- python3 scripts/validate_book_metadata.py: PASS, 552 documents.
- python3 scripts/validate_book_navigation.py: 5 issues, all present on
  f176e40e and none in the changed files.
- python3 scripts/validate_decomposition.py: FAIL altered-source-payload until
  the section-4 source_blocks revision is applied; expected consequence of the
  no-shared-JSON constraint.
- python3 scripts/validate_v12.py: FAIL protected baseline page changed:
  refresh-semantics.md; expected until the integrator refreshes
  edition/v12/protected-baseline.json.
- git diff --check: PASS.
- git status: exactly three paths, the owner page, the V11/C05 landing and this
  note.
- No shared JSON, generated index, promotion record, review report or test file
  is changed.

No full unit suite was run. The lane is a content slice; the batch-end suite is
the integrator's step.

## Limits

- Coverage and review are self-checked. No independent AI review, owner
  acceptance, promotion, CI result or production observation is claimed.
- The Azure page is living pattern documentation; the AWS page is titled for
  Memcached and carries general strategy statements; the Redis page is a vendor
  use case. None is a formal specification or a tested cache-aside contract.
- The stale-fill race, version gate, tombstone distinction, durable
  invalidation and fencing rules are Tycho synthesis. The sources describe the
  surrounding consistency limit, staleness window, fallback and stampede
  mitigation, not those algorithms.
- No cache, origin, node failure, stampede, revocation or latency measurement
  was exercised.
- The card remains inline and V11/C05 keeps its existing evidence_scope until
  the integrator applies the proposals; the chapter source list is therefore not
  yet updated.

## Commit scope

- Exactly three paths: the V06/C01 owner page, the V11/C05 landing and this
  note.
- Lane commit message: "docs(book): bind cache-aside invariant and recovery".
- No shared JSON, generated artifact, promotion record, review report or test
  change. The lane does not claim a sufficient-coverage promotion.
