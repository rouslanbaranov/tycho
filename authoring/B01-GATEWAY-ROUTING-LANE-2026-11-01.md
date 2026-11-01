# B01 — Gateway Routing invariant and alternative lane

Status: lane-local book edit, self-checked on 2026-11-01. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and failure/recovery were supported;
invariant and alternative were partial. This lane binds the two partial
dimensions to public Azure Gateway Routing, Kubernetes Ingress and Gateway API,
and Envoy HTTP routing pages. The four-layer route decomposition and the
alternative-choice rule are labelled Tycho synthesis. The promoted Health
Endpoint Monitoring section stays byte-identical. The Gateway Routing card
remains inline in V11/C02.

## Lane coordinates

- Parent HEAD: `77d3fca1238f0af7cf77146863a46af2416beb1e` (`77d3fca1`).
- Branch: `feature/TYCHO-540-gateway-routing`; worktree:
  `/tmp/tycho-gateway-routing`.
- Scope: the owner section `### Gateway Routing` in V08/C08 and the inline
  V11/C02 card `### Gateway Routing`. Single-entry lane; no other entry,
  shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v08-delivery-deployment-and-recovery/
      c08-network-request-paths-routing-and-edge-delivery/
      routing-and-health.md

- Card path:
  `book/volumes/v11-pattern-atlas/c02-api-communication/README.md`.
- The task brief names an "inline V11/C08 card". The Gateway Routing card is
  `### Gateway Routing` in V11/C02; V11/C08 is the distributed-coordination
  chapter and has no gateway-routing card. This lane edits the V11/C02 card
  and no other card.
- Current source register: `src.microsoft-cloud-patterns`,
  `src.kubernetes` and `src.envoy` are admitted. No new source id is
  proposed.

## Candidate evaluation

- Azure, "Gateway Routing pattern" (retained, selected). Supplies the single
  endpoint, encapsulated instance registration, appropriate-instance routing,
  the simple-application boundary and the single-point-of-failure and
  bottleneck warnings. The 2026-10-21 record remains the binding record.
- Kubernetes, "Ingress" (selected). Supplies the outside-to-Service route,
  the Service-to-Pod membership definition, host/path matching, the default
  backend and the LoadBalancer/NodePort alternatives.
- Kubernetes, "Gateway API" (selected). Supplies the Gateway address, the
  DNS-to-Gateway mapping, Host-header matching, the Service IP or
  EndpointSlices representation and the request-flow order.
- Envoy, "HTTP routing" (selected). Supplies the
  route-to-upstream-cluster-to-host sequence and the edge reverse-proxy and
  service-mesh forms.
- Envoy, "Service discovery" (examined, not selected). Its existing record
  covers discovery types and membership; it does not cover the route layer.
- Kubernetes, "Configure Liveness, Readiness and Startup Probes" (examined,
  not selected). It is the health entry's binding, not routing evidence.
- Azure, "Related resources" (examined, not selected). It names Backends for
  Frontends but does not state that a BFF is preferable.
- Kubernetes, "Service" concept page (not read). The Ingress page's
  Terminology gives the scoped Service definition used here.

## Source binding

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. The binding revision for the new records is the SHA-256 of the raw
served HTML; the main-region text digest is a second, human-inspectable
representation digest. The Azure retained record is the exception described
below.

### Azure — Gateway Routing pattern (retained)

- Source id: `src.microsoft-cloud-patterns` (existing).
- Retained record: `read.microsoft-gateway-routing.2026-10-21`.
- Binding revision: `content_sha256`
  `c2c7ecda427fb76fa98431ccfab5aa20c610e1fc9d2485293625da7e2b435b4f`.
- URL:
  `https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-routing`.
- Unit label: "Gateway Routing — pattern page"; unit type `pattern-page`;
  access date 2026-10-21.
