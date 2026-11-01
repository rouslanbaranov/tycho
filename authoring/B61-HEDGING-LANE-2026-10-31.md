# B61 — Hedged Requests four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 1/4 at the parent HEAD: mechanism was supported; invariant,
failure/recovery and alternative were partial. This lane binds all four
dimensions to four public units inspected on 2026-10-31: Google SRE
"Addressing Cascading Failures", section "Cancellation propagation"; Dean and
Barroso, "The Tail at Scale", CACM February 2013, section "Hedged requests";
gRPC "Request Hedging"; and AWS Builders' Library "Timeouts, Retries, and
Backoff with Jitter". The measured-percentile condition, duplicate-effect
inference and choice rule are labelled Tycho. The task brief names an inline
card at V11/C07; the registered card is inline in the C07 landing and this lane
edits that block.

## Lane coordinates

- Parent HEAD: f19bae8250cc843a70774dab84daeab03c8935ca (f19bae82).
- Lane label: Tycho.
- Branch: b61-hedging; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b61-hedging.
- Scope: the owner section "4. Hedging, replication and selective degradation"
  in V07/C04, the inline "Hedged Requests" card in V11/C07, and this note.
  Single-entry lane; no other entry, shared JSON, promotion or generated file
  is changed.
- Owner path (concatenate):

      book/volumes/v07-performance-scale-and-resilience/
      c04-tail-latency-fan-out-and-time-budgets/deadline-hedging.md

- Inline card path: book/volumes/v11-pattern-atlas/c07-resilience/README.md.
- Exactly three files change: the owner page, the inline card host and this
  note.
- Existing source ids: src.sre-cascading, src.tail-at-scale, src.aws-backoff.
- New source id proposed: src.grpc-hedging, used only by the owner and card
  frontmatter and prose until the integrator registers it.
- New ledger records proposed: four, listed below. Retained records:
  read.batch4-sre-cascading.2026-10-21, read.batch4-hedged.2026-10-21 and
  read.aws-builders-timeouts-retries.2026-10-31.
- Baseline and final line-length and boundary checks pass.

## Card location

The task brief names an inline card at V11/C07. The registry records
atlas_owner.chapter = V11/C07, section hedged-requests, and the card body is
inline in the C07 chapter landing. card-batches.v1.json records no card_path
for this pattern. The C07 landing already contains the card components, so this
lane edits the inline block rather than creating a dedicated page. The chapter
frontmatter evidence_scope.source_ids and notes are updated because they
describe the cards hosted by that page; the registry, card batches and atlas
manifest are left for the integrator. Precedent: B45, B51, B59 and B60 edited
inline card hosts and their chapter source lists the same way.

## Baseline and gap

edition/patterns/owner-units.v1.json records mechanism as supported and the
other three dimensions as partial. The recorded reasons are:

- mechanism: "Defines the trigger, replica choice, response selection and
  cancellation." Its binding is the secondary Morning Paper summary
  read.batch4-hedged.2026-10-21.
- invariant: "External review 2026-10-27: binding does not support the full
  owner claim."
- failure_recovery: "External review 2026-10-27: binding does not support the
  full owner claim."
- alternative: "External review 2026-10-27: binding does not support the full
  owner claim."

The entry records technical_coverage partial, decision_coverage partial-bounded
and review_state self-checked. The 2026-10-27 independent review required each
safety precondition and competing alternative to be bound explicitly or the
affected dimensions to be narrowed and marked partial.

The base owner page is 123 lines, 1,103 words, SHA-256
b9d37e2bb06badc14f3da30b76526d451d2eaaafc808a6106f3c9ddbe7bc07ec. The base
owner section (lines 84-112) is 29 lines, 406 words, SHA-256
c1377d44df38ccbd6965f8fac70c650f6e55bf9960d5314b87e5276fe63a32d2. The base
chapter landing is 423 lines, 2,101 words, SHA-256
ae058acde4a072e2df94841acba6f8d6238b3b1178820aa6f68400d62600cf5a. The base
card block (lines 358-389) is 32 lines, 168 words, SHA-256
aa4cd1eac40e21a83b99c45e9847e094eb8c1b455094bec292b07ba1532d3821.

The gap was evidential. The owner paragraph and card already stated the
conditions, failure path and alternatives as Tycho guidance, but no exact
public quote, section and representation hash were bound to equivalent
replicas, a bounded speculative budget, cancellation, a measured latency
percentile, duplicate effects, or the competing single-attempt and jittered
retry choices. Shared metadata still shows 1/4 until the integrator applies the
proposals below.

The lane narrows the alternative claim. The bound alternative is a single
bounded attempt with a timeout chosen from a measured latency percentile, or a
retry with backoff, jitter and a token-bucket retry budget. The earlier
slow-path and independent-read clauses are retained only as explicitly
unbound Tycho heuristics because no selected unit tests either comparison.
This is a narrowing, not a new source claim.

## Candidate evaluation

- Google SRE, "Addressing Cascading Failures", section "Cancellation
  propagation" (selected). Defines delayed duplicate RPCs to other instances,
  first-response selection, cancellation of the now-superfluous requests and
  propagation through the stack. Primary source for the mechanism and
  cancellation condition.
