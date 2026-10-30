# B25 — API Gateway invariant and failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and alternative were supported;
invariant and failure/recovery were partial. This lane binds both dimensions
to public AWS API Gateway, Azure API Management and microservices.io pages.
Bypass and total-backend-outage consequences remain Tycho analysis because the
selected pages do not test them. The metadata patch was exercised in a detached
scratch copy: preflight passes 1/1, owner units, registry, cards, sources,
book metadata, directory migration and enrichment all pass. The patch is not in
the lane commit; promotion is not claimed or ready.

## Lane coordinates

New source ids are written below as `src.` + `aws-api-gateway` and
`src.` + `azure-api-management`. The split keeps these unregistered ids out
of the `sources` and `authoring` Markdown source-reference scan until the
integrator register patch is applied.

- Parent HEAD: `e369709c` ("feat(research): promote Scatter-Gather").
- Branch: `b25-api-gateway`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b25-api-gateway`.
- Scope: the V08/C08 owner section `## API Gateway` and the inline V11/C02
  card `### API Gateway`. Single-entry lane; no other entry, shared owner
  page, promotion or generated file is changed.
- Owner path (concatenate the three lines):

      book/volumes/v08-delivery-deployment-and-recovery/
      c08-network-request-paths-routing-and-edge-delivery/
      gateway-boundaries-and-offloading.md

- Card path: `book/volumes/v11-pattern-atlas/c02-api-communication/README.md`.
- The card remains inline; the integrator owns any split and `card_path`
  registration.

## Candidate evaluation

- AWS API Gateway Developer Guide, two pages: "Throttle requests to your REST
  APIs for better throughput in API Gateway" and "Set up a stage for a REST API
  in API Gateway". Selected for throttle/quota 429 behavior, best-effort
  targets, stage snapshots and redeploy-before-effective configuration. The
  pages do not discuss gateway bypass or a total backend-blocking outage.
- Azure API Management, four pages: "Authentication and authorization to APIs
  in Azure API Management", "Self-hosted gateway overview", "Azure API
  Management policy reference - rate-limit" and "Azure API Management policy
  reference - quota". Selected for backend-scoped token pass-through,
  gateway-scoped validation, documented delegation, fail-static configuration
  behavior, rate-limit 429 and quota 403 behavior and quota lag after a
  platform restart.
- microservices.io, "API Gateway / Backends for Frontends". The existing
  `read.microservices-api-gateway.2026-10-21` record remains valid: the
  current raw HTML digest `e94bf7ae...` equals the record's
  `content_sha256`. Reused for the single-entry-point and gateway-security
  statements; not read as a new unit.
- No other candidate was selected. No page supports "gateway bypass" or "an
  outage blocks every backend" as an observed failure; those remain Tycho
  consequences of the single-entry-point contract.

## Source binding

### AWS API Gateway — throttle page

- Proposed source id: `src.` + `aws-api-gateway` (new).
- Proposed record: `read.aws-api-gateway-throttling.2026-10-30`.
- URL (concatenate the two lines):

      https://docs.aws.amazon.com/apigateway/latest/developerguide/
      api-gateway-request-throttling.html

- Unit label: "Throttle requests to your REST APIs for better throughput in API
  Gateway".
