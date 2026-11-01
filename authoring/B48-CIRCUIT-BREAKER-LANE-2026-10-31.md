# B48 — Circuit Breaker four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 0/4 at the parent HEAD: zero dimensions supported and all four
`partial`. This lane binds all four dimensions to public sources and labels
the minimum-volume rule, the threshold-comparison boundary, the local-versus-
dependency attribution rule and the alternative choice as Tycho. The card
remains inline in V11/C07.

## Lane coordinates

- Parent HEAD: `4f863e6b0fdaac72c6f3639ed46f5944f6e0bb3d` (`4f863e6b`).
- Branch: `b48-circuit-breaker`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b48-circuit-breaker`.
- Scope: the owner section `### Circuit Breaker` in the V07/C05 page and
  the inline V11/C07 card `### Circuit Breaker`. Single-entry lane; no
  other entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v07-performance-scale-and-resilience/
      c05-overload-protection-and-graceful-degradation/dependency-isolation.md

- Card path:
  `book/volumes/v11-pattern-atlas/c07-resilience/README.md`.
- Exactly three files change: the owner page, the inline card and this note.
  No shared JSON file is edited.

## Baseline and gap

The owner-unit entry for `tycho.pattern.circuit-breaker` records all four
states as `partial`; `technical_coverage` is `partial` and
`decision_coverage` is `partial-bounded`. All four dimensions carry
the same recorded reason: "Local representation hash differs from the recorded
revision; quotes are not accepted for the pinned unit."

That reason points at a representation mismatch, not at missing prose. The
existing `read.batch4-r4j-circuit.2026-10-21` record's
`content_sha256` is
`cad62135427cfee85f2c80095c3b823854aa36d4314a0fd829fa956022036e94`.
The public Markdown alternate
`https://resilience4j.readme.io/docs/circuitbreaker.md` fetched on
2026-10-31 has the same SHA-256, so the recorded digest is reproducible from
that representation. This lane uses the Markdown alternate and does not rely on
the record's earlier HTML-fetch truncation note.

The other three source units were admitted but not bound to this entry:

- `src.sre-overload` has `read.sre-overload.2026-10-21` and a
  register entry verified 2026-10-31 with raw HTML SHA-256
  `945d15db67ad15a7f5e75833f8c0d014c8dc61d57909f7a3abd48459ad12cc9e`
  and canonical text SHA-256
  `8154963544456669d31fb2666db9f6a6a91ea0d4135d01d30e41922172a71bf2`.
  The chapter supports retry budgets, adaptive throttling and overload-error
  handling, but it was not linked to the circuit-breaker owner section.
- `src.aws-backoff` is admitted and has no reading-ledger record. The
  article supports the timeout, retry and jitter alternative.
- `src.microsoft-cloud-patterns` is admitted and has many pattern-page
  records, but no circuit-breaker page record. Azure supplies the state
  definitions, half-open recovery, the flood warning, the external-recovery
  statement and the local-resource contraindication.

The gap is therefore evidential and editorial: the owner section already said
most of the mechanism correctly, but no exact public quote, revision and
representation hash were bound to the four dimensions. The shared metadata still
shows 0/4 until an integrator applies the proposals below.

## Candidate evaluation

- Resilience4j, "CircuitBreaker" documentation (selected). Supplies the finite
  state machine, the sliding window, the failure-rate threshold, the
  minimum-call gate, half-open permitted calls and the rejected-call exception.
- Microsoft Azure Architecture Center, "Circuit breaker pattern" (selected).
  Supplies the Closed, Open and Half-Open definitions, the interval-bounded
  failure threshold, half-open recovery and flooding, external recovery, the
  local-resource contraindication and the retry contrast.
- AWS Builders' Library, "Timeouts, retries, and backoff with jitter"
  (selected). Supplies the breaker recovery-time critique, token-bucket retry
  limiting, timeout selection and jitter.
- Google SRE, "Handling Overload" (selected). Supplies per-request and
  per-client retry budgets, adaptive client-side throttling and the overload
  retry policy.
- Hystrix documentation, Resilience4j source code, the Azure "Retry pattern"
  page and the Google SRE "Addressing Cascading Failures" chapter were not read
  as units for this lane. They are not used as support. The existing
  cascading-failures record remains a broader scope limit, not a circuit-breaker
  quote source.