- Dean and Barroso, "The Tail at Scale", CACM February 2013, section "Hedged
  requests" (selected). Defines the same-replica hedge, the 95th-percentile
  deferral, the approximately 5% load bound in its example, the 99.9th
  percentile benchmark result, and the warning about naive additional load.
  Primary source for the measured-percentile condition and the tail benefit.
- gRPC, "Request Hedging" (selected). Defines multiple copies to different
  backends, first response, cancellation, mandatory maxAttempts with a cap of
  5, retry throttling to prevent overload, the deadline over the whole hedge
  chain, and the classification of hedging as one of two retry policies.
  Primary source for the bounded budget, cancellation behavior and retry
  alternative.
- AWS Builders' Library, "Timeouts, Retries, and Backoff with Jitter"
  (selected). Defines retry load amplification under overload, side-effect and
  idempotency risk, duplicate side effects, timeout selection from a measured
  latency percentile, jitter and a local token bucket. Primary source for the
  duplicate-effect hazard and the competing retry and timeout choices.
- The Morning Paper summary read.batch4-hedged.2026-10-21 was retained as
  historical evidence but not reused. It is a secondary summary; the original
  paper section is now read directly.
- Google SRE "Handling Overload" was considered but not bound. It covers
  client-side adaptive rejection and load shedding, not hedging.
- The gRPC retry design proposal was considered but not bound. The public guide
  already states the budget, cancellation and retry-policy facts used here.
- The AWS idempotency article was considered but not bound. The selected AWS
  retry article states the side-effect, idempotency and duplicate-effect
  warnings used here.
- The Tail at Scale "Tied requests" and "Latency-induced probation" sections
  were considered but not bound. They are alternative tail-tolerance
  mechanisms on the next digital-edition page; binding them would add a second
  TAS representation and was unnecessary after the alternative was narrowed to
  the AWS timeout, jitter and token-bucket comparison.
- DynamoDB request-hedging guidance was considered but not bound. It is
  vendor-specific and its p99 advice is not the same as the paper's
  95th-percentile deferral.
- No hedging, retry, timeout, cancellation, benchmark or failure exercise was
  run.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31. Every unit was fetched twice
and the decompressed bytes were identical on both fetches. HTML canonical text
was extracted with scripts/source_content_hash.py unless a unit-specific
extraction is stated. Raw HTML bytes, served headers and word counts are
recorded separately. HTTP dates are UTC. Byte counts are decompressed bodies
unless marked as the gzip transfer length.

### R1 — Google SRE, Addressing Cascading Failures, Cancellation propagation

- Record: read.sre-cascading-hedging.2026-10-31 (proposed).
- Source: src.sre-cascading.
- URL: https://sre.google/sre-book/addressing-cascading-failures/
- Label/type: "Addressing Cascading Failures — public chapter";
  book-chapter.
- Representation: HTTP/2 200 on 2026-10-31T20:46:15Z; gzip transfer length
  31,399 bytes; decompressed HTML 104,870 bytes; Last-Modified
  Thu, 08 Oct 2026 04:48:00 GMT; no ETag in the served headers; raw HTML
  SHA-256 d67024d52d72a1254c830d3c29e6d1b2afade88e133ffcff64b94711c2aaa11a.
- Canonical extraction: the div#content subtree, whitespace-normalized;
  9,046 words / 55,929 characters; SHA-256
  11a045479e92e27f6b589a5285f971adfdf3d8ec0af0805c5855e29d848f9548.
- Sections read: "Cancellation propagation"; the surrounding "Latency and
  Deadlines" context; the full chapter was previously read in
  read.batch4-sre-cascading.2026-10-21.
- Sections not read: linked child pages, navigation and the bibliography page.
- Claims supported: Q1 and Q8.
- Limits: a book chapter, not a benchmark or production measurement. The
  passage describes hedged requests inside a deadline discussion; it does not
  establish a universal cancellation guarantee or a measured threshold.

Register/ledger note: src.sre-cascading currently records a 2026-10-31 raw
HTML SHA-256 945d15db67ad15a7f5e75833f8c0d014c8dc61d57909f7a3abd48459ad12cc9e
and canonical text 8154963544456669d31fb2666db9f6a6a91ea0d4135d01d30e41922172a71bf2.
The existing ledger record read.batch4-sre-cascading.2026-10-21 records the
raw HTML SHA d67024d5... and says the full 44-heading chapter was read. The
current fetch is byte-identical to that ledger record. This lane uses the
d67024d5... raw representation and the 11a04547... content-div extraction. The
register's older hash is retained as historical; the integrator should
reconcile the version note rather than silently overwrite the ledger record.

### R2 — Dean and Barroso, The Tail at Scale, Hedged requests

- Record: read.tail-at-scale-hedged.2026-10-31 (proposed).
- Source: src.tail-at-scale (proposed representation update).
- URL: https://mags.acm.org/communications/201302/?pg=79
- Publication: Communications of the ACM, February 2013, vol. 56, no. 2;
  DOI 10.1145/2408776.2408794.
