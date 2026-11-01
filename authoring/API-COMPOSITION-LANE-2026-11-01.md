# API Composition — public-source binding lane

Status: lane-local book edit, self-checked on 2026-11-01. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and alternative were supported,
while invariant and failure/recovery were partial. This lane binds the two
missing dimensions to Microsoft's Gateway Aggregation pattern, reuses the
existing microservices.io API Composition record, and adds Microsoft's Web API
design guidance for versioning and trace context. The per-source freshness
format, per-call deadline contract, query-shape limits and transaction boundary
remain Tycho synthesis. The metadata patch is described below but is not in the
lane commit; promotion is not claimed or ready.

## Lane coordinates

- Parent HEAD: `a1902d6447f2ebb5bca39889380791b38192a053` (`a1902d64`).
- Branch: `feature/TYCHO-540-api-composition`; worktree:
  `/tmp/tycho-apicomposition`.
- Scope: the V02/C05 owner section `### API Composition` and the inline
  V11/C02 card `### API Composition`. Single-entry lane; no other entry,
  shared JSON, promotion or generated file is changed.
- Owner path (concatenate the three lines):

      book/volumes/v02-application-boundaries-and-contracts/
      c05-public-apis-http-rpc-and-compatibility/
      http-rpc-contracts-and-compatibility.md

- Card path:
  `book/volumes/v11-pattern-atlas/c02-api-communication/README.md`.
- The card remains inline; the integrator owns any split and `card_path`
  registration.

## Source selection

The requested source labels were the Azure API Composition pattern,
microservices.io API Composition and Microsoft API design. The exact public
pages used are:

- Microsoft, "Gateway Aggregation pattern" — the Azure Architecture Center
  composition/aggregation pattern page.
- microservices.io, "API Composition" — the existing admitted pattern page.
- Microsoft, "Web API design best practices" — used only for versioning and
  trace context.

The Azure label needs a precision note. On 2026-11-01,
`https://learn.microsoft.com/en-us/azure/architecture/patterns/api-composition`
returned HTTP 404, and the Azure Architecture Center pattern index has no
`API Composition` entry. The Azure page that describes query-time aggregation
and composition is "Gateway Aggregation pattern". This lane therefore binds the
Azure claim to that page and does not claim that a page titled "Azure API
Composition pattern" exists.

No selected page tests a composition implementation, a cross-source snapshot,
read-your-writes behavior, a sorted or paginated merged result, or a
transaction boundary.

## Source binding

### Microsoft — Gateway Aggregation pattern

- Source id: `src.microsoft-cloud-patterns` (existing).
- New record: `read.microsoft-gateway-aggregation.2026-11-01`.
- URL (concatenate the two lines):

      https://learn.microsoft.com/en-us/azure/architecture/patterns/
      gateway-aggregation

- Unit label: "Gateway Aggregation — pattern page (2026-11-01 re-read)".
- Unit type: `pattern-page`; access date 2026-11-01.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-10-05T17:33:58Z;
  `ETag` `"WKiF9ohzvwSH9wSpd+l+Ngbuvk4="`; HTTP `Date`
  2026-11-01T13:25:12Z; served HTML 62,568 bytes; `ms.date` 2026-06-02;
  page `updated_at` 2026-10-05T17:32:00Z; `git_commit_id`
  `282a7f99b9f7bba5eddfaf871124d5467e763e11`.
- Canonical text SHA-256:
  `b29c820c64a8ea1394113b5afe2152e4ff5e16551ca83fd4498d6c52f14a5f49`.
- Raw HTML SHA-256:
  `3dff76ba664fc8089dd7974e55123810bdeaf8e2994acf29ec2dc14c55f17d0a`.
- The existing `read.microsoft-gateway-aggregation.2026-10-21` record has
  `content_sha256` `8c2a339d...` and remains historical. The representation
  changed, so a new record is proposed rather than rewriting the dated record.
- Sections read: `Gateway Aggregation pattern`, `Context and problem`,
  `Solution`, `Problems and considerations`, `When to use this pattern`,
  `Workload design`, `Example`, `Next steps`, `Related resources`.