- Unit type: `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-10-30T01:52:40Z.
- Canonical text SHA-256:
  `23e9755e061ae48b18e74d385adb1360d1d58782bdb0dd6dc745423dcc656ae1`.
- Raw HTML SHA-256:
  `8aef7e6bdada50f51aba2fbdbb7dbe5433a2ad9f194672570265b65535030a0f`.
- Sections read: `Overview` (the untitled introduction),
  `How throttling limit settings are applied in API Gateway`,
  `Account-level throttling per Region`.
- Exact quotes used:

      When request submissions exceed the steady-state request rate and burst
      limits, API Gateway begins to throttle requests. Clients may receive
      `429 Too Many Requests` error responses at this point.

      Both throttles and quotas are applied on a best-effort basis and should
      be thought of as targets rather than guaranteed request ceilings.

- Limits: REST API throttling page only; no HTTP API, WebSocket API, usage
  plan quotas or counter-store failure behavior is read. The page states that
  throttles and quotas are best-effort, not that gateway enforcement is
  unavailable.

### AWS API Gateway — stage page

- Proposed source id: `src.` + `aws-api-gateway` (new).
- Proposed record: `read.aws-api-gateway-stages.2026-10-30`.
- URL (concatenate the two lines):

      https://docs.aws.amazon.com/apigateway/latest/developerguide/
      set-up-stages.html

- Unit label: "Set up a stage for a REST API in API Gateway".
- Unit type: `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET; HTTP `Last-Modified` 2026-10-30T01:52:45Z.
- Canonical text SHA-256:
  `f3be77f63ce31d681ae6b8206e28ff6909822786c40dfd2183950223e4ced97b`.
- Raw HTML SHA-256:
  `20f10d32054277440fa05f6afeaf9891d888cc6cbce2b5a87f98b07c71b2da71`.
- Sections read: `Overview` (the introduction), `Create a new stage`,
  `Modify stage settings`.
- Exact quotes used:

      A stage is a named reference to a deployment, which is a snapshot of the
      API.

      Redeploy your API for the new settings to take effect.

- Limits: REST API stage page only. It supports deployment snapshots and the
  need to redeploy after a settings change; it does not define route
  precedence, rollback or canary failure behavior.

### Azure API Management — authorization overview

- Proposed source id: `src.` + `azure-api-management` (new).
- Proposed record: `read.azure-api-management-authorization.2026-10-30`.
- URL (concatenate the two lines):

      https://learn.microsoft.com/en-us/azure/api-management/
      authentication-authorization-overview

- Unit label: "Authentication and authorization to APIs in Azure API
  Management".
- Unit type: `documentation-page`; access date 2026-10-30.
- Page dates: `ms.date` 2025-09-25; displayed "Last updated on"
  2025-09-30; HTTP `Last-Modified` 2026-08-23T22:13:13Z.
- Canonical text SHA-256:
  `15f91d50adc65357c092f4d9ae874a9eea8ccdc74dc415a4d5d01e48e57805ad`.
- Raw HTML SHA-256:
  `5a21d353321dc9c7cb3e5775988b9dc88910e57d108ff8f9b982dc0375a1905e`.
- Sections read: `Authentication versus authorization`, `OAuth flow`,
  `OAuth 2.0 authorization scenarios in API Management`,
  `Scenario 1 - Client app authorizes directly to backend`,
  `Scenario 2 - Client app authorizes to API Management`,
  `Scenario 3: API Management authorizes to backend`,
  `Client side options`, `Service side options`.
- Exact quotes used:

      The access token's scope is between the calling application and backend
      API.

      Azure API Management then acts as a "transparent" proxy between the
      caller and backend API and passes the token through unchanged to the
      backend.

      The scope of the access token is between the calling application and the
      API Management gateway.

      the user or client app delegates backend authentication and
      authorization to API Management.

- Limits: the page documents authorization arrangements and token scopes, not
  object-level authorization or a rule that the gateway must not own backend
  policy. The resource-owner enforcement rule is labelled Tycho guidance.

### Azure API Management — self-hosted gateway overview

- Proposed source id: `src.` + `azure-api-management` (new).
- Proposed record:
  `read.azure-api-management-self-hosted-gateway.2026-10-30`.
- URL (concatenate the two lines):

      https://learn.microsoft.com/en-us/azure/api-management/
      self-hosted-gateway-overview

- Unit label: "Self-hosted gateway overview".
- Unit type: `documentation-page`; access date 2026-10-30.
- Page dates: `ms.date` 2025-09-30; displayed "Last updated on"
  2026-02-22; HTTP `Last-Modified` 2026-10-22T17:17:11Z.