- Label/type: "The Tail at Scale — CACM digital edition"; research article.
- Representation: HTTP/2 200 on 2026-10-31T20:46:23Z; decompressed HTML
  47,159 bytes; no Last-Modified or ETag; raw HTML SHA-256
  16d88b045f33864acddf06fd44aebb50fb41e090a8cb47b7c2f0e093760a6227.
- Served hidden page text (noscript block): 568 words / 3,625 characters;
  SHA-256 648a07852ac2c1e4ae767fca577f91c5f3783ad0ccaa7c25218c733d15151623.
- Canonical text used for binding: the same hidden page text with end-of-line
  print hyphenation rejoined; 561 words / 3,611 characters; SHA-256
  8bcecb9e86b6485cf699b3fac7f0622f468779a74745cfc82305ea278553a828.
- Sections read: "Hedged requests", including the 95th-percentile deferral,
  the approximately 5% load statement and the 99.9th-percentile benchmark
  paragraph.
- Sections not read: pages 80-82 beyond this excerpt were not used; figures
  and tables were not reproduced; the publisher PDF was not read.
- Claims supported: Q2, Q4, Q5, Q10 and Q11.
- Limits: the article reports a 2013 benchmark, not a current production
  measurement or a universal threshold. The representation is ACM's public
  digital-edition HTML, not the print PDF. End-of-line hyphenation was rejoined
  only in the canonical text used for quotes; the raw hash is recorded above.

### R3 — gRPC, Request Hedging

- Record: read.grpc-hedging.2026-10-31 (proposed).
- Source: src.grpc-hedging (proposed).
- URL: https://grpc.io/docs/guides/request-hedging/
- Label/type: "Request Hedging — gRPC guide"; official documentation.
- Rendered representation: HTTP/2 200 on 2026-10-31T20:46:18Z; gzip transfer
  length 14,371 bytes; decompressed HTML 75,016 bytes; no Last-Modified or
  ETag; raw HTML SHA-256
  949634b39f0158e40a52ab3193863de2979b43df4adb9c3550c4201f9c6ffdac;
  canonical article text 957 words / 5,951 characters; SHA-256
  b9c0871d9397d8a4db1ce46b9dfa8018818bafdb77231c193cd698b7646922cf.
- Pinned source Markdown: grpc/grpc.io commit
  d3573082150aa8a1363dcbd86952f8771dc287ed (2023-10-03), file
  content/en/docs/guides/request-hedging.md; 6,165 bytes, 145 lines, 926
  words; SHA-256
  976a95ef7de5b966835ac057ef9817272c51f7e5ce40d02bd1841fe65fe29c85.
- Sections read: Overview; Use cases; Configuring hedging in gRPC; Hedging
  policy; Throttling Hedged RPCs; Server Pushback.
- Sections not read: linked language examples and implementations; images;
  runtime behavior.
- Claims supported: Q3, Q6, Q7, Q9, Q12, Q14 and Q22.
- Limits: documentation, not a benchmark. The maxAttempts cap of 5 is gRPC
  behavior, not a universal default. The guide does not prove that a canceled
  loser has not committed an application effect.

### R4 — AWS Builders' Library, Timeouts, Retries, and Backoff with Jitter

- Record: read.aws-backoff-hedging.2026-10-31 (proposed).
- Source: src.aws-backoff.
- URL: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Resolved URL: builder.aws.com content id 3EumjoZascWd1oZiEgL8ORlv3qE.
- Label/type: "Timeouts, retries, and backoff with jitter — AWS Builders'
  Library"; engineering article.
- Representation: HTTP/2 200 on 2026-10-31T20:46:21Z; 139,053-byte HTML; no
  Last-Modified or ETag; raw HTML SHA-256
  26c69da5738dce97491d1b5d97379ab8c7f5545758ee30cc5221c9c4e53c5922;
  canonical text 2,373 words / 14,549 characters; SHA-256
  c076aeb3beeb4766568d3cf85c5ffda79be9610be186159b925ceb882addfc94. The
  page displays Published 2019-12-05 and Last modified 2019-12-05.
- Sections read: Introduction; Failures Happen; Timeouts; Retries and
  backoff; Jitter; Deciding when to retry; Conclusion.
- Sections not read: linked articles, SDK behavior, service internals and
  benchmarks.
- Claims supported: Q13, Q15, Q16, Q17, Q18, Q19, Q20, Q21 and Q23.
- Limits: an engineering article, not a formal specification or benchmark. Its
  p99.9 example is timeout selection, not a hedge threshold, and it does not
  evaluate hedging directly.

## Selected exact quotes

Quotes reproduce the served prose after whitespace normalization. Line breaks
inside a quote are editorial wrapping. TAS print hyphenation was rejoined in
the canonical text and is flagged in R2. gRPC Markdown code formatting was
retained only where the source has backtick formatting; the owner and card use
the rendered prose. Twenty-three passages were checked against the named
canonical representation on 2026-10-31, 23/23 present. Twelve distinct quoted
fragments appear in the owner and card, 12/12 present.

### Mechanism

- Q1, R1, "Cancellation propagation":

      To reduce latency, some systems use "hedged requests" [Dea13] to send
      RPCs to a primary server, then some time later, send the same request to
      other instances of the same service in case the primary is slow in
      responding; once the client has received a response from any server, it
      sends messages to the other servers to cancel the now-superfluous
      requests.

