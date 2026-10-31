# B65 — Tenant-Based Resource Isolation mechanism, invariant and recovery lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 1/4 at the parent HEAD: alternative was supported; mechanism,
invariant and failure/recovery were partial. This lane binds the three partial
dimensions using four public sources (six units): AWS Well-Architected SaaS
Lens, *Tenant Isolation*, *Pool isolation* and *Preventing cross tenant
access*; Kubernetes, *Multi-tenancy*; PostgreSQL 18.6, *Row Security Policies*;
and Microsoft Learn, *Architectural approaches for a multitenant solution*.
The card is inline in V11/C09 and this lane edits that block. Label Tycho.

## Lane coordinates

- Parent HEAD: 54017a004a471d72070b72b0b60cb56f135ef1a0 (54017a00).
- Lane label: Tycho.
- Branch: b65-tenant-isolation; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b65-tenant-isolation.
- Scope: the owner section "Tenant-Based Resource Isolation" in V09/C05, the
  inline "Tenant-Based Resource Isolation" card in V11/C09, and this note.
  Single-entry lane; no other entry, shared JSON, promotion or generated file
  is changed.
- Owner path (concatenate):

      book/volumes/v09-observability-security-and-operations/
      c05-identity-authorization-and-threat-modeling/multitenant-isolation.md

- Inline card path:
  book/volumes/v11-pattern-atlas/c09-scalability/README.md.
- Exactly three files change: the owner page, the inline card host and this
  note.
- Existing source ids: src.microsoft-multitenant, src.kubernetes,
  src.postgresql, src.owasp-rest-enrichment.
- New source id proposed: src.aws-saas-lens.
- New ledger records proposed: six, listed below.
- Retained historical record: read.batch5-ms-multitenant.2026-10-21, kept as
  the earlier Deployment Stamps context and not the current binding.
- Baseline and final line-length and boundary checks pass.

## Card location

The registry records atlas_owner.chapter = V11/C09 and section
tenant-based-resource-isolation for this pattern, and card-batches.v1.json
records no card_path. The C09 chapter landing already contains the card body,
so this lane edits that inline block rather than creating a dedicated page.
The chapter frontmatter evidence_scope.source_ids and notes are updated because
they describe the cards hosted by that page; the registry, card batches and
atlas manifest are left for the integrator. Precedent: B38, B53, B59, B60,
B61, B62, B63 and B64 edited inline card hosts and their chapter source lists
the same way.

The task coordinates named "inline card V11/C11". That does not match the
registry for tycho.pattern.tenant-based-resource-isolation: the registry entry
at edition/patterns/registry.v1.json lines 5890-5927 records
technical_owner.anchor = tenant-based-resource-isolation and
atlas_owner.chapter = V11/C09, and card-batches.v1.json lines 1086-1093
records owner_anchor = tenant-based-resource-isolation with no card_path.
V11/C11 contains a different inline card, "Multitenant Isolation" (README line
100), and the dedicated card page
book/volumes/v11-pattern-atlas/c11-security-operations/multitenant-isolation.md
serves tycho.pattern.multitenant-isolation, whose owner anchor is
multitenant-isolation-1. Editing V11/C11 would cross entries and change a
second pattern's card. This lane therefore edits V11/C09 and records the
discrepancy; if the integrator intended V11/C11, redirect the card edit before
applying the proposed metadata.

## Baseline and gap

edition/patterns/owner-units.v1.json records mechanism as partial, invariant as
partial, failure_recovery as partial and alternative as supported. The recorded
reasons are:

- mechanism: "External review 2026-10-27: binding does not support the full
  owner claim." Its binding is read.batch5-ms-multitenant.2026-10-21, section
  "Deployment Stamps pattern".
- invariant: "External review 2026-10-27: binding does not support the full
  owner claim."
- failure_recovery: "External review 2026-10-27: binding does not support the
  full owner claim."
- alternative: "Contrasts a shared pool with tenant predicates against
  dedicated resources." Its binding is read.batch5-ms-multitenant.2026-10-21,
  section "Deployment Stamps pattern", quote "You can also apply the Deployment
  Stamps pattern to create multitenant stamps. This approach supports resource
  sharing and reduces infrastructure costs.", revision
  7703a01de01a5465ab16eafbaa61e8d797064032152d0f12b3b0fc8931dbb56f.

The entry records technical_coverage partial, decision_coverage partial-bounded
and review_state self-checked. The entry does not carry a separate
external-review verdict, so this lane does not claim one.

The base owner page is 109 lines, 535 words, SHA-256
909b0a90cda4e289076682d0c25bab57b6b423ea8bbf2a0e50ee5025e29b582c. The base
owner subsection (lines 71-88) is 18 lines, 167 words, SHA-256
ade3c4f6377b416a65d834e08c3222d2fdb9e0ab5872a9172c237b6eaec8fe25. The base
chapter landing is 341 lines, 1,515 words, SHA-256
3861f82caf8e10ee7ac7951a2165eb84470b1b1f46e79399efe1467f80753a30. The base
card block (lines 284-315) is 32 lines, 148 words, SHA-256
1827617a8d2490a97e4c5b93e9aa3a2a9a54e9e865c552416556590c154af85c.

The final owner page is 177 lines, 1,304 words, SHA-256
d827073fc12bf0520daffb2e0d8ca48e2c8872dcd44f1dd10e12c10c8b5e5bd9. The final
owner subsection (lines 75-156) is 82 lines, 955 words, SHA-256
320a370f892a698fc71461749b9d47b5d4b580d34109b27da3240193d7d960a7. The final
chapter landing is 352 lines, 1,624 words, SHA-256
83dd6517fe72a68e34991efb557e036b6925e733f320d06ff9e06d943ab1f467. The final
card block (lines 289-326) is 38 lines, 235 words, SHA-256
77595802d223ebbfbbd491e2e8cf7f778d55472f6ae81da05c4f19175ccc84e1.

The gap was evidential. The owner page and card already stated the bounded
share, the no-crossing rule, the shared-cache/worker hazard and the shared-pool
alternative as Tycho guidance, but no exact public quote, section and
representation hash bound those claims. Shared metadata still shows 1/4 and
partial-bounded until the integrator applies the proposals below.