- No origin claim is made. This lane does not read the historical
  circuit-breaker literature; it binds four current public explanations and
  their stated limits.

The lane also corrects the earlier "failures are fast" framing. Azure lists slow
dependencies as a use case and warns that a breaker does not protect against
long time-outs; Resilience4j has a slow-call-rate threshold. The revised rule
requires a bounded timeout, dependency-local attribution and repeated
amplification, not fast failure.

## Source binding

Quotes reproduce the served or pinned prose. Line breaks inside a quote are
editorial wrapping. Markdown escapes, emphasis, curly quotes and link-extraction
spaces before punctuation are normalized. Every quote was checked as a
whitespace-normalized substring of the named representation on 2026-10-31.
Tycho-labelled sentences are not presented as source quotes.

### Resilience4j — CircuitBreaker documentation

- Source id: `src.resilience4j` (existing, admitted).
- Record: `read.batch4-r4j-circuit.2026-10-21` (existing;
  `content_sha256` matches the representation below).
- Unit URL: `https://resilience4j.readme.io/docs/circuitbreaker.md`;
  canonical page: `https://resilience4j.readme.io/docs/circuitbreaker`.
- Representation: HTTP 200 on 2026-10-31T13:20:46Z; content type
  `text/markdown; charset=utf-8`; 20,004 bytes; 326 lines; 2,481 words;
  SHA-256
  `cad62135427cfee85f2c80095c3b823854aa36d4314a0fd829fa956022036e94`;
  ETag `W/"4e24-kFHnNwDYpMolP5bz28Ena0W+Oqk"`; render id
  `576f099d-c40e-47bb`. The page is rolling documentation with no published
  version; the digest pins this representation.
- Sections used: Introduction; Count-based sliding window; Time-based sliding
  window; Failure rate and slow call rate thresholds; the configuration
  properties `failureRateThreshold`, `minimumNumberOfCalls`,
  `waitDurationInOpenState` and
  `permittedNumberOfCallsInHalfOpenState`.
- Exact quotes:

      The CircuitBreaker is implemented via a finite state machine with three
      normal states: CLOSED, OPEN and HALF_OPEN and three special states
      METRICS_ONLY, DISABLED and FORCED_OPEN.

      The CircuitBreaker uses a sliding window to store and aggregate the
      outcome of calls.

      The state of the CircuitBreaker changes from CLOSED to OPEN when the
      failure rate is equal or greater than a configurable threshold.

      The failure rate and slow call rate can only be calculated, if a
      minimum number of calls were recorded.

      If only 9 calls have been evaluated the CircuitBreaker will not trip
      open even if all 9 calls have failed.

      Configures the minimum number of calls which are required (per sliding
      window period) before the CircuitBreaker can calculate the error rate or
      slow call rate.

      Further calls are rejected with a CallNotPermittedException, until all
      permitted calls have completed.

      If the failure rate and slow call rate is below the threshold, the state
      changes back to CLOSED.

- Limits: the Markdown alternate is a documentation representation, not a
  release tag, formal specification or benchmark. The page describes
  Resilience4j behavior; no library was run. The special states METRICS_ONLY,
  DISABLED and FORCED_OPEN are noted but not analyzed. The earlier HTML-fetch
  truncation note is not used for this representation.

### Microsoft Azure — Circuit breaker pattern

- Source id: `src.microsoft-cloud-patterns` (existing, admitted).
- Proposed record: `read.microsoft-circuit-breaker.2026-10-31`.
- Live unit URL:
  `https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker`.
- Live representation: HTTP 200 on 2026-10-31T13:20:55Z; Last-Modified
  2026-09-26T05:05:04Z; ETag
  `"NThv46B/2aPU5pWB8DJBE6hGdCE="`; 75,396 bytes of HTML; raw HTML
  SHA-256
  `5b83f1575092478594cf049c4c4a0a8505b9bdc851f6db4fbee3d9dd979c1655`;
  `ms.date` 2025-02-05; canonical article text 24,523 characters and
  3,776 words, SHA-256
  `29299b3b788328f0ec127c6f37b5f7bfb6ffc0d4a6bab37d4a0d81b5a4614274`.