- Canonical text SHA-256:
  `2fb2f8b28185086345b4813b433195cdaac8f93fc9cc22268781bcd1e0370d53`.
- Raw HTML SHA-256:
  `0d9cf1e588b82b93636266d5ec4e86d65c826f69eaa2e97c819617b5aab54551`.
- Sections read: `Connectivity to Azure`, `Connectivity failures`.
- Exact quotes used:

      When connectivity to Azure is lost, the self-hosted gateway is unable to
      receive configuration updates, report its status, or upload telemetry.

      Running self-hosted gateways continue to function by using an in-memory
      copy of the configuration.

      When connectivity is restored, each self-hosted gateway affected by the
      outage automatically reconnects with its associated API Management
      instance and downloads all configuration updates that occurred while the
      gateway was offline.

- Limits: self-hosted gateway only, not the managed gateway. The page supports
  fail-static behavior and delayed configuration updates; it does not call the
  retained configuration stale or define a route-versioning rule.

### Azure API Management — rate-limit policy

- Proposed source id: `src.` + `azure-api-management` (new).
- Proposed record: `read.azure-api-management-rate-limit.2026-10-30`.
- URL (concatenate the two lines):

      https://learn.microsoft.com/en-us/azure/api-management/
      rate-limit-policy

- Unit label: "Azure API Management policy reference - rate-limit".
- Unit type: `documentation-page`; access date 2026-10-30.
- Page dates: `ms.date` 2026-08-18; displayed "Last updated on"
  2026-08-19; HTTP `Last-Modified` 2026-08-23T22:13:20Z.
- Canonical text SHA-256:
  `048897863df1f50803bf4f2e56491a2ed09489e2840123e88a34e3e1a86825f7`.
- Raw HTML SHA-256:
  `83f3e07930cddf1f5ef2f53520367230d3da6f90ea3caab19f6ef367953ede04`.
- Sections read: `Limit call rate by subscription`.
- Exact quotes used:

      When the call rate is exceeded, the caller receives a 429 Too Many
      Requests response status code.

      Because of the distributed nature of throttling architecture, rate
      limiting is never completely accurate.

- Limits: policy reference only. The page documents the 429 response and
  inaccuracy; it does not document a counter-store outage.

### Azure API Management — quota policy

- Proposed source id: `src.` + `azure-api-management` (new).
- Proposed record: `read.azure-api-management-quota.2026-10-30`.
- URL (concatenate the two lines):

      https://learn.microsoft.com/en-us/azure/api-management/
      quota-policy

- Unit label: "Azure API Management policy reference - quota".
- Unit type: `documentation-page`; access date 2026-10-30.
- Page dates: `ms.date` 2026-08-18; displayed "Last updated on"
  2026-08-19; HTTP `Last-Modified` 2026-08-23T22:13:14Z.
- Canonical text SHA-256:
  `f002b56b84263bb0b3b9dc99de6eac7560de290fa274878d388187a83bd394dc`.
- Raw HTML SHA-256:
  `736c9102c53047ba3cdd273cb6036786a423be665bf2d30e8387875ebdee97fa`.
- Sections read: `Set usage quota by subscription`.
- Exact quotes used:

      When the quota is exceeded, the caller receives a 403 Forbidden response
      status code, and the response includes a Retry-After header whose value
      is the recommended retry interval in seconds.

      When underlying compute resources restart in the service platform, API
      Management might continue to handle requests for a short period after a
      quota is reached.

- Limits: policy reference only. The page documents a 403 response and a
  bounded post-restart overrun; it does not define a shared counter store or
  per-tenant fairness rule.

### microservices.io — API Gateway / Backends for Frontends

- Existing source id: `src.microservices-patterns`.
- Existing record: `read.microservices-api-gateway.2026-10-21`.
- URL (concatenate the two lines):

      https://microservices.io/patterns/
      apigateway.html