The lane narrows five claims. First, the AWS SaaS Lens *Tenant Isolation* page
states the cross-tenant boundary principle and its severity; it does not
enumerate query, cache, queue or credential paths, and it prescribes no quota.
Second, the AWS *Pool isolation* page describes shared compute and storage and
records noisy-neighbour and all-tenant outage consequences; it does not
prescribe a cache key or worker partition. Third, the Kubernetes *Multi-tenancy*
page documents namespaces, RBAC, quotas, network/storage/node isolation and
sandboxing, but treats "hard" and "soft" multi-tenancy as a spectrum and warns
that quotas cannot protect network traffic. Fourth, PostgreSQL row security
enforces per-user row visibility and default-deny for queries, but superusers
and BYPASSRLS roles bypass it, table owners bypass it by default, and TRUNCATE
and REFERENCES are not subject to it. Fifth, the Microsoft Learn page is a
section overview; its Deployment Stamps comparison is exact, but
service-specific implementation pages were not read. The cache/worker and queue
scoping and the Tycho runbook are synthesis, labelled in the owner section.

## Candidate evaluation

- AWS SaaS Lens, *Tenant Isolation* (selected). States that each tenant must be
  prevented from accessing another tenant's resources and that crossing the
  boundary is potentially unrecoverable. Primary source for the boundary
  invariant.
- AWS SaaS Lens, *Pool isolation* (selected). Describes shared compute and
  storage, the loss of ordinary networking and IAM boundaries, noisy-neighbour
  impact and all-tenant outage scope. Primary source for mechanism context and
  failure/recovery.
- AWS SaaS Lens, *Preventing cross tenant access* (selected). Documents a
  pooled serverless execution role, runtime tenant scoping, JWT-supplied tenant
  context and tenant-scoped credentials, and warns that isolation moves into
  function code. Supporting source for mechanism and failure/recovery.
- Kubernetes, *Multi-tenancy* (selected). Documents namespaces, RBAC, quotas,
  limits, network policies, storage classes and claims, sandboxing, node
  isolation, API priority and fairness, and namespace versus virtual-control-
  plane implementations. Primary source for mechanism and failure/recovery.
- PostgreSQL 18.6, *Row Security Policies* (selected). Defines per-user row
  policies, default-deny, per-row evaluation, superuser/owner/BYPASSRLS
  bypass, whole-table exceptions, the row_security parameter and policy race
  conditions. Primary source for the query-path invariant and supporting source
  for failure/recovery.
- Microsoft Learn, *Architectural approaches for a multitenant solution*
  (selected). Frames shared versus isolated resources across compute, storage
  and data, networking and identity, and contrasts single-tenant and
  multitenant Deployment Stamps. Primary source for the alternative.
- AWS SaaS Lens, *Noisy Neighbor* (considered, not bound). Its short page
  restates the capacity-theft hazard; the pool-isolation page carries the exact
  noisy-neighbour and scope-of-impact sentences used here.
- AWS SaaS Lens, *Silo isolation* (considered, not bound). The pool-isolation
  page and the Microsoft Deployment Stamps section carry the alternative
  comparison; a separate silo unit would duplicate it.
- Kubernetes, *Resource quotas* (considered, not bound). The multi-tenancy page
  section "Quotas" carries the exact quota, limit and fairness statements used
  here.
- PostgreSQL, *CREATE POLICY* (considered, not bound). The row-security page
  includes the policy syntax, examples and bypass caveats needed for this
  entry.
- Azure service-specific compute, storage and networking pages (considered, not
  bound). The selected overview frames the choice; linked implementation pages
  were not read.
- Vendor tutorials and third-party summaries (considered, not bound). They are
  not primary documentation for these claims and would add unverified
  restatements.

No Kubernetes cluster, database, cloud tenant, cache or worker was configured,
and no cross-tenant test or failure drill was run.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31 (UTC), twice per
representation. Raw bytes were hashed from the served decompressed body. HTTP
dates are UTC. Where a page served a Markdown alternate, this lane read that
alternate and records both the human page URL and the representation used.

Canonical extraction for HTML: select the div with id docContent for PostgreSQL
and the second div with class content under main for Microsoft Learn; remove
script, style, nav, footer and header elements and elements with class navheader
or navfooter; convert block tags to newlines; strip remaining tags; decode
entities; normalize non-breaking spaces, typographic quotes and dashes to
ASCII; collapse space runs and blank lines; strip. Markdown alternates are
normalized only for line endings, trailing whitespace and repeated blank lines.
Character counts include spaces and newlines; word counts split on whitespace.
Quoted fragments below were checked against the canonical text after whitespace
normalization.

### R1 — AWS SaaS Lens, *Tenant Isolation*

- Record: read.aws-saas-lens-tenant-isolation.2026-10-31 (proposed).
- Source: src.aws-saas-lens (proposed).
- URL: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-isolation.html
- Representation used: the AWS-served Markdown alternate,
  https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-isolation.md
- Label/type: "Tenant Isolation — SaaS Lens"; official documentation.
- Representation: HTTP/1.1 200 on 2026-10-31T23:20:52Z on both fetches;
  1,239-byte Markdown, 646 transferred bytes; Last-Modified
  Fri, 30 Oct 2026 22:43:11 GMT; ETag "QjE385J4Xif8tU3HZyxIikzZHjM=-gzip";
  raw Markdown SHA-256
  9a6607615ced3b0dfa2f1dff772efd4c2b77b863c7b03232fc533c408ecf74a3 on both
  fetches. Canonical text 1,231 characters / 186 words, SHA-256
  35f895c1980a949a664bde8685a514cd85c34342a72346bd381d9c5b1eb9ae91.
- Sections read: the full page, including the shared-infrastructure framing,
  the cross-tenant access statement and the effectively-isolated-constructs
  conclusion.
- Sections not read: linked pages, images; no AWS environment was configured.
- Claims supported: Q12-Q14.
- Limits: a short framing page; it states no quota mechanism, cache key,
  worker partition or recovery procedure. It describes intended provider
  guidance, not a benchmark.

### R2 — AWS SaaS Lens, *Pool isolation*

- Record: read.aws-saas-lens-pool-isolation.2026-10-31 (proposed).
- Source: src.aws-saas-lens (proposed).
- URL: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.html
- Representation used: the AWS-served Markdown alternate,
  https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.md