- Q2, R2, "Hedged requests":

      A simple way to curb latency variability is to issue the same request to
      multiple replicas and use the results from whichever replica responds
      first.

- Q3, R3, "Overview":

      With hedging, a gRPC client sends multiple copies of the same request to
      different backends and uses the first response it receives.
      Subsequently, the client cancels any outstanding requests and forwards
      the response to the application.

### Invariant

- Q4, R2, "Hedged requests" (print hyphenation rejoined):

      One such approach is to defer sending a secondary request until the
      first request has been outstanding for more than the 95th-percentile
      expected latency for this class of requests.

- Q5, R2, "Hedged requests":

      This approach limits the additional load to approximately 5% while
      substantially shortening the latency tail.

- Q6, R3, "Configuring hedging in gRPC" (pinned Markdown; the rendered page
  drops the backtick formatting):

      `maxAttempts`: maximum number of in-flight requests while waiting for a
      successful response. This is a mandatory field, and must be specified.
      If the specified value is greater than `5`, gRPC uses a value of `5`.

- Q7, R3, "Hedging policy":

      When a successful response is received (in response to any of the hedged
      requests), all outstanding hedged requests are canceled and the response
      is returned to the client application layer.

- Q8, R1, "Cancellation propagation":

      Those requests may themselves transitively fan out to many other
      servers, so cancellations should be propagated throughout the entire
      stack.

- Q9, R3, "Throttling Hedged RPCs":

      gRPC provides a way to throttle hedged RPCs to prevent server overload.

- Q10, R2, "Hedged requests" (print hyphenation rejoined):

      sending a hedging request after a 10ms delay reduces the
      99.9th-percentile latency for retrieving all 1,000 values from 1,800ms
      to 74ms while sending just 2% more requests.

### Failure and recovery

- Q11, R2, "Hedged requests":

      Although naive implementations of this technique typically add
      unacceptable additional load

- Q12, R3, "Use cases":

      While naive implementations could add significant load to the backend
      servers, it is possible to get most of the latency reduction effects
      while increasing load only modestly.

- Q13, R4, "Retries and backoff":

      When failures are caused by overload, retries that increase load can
      make matters significantly worse. They can even delay recovery by
      keeping the load high long after the original issue is resolved.

- Q14, R3, "Hedging policy":

      Essentially, hedging can be seen as retrying the original RPC before a
      failure is even received.

- Q15, R4, "Retries and backoff":

      The other problem with retries is that some remote calls have side
      effects. A timeout or failure doesn't necessarily mean that side effects
      haven't happened. If doing the side effects multiple times is
      undesirable, a best practice is designing APIs to be idempotent, meaning
      they can be safely retried.

- Q16, R4, "Deciding when to retry":

      In general, our view is that APIs with side effects aren't safe to retry
      unless they provide idempotency. This guarantees that the side effects
      happen only once no matter how often you retry.

- Q17, R4, "Retries and backoff":

      A retry can increase the load on the system being called, if the system
      is already failing because it’s approaching an overload.

- Q18, R4, "Conclusion":

      Retries can amplify the load on a dependent system. If calls to a system
      are timing out, and that system is overloaded, retries can make the
      overload worse instead of better.

- Q23, R4, "Deciding when to retry":

      Good API design, and care when implementing clients, is needed to
      prevent duplicate side-effects.

### Alternative

- Q19, R4, "Jitter":

      Our solution is jitter. Jitter adds some amount of randomness to the
      backoff to spread the retries around in time.

- Q20, R4, "Retries and backoff":

      We have found that we can mitigate this risk by limiting retries locally
      using a token bucket

- Q21, R4, "Timeouts":

      A good practice for choosing a timeout for calls within an AWS Region is
      to start with the latency metrics of the downstream service. So at
      Amazon, when we make one service call another service, we choose an
      acceptable rate of false timeouts (such as 0.1%). Then, we look at the
      corresponding latency percentile on the downstream service (p99.9 in
      this example).

- Q22, R3, "Overview":

      Hedging is one of two configurable retry policies supported by gRPC.

## Dimension mapping

- Mechanism. Primary: Q1, record read.sre-cascading-hedging.2026-10-31,
  source src.sre-cascading, section "Cancellation propagation", revision
  11a045479e92e27f6b589a5285f971adfdf3d8ec0af0805c5855e29d848f9548.
  Supporting: Q2 (same request to multiple replicas) and Q3 (gRPC copies to
  different backends). Tycho reading: a hedge is a read-only duplicate; it
  sends the same work to an equivalent replica and accepts the first response,
  not a second business decision.