- Exact quotes used in the book:

      If one or more service calls take too long, it might be acceptable to time
      out and return a partial set of data. Consider how your application will
      handle this scenario.

      This layer becomes responsible for handling unresponsive back-end services
      gracefully and preventing failures from cascading across the aggregated
      response.

      If one of the back-end calls times out or returns an error, API Management
      can apply the behavior that best fits the operation. For example, it might
      return a partial response when missing data is acceptable, or it might fail
      the entire request when complete and consistent order data is required.
      Make this decision explicit in the policy design so that clients experience
      predictable behavior.

      The gateway shouldn't introduce service coupling across the back-end
      services.

      The gateway service might introduce a single point of failure (SPoF).

- Additional checked quotes (supporting context, not printed in the book):

      Use a gateway to aggregate multiple individual requests into a single request.

      Harden your API Management policies by using per-request timeouts,
      conditional error handling, and circuit breakers.

      With this telemetry, you can detect timeout patterns, identify which
      back-end dependency caused a partial or failed response, and create alerts
      for elevated latency or error rates.

- Limits: pattern page and API Management example only. It supports per-request
  timeouts, an explicit partial-response-or-failure choice and failure
  visibility; it does not define per-source freshness, read-your-writes,
  pagination, sorting or a transaction boundary. The quoted timeout sentence
  offers a policy choice, not an executed composition.

### microservices.io — API Composition

- Existing source id: `src.microservices-patterns`.
- Existing record: `read.microservices-api-composition.2026-10-21`.
- URL (concatenate the two lines):

      https://microservices.io/patterns/
      data/api-composition.html

- Unit label: "API Composition — pattern page".
- Unit type: `pattern-page`; record access date 2026-10-21.
- Recheck 2026-11-01: HTTP `Last-Modified` 2026-10-23T01:10:11Z; HTTP
  `ETag` `"6adab3f3-5451"`; served HTML 21,585 bytes; raw HTML digest
  `7ec014c171b2421f216c3a82ddb60af0104a2f38e6bb3af93e93c8065f04750b`
  equals the record's `content_sha256`. No new record is required.
- Sections used: `Solution`, `Resulting context`, `Related patterns`.
- Exact quotes used:

      Implement a query by defining an API Composer

      the services that own the data and performs an in-memory join of the
      results.

      Some queries would result in inefficient, in-memory joins of large
      datasets.

- Limits: pattern page only; no implementation, benchmark, failure experiment
  or freshness contract. The page does not address slow or failed participants,
  deadlines, missing parts or explicit failure.

### Microsoft — Web API design best practices

- Proposed source id: `src.microsoft-api-design` (new).
- Proposed record: `read.microsoft-api-design.2026-11-01`.
- URL (concatenate the two lines):

      https://learn.microsoft.com/en-us/azure/architecture/best-practices/
      api-design

- Unit label: "Web API design best practices — Azure Architecture Center".
- Unit type: `best-practice`; access date 2026-11-01.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-10-23T05:05:51Z;
  `ETag` `"X1y18VRn+dEvWNyEGuAgKcNXejo="`; HTTP `Date`
  2026-11-01T13:25:12Z; served HTML 102,938 bytes; `ms.date` 2025-03-27;
  page `updated_at` 2026-10-23T05:04:00Z; `git_commit_id`
  `dcf29659535a230ee4d73b812d49a6953b912430`.
- Canonical text SHA-256:
  `2891e38400bb5898d6905fed7c324f903ef76c5774da5439646fb7e0fa6face0`.
- Raw HTML SHA-256:
  `9825b790a5306510791741e08be0e4ade313a173464141cd2103311163d83b27`.
- Sections read: `Implement versioning` and `Enable distributed tracing and
  trace context in APIs`.
- Exact quotes used in the book:

      A web API that implements versioning can indicate the features and
      resources that it exposes, and a client application can submit requests
      that are directed to a specific version of a feature or resource.

      APIs that support the inclusion of trace and context information enhance
      their observability level and debugging capabilities.

- Additional checked quote (supporting context, not printed in the book):

      This approach enables tracking of requests as they flow from the client to
      back-end services. It facilitates rapid identification of failures,
      monitors latency, and maps API dependencies across services.