- Unit label: "API Gateway / Backends for Frontends".
- Unit type: `pattern-page`; record access date 2026-10-21.
- Recheck 2026-10-30: HTTP `Last-Modified` 2026-10-23T01:10:11Z; raw HTML
  digest `e94bf7ae68567226222138dc2836247873d5908b63bf07ca05207377a9999d4d`
  equals the record's `content_sha256`. The current
  `scripts/source_content_hash.py` digest is
  `8059c1ca9319b1e674a74b30d13d7c21bf60f46852108d790490c2bfaf117609`
  because that script's fallback includes page chrome; this is not a content
  change. No new record is required.
- Sections read: `Solution`, `Variation: Backends for frontends`,
  `Resulting context`, `Related patterns` (existing record).
- Exact quotes used:

      Implement an API gateway that is the single entry point for all clients.

      The API gateway might also implement security, e.g. verify that the
      client is authorized to perform the request

      The API Gateway may authenticate the user and pass an Access Token
      containing information about the user to the services

- Limits: pattern page only; no implementation, benchmark or failure
  experiment. The page calls the gateway a single entry point and a moving
  part; it does not state that a bypass or gateway outage blocks every
  backend.

## Book edits

### V08/C08 owner section

- The frontmatter keeps its existing source ids because new ids cannot be
  declared before the source register is updated. Review and update dates are
  2026-10-30; the reviewer is "Automated authoring agent". The
  `source_inspection_date` stays 2026-10-20 because the enrichment manifest
  pins that value for this page; the 2026-10-30 inspection is recorded in the
  body Source boundary.
- The mechanism paragraph is retained. The old failure/alternative paragraph
  is replaced by:
  - **Invariant and delegation** with the four Azure authorization quotes and
    two microservices.io quotes above, then a Tycho guidance sentence for the
    resource-owning boundary.
  - **Failure and recovery** with the AWS stage, Azure connectivity, AWS
    throttle, Azure rate/quota and microservices.io single-entry quotes, then
    Tycho labels for bypass and total-backend outage.
  - **Alternative** retaining the existing BFF/service-mesh/direct-exposure
    sentence and the microservices.io BFF variation quote.
- Enforcement and Limits are retained without changing their technical
  meaning. A Source boundary list records the seven canonical revisions.
- Heading `## API Gateway` stays at line 73. The page is 216 lines.
- Raw SHA-256:
  `7b7a653d702d690c85754f2df0b7f1a9b12cbb09826d460d05c7064aec743298`.
- Historical-view SHA-256:
  `ff3d2e97b0a88702fef3c2d8b83c5946b655ee0661a4ca27870cc8d8a1998b66`.

### V11/C02 inline card

- Frontmatter review, update and inspection dates are 2026-10-30.
- **Failure and recovery** now names the AWS stage, redeploy, throttling and
  429 statements, the Azure 429/403 and quota-lag statements and the
  self-hosted last-configuration behavior, then labels bypass and total
  outage as Tycho analysis.
- **Sources** retains the microservices.io record citation and names the AWS
  and Azure pages, pointing to the owner section for exact quotes, sections
  and revisions.
- `### API Gateway` stays at line 74. The chapter page is 407 lines.
- Raw SHA-256:
  `fc497d3d5ff8946ff6b5dad0f8d1bda12948b718cd1d0cfed51a8fb00ad40b39`.
- Historical-view SHA-256:
  `7fec455b18bbc2157d5e6efe17f05cc040403353065e78834813e5ade86236a4`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was exercised in a detached
scratch copy of this worktree with the two book files and the register, ledger,
source-plan, registry, owner-unit, card and content-revision updates. The
scratch results are in the Validation section; no scratch file is part of the
lane commit.

### Source register `sources/register.json`

Add two source records; both are public official documentation and need the
usual title, publisher, URL, topics, priority, admission, access, reading
status, version, dates, license note and verification scope fields.

- `src.` + `aws-api-gateway` — "Amazon API Gateway Developer Guide"; version string
  records the two canonical revisions and the 2026-10-30 access check;
  `access_checked` and `content_verified` 2026-10-30.