- Label/type: "Pool isolation — SaaS Lens"; official documentation.
- Representation: HTTP/1.1 200 on 2026-10-31T23:22:06Z on both fetches;
  6,468-byte Markdown, 2,614 transferred bytes; Last-Modified
  Fri, 30 Oct 2026 22:43:10 GMT; ETag "IrcZPCehearoWeiwBHw/mLUQv5s=-gzip";
  raw Markdown SHA-256
  d68d4fcf00a8e10e72851cc64927fc38e5eca7a4d54ab037837c282c2f28cffe on both
  fetches. Canonical text 6,418 characters / 1,025 words, SHA-256
  f3278a3291b95cf0d2fe217a4af2d86e81f4b03df6af168ef69affd312e703b0.
- Sections read: the full page, including the pool-model description, the
  networking/IAM boundary warning, "Pool model pros and cons", and the Cons
  entries "Noisy neighbor", "Tenant cost tracking", "Increased scope of
  impact" and "Compliance pushback".
- Sections not read: linked pages, images; no pooled environment was built.
- Claims supported: Q6-Q7, Q26-Q28 and Q40.
- Limits: living architecture guidance; it describes the pooled model and its
  consequences, not a cache/worker keying protocol or a measurement.

### R3 — AWS SaaS Lens, *Preventing cross tenant access*

- Record: read.aws-saas-lens-preventing-cross-tenant.2026-10-31 (proposed).
- Source: src.aws-saas-lens (proposed).
- URL (concatenate):
  https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/
  preventing-cross-tenant-access.html
- Representation used: the AWS-served Markdown alternate,
  https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/
  preventing-cross-tenant-access.md
- Label/type: "Preventing cross tenant access — SaaS Lens"; official
  documentation.
- Representation: HTTP/1.1 200 on 2026-10-31T23:22:08Z on both fetches;
  2,767-byte Markdown, 1,244 transferred bytes; Last-Modified
  Fri, 30 Oct 2026 22:43:39 GMT; ETag "a4158A/ZIzRhxtk/3UZ/2vczr6w=-gzip";
  raw Markdown SHA-256
  425fc5e0369bd14e86e1b23288d27621a1cc1bce9c20909edcf7fda1b3bdf73e on both
  fetches. Canonical text 2,751 characters / 426 words, SHA-256
  7b52f51473f2297430c24f55c9c8260206c65c008e9d5751441ab3919fe4fbc3.
- Sections read: the full page, including the silo execution-role option, the
  pooled execution-role option, the JWT/STS tenant-scoped-credential flow and
  the warning that isolation moves into function code.
- Sections not read: linked pages, images; no serverless function was deployed.
- Claims supported: Q10-Q11, Q21 and Q29.
- Limits: a serverless example, not a general cache or queue design; it
  describes intended provider guidance, not a benchmark.

### R4 — Kubernetes, *Multi-tenancy*

- Record: read.k8s-multitenancy.2026-10-31 (proposed).
- Source: src.kubernetes (existing; add this unit).
- URL: https://kubernetes.io/docs/concepts/security/multi-tenancy/
- Representation used (concatenate): the pinned website content at
  https://raw.githubusercontent.com/kubernetes/website/
  56db43a06302ec920fbd53b4f276fb0878b1a74f/content/en/docs/concepts/security/
  multi-tenancy.md
- Label/type: "Multi-tenancy — Kubernetes documentation"; official
  documentation; content commit 56db43a06302ec920fbd53b4f276fb0878b1a74f
  (2025-05-22T15:54:21Z, the latest commit for the path at fetch time).
- Representation: HTTP/2 200 on 2026-10-31T23:21:14Z and 23:21:15Z;
  29,514-byte Markdown, 10,434 transferred bytes; ETag
  W/"139234b2548b34ad31cb5796dea5a97269aa5a2d20e4925e7b9c95e76ef019c6";
  no Last-Modified; raw Markdown SHA-256
  4fa87adc3371db47420272e1219bd57742a9b5126c0d2b2b70b8738b3926c74d on both
  fetches. Canonical text 29,490 characters / 4,281 words, SHA-256
  1d535523a0692d7d656d87bcdc3efdf0d6ceb43ea02bee8a62a9149188075841.
- Sections read: the full page, including "Use cases", "Terminology",
  "Isolation", "Control plane isolation" (Namespaces, Access controls,
  Quotas), "Data Plane Isolation" (Network isolation, Storage isolation,
  Sandboxing containers, Node Isolation), "Additional Considerations" and
  "Implementations" (Namespace per tenant, Virtual control plane per tenant).
- Sections not read: linked pages, images; no cluster was created.
- Claims supported: Q1-Q5, Q18-Q20, Q22-Q25,
  Q38-Q39, Q42-Q43 and Q44.
- Limits: configuration guidance, not a guarantee; "hard" and "soft"
  multi-tenancy are a spectrum; quotas cannot protect network traffic; node
  isolation still shares the kubelet and API service.

### R5 — PostgreSQL 18.6, *Row Security Policies*

- Record: read.postgres-rowsecurity.2026-10-31 (proposed).
- Source: src.postgresql (existing; add this unit).
- URL: https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- Label/type: "PostgreSQL 18: 5.9. Row Security Policies"; official
  documentation, PostgreSQL 18.6.
- Representation: HTTP/2 200 on 2026-10-31T15:41:35Z on both fetches;
  31,248-byte HTML; no Last-Modified or ETag served; raw HTML SHA-256
  9a68f1a82568a8421f3d8973dde5061607020f1a4de50699c9b6eb002111a8fa on both
  fetches. Canonical text 15,764 characters / 2,431 words, SHA-256
  7121afa0bff4b9a94f7f1a547fc5856b83ac6152566f1bd859c28f74f46b8364.
- Sections read: the full page, including ordinary and restrictive policies,
  default-deny, per-row evaluation, superuser/BYPASSRLS/owner bypass, the
  referential-integrity caveat, the row_security parameter and the
  policy-subquery race example.
- Sections not read: linked CREATE POLICY and ALTER TABLE pages, source code,
  images; no database was configured or tested.
- Claims supported: Q15-Q17 and Q30-Q34.
- Limits: feature documentation; bypass and whole-table exceptions are
  documented, not defeated; no recovery procedure or performance measurement is
  supplied.

### R6 — Microsoft Learn, *Architectural approaches for a multitenant solution*

- Record: read.ms-multitenant-approaches.2026-10-31 (proposed).
- Source: src.microsoft-multitenant (existing; add this unit).
- URL: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/overview
- Label/type: "Architectural approaches for a multitenant solution — Azure
  Architecture Center"; official documentation.