- Invariant. Primary: Q4, record read.tail-at-scale-hedged.2026-10-31, source
  src.tail-at-scale, section "Hedged requests", revision
  8bcecb9e86b6485cf699b3fac7f0622f468779a74745cfc82305ea278553a828.
  Supporting: Q5 (approximately 5% load in the example), Q6 (maxAttempts
  mandatory and capped at 5), Q7 (outstanding requests canceled), Q8
  (cancellation propagation), Q9 (throttling to prevent overload) and Q10 (the
  99.9th-percentile benchmark result). Tycho rule: record the measured
  percentile, the replica-equivalence check, the attempt cap and the
  cancellation evidence; a hedge without all four is an unbounded duplicate.
  The brief's "measured p99" is represented as a measured latency percentile:
  the paper uses a 95th-percentile deferral and reports a 99.9th-percentile
  effect, while AWS's timeout example uses p99.9. No bound source states a
  literal p99 hedge trigger.
- Failure and recovery. Primary: Q13, record
  read.aws-backoff-hedging.2026-10-31, source src.aws-backoff, section
  "Retries and backoff", revision
  c076aeb3beeb4766568d3cf85c5ffda79be9610be186159b925ceb882addfc94.
  Supporting: Q11 (unacceptable additional load), Q12 (significant backend
  load), Q14 (hedging is retrying before failure), Q15 and Q16 (side effects,
  idempotency), Q17 and Q18 (retry load amplification) and Q23 (duplicate
  side-effects). Tycho inference: because gRPC frames hedging as a retry
  before failure, the AWS duplicate-effect warning applies to a hedged write;
  treat a speculative write as unsafe until the effect has an idempotency
  identity and cancellation is shown to stop committed work.
- Alternative. Primary: Q21, record read.aws-backoff-hedging.2026-10-31,
  source src.aws-backoff, section "Timeouts", revision
  c076aeb3beeb4766568d3cf85c5ffda79be9610be186159b925ceb882addfc94.
  Supporting: Q19 (jitter), Q20 (token bucket), Q22 (hedging is one of two
  retry policies) and Q14 (hedging is retrying before failure). Tycho choice
  rule: reverse when the extra copy's measured tail benefit is smaller than its
  added load, or when a loser can commit an effect before cancellation. The
  slow-path and independent-read clauses are explicitly unbound Tycho
  heuristics and are not part of the supporting binding set.

Recommended shared state after the integrator applies the proposals:
technical_evidence.mechanism, invariant, failure_recovery and alternative all
supported; technical_coverage sufficient; decision_coverage sufficient;
review_state self-checked. This is not independent review, owner acceptance or
a promotion.

## Book edits

- Owner page (concatenate):

      book/volumes/v07-performance-scale-and-resilience/
      c04-tail-latency-fan-out-and-time-budgets/deadline-hedging.md

  - Frontmatter adds proposed src.grpc-hedging to evidence_scope.source_ids;
    evidence_scope.notes records the four-unit binding; content_review becomes
    self-checked with reviewer "Automated authoring agent"; updated_at and
    source_inspection_date become 2026-10-31.
  - The owner section gains a mechanism paragraph, a four-part invariant, a
    Tycho decision aid, a failure/recovery paragraph, a sourced alternative, an
    unbound-heuristics paragraph and a bound-source-limits paragraph. The
    original writes warning and navigation are retained.
  - Page 213 lines; 1,720 words; owner heading line 92.
  - Section lines 92-202: 111 lines, 994 words, SHA-256
    75271942d3d038b0084f23913a7b167329166afa55fb08c8dda77b091c579cca.
  - Page SHA-256:
    2aed559ca3f1326c499ee052fb05190333848da880605e57327d90575d14378f.
- Inline card: book/volumes/v11-pattern-atlas/c07-resilience/README.md.

  - Chapter frontmatter adds src.aws-backoff, proposed src.grpc-hedging and
    src.tail-at-scale to evidence_scope.source_ids; the notes record the Hedged
    Requests four-dimension binding.
  - The inline card expands Good-fit conditions, Hard contraindications,
    Competing alternative, Failure and recovery and Sources with the same
    bindings. The owner link, decision state and related entries are unchanged.
  - Card heading line 364; chapter 464 lines; 2,535 words.
  - Card block (heading through related entries): 67 lines, 569 words, SHA-256
    abfc142d82dc0480eeb9b34bcdc6f9987b5bcfa523b4208c1a5446b0a272736d.
  - Chapter SHA-256:
    d7d35723748c6d68619d3a68071d6adaa7d3d5ccb3833b3221bad319586a0914.
- No other book file, edition JSON, promotion or generated file is changed.
- One pre-existing 160-character HTTP/RPC link line in the writes warning is
  retained verbatim. The V11 line-length gate passes with 145 exact owner-link
  exceptions; the owner page is not covered by that gate.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
owner unit can move to 4/4 supported and before atlas hash checks pass.

### Source register sources/register.json

Set updated to 2026-10-31; the source count moves from 328 to 329 for the new
gRPC unit.