- 2026-11-01 verification fetch: HTTP 200, 56,152 bytes, HTTP Date
  2026-11-01T14:45:28Z, Last-Modified 2026-09-19T05:02:53Z, ETag
  `"A71iEG9zmwSX2GKMzzdn3zW+zJs="`; raw HTML SHA-256
  `eee2c71dc344b966259e77b4ea94c9fbd86554ab7150a99a207ad49c01cbee4b`;
  reading-width text 8,829 characters, SHA-256
  `13bdf6f76a4cae0874070d4e53065d83350c3cdb420f3c3545872aabb417bd9f`.
  The raw digest differs from the retained record's content digest; the two
  use different representations, and no byte-identity with the 2026-10-21
  fetch is claimed. The retained record remains the binding revision and is
  not replaced.
- Sections used: "Solution", "Multiple instances of the same service",
  "Issues and considerations", "When to use this pattern".
- Exact source sentences:

      Place a gateway in front of a set of applications, services, or
      deployments. Use application Layer 7 routing to route the request to the
      appropriate instances.

      The complexity of registering and unregistering service instances is
      encapsulated in the gateway.

      This pattern might not be suitable when you have a simple application
      that uses only one or two services.

      The gateway service can introduce a single point of failure.

      The gateway service can introduce a bottleneck.

- Limits: one vendor pattern page; it states design guidance, not an
  implementation, benchmark or proof that an alternative is preferable. The
  page does not name client-side discovery or BFF as alternatives.

### Kubernetes — Ingress

- Source id: `src.kubernetes` (existing).
- Proposed record: `read.k8s-ingress.2026-11-01`.
- Proposed `content_sha256` (raw HTML):
  `43cd6851dcbfb321feee973e676f9c2b6369cdc328a3b4d1279a0c779e7cd688`.
- URL:
  `https://kubernetes.io/docs/concepts/services-networking/ingress/`.
- Unit label: "Ingress — Kubernetes documentation"; unit type
  `documentation-page`; access date 2026-11-01.
- Representation: HTTP 200, 588,103 bytes, HTTP Date 2026-11-01T14:46:09Z,
  ETag `"474762a44bf7b72cb9e4f860c7898de4-ssl"`, no Last-Modified header;
  page text "Last modified November 24, 2025"; raw HTML SHA-256 as above;
  main-region text 24,031 characters, SHA-256
  `3a93496eea49f462a0d3e3ca6b69e4b3da16f1062da6be5bd592536ecca965b7`.
- Sections used: "Terminology", "What is Ingress?", "Ingress rules",
  "DefaultBackend", "Alternatives".
- Exact source sentences:

      An API object that manages external access to the services in a cluster,
      typically HTTP.

      Ingress exposes HTTP and HTTPS routes from outside the cluster to
      services within the cluster.

      Traffic routing is controlled by rules defined on the Ingress resource.

      A Kubernetes Service that identifies a set of Pods using label
      selectors.

      Both the host and path must match the content of an incoming request
      before the load balancer directs traffic to the referenced Service.

      If none of the hosts or paths match the HTTP request in the Ingress
      objects, the traffic is routed to your default backend.

      You can expose a Service in multiple ways that don't directly involve the
      Ingress resource:

      Use Service.Type=LoadBalancer

      Use Service.Type=NodePort

- Limits: one concept page; no cluster, Ingress controller or Service was
  exercised. The page's Service definition is scoped to this guide; the
  separate Service concept page was not read. The "Alternatives" list is
  short and does not mention client-side discovery or a BFF.

### Kubernetes — Gateway API

- Source id: `src.kubernetes` (existing).
- Proposed record: `read.k8s-gateway-api.2026-11-01`.
- Proposed `content_sha256` (raw HTML):
  `309a8a58019953a763e9eb7f6251cdde02772aab8b4b3e7acc42a5bdd7ccc3ff`.
- URL:
  `https://kubernetes.io/docs/concepts/services-networking/gateway/`.
- Unit label: "Gateway API — Kubernetes documentation"; unit type
  `documentation-page`; access date 2026-11-01.
- Representation: HTTP 200, 523,753 bytes, HTTP Date 2026-11-01T14:46:10Z,
  ETag `"580f2c7f1f0fe2aebdea3ac849d9a7ce-ssl"`, no Last-Modified header;
  page text "Last modified August 19, 2026"; raw HTML SHA-256 as above;
  main-region text 10,248 characters, SHA-256
  `bab366dacd9d1c30f5c1a1a0a147c04dcd342727bc92815bce28c7124eb6994d`.