- Representation: HTTP/2 200 on 2026-10-31T23:20:59Z and 23:21:00Z;
  51,520-byte HTML; Last-Modified Fri, 18 Sep 2026 05:05:15 GMT; ETag
  "XuBZovVSP5EQWy2v4GKeDJTbV5Y="; raw HTML SHA-256
  606fb4309ecf7e048679049265045e4b2685f9d4b744ff737d2b14ffb4b5881c on both
  fetches. Canonical article text 3,796 characters / 563 words, SHA-256
  a9575f30cd494c541772bafbeee1bc025d65c7b7ef03f19f8f1f3fd193adc4be.
- Sections read: the article body, including the shared-versus-isolated
  framing, "Deployment Stamps pattern", "Intended audience" and "Related
  resource".
- Sections not read: linked service-specific approach pages, images; no Azure
  deployment was inspected.
- Claims supported: Q8-Q9, Q35-Q37 and Q41.
- Limits: a section overview; the single-tenant and multitenant stamp
  trade-offs are stated, but service-level implementation details were not
  read.

## Selected exact quotes

Quotes reproduce the served prose after the normalization above. Typographic
apostrophes and quotation marks are ASCII in this note. Line breaks inside
quotes are reflowed and are not part of the source text. Forty-four named
passages and fragments were checked against the six canonical representations
on 2026-10-31; 44/44 were present. The owner and card use a subset; every
fragment used there was also checked. Q numbers group fragments by source and
dimension, not by page order.

### Mechanism

- Q1, R4, section "Quotas": "to manage resource usage of tenant workloads".
- Q2, R4, section "Quotas": "Quotas prevent a single tenant from consuming
  greater than their allocated share of resources".
- Q3, R4, section "Quotas": "Limits are the upper bound for the amount of
  resources that a container can consume."
- Q4, R4, section "Storage isolation": "to ensure that a PersistentVolume
  cannot be reused across different namespaces".
- Q5, R4, section "Namespaces": "helps segment a tenant's workload into a
  logical and distinct management unit".
- Q6, R2, pool-model description: "tenants are consuming infrastructure that is
  shared by all tenants".
- Q7, R2, pool-model description: "a table indexed by individual tenant
  identifiers".
- Q8, R6, article introduction: "share every resource".
- Q9, R6, article introduction: "isolated resources for every tenant".
- Q10, R3, JWT/STS flow: "tenant-scoped credentials".
- Q11, R3, JWT/STS flow: "supplied via a JWT".
- Q44, R4, section "Quotas": "a tenant cannot monopolize a cluster's
  resources or overwhelm its control plane".

### Invariant

- Q12, R1, section "Tenant Isolation": "ensure that each tenant is prevented
  from accessing another tenant's resources".
- Q13, R1, section "Tenant Isolation": "Crossing this boundary in any form
  would represent a significant and potentially unrecoverable event".
- Q14, R1, section "Tenant Isolation": "each SaaS architecture needs to ensure
  that it has put in place the constructs that are needed to ensure that each
  tenant's resources have been effectively isolated".
- Q15, R5, introduction: "on a per-user basis, which rows can be returned by
  normal queries or inserted, updated, or deleted".
- Q16, R5, introduction: "a default-deny policy".
- Q17, R5, introduction: "will be evaluated for each row prior to any
  conditions or functions coming from the user's query".
- Q18, R4, section "Access controls": "ensure that each tenant has the
  appropriate access to only the namespaces they need".
- Q19, R4, section "Access controls": "Role-based access control (RBAC) is
  commonly used to enforce authorization".
- Q20, R4, section "Network isolation": "By default, all pods in a Kubernetes
  cluster are allowed to communicate with each other".
- Q21, R3, pooled execution role: "you must apply isolation scoping at runtime
  in the implementation of your multi-tenant functions".

### Failure and recovery

- Q22, R4, section "Quotas": "Quotas cannot protect against all kinds of
  resource sharing, such as network traffic."
- Q23, R4, section "Storage isolation": "reused across different namespaces".
- Q24, R4, section "Node Isolation": "still shared services".
- Q25, R4, section "Node Isolation": "move laterally".
- Q26, R2, Cons "Noisy neighbor": "The more resources are shared, the more
  chances there are for one tenant to impact the experience of another."
- Q27, R2, Cons "Increased scope of impact": "an outage will likely impact all
  the tenants".
- Q28, R2, Cons "Increased scope of impact": "gracefully recover from
  failures".
- Q29, R3, function-code warning: "does push part of the isolation model into
  the code".
- Q30, R5, bypass rules: "always bypass the row security system".
- Q31, R5, bypass rules: "Table owners normally bypass row security as well".
- Q32, R5, whole-table operations: "are not subject to row security".
- Q33, R5, row_security parameter: "you can set the row_security configuration
  parameter to off".
- Q34, R5, row_security parameter: "throw an error if any query's results would
  get filtered by a policy".

### Alternative

- Q35, R6, "Deployment Stamps pattern": "This pattern provides the highest level
  of isolation and helps to avoid the noisy neighbor problem."
- Q36, R6, "Deployment Stamps pattern": "the noisy neighbor problem still might
  occur".
- Q37, R6, "Deployment Stamps pattern": "that infrastructure can't be shared
  with other tenants".
- Q38, R4, section "Namespace per tenant": "Namespace per tenant".
- Q39, R4, section "Virtual control plane per tenant": "Virtual control plane
  per tenant".
- Q40, R2, pool-model description: "typical networking and IAM constructs
  cannot be relied upon to create boundaries between tenants".
- Q41, R6, "Deployment Stamps pattern": "This approach supports resource
  sharing and reduces infrastructure costs".
- Q42, R4, section "Isolation": "hard" multi-tenancy.
- Q43, R4, section "Isolation": "soft" multi-tenancy.

## Dimension mapping