- Add src.grpc-hedging:
  - title: "Request Hedging"
  - category: "resilience"
  - publisher: "gRPC authors"
  - kind: "official-docs"
  - url and resolved_url: https://grpc.io/docs/guides/request-hedging/
  - topics: ["resilience", "tail-latency", "retries"]
  - priority: "core"
  - planned_use: "Hedged request budget, cancellation, retry alternative and
    overload throttling."
  - admission: "admitted-for-research"
  - access: "public-web-or-author-download"
  - reading_status: "full-public-page-inspected"
  - version: "Pinned source Markdown at grpc/grpc.io commit
    d3573082150aa8a1363dcbd86952f8771dc287ed (2023-10-03), 6,165 bytes,
    SHA-256 976a95ef7de5b966835ac057ef9817272c51f7e5ce40d02bd1841fe65fe29c85;
    rendered page fetched 2026-10-31, raw HTML SHA-256 949634b3..., canonical
    text SHA-256 b9c0871d..., 957 words; page footer identifies commit
    d357308."
  - access_checked and content_verified: 2026-10-31
  - license_notes: "Public gRPC documentation; cite short excerpts and
    paraphrase; do not mirror."
  - verification_scope: "Complete guide page and pinned source Markdown read;
    linked examples, language implementations and runtime behavior not
    verified."
  - observed_title: "Request Hedging"
- Update src.tail-at-scale:
  - reading_status: "full-public-page-inspected"
  - resolved_url: https://mags.acm.org/communications/201302/?pg=79
  - version: "CACM February 2013, vol. 56, no. 2; DOI
    10.1145/2408776.2408794. Digital-edition page fetched 2026-10-31;
    decompressed HTML 47,159 bytes, raw SHA-256 16d88b04...; hidden page text
    568 words / 3,625 characters, SHA-256 648a0785...; dehyphenated canonical
    text 561 words / 3,611 characters, SHA-256 8bcecb9e...; no Last-Modified
    or ETag."
  - access_checked and content_verified: 2026-10-31
  - verification_scope: "Section 'Hedged requests' read in the served article
    text; figures, tables, pages 80-82 and the publisher PDF were not read."
  - observed_title: "The Tail at Scale"
- src.sre-cascading: no forced field change. Reconcile the version note's
  older raw/canonical hashes with the d67024d5... / 11a04547... representation
  recorded here. Do not overwrite the historical ledger record.
- src.aws-backoff: no change. The existing
  read.aws-builders-timeouts-retries.2026-10-31 record and the c076aeb3...
  canonical representation are reused.

### Reading ledger edition/patterns/reading-ledger.v1.json

Add four records. All use reviewer "Automated authoring agent", status "read",
access_date 2026-10-31 and read_scope "publicly served page as returned by
fetch, excluding navigation, linked pages and unrelated chrome".

- read.sre-cascading-hedging.2026-10-31
  - source: src.sre-cascading
  - unit: Addressing Cascading Failures — public chapter
  - sections_read: Cancellation propagation; Latency and Deadlines context
  - content_sha256: 11a045479e92e27f6b589a5285f971adfdf3d8ec0af0805c5855e29d848f9548
  - words/chars: 9,046 / 55,929
- read.tail-at-scale-hedged.2026-10-31
  - source: src.tail-at-scale
  - unit: The Tail at Scale — CACM digital edition
  - sections_read: Hedged requests
  - content_sha256: 8bcecb9e86b6485cf699b3fac7f0622f468779a74745cfc82305ea278553a828
  - words/chars: 561 / 3,611
- read.grpc-hedging.2026-10-31
  - source: src.grpc-hedging
  - unit: Request Hedging — gRPC guide
  - sections_read: Overview; Use cases; Configuring hedging in gRPC; Hedging
    policy; Throttling Hedged RPCs; Server Pushback
  - content_sha256: 976a95ef7de5b966835ac057ef9817272c51f7e5ce40d02bd1841fe65fe29c85
  - words/bytes: 926 / 6,165
- read.aws-backoff-hedging.2026-10-31
  - source: src.aws-backoff
  - unit: Timeouts, retries, and backoff with jitter — AWS Builders' Library
  - sections_read: Timeouts; Retries and backoff; Jitter; Deciding when to
    retry; Conclusion
  - content_sha256: c076aeb3beeb4766568d3cf85c5ffda79be9610be186159b925ceb882addfc94
  - words/chars: 2,373 / 14,549

Additional fields per record:

- SRE: unit_url https://sre.google/sre-book/addressing-cascading-failures/;
  unit_type book-chapter; access_method records the HTTP/2 200 on
  2026-10-31T20:46:15Z, gzip length 31,399 bytes, decompressed 104,870 bytes,
  Last-Modified 2026-10-08T04:48:00Z, raw SHA d67024d5..., content-div
  extraction; claims_supported "Delayed duplicate RPCs to other instances are
  canceled after the first response and cancellation should propagate; this is
  the chapter's hedged-request definition."; claims_not_supported "universal
  cancellation guarantee; benchmark; implementation behavior."; limitations
  "Book chapter; hedged-request passage only; linked pages not read."
- TAS: unit_url https://mags.acm.org/communications/201302/?pg=79; unit_type
  article; access_method records the HTTP/2 200 on 2026-10-31T20:46:23Z,
  decompressed 47,159 bytes, raw SHA 16d8..., hidden-text SHA 648a..., and
  the dehyphenation step to 8bce...; claims_supported "95th-percentile
  deferral, approximately 5% additional load in the example, 99.9th-percentile
  benchmark improvement to 74ms, and the warning about naive additional load.";
  claims_not_supported "current production measurement; universal threshold;
  pages 80-82; the publisher PDF."; limitations "2013 CACM digital-edition
  representation; print hyphenation rejoined; figures not reproduced."