- Sections used: "Resource model", "HTTPRoute", "Request flow".
- Exact source sentences:

      Defines HTTP-specific rules for mapping traffic from a Gateway listener
      to a representation of backend network endpoints.

      For a Service backend, an implementation may represent the backend
      network endpoint as a Service IP or the backing EndpointSlices of the
      Service.

      The client's DNS resolver queries for the destination name and learns a
      mapping to one or more IP addresses associated with the Gateway.

      The client sends a request to the Gateway IP address; the reverse proxy
      receives the HTTP request and uses the Host: header to match a
      configuration that was derived from the Gateway and attached HTTPRoute.

      Lastly, the reverse proxy forwards the request to one or more backends.

- Limits: one concept page; no Gateway or HTTPRoute was applied. The request
  flow is an example for a Gateway implemented as a reverse proxy; other
  implementations may differ.

### Envoy — HTTP routing

- Source id: `src.envoy` (existing).
- Proposed record: `read.envoy-http-routing.2026-11-01`.
- Proposed `content_sha256` (raw HTML):
  `d16659a8025833f15c330a33909c59f29b2de1de5b262993e42d63e23725491c`.
- URL:
  `https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_routing`.
- Unit label: "HTTP routing — Envoy documentation"; unit type
  `documentation-page`; access date 2026-11-01.
- Representation: HTTP 200, 60,629 bytes, HTTP Date 2026-11-01T14:46:10Z;
  no Last-Modified header and no ETag; page title
  "HTTP routing — envoy 1.41.0-dev-0573fc documentation"; raw HTML SHA-256
  as above; main-region text 12,150 characters, SHA-256
  `bd4c77c60570b0d46c5e2bb169d0b32296d2d772a95e64b2c2f7d6436b7dacc8`.
- Sections used: "HTTP routing", "Route table".
- Exact source sentences:

      This is useful both for handling edge traffic (traditional reverse proxy
      request handling) as well as for building a service to service Envoy
      mesh (typically via routing on the host/authority HTTP header to reach a
      particular upstream service cluster).

      At a high level the router takes an incoming HTTP request, matches it to
      an upstream cluster, acquires a connection pool to a host in the upstream
      cluster, and forwards the request.

      Map domains/authorities to a set of routing rules.

- Limits: one architecture overview page under a rolling `latest` URL; the
  title pins a development version, but the page is not a configuration or a
  test. No proxy was configured or exercised, and the page's scoped-routing
  no-match note was not used.

## Tycho synthesis

The four-layer separation is Tycho's framing. Azure supports the single
endpoint and encapsulated registration; Kubernetes supports the route-to-Service
layer and the Pod membership view; Gateway API supports the DNS-to-Gateway
address, the Host match and the Service IP/EndpointSlices representation; Envoy
supports the route-to-cluster-to-host sequence. No selected page states all
four layers together, and no page states the trace-emission rule.

The alternative-choice rule is Tycho guidance. Azure supports the
simple-application boundary and the single-point-of-failure and bottleneck
warnings; Kubernetes supports the LoadBalancer/NodePort simpler exposure; Envoy
supports the edge reverse-proxy and service-mesh forms. The page's list of
client-side discovery and BFF alternatives, and the preference rule itself, are
not source-quoted.

The mechanism sentence and the failure/recovery sentence are unchanged; their
existing bindings remain in place.

## Book edits

### Owner section

- Frontmatter is unchanged, including `updated_at` 2026-10-30,
  `evidence_scope`, `content_review`, `source_inspection_date` and
  `content_verified_at`.
- The mechanism paragraph is unchanged.
- The second paragraph is labelled **Invariant and route decomposition
  (Tycho synthesis)**. The existing invariant quote and the failure/recovery
  sentence are unchanged; Azure, Kubernetes and Envoy phrases are added.
- The third paragraph is labelled **Alternative (Tycho comparison)**. The
  existing alternative quote is unchanged; Azure, Kubernetes and Envoy
  phrases are added; the preference rule and the client-side discovery and BFF
  alternatives are labelled Tycho guidance.