- Mechanism. Primary: Q2, record read.k8s-multitenancy.2026-10-31, source
  src.kubernetes, section "Quotas", revision
  1d535523a0692d7d656d87bcdc3efdf0d6ceb43ea02bee8a62a9149188075841.
  Supporting: Q1 and Q3-Q5 (namespace, quota, limits, storage class and
  claim), Q6-Q7 (shared compute and tenant-indexed storage in the AWS pool),
  Q8-Q9 (shared versus isolated resources in the Azure overview), and Q10-Q11
  (JWT-supplied context exchanged for tenant-scoped credentials). Tycho
  reading: a bounded share is a per-resource contract, not a deployment label;
  a quota the resource does not enforce is not isolation. The owner claim
  remains: "Tenant-based isolation assigns each tenant a bounded share of
  compute, storage and quota, with routing and credentials that keep the tenant
  scope explicit."
- Invariant. Primary: Q12, record read.aws-saas-lens-tenant-isolation.2026-10-31,
  source src.aws-saas-lens, section "Tenant Isolation", revision
  35f895c1980a949a664bde8685a514cd85c34342a72346bd381d9c5b1eb9ae91.
  Supporting: Q13-Q14 (boundary severity and the effectively-isolated
  constructs rule), Q15-Q17 (per-user row visibility, default-deny and per-row
  evaluation), Q18-Q20 (RBAC, namespaced access and default-allow pod
  networking), and Q21 (runtime isolation scoping for a pooled execution role).
  Tycho rule: derive the tenant from authenticated context; require it in every
  query, cache key, queue consumer and credential; enforce it centrally and
  never trust an arbitrary caller field alone. The owner claim remains: "No
  query, cache key, queue consumer or credential may cross a tenant boundary
  without an explicit shared-resource contract." Narrowing: the AWS page states
  the boundary principle but does not enumerate those four paths; PostgreSQL
  and Kubernetes bind the query and credential/network paths; cache and queue
  scoping remain Tycho synthesis.
- Failure and recovery. Primary: Q22, record
  read.k8s-multitenancy.2026-10-31, source src.kubernetes, section "Quotas",
  revision 1d535523a0692d7d656d87bcdc3efdf0d6ceb43ea02bee8a62a9149188075841.
  Supporting: Q23-Q25 (volume reuse, shared kubelet/API and lateral movement),
  Q26-Q28 (noisy-neighbour impact, all-tenant outage scope and recovery
  commitment), Q29 (isolation pushed into function code), and Q30-Q34
  (superuser/BYPASSRLS bypass, owner bypass, whole-table exceptions and the
  row_security error path). Tycho runbook: default-deny network paths between
  tenants; scope cache keys and queue partitions by tenant; partition or
  dedicate workers; set a Delete reclaim policy on shared storage classes;
  force row security where the tenant is the database principal; test indirect
  paths with a foreign tenant identifier; monitor per-tenant consumption; fail
  closed when tenant scope is missing. The owner claim remains: "A shared cache
  or background worker leaks one tenant's data or consumes another's capacity;
  scope keys by tenant and test indirect paths with a foreign identifier."
  Narrowing: no selected unit tests a cache or worker leak; the runbook is
  synthesis from the shared-resource, storage-reuse, network and bypass
  evidence.
- Alternative. Primary: Q35, record
  read.ms-multitenant-approaches.2026-10-31, source src.microsoft-multitenant,
  section "Deployment Stamps pattern", revision
  a9575f30cd494c541772bafbeee1bc025d65c7b7ef03f19f8f1f3fd193adc4be.
  Supporting: Q36-Q37 and Q41 (noisy-neighbour residual, unshareable
  infrastructure cost and resource-sharing benefit), Q38-Q39 (namespace per
  tenant versus virtual control plane per tenant), and Q40 (loss of ordinary
  networking and IAM boundaries in a pool). Tycho choice rule: use a shared
  pool only when tenant scope is enforced on every path and fairness is
  observable; move a tenant to a dedicated stamp when measured noisy-neighbour
  cost, compliance constraints or a bypass path dominates the operational
  saving. The owner claim remains: "A shared pool with tenant-scoped predicates
  is cheaper at low scale; choose dedicated resources when noisy-neighbour or
  compliance risk dominates."
- Retention and coverage. The lane proposes technical_coverage sufficient and
  decision_coverage sufficient because each of the four owner claims now has a
  bound primary passage, supporting passages, explicit limits and a narrowed
  reading. This is a self-check, not independent review or owner acceptance.

## Proposed shared metadata

The following changes are proposals only. No shared JSON is edited in this lane.

### sources/register.json

Add src.aws-saas-lens:

- title "AWS Well-Architected SaaS Lens"; observed_title "Tenant Isolation -
  SaaS Lens"; category security; publisher Amazon Web Services; kind
  official-docs; url the R1 human page; resolved_url the same; topics
  tenant-isolation, multitenancy and security; priority supporting; planned_use
  "Tenant isolation, pool isolation and serverless tenant-scoping guidance for
  the tenant-based resource isolation entry."; admission
  admitted-for-research; access public-web-or-author-download; reading_status
  full-public-page-inspected; access_checked and content_verified 2026-10-31;
  license_notes "Public architecture guidance; cite short excerpts and
  paraphrase; do not mirror."; verification_scope "SaaS Lens tenant-isolation
  topic read 2026-10-31: Tenant Isolation, Pool isolation and Preventing cross
  tenant access, each in full from its Markdown alternate; linked pages, images
  and any AWS environment were not read; no service behavior was tested.";
  version "Living documentation; three units fetched 2026-10-31.
  tenant-isolation.md 1,239 bytes, Last-Modified 2026-10-30T22:43:11Z, ETag
  QjE385J4Xif8tU3HZyxIikzZHjM=-gzip, canonical SHA-256 35f895c1....
  pool-isolation.md 6,468 bytes, Last-Modified 2026-10-30T22:43:10Z, ETag
  IrcZPCehearoWeiwBHw/mLUQv5s=-gzip, canonical SHA-256 f3278a32....
  preventing-cross-tenant-access.md 2,767 bytes, Last-Modified
  2026-10-30T22:43:39Z, ETag a4158A/ZIzRhxtk/3UZ/2vczr6w=-gzip, canonical
  SHA-256 7b52f514.... No pinned release identifier is published."

Extend src.kubernetes:

- reading_status full-public-page-inspected; access_checked and content_verified
  2026-10-31; append to version "Multi-tenancy concept page fetched 2026-10-31
  from content commit 56db43a06302ec920fbd53b4f276fb0878b1a74f; raw Markdown
  29,514 bytes, ETag W/139234b2548b34ad31cb5796dea5a97269aa5a2d20e4925e7b9c95e76ef019c6;
  no Last-Modified; canonical text 29,490 characters / 4,281 words, SHA-256
  1d535523...."; append to verification_scope "The Multi-tenancy concept page
  was read in full 2026-10-31 for namespaces, RBAC, quotas, limits, network and
  storage isolation, sandboxing, node isolation and implementations; no cluster
  was created and linked pages were not read."