- gRPC: unit_url https://grpc.io/docs/guides/request-hedging/; unit_type
  documentation-page; access_method records the rendered page and the pinned
  Markdown commit d357308...; claims_supported "multiple copies to different
  backends, first response, cancellation, maxAttempts capped at 5, retry
  throttling, deadline over the chain, and hedging as one of two retry
  policies."; claims_not_supported "application-level effect rollback;
  benchmark; language implementation behavior."; limitations "Documentation;
  linked examples and runtime behavior not verified."
- AWS: unit_url
  https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/;
  unit_type engineering-article; access_method records the redirect to the
  Builder Center content id, HTTP/2 200 on 2026-10-31T20:46:21Z, 139,053
  bytes, raw SHA 26c6..., canonical SHA c076..., and the displayed 2019-12-05
  dates; claims_supported "retry load amplification, duplicate side effects
  without idempotency, timeout selection from a measured latency percentile,
  jitter, token-bucket retry limiting."; claims_not_supported "formal
  specification; benchmark; hedging-specific measurement."; limitations
  "Engineering article; p99.9 example is timeout selection, not a hedge
  threshold."

### Source plan edition/patterns/source-plan.v1.json

Replace the hedged-requests required_units array with the four selected units;
keep the Morning Paper read.batch4-hedged.2026-10-21 as a historical auxiliary
record if the schema permits, otherwise drop it from required_units and record
it in the entry notes. Proposed notes: "Four public units bound 2026-10-31:
Google SRE cancellation propagation, the 2013 Tail at Scale hedged-request
section, gRPC request hedging and AWS retry/backoff guidance; the alternative
is narrowed to measured-timeout and jittered-retry comparisons; slow-path and
independent-read clauses remain unbound Tycho heuristics."

Required units:

    [
      {
        "source_id": "src.sre-cascading",
        "unit": "Addressing Cascading Failures — public chapter",
        "unit_type": "book-chapter",
        "url": "https://sre.google/sre-book/addressing-cascading-failures/",
        "sections": ["Cancellation propagation"],
        "status": "read",
        "read_record_id": "read.sre-cascading-hedging.2026-10-31",
        "blocked_reason": null
      },
      {
        "source_id": "src.tail-at-scale",
        "unit": "The Tail at Scale — CACM digital edition",
        "unit_type": "article",
        "url": "https://mags.acm.org/communications/201302/?pg=79",
        "sections": ["Hedged requests"],
        "status": "read",
        "read_record_id": "read.tail-at-scale-hedged.2026-10-31",
        "blocked_reason": null
      },
      {
        "source_id": "src.grpc-hedging",
        "unit": "Request Hedging — gRPC guide",
        "unit_type": "documentation-page",
        "url": "https://grpc.io/docs/guides/request-hedging/",
        "sections": ["Overview", "Configuring hedging in gRPC", "Hedging policy",
                     "Throttling Hedged RPCs"],
        "status": "read",
        "read_record_id": "read.grpc-hedging.2026-10-31",
        "blocked_reason": null
      },
      {
        "source_id": "src.aws-backoff",
        "unit": "Timeouts, retries, and backoff with jitter — AWS Builders' Library",
        "unit_type": "engineering-article",
        "url": "https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/",
        "sections": ["Timeouts", "Retries and backoff", "Jitter",
                     "Deciding when to retry"],
        "status": "read",
        "read_record_id": "read.aws-backoff-hedging.2026-10-31",
        "blocked_reason": null
      }
    ]

### Owner units edition/patterns/owner-units.v1.json