- A **Sources and limits** paragraph names the four records and states that
  the pages do not measure this page's route table or prove a preference.
- `### Gateway Routing` stays at line 169; `## Health endpoint monitoring`
  stays at line 93. The page is 217 lines after the edit (191 before).
- Raw SHA-256: before
  `e3cde1049de14b0adacde48be48e9329dd618a75414d238cb95be0c5a55461c4`;
  after
  `9dadb2b6bda7beea9becd974359d3c382f1a7c93ddc5a92a2d6befff1977757a`.
- Promoted Health Endpoint Monitoring section, lines 93-156 (no trailing
  blank): 4,805 bytes, SHA-256
  `11354d292cb829daac166c638ebb31fd2c344183472f87085ccb93ad89f0ea70`
  before and after.
- The same range with the separator blank line (lines 93-157): 4,806 bytes,
  SHA-256
  `1a4f9e8b28e11852ac073476908fe83033dd837c5166f40a63304b9ab338139b`
  before and after.

### V11/C02 inline card

- Frontmatter is unchanged.
- **Good-fit conditions** add the separability of route selection, service
  membership and backend endpoints.
- **Competing alternative** now names direct calls, a simpler reverse proxy,
  client-side discovery and a BFF; it records Azure's simple-application and
  single-point-of-failure position, Envoy's reverse-proxy and mesh forms, and
  the Tycho choice rule.
- **Sources** adds the three proposed records; exact quotes and revisions are
  in the owner section.
- `### Gateway Routing` stays at line 82. The card page is 316 lines after
  the edit (308 before).
- Raw SHA-256: before
  `803624122e0f39680d0ab6cd52abf5a14714822b64991471653ca54b7e7235e2`;
  after
  `e08b1e91ded4fef6b8f573098e64271a4370ae4b127a60148e5829657f962d64`.
- Card headings move by +8: Gateway Aggregation 118 -> 126; Gateway
  Offloading 155 -> 163; Backend for Frontend (BFF) 190 -> 198; API
  Composition 194 -> 202; Reverse Proxy 198 -> 206; Service Discovery
  232 -> 240; Client-Side Discovery 236 -> 244; Server-Side Discovery
  272 -> 280; Asynchronous Request-Reply 276 -> 284; Gatekeeper 280 -> 288.
- If the integrator adds `src.kubernetes` to the V11/C02 frontmatter, every
  card heading moves by one more line; API Gateway becomes 79, Gateway Routing
  83 and the +8 list above becomes +9.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following changes are not in the lane commit. They were not applied here
because the lane is content-only and no shared JSON is touched.

### Reading ledger

Add three records; keep `read.microsoft-gateway-routing.2026-10-21`
unchanged.

- `read.k8s-ingress.2026-11-01` — source `src.kubernetes`; unit URL
  `https://kubernetes.io/docs/concepts/services-networking/ingress/`; label
  "Ingress — Kubernetes documentation"; type `documentation-page`;
  sections as listed above; `content_sha256`
  `43cd6851...`; access date 2026-11-01.
- `read.k8s-gateway-api.2026-11-01` — source `src.kubernetes`; unit URL
  `https://kubernetes.io/docs/concepts/services-networking/gateway/`; label
  "Gateway API — Kubernetes documentation"; type `documentation-page`;
  sections as listed above; `content_sha256`
  `309a8a58...`; access date 2026-11-01.
- `read.envoy-http-routing.2026-11-01` — source `src.envoy`; unit URL
  `https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_routing`;
  label "HTTP routing — Envoy documentation"; type `documentation-page`;
  sections as listed above; `content_sha256`
  `d16659a8...`; access date 2026-11-01.

### Source plan

Append the three units to `tycho.pattern.gateway-routing` after the Azure
unit, with the same source ids, URLs, labels, types and sections. Set each
`status` to `read`, each `read_record_id` to the matching record and each
`blocked_reason` to `null`. Replace the entry notes with the coverage text
below. Recompute `registry_sha256` and `route_index_snapshot`.

### Owner units

Entry `tycho.pattern.gateway-routing`:

- Keep `owner.line` at 169.
- Invariant: set `state` to `supported`; keep the existing quote; reason:
  Azure documents encapsulated instance registration, Kubernetes separates
  Ingress routes from a Service's Pod membership, Gateway API separates the
  Gateway address, Host match and Service IP/EndpointSlices, and Envoy
  separates route matching from the upstream cluster and host. The four-layer
  decomposition is Tycho synthesis.
  - Primary binding: Azure, `read.microsoft-gateway-routing.2026-10-21`,
    section "Multiple instances of the same service", quote "The complexity
    of registering and unregistering service instances is encapsulated in the
    gateway.", revision `c2c7ecda...`.
  - Supporting: Kubernetes Ingress, `read.k8s-ingress.2026-11-01`, section
    "Terminology", quote "A Kubernetes Service that identifies a set of
    Pods using label selectors.", revision `43cd6851...`.
  - Supporting: Kubernetes Gateway API, `read.k8s-gateway-api.2026-11-01`,
    section "HTTPRoute", quote "For a Service backend, an implementation may
    represent the backend network endpoint as a Service IP or the backing
    EndpointSlices of the Service.", revision `309a8a58...`.
  - Supporting: Envoy, `read.envoy-http-routing.2026-11-01`, section
    "HTTP routing", quote "At a high level the router takes an incoming
    HTTP request, matches it to an upstream cluster, acquires a connection
    pool to a host in the upstream cluster, and forwards the request.",
    revision `d16659a8...`.
- Alternative: set `state` to `supported`; keep the existing quote; reason:
  Azure bounds the pattern to multi-service routing and warns about a single
  point of failure and bottleneck; Kubernetes lists LoadBalancer and NodePort
  without Ingress; Envoy describes edge reverse-proxy handling and a
  service-to-service mesh. The preference rule, client-side discovery and BFF
  alternatives are Tycho guidance.
  - Primary binding: Azure, `read.microsoft-gateway-routing.2026-10-21`,
    section "When to use this pattern", quote "This pattern might not be
    suitable when you have a simple application that uses only one or two
    services.", revision `c2c7ecda...`.
  - Supporting: Azure, section "Issues and considerations", quote "The
    gateway service can introduce a single point of failure.", revision
    `c2c7ecda...`.
  - Supporting: Azure, section "Issues and considerations", quote "The
    gateway service can introduce a bottleneck.", revision `c2c7ecda...`.
  - Supporting: Kubernetes Ingress, `read.k8s-ingress.2026-11-01`, section
    "Alternatives", quote "You can expose a Service in multiple ways that
    don't directly involve the Ingress resource:", revision
    `43cd6851...`.
  - Supporting: Envoy, `read.envoy-http-routing.2026-11-01`, section
    "HTTP routing", quote "This is useful both for handling edge traffic
    (traditional reverse proxy request handling) as well as for building a
    service to service Envoy mesh", revision `d16659a8...`.
- Set `technical_coverage` to `partial-bounded`.
- Set `decision_evidence.competing_alternative` to the new card text:
  "Direct client-to-backend calls, a simpler reverse proxy, client-side
  discovery or a BFF. Azure's pattern says gateway routing may not suit a
  simple application and warns that the gateway can become a single point of
  failure; Envoy describes edge reverse-proxy handling and a service-to-service
  mesh. Reverse the choice when routing logic becomes domain logic or the
  gateway cannot observe backend health. The choice rule is Tycho guidance."
- Add the three new record/source/revision tuples to
  `source_support.auxiliary`; keep the Azure primary record.
- Set `notes` to: "Invariant and alternative bound 2026-11-01 to the Azure
  Gateway Routing page, Kubernetes Ingress and Gateway API pages, and Envoy
  HTTP routing; the four-layer route decomposition and the alternative-choice
  rule remain Tycho synthesis. Coverage partial-bounded; no promotion."
- Shared page: set `bounded_entries` from 0 to 1.
- Recompute the summary counters from artifacts; at the parent HEAD they were
  invariant 99, alternative 99, technical partial-bounded 10 and technical
  partial 48.

### Registry