Extend src.postgresql:

- access_checked and content_verified 2026-10-31; append to version "Row
  Security Policies (section 5.9) fetched 2026-10-31 on PostgreSQL 18.6;
  31,248-byte HTML; no Last-Modified or ETag; raw HTML SHA-256 9a68f1a8...;
  canonical text 15,764 characters / 2,431 words, SHA-256 7121afa0....";
  append to verification_scope "Section 5.9 Row Security Policies was read in
  full 2026-10-31 for per-user policies, default-deny, per-row evaluation,
  superuser/BYPASSRLS/owner bypass, whole-table exceptions, the row_security
  parameter and policy-subquery race conditions; no database was configured or
  tested."

Extend src.microsoft-multitenant:

- reading_status full-public-page-inspected; access_checked and content_verified
  2026-10-31; append to version "Re-fetched 2026-10-31; 51,520-byte HTML;
  Last-Modified 2026-09-18T05:05:15Z; ETag XuBZovVSP5EQWy2v4GKeDJTbV5Y=;
  raw HTML SHA-256 606fb430...; canonical article text 3,796 characters / 563
  words, SHA-256 a9575f30.... The 2026-10-21 record
  read.batch5-ms-multitenant.2026-10-21 remains historical."; append to
  verification_scope "The article body (introduction, Deployment Stamps
  pattern, Intended audience and Related resource) was read 2026-10-31; linked
  service-specific pages and images were not read."

### reading-ledger.v1.json

Add six records. All use access_date 2026-10-31, access_method "public HTTPS
GET; served representation inspected", reviewer "Automated authoring agent" and
status "read". The content_sha256 values are canonical-text hashes, matching the
revisions proposed for owner-units.

- read.aws-saas-lens-tenant-isolation.2026-10-31
  - source: src.aws-saas-lens
  - unit_url: the R1 human page
  - unit_label: AWS SaaS Lens — Tenant Isolation
  - unit_type: documentation-page
  - sections_read: the full Tenant Isolation page
  - sections_not_read: linked pages and images
  - content_sha256: 35f895c1980a949a664bde8685a514cd85c34342a72346bd381d9c5b1eb9ae91
  - characters/words: 1,231 / 186
  - claims_supported: Q12-Q14
  - claims_not_supported: quota mechanics, cache keys, worker partitions,
    recovery procedure, benchmark
  - limitations: short framing page; no environment configured.
- read.aws-saas-lens-pool-isolation.2026-10-31
  - source: src.aws-saas-lens
  - unit_url: the R2 human page
  - unit_label: AWS SaaS Lens — Pool isolation
  - unit_type: documentation-page
  - sections_read: the full page, including Pool model pros and cons
  - sections_not_read: linked pages and images
  - content_sha256: f3278a3291b95cf0d2fe217a4af2d86e81f4b03df6af168ef69affd312e703b0
  - characters/words: 6,418 / 1,025
  - claims_supported: Q6-Q7, Q26-Q28 and Q40
  - claims_not_supported: cache/worker keying, implementation behavior,
    benchmark
  - limitations: living architecture guidance; no pooled environment built.
- read.aws-saas-lens-preventing-cross-tenant.2026-10-31
  - source: src.aws-saas-lens
  - unit_url: the R3 human page (concatenated there)
  - unit_label: AWS SaaS Lens — Preventing cross tenant access
  - unit_type: documentation-page
  - sections_read: the full page, including the silo and pooled execution-role
    options and the JWT/STS tenant-scoped-credential flow
  - sections_not_read: linked pages and images
  - content_sha256: 7b52f51473f2297430c24f55c9c8260206c65c008e9d5751441ab3919fe4fbc3
  - characters/words: 2,751 / 426
  - claims_supported: Q10-Q11, Q21 and Q29
  - claims_not_supported: cache/queue design, deployed function behavior,
    benchmark
  - limitations: serverless example; no function deployed.
- read.k8s-multitenancy.2026-10-31
  - source: src.kubernetes
  - unit_url: the R4 human page; representation is the pinned content URL
  - unit_label: Kubernetes — Multi-tenancy
  - unit_type: documentation-page
  - sections_read: the full page, including Use cases, Terminology, Isolation,
    Control plane isolation, Data Plane Isolation, Additional Considerations
    and Implementations
  - sections_not_read: linked pages and images
  - content_sha256: 1d535523a0692d7d656d87bcdc3efdf0d6ceb43ea02bee8a62a9149188075841
  - characters/words: 29,490 / 4,281
  - claims_supported: Q1-Q5, Q18-Q20, Q22-Q25, Q38-Q39, Q42-Q43 and Q44
  - claims_not_supported: cache or queue isolation, a guarantee of hard
    multi-tenancy, a tested cluster
  - limitations: configuration guidance; no cluster created; quotas do not
    protect network traffic.
- read.postgres-rowsecurity.2026-10-31
  - source: src.postgresql
  - unit_url: the R5 human page
  - unit_label: PostgreSQL 18.6 — Row Security Policies
  - unit_type: documentation-page
  - sections_read: the full page, including ordinary and restrictive policies,
    bypass rules, the referential-integrity caveat and the row_security
    parameter
  - sections_not_read: linked CREATE POLICY and ALTER TABLE pages, source code
    and images
  - content_sha256: 7121afa0bff4b9a94f7f1a547fc5856b83ac6152566f1bd859c28f74f46b8364
  - characters/words: 15,764 / 2,431
  - claims_supported: Q15-Q17 and Q30-Q34
  - claims_not_supported: recovery procedure, performance measurement, tested
    database behavior
  - limitations: feature documentation; bypasses remain; no database configured
    or tested.
- read.ms-multitenant-approaches.2026-10-31
  - source: src.microsoft-multitenant
  - unit_url: the R6 human page
  - unit_label: Microsoft Learn — Architectural approaches for a multitenant
    solution
  - unit_type: documentation-page
  - sections_read: the article body, including the shared-versus-isolated
    framing, Deployment Stamps pattern, Intended audience and Related resource
  - sections_not_read: linked service-specific approach pages and images
  - content_sha256: a9575f30cd494c541772bafbeee1bc025d65c7b7ef03f19f8f1f3fd193adc4be
  - characters/words: 3,796 / 563
  - claims_supported: Q8-Q9, Q35-Q37 and Q41
  - claims_not_supported: service-specific implementation guidance, a deployed
    stamp, benchmark
  - limitations: section overview; linked implementation pages not read.