- `src.` + `azure-api-management` — "Azure API Management documentation"; version
  string records the four canonical revisions and the 2026-10-30 access
  check; `access_checked` and `content_verified` 2026-10-30.

Regenerate `sources/CATALOG.md` with `python3 scripts/source_catalog.py`
after the register change. The source count moves from 283 to 285.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add six read records. Each needs the existing schema fields, the sections
listed above, `content_sha256` equal to the canonical digest, and
`read_scope` describing the fetched public page.

- `read.aws-api-gateway-throttling.2026-10-30` — 23e9755e...
- `read.aws-api-gateway-stages.2026-10-30` — f3be77f6...
- `read.azure-api-management-authorization.2026-10-30` — 15f91d50...
- `read.azure-api-management-self-hosted-gateway.2026-10-30` — 2fb2f8b2...
- `read.azure-api-management-rate-limit.2026-10-30` — 04889786...
- `read.azure-api-management-quota.2026-10-30` — f002b56b...

Keep `read.microservices-api-gateway.2026-10-21` unchanged. Its raw digest
reproduces on 2026-10-30, so no new micro record is needed.

### Source plan `edition/patterns/source-plan.v1.json`

Add the six units above to `tycho.pattern.api-gateway.required_units`, each
with its `source_id`, unit label, URL, section list, `status: "read"`,
`read_record_id` and `blocked_reason: null`. Keep the existing micro unit.
Replace the entry notes with the same bounds text proposed for the owner unit.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.api-gateway`:

- Set `technical_owner.state` and `coverage.technical` to
  `partial-bounded`; the owner-unit technical derivation becomes
  `partial-bounded` once invariant is supported.
- Keep `atlas_owner.state` and `coverage.decision` at `partial-bounded`;
  set `coverage.overall` to `partial-bounded`.
- Add `source_units` entries for `src.` + `aws-api-gateway` and
  `src.` + `azure-api-management` with status `read`.
- Replace `notes` with: "Invariant and failure/recovery bound 2026-10-30 to
  Azure API Management authorization and connectivity pages, AWS API Gateway
  stage and throttle pages, and the microservices.io single-entry statement;
  bypass and total-backend outage remain Tycho analysis. Coverage
  partial-bounded; no promotion."
- Keep `review_status` `self-checked`. The registry pattern entry has no
  `updated_at` field in the current schema; do not add one.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.api-gateway`:

- Keep `owner.line` at 73.
- Invariant:
  - `state`: `supported`.
  - `quote`: "Keep resource authorization at the boundary owning the resource,
    with documented delegation if a central decision service is used."
  - `reason`: Azure documents backend-scoped pass-through, gateway-scoped
    validation and explicit delegation of backend authorization; the
    resource-owner enforcement rule is Tycho guidance.
  - `binding`: `src.` + `azure-api-management`, record
    `read.azure-api-management-authorization.2026-10-30`, section
    "Scenario 3: API Management authorizes to backend", quote "the user or
    client app delegates backend authentication and authorization to API
    Management.", revision 15f91d50...
  - Supporting bindings: Scenario 1 quote "The access token's scope is between
    the calling application and backend API."; Scenario 2 quote "The scope of
    the access token is between the calling application and the API Management
    gateway."; microservices.io `Solution` quote "The API gateway might also
    implement security, e.g. verify that the client is authorized to perform
    the request"; microservices.io `Related patterns` quote "The API Gateway
    may authenticate the user and pass an Access Token containing information
    about the user to the services".