Replace the hedged-requests technical_evidence and the related fields. Keep
the existing document id, path, heading, anchor and level; set owner.line to
92 and update owner.unit_terms to ["hedged request", "same read to another
replica", "measured latency distribution", "cancellation evidence"].

Technical evidence (use the exact quote text from "Selected exact quotes"):

- mechanism: state supported. Claim quote: the owner mechanism sentence
  beginning "A hedged request sends the same read...". Reason: Google SRE
  defines the delayed duplicate and cancellation; gRPC and the Tail at Scale
  paper repeat the same shape; the Tycho reading bounds it to reads. Primary
  binding: Q1, read.sre-cascading-hedging.2026-10-31, section "Cancellation
  propagation", revision 11a045479e92e27f6b589a5285f971adfdf3d8ec0af0805c5855e29d848f9548.
  Supporting: Q2 (src.tail-at-scale, revision 8bcecb9e...) and Q3
  (src.grpc-hedging, revision 976a95ef...).
- invariant: state supported. Claim quote: "A hedge is defensible only when the
  replicas are equivalent, the speculative budget is bounded, cancellation
  stops the losers, and the delay comes from the measured latency distribution
  of that request class." Reason: the TAS paper uses a 95th-percentile delay
  and reports a 99.9th-percentile effect; gRPC caps maxAttempts at 5 and
  throttles hedges; SRE and gRPC cancel losers and SRE requires propagation
  through the stack; the recording rule is Tycho. Primary binding: Q4,
  read.tail-at-scale-hedged.2026-10-31, section "Hedged requests", revision
  8bcecb9e86b6485cf699b3fac7f0622f468779a74745cfc82305ea278553a828.
  Supporting: Q5/Q10 (same record), Q6/Q7/Q9 (read.grpc-hedging.2026-10-31,
  revision 976a95ef...), Q8 (read.sre-cascading-hedging.2026-10-31, revision
  11a04547...).
- failure_recovery: state supported. Claim quote: "A hedge adds a second copy
  of the work and can raise load when a shared dependency is saturated; a
  hedged write can duplicate an effect unless the effect has an idempotency
  identity and canceled losers can be reconciled." Reason: TAS and gRPC warn
  about additional load; AWS records retry amplification and duplicate side
  effects without idempotency; gRPC frames hedging as retrying before failure;
  the write inference and reconciliation rule are Tycho. Primary binding: Q13,
  read.aws-backoff-hedging.2026-10-31, section "Retries and backoff", revision
  c076aeb3beeb4766568d3cf85c5ffda79be9610be186159b925ceb882addfc94.
  Supporting: Q11 (TAS), Q12/Q14 (gRPC), Q15/Q16/Q23 (AWS).
- alternative: state supported. Claim quote: "Prefer a single bounded attempt
  with a timeout chosen from the measured latency distribution, or a retry with
  backoff, jitter and a token-bucket retry budget, when the replicas share a
  bottleneck or the operation is not safely repeatable." Reason: AWS recommends
  timeout selection from the downstream latency percentile, jitter and a local
  token bucket; gRPC classifies hedging as one of two retry policies. The
  slow-path and independent-read clauses are Tycho heuristics and are not in
  the bound claim. Primary binding: Q21,
  read.aws-backoff-hedging.2026-10-31, section "Timeouts", revision
  c076aeb3... Supporting: Q19/Q20 (AWS), Q22 (gRPC).

Other owner-units fields:

- technical_evidence as above; technical_coverage "sufficient";
  decision_coverage "sufficient"; review_state "self-checked".
- notes: "Four dimensions bound 2026-10-31 to four public units: Google SRE
  cascading-failure cancellation, the 2013 Tail at Scale hedged-request
  section, gRPC request hedging and AWS retry/backoff guidance; the
  alternative is narrowed to measured-timeout and jittered-retry comparisons;
  coverage is self-checked, not independently reviewed."
- source_support: primary ledger_record read.sre-cascading-hedging.2026-10-31,
  source_id src.sre-cascading, unit_type book-chapter, status read,
  card_citation true; auxiliary entries for read.tail-at-scale-hedged..., the
  two gRPC records, read.aws-backoff-hedging... and the retained
  read.batch4-hedged.2026-10-21.
- decision_evidence.competing_alternative: "A single bounded attempt with a
  timeout chosen from the measured latency percentile, or a retry with
  backoff, jitter and a token-bucket retry budget. Reverse when duplicate load
  and cancellation cost exceed the measured tail benefit."
- decision_evidence.card_components: 10; decision_state
  applicable-under-conditions; atlas_section hedged-requests.

### Registry, card batches and derived artifacts

No registry or card-batch content change is proposed: tycho.pattern.hedged-requests
already records atlas_section hedged-requests and the card remains inline. The
integrator should regenerate any content revisions, atlas hashes, route index,
sufficient-ready counts and owner-unit audit artifacts that depend on the two
edited pages. Those derived changes are outside this lane.

## Validation

- python3 scripts/check_markdown_line_length.py: PASS, V11 prose <=100; 145
  exact owner-link exceptions.
- python3 scripts/check_boundary.py: PASS, configured lexical boundary checks;
  independent-origin review still required.
- Quote check: 12/12 distinct owner/card fragments present in the named
  canonical representations; 23/23 lane-note passages present.
- git diff --check: clean.
- No full test suite was run. This is a documentation-only lane; rule 31 keeps
  the batch-end suite out of the per-entry edit. No hedging, retry, timeout,
  cancellation, benchmark or failure exercise was run.

## Limits

- No runtime experiment, benchmark, production observation or independent
  review is claimed. The 2013 Tail at Scale benchmark is the only measured
  result cited; it is not a prediction for another deployment.
- The owner and card now distinguish bound source claims from Tycho guidance.
  The slow-path and independent-read alternatives remain unbound heuristics;
  binding them requires a separate source that tests those comparisons.
- "Measured p99" in the task brief is represented as a measured latency
  percentile: the paper uses a 95th-percentile deferral and a 99.9th-percentile
  outcome, and AWS uses p99.9 for timeout selection. No source supports a
  literal p99 hedge trigger.
- The CACM representation is the public digital-edition HTML, not the
  publisher PDF. End-of-line hyphenation was rejoined for the canonical text;
  raw and hidden-text hashes are recorded.
- Shared register, ledger, source-plan and owner-unit changes are proposals
  only. Until the integrator applies them, shared metadata still shows the
  entry at 1/4.
- No promotion, owner acceptance, CI run or merge is claimed.

## Lane commit

Commit "docs(book): bind hedged-requests dimensions" on b61-hedging. The commit
contains exactly the owner page, the inline card host and this note.