- Limits: API-design guidance, not a composition pattern. It supports versioning
  and trace-context claims only; it does not describe composition, partial
  failure or freshness.

## Book edits

### V02/C05 owner section

- The section now has a mechanism paragraph, a Tycho-labelled invariant
  paragraph, a failure/recovery paragraph with Azure quotes, retained
  `No snapshot` and `Query shape` paragraphs, a contract-boundary paragraph,
  a retained alternative, a limits paragraph and a source-boundary list.
- The old mechanism, invariant, failure and alternative sentences remain
  verbatim, so existing owner-unit quotes still resolve.
- The mechanism is bound to the microservices.io solution and drawback quotes.
- The invariant labels the freshness format Tycho synthesis and binds the
  partial-failure declaration to the Azure timeout/error choice.
- The failure/recovery paragraph binds per-request timeouts, the explicit
  partial-or-fail choice and the unresponsive-service context to Azure. The
  per-call deadline contract remains Tycho synthesis.
- The contract-boundary paragraph binds versioning and trace context to
  Microsoft API design; the versioned adapter and propagated trace context are
  Tycho synthesis.
- The heading stays at line 193. The page is 261 lines.
- Raw SHA-256:
  `c65b152cc6fb93934552f0ca595891768b7e2c3adfa9a48f86e6e406d74d220b`.
- Promoted BFF section: lines 125-191 plus the separating blank line, 4,962
  bytes. SHA-256 before and after:
  `0b9aeb9f06f54ca9bf269fd01c76f883e7e51cf421d0fb821dbb6815b38bc2e3`.
  The section is byte-identical.
- Full page SHA-256 changed from
  `dbfe71a035d8e47080eedfba4b4720aefdddfe7e2c92d84a9b008482d860a000`
  to the value above. The promotion record's whole-page hash therefore needs an
  integrator rebind; the BFF section hash is unchanged.

### V11/C02 inline card

- Frontmatter adds `src.microsoft-api-design` to
  `evidence_scope.source_ids`.
- **Good-fit conditions** now requires partial results and their declared
  failure behavior to be representable.
- **Failure and recovery** names the Azure timeout, conditional-error and
  partial-or-fail guidance, and labels the contract declaration Tycho
  synthesis.
- **Sources** adds the new Azure Gateway Aggregation record and the proposed
  Microsoft API design record, while retaining the microservices.io record.
- The heading moves from line 193 to 194 because of the frontmatter source id.
  The chapter page is 348 lines.
- Raw SHA-256:
  `9489d13d198b748152dfc92734a2e56fa6dd77b1efe520d809efc85219955078`.
- The BFF card block, lines 190-192, 111 bytes, SHA-256
  `86bfebd9a576a05753fc7cd07e406008b2920e53d61fccde9ab942ea7aa1daf0`,
  is unchanged.
- Card location: V11/C02 README, `### API Composition` at line 194, anchor
  `#api-composition`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was not applied to any shared
JSON. It is recorded so the integrator can bind the page text without
re-research.

### Source register `sources/register.json`

Add one source record, written as `src.` + `microsoft-api-design`, with:

- title "Web API design best practices"; category "api"; publisher "Microsoft
  Learn"; kind "best-practice"; URL and resolved URL as above; topics
  `["api", "versioning", "observability"]`; priority "supporting".
- planned use "Bounded Microsoft API-design guidance for composition endpoint
  versioning and trace context."
- admission "admitted-for-research"; access "public-web-or-author-download";
  reading status "full-public-page-inspected".
- version with the 2025-03-27 `ms.date`, 2026-11-01 access, canonical revision
  `2891e384...` and raw revision `9825b790...`.
- `access_checked` and `content_verified` 2026-11-01.
- license note "Public Microsoft Learn documentation; cite short excerpts and
  paraphrase; do not mirror."
- verification scope naming the two sections read and excluding linked pages,
  images and other sites; observed title "Web API Design Best Practices -
  Azure Architecture Center | Microsoft Learn".