- Failure/recovery:
  - `state`: `supported`.
  - `quote`: "Gateway bypass, configuration drift, a stale route, a rate-limit
    or quota failure and an outage that blocks every backend are common."
  - `reason`: AWS documents stage snapshots, redeploy-before-effective
    settings, best-effort throttles and 429 responses; Azure documents
    fail-static configuration, delayed updates, 429 rate-limit, 403 quota and
    post-restart quota lag. Bypass and total-backend outage are Tycho
    consequences, not provider observations.
  - `binding`: `src.` + `azure-api-management`, record
    `read.azure-api-management-self-hosted-gateway.2026-10-30`, section
    "Connectivity failures", quote "When connectivity to Azure is lost, the
    self-hosted gateway is unable to receive configuration updates, report its
    status, or upload telemetry.", revision 2fb2f8b2...
  - Supporting bindings: AWS stages `Overview` snapshot quote; AWS stages
    `Modify stage settings` redeploy quote; AWS throttle `Overview` 429 and
    best-effort quotes; Azure rate-limit `Limit call rate by subscription`
    429 quote; Azure quota `Set usage quota by subscription` 403 and lag
    quotes; microservices.io `Solution` single-entry quote.
- `source_support.auxiliary`: add the six new source/record/revision tuples
  listed in the reading-ledger section.
- `technical_coverage`: `partial-bounded`.
- `notes`: "Invariant and failure/recovery bound 2026-10-30 to Azure, AWS
  and microservices.io public pages; bypass and total-backend outage remain
  Tycho analysis. Coverage partial-bounded; no promotion."

Summary counters: `invariant_supported` 64 -> 65;
`failure_recovery_supported` 55 -> 56; `technical_partial_bounded`
20 -> 21; `technical_partial` 86 -> 85. No other counter changes from this
entry.

Shared-page line shifts in the same file: `tycho.pattern.gateway-aggregation`
101 -> 158; `tycho.pattern.gateway-offloading` 117 -> 174;
`tycho.pattern.reverse-proxy` 134 -> 191. The API Gateway heading stays at 73.
The shared-page record for this page keeps `pattern_count` 4 and
`dedicated_units` 4, but `bounded_entries` moves from 2 to 3 because API
Gateway now has partial-bounded technical coverage.

### Card registration `edition/patterns/card-batches.v1.json`

The entry still has no `card_path`. Register the inline chapter path
`book/volumes/v11-pattern-atlas/c02-api-communication/README.md`; the two
source ids in that chapter's frontmatter make the card 409 lines and move
`### API Gateway` from line 74 to 76. Alternatively split the card and set
the split path. A split must keep both new source ids, the 2026-10-30 dates and
the owner anchor `api-gateway`. No split is performed by this lane.

### Frontmatter source ids (after register update)

- V11/C02 chapter frontmatter `evidence_scope.source_ids`: add
  `src.` + `aws-api-gateway` and `src.` + `azure-api-management`; the card's
  `Sources` field cites both and preflight requires the binding sources in
  this declaration. Keep the existing `src.microservices-patterns`
  declaration.
- Owner page `evidence_scope.source_ids`: do **not** add the two ids in this
  patch. The enrichment manifest's `new_documents` record for this page pins
  the exact list to `src.http-semantics` and
  `src.owasp-rest-enrichment`; adding ids without updating that manifest
  raises `enrichment-source-drift`. The owner body Source boundary is the
  binding record for the new sources. A later enrichment-manifest update can
  add the ids, but it must also move `## API Gateway` from line 73 to 75,
  shift the other shared-page headings by two, and recompute the owner
  content-revision hash.

### Content revisions `edition/content-revisions.json`

Add issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B25 API Gateway source binding".

- `directory_documents`:
  - owner path previous
    `25f134dfd900707f90b42b7785fc5a987f16a060090cce247b7ddb53a1b3842d`
    (migration baseline), current
    `ff3d2e97b0a88702fef3c2d8b83c5946b655ee0661a4ca27870cc8d8a1998b66`
    (historical-view text after link rewriting).
  - card path previous
    `aae986266f0a3b93e2711c8a33f9026c6e68413cd6fab37e03fefa5cceb27e3f`
    (migration baseline), current
    `87a17f6f4ac4e1ea23ecacdb35c7a600c3c0b649dafca5a343eccddcaca438f0`
    (historical-view text after the two source ids are added to the chapter
    frontmatter). The lane-tree card hash without those ids is
    `7fec455b18bbc2157d5e6efe17f05cc040403353065e78834813e5ade86236a4`;
    use that only if the integrator chooses a split card with its own
    frontmatter instead of the inline chapter path.