For `tycho.pattern.gateway-routing`: keep `technical_owner.state`,
`atlas_owner.state` and `coverage.decision` at their current values; set
`coverage.technical` and `coverage.overall` to `partial-bounded`; append
the three source units with status `read`; replace `notes` with the coverage
text above; keep `review_status` `self-checked`. Do not claim promotion or
sufficient coverage.

### Card and chapter frontmatter

- Add `src.kubernetes` to the V11/C02 chapter
  `evidence_scope.source_ids`. `src.envoy` and
  `src.microsoft-cloud-patterns` are already declared. This is required by
  the card preflight; it moves every V11/C02 card heading by one line.
- `card-batches.v1.json` needs no `card_path` change: the card remains
  inline. The existing `ledger_record` stays
  `read.microsoft-gateway-routing.2026-10-21`.
- Do not add the new source ids to the owner page `evidence_scope`; the
  enrichment manifest pins that list, and the owner body uses record ids.

### Promotion record caution

The health entry's promotion record in
`edition/patterns/sufficient-promotions.v1.json` carries
`owner_page_sha256`
`e3cde1049de14b0adacde48be48e9329dd618a75414d238cb95be0c5a55461c4`,
which is the before-page hash. The whole page changes, so that field no longer
matches. The promoted section bytes are unchanged (hashes above). This lane
does not update the promotion record and does not claim a review, a
format-only rebind or a promotion. Resolving the page-level hash belongs to the
integrator and the applicable review process.

### Derived artifacts

The owner page and the V11/C02 chapter page change. The atlas manifest
V11/C02 `sha256`, content revisions, route index, page census and other
derived artifacts need the normal batch-end refresh. No generated file is in
the lane commit.

## Validation

- `python3 scripts/check_markdown_line_length.py` — PASS; 145 exact
  owner-link exceptions.
- `python3 scripts/check_boundary.py` — PASS; one hash-pinned reviewed media
  file skipped.
- All new and edited prose lines are at or below 100 characters. The page
  retains pre-existing long frontmatter, link, table and promoted-section
  lines; the promoted section is byte-identical and was not reformatted.
- The four owner-unit dimension quotes from the parent HEAD are still
  verbatim in the owner section after whitespace normalization.
- The new source sentences above were checked against the 2026-11-01 fetched
  pages after whitespace normalization.
- The health section hash is identical before and after (both ranges above).
- `git diff --check` passes.
- `python3 scripts/validate_pattern_cards.py` — PASS; 11 batches, 145
  entries.
- `python3 scripts/validate_pattern_owner_units.py` — expected FAIL
  `owner-units-alternative: tycho.pattern.gateway-routing` until the
  integrator applies the owner-unit patch above. The card field and the
  shared decision-evidence field are intentionally out of sync in the lane
  tree; this is metadata work, not a content defect.
- The source-plan and registry validators also require the integrator patch;
  they were not run here and no pass is claimed.

## Limits

The binding uses four public pages. They describe route decomposition, service
membership, simpler exposure forms and reverse-proxy mechanics. None measures
this page's route table, observes a gateway in operation, proves that one
alternative is preferable or establishes one no-match behavior across
products. The alternative's client-side discovery and BFF list and the
four-layer decomposition are Tycho synthesis. The Azure retained record's
content digest and the 2026-11-01 raw digest differ; only the quoted text is
verified, not byte-identity. The Kubernetes pages are rolling documentation;
the Ingress page predates this lane by about a year and the Gateway API page
by about two months. The Envoy URL is a rolling `latest` page whose title identifies a
development version. No independent review, CI, owner acceptance or promotion
is claimed.

## Review needs

- The book/atlas independent review gate applies to the changed owner page and
  card. A fresh external reviewer should check quote-to-claim fit for both
  dimensions, the Tycho labels for the four-layer decomposition and the
  alternative-choice rule, the four revisions, the card and owner-page
  together, the promoted-health byte-identity claim and the metadata patch.
- The reviewer must use read-only repository access and must not run tests.
- No review is performed by this lane.

## Commit scope

The lane commit contains this note, the owner page and the V11/C02 card only.
No shared JSON, promotion, test or generated file is in the lane commit.