Update `src.microsoft-cloud-patterns`: append the 2026-11-01 Gateway
Aggregation re-read, canonical revision `b29c820c...` and raw revision
`3dff76ba...` to `version`, and append the re-read and hash difference to
`verification_scope`. Regenerate `sources/CATALOG.md` with
`python3 scripts/source_catalog.py`.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add two records; keep the 2026-10-21 Gateway Aggregation record historical.

- `read.microsoft-gateway-aggregation.2026-11-01` — source
  `src.microsoft-cloud-patterns`; unit label "Gateway Aggregation — pattern
  page (2026-11-01 re-read)"; the nine sections above; `content_sha256`
  `b29c820c...`; access method records the canonical and raw revisions.
- `read.microsoft-api-design.2026-11-01` — source
  `src.` + `microsoft-api-design`; unit label "Web API design best practices
  — Azure Architecture Center"; sections `Implement versioning` and `Enable
  distributed tracing and trace context in APIs`; `content_sha256`
  `2891e384...`; access method records the canonical and raw revisions.

Set `updated` to 2026-11-01.

### Source plan `edition/patterns/source-plan.v1.json`

Append two units to `tycho.pattern.api-composition`:

- `src.microsoft-cloud-patterns`: unit "Gateway Aggregation — pattern page
  (2026-11-01 re-read)", type `pattern-page`, the Gateway Aggregation URL,
  the nine sections, status `read`, record
  `read.microsoft-gateway-aggregation.2026-11-01`.
- `src.microsoft-api-design`: unit "Web API design best practices — Azure
  Architecture Center", type `best-practice`, the API design URL, the two
  sections, status `read`, record `read.microsoft-api-design.2026-11-01`.

Keep the existing microservices.io unit. Replace the entry notes with the
bounds text above. Set `updated` to 2026-11-01 and recompute summary counters.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.api-composition`:

- Keep `technical_owner.state` and `coverage.technical` at
  `partial-bounded` until the owner-unit metadata and card registration are
  complete; then the integrator may set them to `sufficient` for a promotion
  pass.
- Add the Gateway Aggregation re-read and Microsoft API design units to
  `source_units`.
- Update `notes` to record the 2026-11-01 Azure and Microsoft binding and the
  Tycho-synthesis labels; retain `no promotion`.