- Pinned revision: public raw Markdown `docs/patterns/circuit-breaker.md` in
  `MicrosoftDocs/architecture-center` at commit
  `9fdb775034a2faf6b2dcf699fb870d49fe50c992` (commit date
  2026-09-25T19:33:08Z; "PnP edit: Health Endpoint Monitoring pattern
  (#16771)"). The page's own GitHub metadata names this commit. Pinned
  representation: 25,769 bytes; 187 lines; 3,744 words; SHA-256
  `29baeab9e19c54c9fdae01dfa4c431bae0c6811e0c5267a1d6c8c78267b8146e`.
- Sections used: Context and problem; Solution; Problems and considerations;
  When to use this pattern; Workload design.
- Exact quotes:

      You can implement the proxy as a state machine that includes the
      following states.

      Closed: The request from the application is routed to the operation.

      Open: The request from the application fails immediately and an
      exception is returned to the application.

      Half-Open: A limited number of requests from the application are allowed
      to pass through and invoke the operation.

      If any request fails, the circuit breaker assumes that the fault is
      still present, so it reverts to the Open state.

      The failure threshold triggers the Open state only when a specified
      number of failures occur during a specified interval.

      The Half-Open state helps prevent a recovering service from suddenly
      being flooded with requests.

      System recovery is based on external operations, such as restoring or
      restarting a failed component or repairing a network connection.

      A circuit breaker might not fully protect applications from failures in
      external services that have long time-out periods.

      You need to manage access to local private resources in an application,
      such as in-memory data structures.

      Waiting for a circuit breaker to reset might introduce unacceptable
      delays.

      Well-known retry algorithms are sufficient and your dependencies are
      designed to handle retry mechanisms.

- Limits: living documentation with no published version identifier. The
  pinned Markdown is the quote authority; the live page is a cross-check. The
  page says thresholds are configurable and does not prescribe values. Its
  Closed-state failure counter is time based and resets periodically, while
  Resilience4j offers count-based and time-based sliding windows; the lane does
  not treat those window models as equivalent. The example uses a managed
  database and was not executed. The local-resource contraindication is a scope
  limit, not proof that a breaker cannot help elsewhere.

### AWS Builders' Library — Timeouts, retries, and backoff with jitter

- Source id: `src.aws-backoff` (existing, admitted).
- Proposed record: `read.aws-builders-timeouts-retries.2026-10-31`.
- Unit URL: `https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/`;
  HTTP 301 to the Builder Center article at content id
  `3EumjoZascWd1oZiEgL8ORlv3qE`, slug
  `timeouts-retries-and-backoff-with-jitter`.
- Representation: HTTP 200 on 2026-10-31T13:21:11Z; 139,053 bytes of HTML;
  raw HTML SHA-256
  `d289c95d849b6d082f8b9aac64f1df92d7383d9b49ff3326d4d181ba8140f636`;
  canonical article text 14,549 characters and 2,373 words, SHA-256
  `c076aeb3beeb4766568d3cf85c5ffda79be9610be186159b925ceb882addfc94`.
  The page displays "Published Dec 5, 2019" and "Last modified Dec 5, 2019";
  the response has no Last-Modified header and no published version identifier.
- Sections used: Introduction; Failures Happen; Timeouts; Retries and backoff;
  Jitter; Conclusion.
- Exact quotes:

      Retries are "selfish."

      When failures are caused by overload, retries that increase load can
      make matters significantly worse.

      Circuit breakers, where calls to a downstream service are stopped
      entirely when an error threshold is exceeded, are widely promoted to
      solve this problem.

      Unfortunately, circuit breakers introduce modal behavior into systems
      that can be difficult to test, and can introduce significant addition
      time to recovery.

      We have found that we can mitigate this risk by limiting retries locally
      using a token bucket.

      A best practice in Amazon is to set a timeout on any remote call, and
      generally on any call across processes even on the same box.

      Setting a timeout too high reduces its usefulness, because resources are
      still consumed while the client waits for the timeout.

      Jitter adds some amount of randomness to the backoff to spread the
      retries around in time.

      If all the failed calls back off to the same time, they cause contention
      or overload again when they are retried.

- Limits: engineering article, not a formal specification or benchmark. The
  word "addition" in the recovery-time sentence is in the served text and is
  retained in the quote. The article states one public provider's practice; it
  does not establish a universal rule. No service, SDK or retry path was run.

### Google SRE — Handling Overload

- Source id: `src.sre-overload` (existing, admitted).
- Record: `read.sre-overload.2026-10-21` (existing; the raw HTML digest
  below matches the record and the 2026-10-31 register verification).
- Unit URL: `https://sre.google/sre-book/handling-overload/`.
- Representation: HTTP 200 on 2026-10-31T13:21:10Z; Last-Modified
  2026-10-08T04:48:00Z; 71,785 bytes of HTML; raw HTML SHA-256
  `945d15db67ad15a7f5e75833f8c0d014c8dc61d57909f7a3abd48459ad12cc9e`;
  canonical text 30,636 characters and 4,901 words, SHA-256
  `8154963544456669d31fb2666db9f6a6a91ea0d4135d01d30e41922172a71bf2`.
  The chapter is from the 2017 SRE book and is licensed CC BY-NC-ND 4.0; no
  separate version identifier is published.
- Sections used: Client-Side Throttling; Client request rejection probability;
  Handling Overload Errors; Deciding to Retry; Utilization Signals;
  Conclusions.
- Exact quotes:

      When a client detects that a significant portion of its recent requests
      have been rejected due to "out of quota" errors, it starts
      self-regulating and caps the amount of outgoing traffic it generates.

      Requests above the cap fail locally without even reaching the network.

      First, we implement a per-request retry budget of up to three attempts.

      Secondly, we implement a per-client retry budget.

      Each client keeps track of the ratio of requests that correspond to
      retries.

      A request will only be retried as long as this ratio is below 10%.

      If a large subset of backend tasks in the datacenter are overloaded,
      requests should not be retried and errors should bubble up all the way to
      the caller (e.g., returning an error to the end user).

      The key point is that a failed request from the DB Frontend should only
      be retried by Backend B, the layer immediately above it.

- Limits: one 2017 book chapter. The examples name public services and are not
  reproduced or run. The chapter describes a particular large-scale serving
  stack; its retry budgets and adaptive throttling are not universal defaults.
  No benchmark or production measurement is claimed.

## Proposed metadata (not applied)

### Source register

No new source identity is required; all four units belong to existing admitted
sources. Proposed version updates only:

- `src.resilience4j`: record the 2026-10-31 Markdown alternate, SHA-256
  `cad62135427cfee85f2c80095c3b823854aa36d4314a0fd829fa956022036e94`,
  and note that the documentation is rolling with no version selector.
- `src.microsoft-cloud-patterns`: add the circuit-breaker page to the
  version note: canonical text SHA-256
  `29299b3b788328f0ec127c6f37b5f7bfb6ffc0d4a6bab37d4a0d81b5a4614274`,
  pinned commit `9fdb775034a2faf6b2dcf699fb870d49fe50c992`,
  `ms.date` 2025-02-05.
- `src.aws-backoff`: record the 2026-10-31 Builder Center fetch, raw
  HTML SHA-256
  `d289c95d849b6d082f8b9aac64f1df92d7383d9b49ff3326d4d181ba8140f636`,
  canonical text SHA-256
  `c076aeb3beeb4766568d3cf85c5ffda79be9610be186159b925ceb882addfc94`,
  and the displayed 2019-12-05 dates.
- `src.sre-overload`: already records the 2026-10-31 raw HTML and
  canonical hashes; no change is needed.

### Reading ledger

Add two records; the existing two are revalidated, not replaced.

- `read.microsoft-circuit-breaker.2026-10-31` — source
  `src.microsoft-cloud-patterns`; pattern page; pinned Markdown at
  commit `9fdb775034a2faf6b2dcf699fb870d49fe50c992`; sections Context and
  problem, Solution, Problems and considerations, When to use this pattern,
  Workload design; content SHA-256
  `29baeab9e19c54c9fdae01dfa4c431bae0c6811e0c5267a1d6c8c78267b8146e`;
  claims: state machine, threshold interval, half-open probe and flood
  warning, external recovery, local-resource contraindication, retry contrast;
  excludes linked pages, the executed example, images and unrelated chrome.
- `read.aws-builders-timeouts-retries.2026-10-31` — source
  `src.aws-backoff`; engineering article; sections Introduction, Failures
  Happen, Timeouts, Retries and backoff, Jitter, Conclusion; content SHA-256
  `c076aeb3beeb4766568d3cf85c5ffda79be9610be186159b925ceb882addfc94`;
  claims: timeout budget, retry amplification, token-bucket limiting, breaker
  recovery-time critique, jitter; excludes SDK behavior, benchmarks and
  linked articles.
- `read.batch4-r4j-circuit.2026-10-21` — existing record; its
  `content_sha256` matches the 2026-10-31 Markdown alternate exactly. It
  remains the circuit-breaker record for `src.resilience4j`.
- `read.sre-overload.2026-10-21` — existing record; its raw HTML
  `content_sha256` matches the 2026-10-31 representation. It remains the
  overload chapter record.

### Owner units

Proposed state for `tycho.pattern.circuit-breaker`: all four dimensions
`supported`; `technical_coverage` becomes `partial-bounded`;
`decision_coverage` stays `partial-bounded`; notes record this lane
and its source boundary.

- mechanism: quote "A circuit breaker is a state machine around one dependency:
  closed counts outcomes over a rolling window, open rejects fast for a
  cooldown, half-open admits a bounded probe." Reason: Resilience4j
  finite-state machine and sliding window; Azure Closed, Open and Half-Open
  definitions.
- invariant: quote "Threshold semantics need both a rate and a minimum volume."
  Reason: Resilience4j minimum calls and "equal or greater" threshold; Azure
  interval-bounded failure threshold and "exceeds" wording. The comparison
  boundary remains a recorded disagreement.
- failure_recovery: quote "An open caused by local resource exhaustion hides
  the real bottleneck." Reason: Azure half-open probe, flood warning and
  external-recovery statement; Azure local-resource contraindication; SRE
  utilization signals based on local state; Tycho fallback/fail-fast contract.
- alternative: quote "Use a breaker when failures are dependency-local,
  observable and repeated calls amplify them, whether the symptom is an error
  or a slow call." Reason: Resilience4j slow-call-rate threshold and Azure
  slow-dependency scope; AWS token-bucket retry limiting, timeout budget and
  jitter; Google SRE per-request and per-client retry budgets and adaptive
  throttling; Azure retry contrast and long-time-out warning.

Counter deltas if the four states move from `partial` to `supported`:
mechanism 114 -> 115, invariant 79 -> 80, failure/recovery 73 -> 74,
alternative 78 -> 79; technical partial 69 -> 68 and partial-bounded 15 -> 16;
sufficient stays 61. These counts are derived from the current
`owner-units.v1.json`; this lane does not apply them.

### Source plan, registry and card metadata

No new source identity is added, so the register source count does not change.
The source plan and registry should add the two reading records above and
recompute their own counters when an integrator applies the proposal. No
manifest, card batch, promotion record or generated index is changed here.

## Validation

- `python3 scripts/check_markdown_line_length.py`: PASS; 145 exact
  owner-link exceptions. The card's only long line is the existing
  `**Technical owner.**` exception.
- Owner page: every newly written line is <=100 characters. Pre-existing
  frontmatter, table and prose lines that already exceeded 100 are unchanged.
- This note: every line is <=100 characters.
- `python3 scripts/check_boundary.py`: PASS; independent-origin review is
  still required.
- Links in the owner and card are unchanged; the card anchor remains
  `#circuit-breaker`.
- The owner frontmatter `evidence_scope.source_ids` lists the four source
  identities used; no shared source register or reading-ledger entry is
  changed.
- `git diff --stat` after the edits reports two modified files; this note is
  new, so the commit changes three files.
- Raw SHA-256 after the book edits:
  - owner page:
    `c27480285dd97b6196b3ef6a41882672861c9d4064b6721c17e26d76b42078ab`
  - card:
    `55bef0ff27a647e7576b9f856bc4db706de925400e98864b00fb789a7db6804f`

## Limits

- Shared metadata is not updated. The generated owner units, registry, source
  plan, ledger, card batches and indexes still show the entry as 0/4 or partial
  until an integrator applies the proposals above.
- No promotion, owner acceptance, coverage sufficiency or independent AI review
  is claimed. The book/atlas review gate remains outstanding.
- No benchmark, production observation, library run or runtime measurement is
  claimed.
- Resilience4j is rolling documentation; Azure and AWS are living public pages.
  Their pinned hashes are the revision evidence, not release tags.
- The Google SRE chapter is from 2017; its examples are not reproduced.
- The sources do not agree on the threshold boundary: Resilience4j says
  "equal or greater"; Azure says "exceeds." The owner text records that
  disagreement rather than resolving it silently.