- `enrichment_documents`:
  - owner **enrichment key** path
    `book/volumes/v08/c08/gateway-boundaries-and-offloading.md` (the old path
    in `edition/enrichment-manifest.json`, not the current path), previous
    `c62562445f531b633b53cfb924c4e1f013326375d03e6fb58dccdba61aabb511`
    (enrichment manifest baseline), current
    `ff3d2e97b0a88702fef3c2d8b83c5946b655ee0661a4ca27870cc8d8a1998b66`.
  - The card is not an enrichment new document; no card enrichment revision.
- Leave `source_blocks`, `enrichment_additions` and
  `enrichment_baselines` empty. The owner page is retained and no page split
  is performed.

### Derived artifacts and tests

The book edit changes one canonical page and one atlas chapter. Update or
regenerate the affected route index, atlas coverage/census, reverse-map,
sufficient-workflow and semantic-audit artifacts at batch end. Do not treat a
stale derived count or hash as a lane content failure.

## Validation

At the parent HEAD:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

After the two book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS; V11 prose <=100,
  145 exact owner-link exceptions.
- `python3 scripts/check_boundary.py` — PASS; independent-origin review still
  required.
- `python3 scripts/validate_book_metadata.py` — PASS; 479 canonical
  documents.
- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_sources.py` — PASS; 283 source records.
- `python3 scripts/validate_pattern_registry.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_owner_units.py` — FAIL
  `owner-units-quote-not-verbatim: tycho.pattern.api-gateway:
  failure_recovery` because shared metadata is unchanged.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.api-gateway` — FAIL: invariant partial, failure/recovery
  partial and `card_path` missing; all three are integrator metadata work.
- `python3 scripts/validate_directory_migration.py` — FAIL
  `directory-baseline-payload-drift` until the content revision is applied.
- `python3 scripts/validate_enrichment.py` — FAIL
  `enrichment-new-document-drift` until the enrichment-document revision is
  applied.

In the detached scratch copy with the metadata patch above, including the two
source ids in the V11/C02 chapter frontmatter and no owner-page source ids:

    PASS: tycho.pattern.api-gateway
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: 479 canonical documents
    PASS: 285 source records, mandatory IDs, cross-references and catalogue
    freshness
    PASS: directory migration; 479 canonical documents, 339 moved documents,
    12 post-migration directories
    PASS: enrichment; explicit membership and byte conservation

The scratch card with the two source ids is 409 lines and moves
`### API Gateway` from line 74 to 76; the owner page stays 216 lines with
`## API Gateway` at line 73. Derived atlas, coverage and semantic-audit
artifacts still need regeneration after the metadata patch. The lane does not
run the full suite; batch-end tests remain with the integrator.

## Limits

The binding uses seven public documentation units. The AWS and Azure pages
describe vendor behavior and policy semantics; they do not test a local
gateway, a bypass path, a counter-store outage or a total backend-blocking
outage. The microservices.io page is a pattern reference, not an
implementation or benchmark. All such consequences are labelled Tycho
analysis in the owner section and card.

Coverage remains partial-bounded after the proposed metadata patch.
Independent review, promotion, owner acceptance and merge permission are not
claimed. The historical record that this entry was 2/4 and that both
dimensions were partial is retained in the pilot batch records.

## Review needs

- Request a fresh external review under the book/atlas gate. Historical
  API Gateway reviews predate this text; this lane is self-checked only.
- The reviewer should check quote-to-claim fit for the invariant and for each
  failure mode, the Tycho labels for bypass and total outage, the REST/self-
  hosted scope limits, the seven revisions and the shared-page line shifts.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- owner path above;
- `book/volumes/v11-pattern-atlas/c02-api-communication/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