- Keep `review_status` `self-checked`.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.api-composition`:

- Keep `owner.line` at 193.
- Mechanism: keep `supported`; binding remains microservices.io
  `read.microservices-api-composition.2026-10-21`, section `Solution`,
  quote "Implement a query by defining an API Composer", revision
  `7ec014c1...`.
- Invariant: propose `supported`; keep the owner quote
  "The composed response must declare per-source freshness and what partial
  failure means, rather than presenting one aggregate result as uniformly
  current."; binding Microsoft `read.microsoft-gateway-aggregation.2026-11-01`,
  section `Example`, quote "Make this decision explicit in the policy design so
  that clients experience predictable behavior.", revision `b29c820c...`;
  reason states that Azure supports the explicit partial-response-or-failure
  choice while the freshness format remains Tycho synthesis.
- Failure/recovery: propose `supported`; keep the owner quote
  "One slow or failed participant must not silently disappear from the result;
  apply per-call deadlines, mark missing parts or fail the composition
  explicitly."; binding Microsoft
  `read.microsoft-gateway-aggregation.2026-11-01`, section `Problems and
  considerations`, quote "If one or more service calls take too long, it might
  be acceptable to time out and return a partial set of data. Consider how your
  application will handle this scenario.", revision `b29c820c...`; supporting
  bindings for the unresponsive-service context, the partial-or-fail choice and
  the trace-context quote; reason separates the source-supported policy choices
  from the Tycho per-call deadline contract.
- Alternative: keep `supported`; binding remains microservices.io
  `Related patterns`, quote "The CQRS pattern is an alternative solution",
  revision `7ec014c1...`.
- `source_support`: record `read.microsoft-gateway-aggregation.2026-11-01`,
  source `src.microsoft-cloud-patterns`, unit type `pattern-page`, status
  `read`, `card_citation` true. Auxiliary: the microservices.io record and
  the proposed `read.microsoft-api-design.2026-11-01`.
- `technical_coverage`: proposed `sufficient` after all four dimensions are
  bound; `decision_coverage` remains `partial-bounded` unless a separate
  decision review changes it.
- `notes`: record the 2026-11-01 binding and the Tycho labels; retain
  `no promotion`.

### Card registration `edition/patterns/card-batches.v1.json`

Set `ledger_record` to `read.microsoft-gateway-aggregation.2026-11-01` and
add `card_path: "book/volumes/v11-pattern-atlas/c02-api-communication/README.md"`.
The card remains inline; no split is performed.

### Promoted BFF rebind

The page edit changes the whole owner-page hash. The BFF section itself is
byte-identical. The integrator must rebind
`tycho.pattern.backend-for-frontend-bff` `owner_page_sha256` from
`dbfe71a0...` to `c65b152c...`. The BFF card hash is unchanged because the
dedicated card is untouched. Record the section hash above as the proof that
only the API Composition section changed; do not describe this as a format-only
rebind of the BFF content.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-11-01 and authorization
"API Composition invariant and failure/recovery source binding; no promotion or
owner acceptance." Record the owner and card historical-view hashes from the
integrator's content-revision process.

### Derived artifacts and tests

The book edit changes one canonical page and one atlas chapter. Coverage and
atlas validators may fail on stale derived hashes until the affected route
index, atlas coverage/census, reverse-map, sufficient-workflow and
semantic-audit artifacts are regenerated once at batch end. The full unit suite
is not run here; batch-end tests remain with the integrator.

## Validation

Baseline checker output before the edits, in the lane worktree:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

After the two book edits only:

- `python3 scripts/check_markdown_line_length.py` — PASS; 145 exact owner-link
  exceptions.
- `python3 scripts/check_boundary.py` — PASS; one reviewed-media file
  skipped.
- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_registry.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_owner_units.py` — FAIL
  `owner-units-promotion-owner-hash: tycho.pattern.backend-for-frontend-bff`
  because the shared promotion record still pins the old whole-page hash. The
  BFF section hash is unchanged; the integrator rebind is described above.
- `python3 scripts/validate_book_metadata.py` — FAIL unknown source ID
  `src.microsoft-api-design` in the card frontmatter; integrator register
  work.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.api-composition` — FAIL: invariant and failure/recovery still
  report `partial` and `card_path` is absent because shared metadata is
  unchanged. These are integrator metadata work, not lane content failures.

The quote-to-source check in this lane compared every quoted sentence above
with the fetched canonical page text after whitespace normalization and
link-boundary space normalization. The Azure quotes with a trailing link
boundary (`circuit breakers .`) are recorded without the artificial space; the
lane note does not use that quote in the book text. No full test suite was run.

## Limits

The binding uses one Azure pattern page, one public pattern page and one
Microsoft API-design page. The Azure page is titled "Gateway Aggregation
pattern", not "API Composition pattern"; it describes a gateway or aggregation
service and an API Management example, not a general-purpose composer. It
supports per-request timeouts, partial-result-or-failure choices and failure
visibility; it does not test an implementation or define a freshness protocol.
Microsoft API design supports versioning and trace context only. The
microservices.io page supports the in-memory join and its inefficiency
drawback, not failure handling or freshness.

The owner section and card label the freshness format, per-call deadline
contract, versioned adapter, trace propagation, query-shape limits and
transaction boundary as Tycho synthesis. The `invariant` state is proposed as
`supported` only because the page explicitly separates the Azure-supported
partial-failure choice from the Tycho freshness format; a reviewer that requires
the whole invariant sentence to be source-quoted should treat the dimension as
partial instead.

Coverage remains lane-local. Independent review, promotion, owner acceptance,
CI and merge permission are not claimed.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer should
  check quote-to-claim fit for the invariant and failure/recovery bindings, the
  Tycho-synthesis labels, the Azure Gateway Aggregation substitution for the
  requested Azure API Composition label, the absent shared metadata, and the
  BFF section hash preservation.
- The reviewer must use read-only repository access and must not run tests.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path above;
- `book/volumes/v11-pattern-atlas/c02-api-communication/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