### Source plan edition/patterns/source-plan.v1.json

Replace the required_units array for tycho.pattern.tenant-based-resource-
isolation with the six units below. Each unit keeps the existing schema fields
(source_id, unit, unit_type, url, sections, status, read_record_id,
blocked_reason: null). URLs are the exact ones recorded in R1-R6 and are not
repeated here, because several exceed the 100-character line limit.

- src.aws-saas-lens — "AWS SaaS Lens — Tenant Isolation"; documentation-page;
  URL as in R1; full page; status read; record
  read.aws-saas-lens-tenant-isolation.2026-10-31.
- src.aws-saas-lens — "AWS SaaS Lens — Pool isolation"; documentation-page;
  URL as in R2; full page, including Pool model pros and cons; status read;
  record read.aws-saas-lens-pool-isolation.2026-10-31.
- src.aws-saas-lens — "AWS SaaS Lens — Preventing cross tenant access";
  documentation-page; URL as in R3; full page; status read; record
  read.aws-saas-lens-preventing-cross-tenant.2026-10-31.
- src.kubernetes — "Kubernetes — Multi-tenancy"; documentation-page; URL as in
  R4; full page; status read; record read.k8s-multitenancy.2026-10-31.
- src.postgresql — "PostgreSQL 18.6 — Row Security Policies";
  documentation-page; URL as in R5; full page; status read; record
  read.postgres-rowsecurity.2026-10-31.
- src.microsoft-multitenant — "Microsoft Learn — Architectural approaches for a
  multitenant solution"; documentation-page; URL as in R6; article body,
  Deployment Stamps pattern, Intended audience and Related resource; status
  read; record read.ms-multitenant-approaches.2026-10-31.

Proposed notes: "Four public sources (six units) bound 2026-10-31: AWS SaaS
Lens tenant isolation, pool isolation and serverless tenant scoping; Kubernetes
multi-tenancy; PostgreSQL row security; and Microsoft multitenant approaches.
The earlier Microsoft record read.batch5-ms-multitenant.2026-10-21 is retained
as historical context."

### Owner units edition/patterns/owner-units.v1.json

Keep the document id, path, heading, anchor and level. Update owner.line from
71 to 75 because four frontmatter lines were added by the source-list update.
Keep unit_kind dedicated. Consider adding unit_terms "bounded share", "tenant
boundary" and "capacity theft".

Technical evidence:

- mechanism: state supported. Claim quote unchanged: "Tenant-based isolation
  assigns each tenant a bounded share of compute, storage and quota, with
  routing and credentials that keep the tenant scope explicit." Reason:
  Kubernetes namespaces, ResourceQuotas, limits, storage classes and claims
  bound compute and storage and keep the namespace scope explicit; the AWS pool
  page describes shared compute and tenant-indexed storage; the Azure overview
  frames shared versus isolated resources; the AWS serverless example exchanges
  JWT-supplied context for tenant-scoped credentials. Primary binding: Q2,
  record read.k8s-multitenancy.2026-10-31, section "Quotas", revision
  1d535523.... Supporting: Q1, Q3-Q5 and Q44 (same record), Q6-Q7 (record
  read.aws-saas-lens-pool-isolation.2026-10-31, revision f3278a32...), Q8-Q9
  (record read.ms-multitenant-approaches.2026-10-31, revision a9575f30...), and
  Q10-Q11 (record read.aws-saas-lens-preventing-cross-tenant.2026-10-31,
  revision 7b52f514...). Tycho reading: a per-resource contract, not a
  deployment label.
- invariant: state supported. Claim quote unchanged: "No query, cache key,
  queue consumer or credential may cross a tenant boundary without an explicit
  shared-resource contract." Reason: AWS states the cross-tenant prohibition
  and its severity; PostgreSQL enforces per-user row visibility with
  default-deny and per-row evaluation; Kubernetes scopes RBAC, network and
  storage; the AWS serverless example scopes runtime credentials. Primary
  binding: Q12, record read.aws-saas-lens-tenant-isolation.2026-10-31, section
  "Tenant Isolation", revision 35f895c1.... Supporting: Q13-Q14 (same record),
  Q15-Q17 (record read.postgres-rowsecurity.2026-10-31, revision 7121afa0...),
  Q18-Q20 (record read.k8s-multitenancy.2026-10-31, revision 1d535523...), and
  Q21 (record read.aws-saas-lens-preventing-cross-tenant.2026-10-31, revision
  7b52f514...). Tycho rule: derive the tenant from authenticated context and
  enforce it centrally; the four-path enumeration and cache/queue scoping are
  synthesis.
- failure_recovery: state supported (narrowed). Claim quote unchanged: "A
  shared cache or background worker leaks one tenant's data or consumes another's
  capacity; scope keys by tenant and test indirect paths with a foreign
  identifier." Reason: Kubernetes documents network traffic and shared node
  services as residuals left by quotas and node isolation, and requires a
  Delete reclaim policy to stop volume reuse; AWS records noisy-neighbour and
  all-tenant outage consequences and asks for graceful recovery; PostgreSQL
  documents superuser, BYPASSRLS, owner and whole-table bypasses and a
  fail-closed row_security error; the AWS serverless example pushes isolation
  into function code. Primary binding: Q22, record
  read.k8s-multitenancy.2026-10-31, section "Quotas", revision 1d535523....
  Supporting: Q23-Q25 (same record), Q26-Q28 (record
  read.aws-saas-lens-pool-isolation.2026-10-31, revision f3278a32...), Q29
  (record read.aws-saas-lens-preventing-cross-tenant.2026-10-31, revision
  7b52f514...), and Q30-Q34 (record read.postgres-rowsecurity.2026-10-31,
  revision 7121afa0...). Narrowing: no selected unit tests a cache or worker
  leak; the runbook is synthesis.
- alternative: state supported. Claim quote unchanged: "A shared pool with
  tenant-scoped predicates is cheaper at low scale; choose dedicated resources
  when noisy-neighbour or compliance risk dominates." Reason: Microsoft
  contrasts single-tenant and multitenant Deployment Stamps, including the
  isolation/noisy-neighbour benefit and the unshareable infrastructure cost;
  Kubernetes frames namespace-per-tenant against virtual-control-plane-per-
  tenant; the AWS pool page records the loss of ordinary networking and IAM
  boundaries. Primary binding: Q35, record
  read.ms-multitenant-approaches.2026-10-31, section "Deployment Stamps
  pattern", revision a9575f30.... Supporting: Q36-Q37 and Q41 (same record),
  Q38-Q39 (record read.k8s-multitenancy.2026-10-31, revision 1d535523...), and
  Q40 (record read.aws-saas-lens-pool-isolation.2026-10-31, revision
  f3278a32...). Tycho choice rule: shared pool only with enforced scope and
  observable fairness; dedicated stamps when measured noisy-neighbour or
  bypass risk dominates.

Other owner-units fields:

- technical_coverage "sufficient"; decision_coverage "sufficient";
  review_state "self-checked".
- notes: "Four dimensions bound 2026-10-31 to AWS SaaS Lens tenant, pool and
  serverless isolation, Kubernetes multi-tenancy, PostgreSQL row security and
  Microsoft multitenant approaches; the cache/queue instance and quota-
  enforcement rule are Tycho synthesis; no cross-tenant test was executed;
  coverage is self-checked, not independently reviewed."
- source_support: primary ledger_record read.k8s-multitenancy.2026-10-31,
  source_id src.kubernetes, unit_type documentation-page, status read,
  card_citation true; auxiliary entries for
  read.aws-saas-lens-tenant-isolation.2026-10-31,
  read.aws-saas-lens-pool-isolation.2026-10-31,
  read.aws-saas-lens-preventing-cross-tenant.2026-10-31,
  read.postgres-rowsecurity.2026-10-31 and
  read.ms-multitenant-approaches.2026-10-31.
- decision_evidence.competing_alternative: "Shared pool with per-tenant rate
  limits, or dedicated deployment stamps. Reverse when isolation cost exceeds
  measured noisy-neighbour or compliance risk."; decision_state
  applicable-under-conditions; card_components 10; atlas_section
  tenant-based-resource-isolation.

### Registry, card batches and derived artifacts

The registry currently records technical_owner.state partial,
atlas_owner.state partial-bounded and coverage partial. After the owner-units
proposal is applied, regenerate those fields from owner-units rather than
editing them by hand. The proposed state is technical_owner.state sufficient,
atlas_owner.state sufficient and coverage technical/decision/overall
sufficient, confidence high. source_units should list the six records above.
The registry notes should say the four dimensions are self-checked and that
promotion is not part of this lane.

card-batches.v1.json needs no card_path; the card remains inline in V11/C09.
If the integrator adopts this lane, the single ledger_record should point to
read.k8s-multitenancy.2026-10-31 or keep the historical Microsoft record as an
auxiliary, not as the only binding. edition/atlas-manifest.json and generated
indexes should be regenerated by the integrator after the owner and card hashes
are final. This lane does not claim that regeneration.

## Verification

Commands run in
/Users/rbaranov/Projects/tycho-worktrees/b65-tenant-isolation:

- python3 scripts/check_markdown_line_length.py
  Result: PASS: V11 prose <=100; 145 exact owner-link exceptions.
- python3 scripts/check_boundary.py
  Result: PASS: configured lexical boundary checks; independent-origin review
  still required.
- Added-line length scan: 107 added owner/card lines; 106 are at most 100
  characters. The one longer line is the exempt Technical owner line (318
  characters, one Markdown link), which the checker classifies as an exact
  owner-link exception. The pre-existing long frontmatter and pattern-atlas
  lines outside the edited section are unchanged.
- Quote check: 44 named passages and fragments checked against the six
  canonical representations; 44/44 present after whitespace normalization.
- git status: exactly three paths, the owner page, the V11/C09 landing and this
  note.
- python3 scripts/validate_book_metadata.py
  Result: FAIL:
  book/volumes/v11-pattern-atlas/c09-scalability/README.md: unknown source ID.
  This is the expected consequence of the no-shared-JSON constraint: the
  proposed src.aws-saas-lens row is not yet in sources/register.json.
- python3 scripts/validate_knowledge.py
  Result: failed at the book-metadata step with the same unknown-source error.
  The preceding source-register, source-catalogue, public-repo-lock,
  claim-provenance, document-observations, research-checkpoint and
  strict-json-schema steps passed their own checks.

No full unit suite was run. The lane is a content slice; the batch-end suite is
the integrator's step.

## Limits

- Coverage and review are self-checked. No independent AI review, owner
  acceptance, promotion, CI result or production observation is claimed.
- The AWS SaaS Lens *Tenant Isolation* page is a short framing page. It states
  the cross-tenant boundary principle and its severity but does not enumerate
  query, cache, queue or credential paths, prescribe quotas or document a
  recovery procedure. The pool and serverless pages supply the shared-resource
  and credential context, not a cache/worker keying protocol.
- The Kubernetes *Multi-tenancy* page is configuration guidance, not a
  guarantee. It treats hard and soft multi-tenancy as a spectrum, warns that
  quotas cannot protect network traffic, and notes that node isolation still
  shares the kubelet and API service. No cluster was created.
- PostgreSQL row security is documented with its bypasses: superusers and
  BYPASSRLS roles, table owners unless FORCE ROW LEVEL SECURITY is set, and
  whole-table operations such as TRUNCATE and REFERENCES. The row_security
  error behavior was not exercised, and the page supplies no recovery
  procedure.
- The Microsoft Learn page is a section overview. Single-tenant and multitenant
  Deployment Stamps are contrasted exactly, but linked service-specific
  implementation pages were not read.
- The cache/worker and queue scoping rules, the quota-enforcement test and the
  Tycho runbook are synthesis over the selected evidence, not statements made
  by a single source.
- No cross-tenant test, benchmark, failure drill, cache experiment or
  Kubernetes, PostgreSQL, AWS or Azure configuration was performed.
- The task coordinates named V11/C11 for the inline card. The registry places
  this pattern's card in V11/C09; V11/C11 hosts a different pattern's card. If
  the integrator intended V11/C11, this lane's card edit must be redirected
  before any shared metadata is applied. See "Card location".
