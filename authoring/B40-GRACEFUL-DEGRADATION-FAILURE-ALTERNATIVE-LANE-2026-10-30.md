# B40 — Graceful degradation failure/recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and invariant were supported;
failure/recovery and alternative were partial. This lane binds both partial
dimensions to public Google SRE, AWS Builder Center and Kubernetes pages, and
labels the silent-correctness judgment, the application of autoscaling
hysteresis to a degraded mode and the alternative-choice rule as Tycho. The
card remains inline in V11/C07.

## Lane coordinates

- Parent HEAD: `4831a24eb6458253db2143bb1dc129405c66c568` (`4831a24e`).
- Branch: `b40-degradation`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b40-degradation`.
- Scope: the owner section `### Graceful Degradation` in V07/C05 and the
  inline V11/C07 card `### Graceful Degradation`. Single-entry lane; no other
  entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v07-performance-scale-and-resilience/
      c05-overload-protection-and-graceful-degradation/
      overload-admission-control-and-graceful-degradation.md

- Card path:
  `book/volumes/v11-pattern-atlas/c07-resilience/README.md`.
- Current source register: `src.sre-cascading`, `src.sre-overload` and
  `src.kubernetes` are admitted. This lane proposes two new source ids,
  `src.sre-best-practices` and `src.aws-load-shedding`.
- Baseline line-length and boundary checks pass before and after the edit.

## Candidate evaluation

- Google SRE, "Addressing Cascading Failures" (selected). Supplies the
  under-exercised degraded path, accidental activation, feedback cycles,
  monitoring and alerting, the instruction to keep a way to turn the mode off
  or tune it, and added tasks as an expedient recovery. The 2026-10-30 fetch is
  byte-identical to the retained record
  `read.batch4-sre-cascading.2026-10-21`.
- Google SRE, "Handling Overload" (selected). Supplies degraded responses as
  less accurate or less complete, the statement that a service may have no
  option but to serve errors when it cannot compute a degraded response, and
  the transparent-handling instruction. The 2026-10-30 fetch is byte-identical
  to `read.sre-overload.2026-10-21`.
- Google SRE, "A Collection of Best Practices for Production Services"
  (selected). Supplies reasonable but suboptimal overload results and the
  explicit switch to load shedding plus a consistent subset of clients
  receiving errors when degraded responses are too expensive.
- AWS, "Using load shedding to avoid overload" (selected). Supplies visibility
  instrumentation and alarms for rejected work, the false-positive concern,
  added capacity as the brownout priority, and the warning that misconfigured
  shedding can disable reactive automatic scaling.
- Kubernetes, "Horizontal Pod Autoscaling" (selected). Supplies automatic
  capacity scaling, thrashing/flapping, the comparison to hysteresis and the
  stabilization-window mechanism.
- Kubernetes, "Autoscaling Workloads" (examined, not selected). It describes
  horizontal and vertical scaling, but the HPA page binds the hysteresis and
  capacity statements more directly. The existing record remains unused by
  this lane.
- Google SRE Workbook, "Managing Load" (examined, not selected). It covers
  load balancing, autoscaling and load shedding interactions, but not a
  degraded-mode failure contract or the explicit-outage alternative.
- Kubernetes probe documentation (examined, not selected). Readiness removal
  is traffic management, not a degraded result; it belongs to the separate
  health entry.
- AWS, "Timeouts, Retries, and Backoff with Jitter" (examined, not selected).
  It supports retry amplification, not graceful degradation or the
  explicit-outage alternative.

## Source binding

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. The binding revision is the SHA-256 of the raw served HTML, the same
convention as the retained records. Source punctuation is preserved in this
note; page prose uses straight apostrophes except where a source fragment is
quoted directly.

### Google SRE — Addressing Cascading Failures

- Source id: `src.sre-cascading` (existing).
- Retained record: `read.batch4-sre-cascading.2026-10-21`.
- URL: `https://sre.google/sre-book/addressing-cascading-failures/`.
- Unit label: "Addressing Cascading Failures — public chapter"; unit type
  `book-chapter`; access date 2026-10-21.
- Representation: HTTP 200, 104,870 bytes, HTTP Date
  2026-10-30T21:36:21Z, Last-Modified Thu, 08 Oct 2026 04:48:00 GMT; raw HTML
  SHA-256
  `d67024d52d72a1254c830d3c29e6d1b2afade88e133ffcff64b94711c2aaa11a`.
  The 2026-10-30 raw digest equals the retained `content_sha256`; the record
  is not replaced.
- Sections used: "Load Shedding and Graceful Degradation"; "Immediate Steps
  to Address Cascading Failures", subsection "Increase Resources".
- Exact quotes:

      Graceful degradation shouldn’t trigger very often—usually in cases of a
      capacity planning failure or unexpected load shift. Keep the system
      simple and understandable, particularly if it isn’t used often.

      Remember that the code path you never use is the code path that (often)
      doesn’t work. In steady-state operation, graceful degradation mode won’t
      be used, implying that you’ll have much less operational experience with
      this mode and any of its quirks, which increases the level of risk.

      Monitor and alert when too many servers enter these modes.

      Complex load shedding and graceful degradation can cause problems
      themselves—excessive complexity may cause the server to trip into a
      degraded mode when it is not desired, or enter feedback cycles at
      undesired times. Design a way to quickly turn off complex graceful
      degradation or tune parameters if needed.

      If your system is running at degraded capacity and you have idle
      resources, adding tasks can be the most expedient way to recover from
      the outage. However, if the service has entered a death spiral of some
      sort, adding more resources may not be sufficient to recover.

- Limits: one book chapter; it does not measure this page's service or state
  that an explicit error is always better than a degraded result.

### Google SRE — Handling Overload

- Source id: `src.sre-overload` (existing).
- Retained record: `read.sre-overload.2026-10-21`.
- URL: `https://sre.google/sre-book/handling-overload/`.
- Unit label: "Handling Overload — complete public chapter"; unit type
  `book-chapter`; access date 2026-10-21.
- Representation: HTTP 200, 71,785 bytes, HTTP Date 2026-10-30T21:36:21Z,
  Last-Modified Thu, 08 Oct 2026 04:48:00 GMT; raw HTML SHA-256
  `945d15db67ad15a7f5e75833f8c0d014c8dc61d57909f7a3abd48459ad12cc9e`.
  The 2026-10-30 raw digest equals the retained `content_sha256`.
- Section used: "Handling Overload".
- Exact quotes:

      One option for handling overload is to serve degraded responses:
      responses that are not as accurate as or that contain less data than
      normal responses, but that are easier to compute.

      However, under extreme overload, the service might not even be able to
      compute and serve degraded responses. At this point it may have no
      immediate option but to serve errors.

      At the end of the day, it's best to build clients and backends to handle
      resource restrictions gracefully: redirect when possible, serve degraded
      results when necessary, and handle resource errors transparently when
      all else fails.

- Limits: one chapter; it states an option and a fallback, not a rule that a
  particular degraded mode is safe for every correctness contract.

### Google SRE — A Collection of Best Practices for Production Services

- Source id: `src.sre-best-practices` (proposed).
- Proposed record: `read.sre-best-practices-overload.2026-10-30`.
- URL: `https://sre.google/sre-book/service-best-practices/`.
- Unit label: "A Collection of Best Practices for Production Services —
  Google SRE book appendix"; unit type `book-chapter`; access date
  2026-10-30.
- Representation: HTTP 200, 50,907 bytes, HTTP Date 2026-10-30T21:39:43Z,
  Last-Modified Thu, 08 Oct 2026 04:48:00 GMT; raw HTML SHA-256
  `03ad19970146a1a0ed8406a60f9702af0fd5fa8470ce2c6b33846280e4f9a4be`.
  No separate version identifier.
- Section used: "Overloads and Failure".
- Exact quotes:

      Services should produce reasonable but suboptimal results if overloaded.

      For times when load is high enough that even degraded responses are too
      expensive for all queries, practice graceful load shedding, using
      well-behaved queuing and dynamic timeouts; see Handling Overload. Other
      techniques include answering requests after a significant delay
      (“tarpitting”) and choosing a consistent subset of clients to receive
      errors, preserving a good user experience for the remainder.

- Limits: one appendix under CC BY-NC-ND 4.0; it does not define which
  degraded result preserves a correctness contract.

### AWS — Using load shedding to avoid overload

- Source id: `src.aws-load-shedding` (proposed).
- Proposed record: `read.aws-load-shedding.2026-10-30`.
- URL (concatenate the two lines):

      https://aws.amazon.com/builders-library/
      using-load-shedding-to-avoid-overload/
- Resolved URL (concatenate the two code spans):
  `https://builder.aws.com/content/`
  `3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload`.
- Unit label: "Using load shedding to avoid overload — AWS Builder Center";
  unit type `engineering-article`; access date 2026-10-30.
- Representation: HTTP 200 after a 301 redirect, 206,813 bytes, HTTP Date
  2026-10-30T21:39:40Z, Last-Modified Tue, 27 Oct 2026 00:29:08 GMT; no ETag;
  raw HTML SHA-256
  `a48240c61fea2792e6a8958f696867dfb02d7c812a0874cdc220de8fe77486db`.
  No published version identifier beyond the article dates.
- Sections used: "Visibility"; "Load shedding effects on automatic scaling and
  Availability Zone failure".
- Exact quotes:

      When brownout protection rejects a request, that rejection reduces the
      availability of a service. When the service gets it wrong and rejects a
      request although it has capacity (for example, when the maximum number
      of connections is set too low), it generates a false positive. We strive
      to keep a service’s false positive rate at zero.

      In terms of visibility, when load shedding rejects requests, we make
      sure that we have proper instrumentation to know who the client was,
      which operation they were calling, and any other information that will
      help us tune our protection measures. We also use alarms to detect
      whether the countermeasures are rejecting any significant volume of
      traffic.

      When there is a brownout, our priority is to add capacity and to address
      the current bottleneck.

      If misconfigured, load shedding can disable reactive automatic scaling.

- Limits: one public article; it does not measure this page's service, and
  "adding capacity" is described as an operational priority, not a guarantee.

### Kubernetes — Horizontal Pod Autoscaling

- Source id: `src.kubernetes` (existing).
- Proposed record: `read.k8s-hpa.2026-10-30`.
- Requested URL:
  `https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/`;
  it returns a 301 to the resolved URL below.
- URL:
  `https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/`.
- Unit label: "Horizontal Pod Autoscaling — Kubernetes documentation"; unit
  type `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 559,290 bytes, HTTP Date 2026-10-30T21:39:46Z,
  ETag `"0a016345798fe0b328d49068b74a9184-ssl"`; no Last-Modified; raw HTML
  SHA-256
  `5b55be37d316eb65f59a93f058d3ef54b7388c9280440782180ff2e2e4823e3c`.
- Sections used: "Horizontal Pod Autoscaling"; "Stability of workload scale";
  "Stabilization window".
- Exact quotes:

      In Kubernetes, a HorizontalPodAutoscaler automatically updates a
      workload resource (such as a Deployment or StatefulSet), with the aim of
      automatically scaling capacity to match demand.

      Horizontal scaling means that the response to increased load is to
      deploy more Pods.

      When managing the scale of a group of replicas using the
      HorizontalPodAutoscaler, it is possible that the number of replicas
      keeps fluctuating frequently due to the dynamic nature of the metrics
      evaluated. This is sometimes referred to as thrashing, or flapping. It's
      similar to the concept of hysteresis in cybernetics.

      The stabilization window is used to restrict the flapping of replica
      count when the metrics used for scaling keep fluctuating. The
      autoscaling algorithm uses this window to infer a previous desired state
      and avoid unwanted changes to workload scale.

- Limits: one rolling Kubernetes documentation page; no cluster, autoscaler
  or benchmark was run. Applying a replica-stabilization window to a degraded
  response mode is Tycho composition, not a Kubernetes statement.

## Book edits

### Owner section

- Frontmatter: only `updated_at` moves from 2026-10-21 to 2026-10-30.
  `evidence_scope`, `content_review`, `source_inspection_date` and
  `content_verified_at` are unchanged; the new records are proposed, not new
  `evidence_scope` ids.
- The mechanism and invariant sentences are unchanged.
- The failure/recovery paragraph is labelled **Tycho synthesis**. It binds
  Google SRE's under-exercised path, accidental activation, feedback cycles,
  monitoring and turn-off/tuning guidance, and adds AWS visibility
  instrumentation and alarms. The silent-correctness comparison is labelled
  **Tycho judgment**. Hysteresis is retained as a requirement; the Kubernetes
  stabilization window is source-bound, while applying it to a degraded mode
  is labelled Tycho composition.
- The alternative paragraph is labelled **Tycho comparison**. It binds Google
  SRE's suboptimal-results statement and the switch to load shedding plus a
  consistent subset of clients receiving errors when degraded responses are
  too expensive, then the added-capacity statements from Google SRE and AWS.
  The preference rule is labelled **Tycho choice rule**; the AWS warning that
  shedding can disable reactive autoscaling and the Google SRE warning that
  added resources may not recover a death spiral are retained as limits.
- The `### Graceful Degradation` heading stays at line 178. The page grows
  from 244 to 266 lines. `### Load Shedding` moves from 194 to 216,
  `### Throttling` from 211 to 233 and `### Rate Limiting` from 232 to 254.
- Raw SHA-256:
  `251f7f4d18fd46c8173dd4cee54c6c70518bc2c3dc3c9e11e0f1ce6d33a88ba3`.
- Historical-view SHA-256:
  `e115f1327ae7dea8fd0b70240bd5154cefca6151cf2f313c856a6a340c1c9f76`.
- Base raw SHA-256:
  `c89ed098b81d8094f7968a5067e464123a9228aebf461dbccedccf0229d369c3`;
  base historical-view SHA-256:
  `56713af9a6510fac56c11063b0503887bc3962058cde9b2ac3d5186f4329aaa9`.

### V11/C07 inline card

- `evidence_scope.source_ids` adds `src.aws-load-shedding` and
  `src.sre-best-practices`; `src.sre-cascading`, `src.sre-overload` and
  `src.kubernetes` were already declared. Other frontmatter is unchanged; the
  card dates were already 2026-10-30.
- **Good-fit conditions** now require an explicitly less accurate or less
  complete degraded response and an exercised recovery path.
- **Hard contraindications** add the case where no degraded response can be
  computed and an explicit error is the remaining option.
- **Competing alternative** now compares an explicit outage or added capacity,
  with the Tycho choice rule.
- **Failure and recovery** now names the under-exercised path, accidental
  activation, feedback cycles, monitoring/tuning, AWS visibility, the Tycho
  silent-correctness judgment and Kubernetes hysteresis.
- **Sources** names the existing cascading and overload records and the three
  proposed records; it states that the units are public documentation, not
  benchmarks.
- The `### Graceful Degradation` heading moves from line 277 to 279 because
  of the two added source ids. `### Load Shedding` moves from 308 to 323. The
  chapter page is 572 lines.
- Raw SHA-256:
  `718c5146cd4848ce428e87a00b0abbffe35dcc030617e9274e56c6e609d89cfd`.
- Historical-view SHA-256:
  `d7cf97798223303a64bc870d938d1035054c5c6a877fc839772d3ce22477a172`.
- Base raw SHA-256:
  `e6a0dbf4c930fd9e6ec22fbf3f5255481d73bd5bc513ccceaf9398082e1f0186`;
  base historical-view SHA-256:
  `332786e26954b8e1c1b007229f41a882d8f91e7712d5286fd670bb7d538842f9`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following changes are not in the lane commit. They were exercised in a
detached scratch copy of this worktree with the two book files plus the source
register, ledger, source plan, registry, owner units, card batches, content
revision and atlas manifest. The scratch results are in the Validation
section; no scratch file is part of the lane commit.

### Source register `sources/register.json`

Set `updated` to 2026-10-30; the source count moves from 299 to 301.

- `src.aws-load-shedding` — title "Using load shedding to avoid overload";
  category `performance`; publisher "Amazon Web Services"; kind
  `engineering-article`; URL the AWS page above; resolved URL
  `https://builder.aws.com/content/`
  `3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload`;
  topics `["overload","load-shedding","availability","capacity"]`; priority
  `core`; planned use "Load-shedding rejection, visibility, false-positive
  measurement and capacity response."; admission `admitted-for-research`;
  access `public-web-or-author-download`; reading status
  `full-public-page-inspected`; version records the 2026-10-30 access,
  206,813-byte HTML, raw HTML SHA-256 `a48240c6...`, HTTP Date
  2026-10-30T21:39:40Z, Last-Modified 2026-10-27T00:29:08Z and the absence of
  a separate version identifier; `access_checked` and `content_verified`
  2026-10-30; license note "Public AWS Builder Center article; cite short
  excerpts and paraphrase; do not mirror."; verification scope names the full
  article and the sections above, and excludes linked pages and images;
  observed title "Using load shedding to avoid overload | AWS Builder Center".
- `src.sre-best-practices` — title "A Collection of Best Practices for
  Production Services"; category `operations`; publisher "Google SRE
  authors"; kind `book-chapter`; URL the SRE appendix above; topics
  `["reliability","overload","capacity-planning","best-practices"]`;
  priority `supporting`; planned use "Overload response choices: degraded
  results, load shedding and explicit client errors."; admission
  `admitted-for-research`; access `public-web-or-author-download`; reading
  status `full-public-page-inspected`; version records the 2026-10-30 access,
  50,907-byte HTML, raw HTML SHA-256 `03ad1997...`, HTTP Date
  2026-10-30T21:39:43Z and Last-Modified 2026-10-08T04:48:00Z;
  `access_checked` and `content_verified` 2026-10-30; license note "Public
  SRE book appendix under CC BY-NC-ND 4.0; cite short excerpts and paraphrase;
  do not mirror."; verification scope names the full appendix and the sections
  above, and excludes linked pages; observed title "Google SRE: Production
  Services Best Practices".
- `src.kubernetes` — set `content_verified` to 2026-10-30. Append these
  facts to `version`: the Horizontal Pod Autoscaling page was inspected
  2026-10-30; raw HTML SHA-256 `5b55be37...`; HTTP Date
  2026-10-30T21:39:46Z; ETag
  `0a016345798fe0b328d49068b74a9184-ssl` (without the surrounding quotes).
  Append to `verification_scope`: "Horizontal Pod Autoscaling was read on
  2026-10-30; other Kubernetes pages and linked content were not read in this
  lane." Do not change the URL or admission state.

The retained cascading and overload records stay unchanged; their 2026-10-30
fetches returned the same raw digests.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add three records; set `updated` to 2026-10-30. Records move from 197 to 200.
Each record is `status: read`, `reviewer: "Automated authoring agent"`, and
uses the exact URL, label, sections and `content_sha256` below.

- `read.aws-load-shedding.2026-10-30` — source `src.aws-load-shedding`;
  label "Using load shedding to avoid overload — AWS Builder Center"; type
  `engineering-article`; sections "Using load shedding to avoid overload",
  "Introduction", "The anatomy of overload", "Testing", "Visibility", "Load
  shedding effects on automatic scaling and Availability Zone failure", "Load
  shedding mechanisms", "Thinking about overload differently";
  content_sha256
  `a48240c61fea2792e6a8958f696867dfb02d7c812a0874cdc220de8fe77486db`.
- `read.sre-best-practices-overload.2026-10-30` — source
  `src.sre-best-practices`; label "A Collection of Best Practices for
  Production Services — Google SRE book appendix"; type `book-chapter`;
  sections "A Collection of Best Practices for Production Services", "Capacity
  Planning", "Overloads and Failure"; content_sha256
  `03ad19970146a1a0ed8406a60f9702af0fd5fa8470ce2c6b33846280e4f9a4be`.
- `read.k8s-hpa.2026-10-30` — source `src.kubernetes`; label "Horizontal
  Pod Autoscaling — Kubernetes documentation"; type `documentation-page`;
  sections "Horizontal Pod Autoscaling", "Stability of workload scale",
  "Configurable scaling behavior", "Stabilization window"; content_sha256
  `5b55be37d316eb65f59a93f058d3ef54b7388c9280440782180ff2e2e4823e3c`.

The retained cascading and overload records stay unchanged.

### Source plan `edition/patterns/source-plan.v1.json`

Append four units to `tycho.pattern.graceful-degradation` after the existing
cascading unit, in this order:

1. `src.sre-overload`, label "Handling Overload — complete public chapter",
   type `book-chapter`, URL
   `https://sre.google/sre-book/handling-overload/`, record
   `read.sre-overload.2026-10-21`, sections equal to that record's eleven-entry
   `sections_read`.
2. `src.sre-best-practices`, the appendix label, URL and three sections from
   the ledger record above, record
   `read.sre-best-practices-overload.2026-10-30`.
3. `src.aws-load-shedding`, the AWS label, resolved URL and eight sections
   from the ledger record above, record
   `read.aws-load-shedding.2026-10-30`.
4. `src.kubernetes`, the HPA label, resolved URL and four sections from the
   ledger record above, record `read.k8s-hpa.2026-10-30`.

Set every unit `status` to `read` and `blocked_reason` to `null`.
Replace the entry notes with: "Failure/recovery and alternative bound
2026-10-30 to Google SRE cascading/overload/best-practices, AWS load shedding
and Kubernetes HPA; silent-correctness judgment, degradation hysteresis
application and the alternative choice rule remain Tycho."

Summary: `required_units` 237 -> 241; `read_units` 236 -> 240;
`blocked_units` stays 1; `ledger_records` 197 -> 200. Recompute
`registry_sha256` after saving the registry; the scratch serialization
produced
`49da330a0df80352039bccc3e19a5402cab19e4920229bff32f39a178ce81940`,
but the authoritative value is the SHA-256 of the saved registry file. Refresh
`route_index_snapshot` from the rebuilt route index; the scratch route build
produced `02312cdd3bfa50b3dc0bbf64705cc3ab9698b26cdb17b244fcea517870a52c1a`.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.graceful-degradation`:

- Keep `technical_owner.state`, `atlas_owner.state` and all coverage values
  at `partial-bounded`.
- Append the four units above to `source_units` after the existing cascading
  unit, in the source-plan order, all with status `read`; the unit labels must
  equal the plan labels.
- Replace `notes` with the source-plan notes plus "Coverage
  partial-bounded; no promotion."
- Keep `review_status` `self-checked`. The registry pattern entry has no
  `updated_at` field in the current schema; do not add one.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.graceful-degradation`:

- Keep `owner.line` at 178, the heading, document id and unit terms unchanged.
- Failure/recovery: set `state: supported`; keep the existing `quote`
  ("Silent loss of correctness is worse than an explicit failure.") because it
  is verbatim in the owner section. Reason: "Google SRE documents that the
  degraded path is rarely exercised and may fail, that complexity can activate
  it unintentionally or create feedback cycles, and that operators need
  monitoring and a way to disable or tune it; AWS documents visible
  instrumentation and alarms for rejected work. The claim that silent
  correctness loss is worse than explicit failure is Tycho judgment, labelled
  in the page." Primary binding `src.sre-cascading`, record
  `read.batch4-sre-cascading.2026-10-21`, section "Load Shedding and
  Graceful Degradation", quote "Complex load shedding and graceful degradation
  can cause problems themselves—excessive complexity may cause the server to
  trip into a degraded mode when it is not desired, or enter feedback cycles
  at undesired times. Design a way to quickly turn off complex graceful
  degradation or tune parameters if needed.", revision `d67024d5...`.
  Supporting bindings: Google SRE "the code path you never use ... doesn’t
  work" and "Monitor and alert when too many servers enter these modes", same
  record and section; Google SRE "responses that are not as accurate as or
  that contain less data than normal responses" and "may have no immediate
  option but to serve errors", `src.sre-overload`, record
  `read.sre-overload.2026-10-21`, section "Handling Overload", revision
  `945d15db...`; AWS instrumentation/alarms quote, `src.aws-load-shedding`,
  record `read.aws-load-shedding.2026-10-30`, section "Visibility", revision
  `a48240c6...`; Kubernetes stabilization-window quote, `src.kubernetes`,
  record `read.k8s-hpa.2026-10-30`, section "Stabilization window", revision
  `5b55be37...`.
- Alternative: set `state: supported`; keep the existing `quote` ("A
  complete, explicit outage or added capacity may be preferable when no safe
  mode exists.") because it is verbatim in the owner section. Reason: "Google
  SRE documents explicit errors when degraded responses cannot be computed or
  are too expensive, and adding tasks as an expedient recovery; AWS makes
  adding capacity the priority during a brownout. The preference rule is Tycho
  guidance, labelled in the page." Primary binding
  `src.sre-best-practices`, record
  `read.sre-best-practices-overload.2026-10-30`, section "Overloads and
  Failure", quote the "even degraded responses are too expensive ... choosing
  a consistent subset of clients to receive errors" passage, revision
  `03ad1997...`. Supporting bindings: Google SRE "may have no immediate
  option but to serve errors", `src.sre-overload`, record
  `read.sre-overload.2026-10-21`, section "Handling Overload", revision
  `945d15db...`; Google SRE "adding tasks can be the most expedient way to
  recover", `src.sre-cascading`, record
  `read.batch4-sre-cascading.2026-10-21`, section "Immediate Steps to Address
  Cascading Failures", revision `d67024d5...`; AWS "our priority is to add
  capacity", `src.aws-load-shedding`, record
  `read.aws-load-shedding.2026-10-30`, section "Visibility", revision
  `a48240c6...`; AWS "can disable reactive automatic scaling", same record,
  section "Load shedding effects on automatic scaling and Availability Zone
  failure", same revision; Kubernetes HPA capacity quote,
  `src.kubernetes`, record `read.k8s-hpa.2026-10-30`, section "Horizontal
  Pod Autoscaling", revision `5b55be37...`.
- Mechanism: keep the supported state and binding, but replace its `quote`
  with the verbatim page sentence "Graceful degradation removes optional
  features or reduces quality to protect an essential outcome under overload."
  The prior quote dropped "Graceful"; preflight rejects it as non-verbatim.
  The invariant state, quote and binding stay unchanged.
- `source_support`: keep `read.batch4-sre-cascading.2026-10-21` as the
  primary record and add auxiliary entries for `read.sre-overload.2026-10-21`
  (`945d15db...`), `read.sre-best-practices-overload.2026-10-30`
  (`03ad1997...`), `read.aws-load-shedding.2026-10-30`
  (`a48240c6...`) and `read.k8s-hpa.2026-10-30` (`5b55be37...`).
- Set `technical_coverage` to `partial-bounded`. Set `notes` to the
  registry notes above.
- Set `decision_evidence.competing_alternative` to the new card text:
  "An explicit outage or added capacity. Reverse the choice when no safe
  degraded response exists, when no reduced result preserves the correctness
  contract, or when capacity can be added faster than a degraded mode can be
  made safe. The choice rule is Tycho guidance."
- The shared page also carries `tycho.pattern.load-shedding`,
  `tycho.pattern.throttling` and `tycho.pattern.rate-limiting`; set their
  `owner.line` from 194 to 216, 211 to 233 and 232 to 254 because the
  graceful-degradation section grew. No other field of those entries changes.
- Summary counters: `failure_recovery_supported` 66 -> 67;
  `alternative_supported` 72 -> 73. `technical_partial_bounded` stays 17
  and `technical_partial` stays 75 because coverage is derived from mechanism
  and invariant for this entry.

### Card registration `edition/patterns/card-batches.v1.json`

Add `card_path`:
`book/volumes/v11-pattern-atlas/c07-resilience/README.md` to the
`tycho.pattern.graceful-degradation` entry. The card remains inline; no split
is performed. Keep `ledger_record`
`read.batch4-sre-cascading.2026-10-21`.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B40 graceful degradation failure/recovery and alternative source binding; no
promotion or owner acceptance." Use these historical-view hashes:

- Owner path, previous:
  `72959e7c00b5f974388af3ce802ff66239452cb6f618bf188d0bfd989fbb9f92`;
  current:
  `e115f1327ae7dea8fd0b70240bd5154cefca6151cf2f313c856a6a340c1c9f76`.
- Card path, previous:
  `539ad3a246c5b160b09d32174b5bac6e66cc204ca24f57862e36b318eec9929f`;
  current:
  `d7cf97798223303a64bc870d938d1035054c5c6a877fc839772d3ce22477a172`.
- Leave `source_blocks`, `enrichment_documents`, `enrichment_additions`
  and `enrichment_baselines` empty.

Raw file hashes for reference:
`251f7f4d18fd46c8173dd4cee54c6c70518bc2c3dc3c9e11e0f1ce6d33a88ba3`
(owner) and
`718c5146cd4848ce428e87a00b0abbffe35dcc030617e9274e56c6e609d89cfd`
(card).

### Atlas manifest `edition/atlas-manifest.json`

Set the V11/C07 document `sha256` to
`718c5146cd4848ce428e87a00b0abbffe35dcc030617e9274e56c6e609d89cfd` and
`registry_sha256` to the new registry file hash
(`49da330a...` in the scratch serialization).

### Frontmatter and evidence scope

The lane leaves the owner page's `evidence_scope`,
`source_inspection_date` and `content_review` unchanged. The new records are
supporting bindings, not new `evidence_scope` ids. The card gains the two
source ids listed above because preflight requires every binding source to be
declared on the card. If the integrator also wants the new records in the
owner `evidence_scope.source_ids`, treat it as a separate change: update
`edition/enrichment-manifest.json`, recompute both historical-view hashes and
the content revision, and re-run the decomposition and enrichment validators.

### Derived artifacts and review metadata

The book edit changes one canonical owner page and one atlas chapter. The
source register gains two ids and the ledger, source plan, registry,
owner-units, card registration and content revision change. Refresh once at
batch end: route index, page census, coverage/reverse map, phase 4,
delivery-evidence counts, edition inventory and the source catalogue
(`python3 scripts/source_catalog.py`). The semantic audit records a hash
change for both pages and requires re-review; do not treat a stale derived
hash as a lane content failure or update the semantic-audit sha without
review.

The 2026-10-22 sufficient review record in
`edition/patterns/sufficient-review-records.v1.json` carries owner-page
`page_sha256`
`f504ca8e49eef012e206047ffe8de14c022f90bd756115c7a275be490ecedbab` and
already records a pending delta review after a 2026-10-28 change. This edit
adds more changed bytes. Do not update the record without a fresh review; the
book/atlas independent review gate applies.

## Validation

Checker output in the lane worktree after the two book edits:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Owner-section quote audit: every quoted fragment in the failure/recovery and
alternative paragraphs is a whitespace-normalized substring of the five
served pages. The Tycho-labelled sentences are not presented as source quotes.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_registry.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_sources.py` — PASS; 236 read; 197
  ledger records (the lane changes no source metadata).
- `python3 scripts/validate_pattern_owner_units.py` — FAIL
  `owner-units-alternative` because the existing metadata still carries the
  old card alternative. This is metadata work, not a content defect.
- `python3 scripts/validate_book_metadata.py` — FAIL unknown source ID for
  the card's two new source ids; integrator register work.
- `python3 scripts/validate_pattern_atlas.py` — FAIL
  `atlas-document-sha` in the lane tree.
- `python3 scripts/validate_decomposition.py` — PASS.
- `python3 scripts/validate_enrichment.py` — PASS.
- `python3 scripts/validate_directory_migration.py` — FAIL
  `directory-baseline-payload-drift` until the content revision is applied.

In the detached scratch copy with the metadata patch above:

    PASS: tycho.pattern.graceful-degradation
    1/1 entries preflight clean

    PASS: source plan 145 entries; 240 read; 200 ledger records
    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: 301 source records, mandatory IDs, cross-references and catalogue
    freshness after one `source_catalog.py` regeneration
    PASS: 493 documents, structural metadata and registry references
    PASS: atlas V11 11 chapters, 70 documents, 145 patterns
    PASS: directory migration; 493 canonical documents, 339 moved documents
    PASS: decomposition; 739 preserved source blocks, 174 new question pages
    PASS: enrichment; explicit membership and byte conservation
    PASS: edition validation after one route-index build and one inventory
    refresh; 549 files

The scratch `book_change.py --plan` then reported 0 changed book pages, 0
missing revisions and 0 atlas page changes; the remaining items were the stale
page census, coverage/reverse map, phase 4, delivery-evidence counts and the
semantic audit. The source-plan route snapshot and registry hash were rebound
and the edition inventory was refreshed after that. Those remaining items are
batch-end derived refreshes, not lane content failures. The full unit suite was
not run; batch-end tests remain with the integrator.

## Limits

The binding uses five public pages. They describe degraded responses, explicit
errors under extreme overload, load shedding with a consistent subset of
clients receiving errors, under-exercised degraded paths, accidental
activation, feedback cycles, visibility instrumentation, added capacity and
autoscaling hysteresis. None observes this page's service, proves that a
degraded response preserves the correctness contract, or measures a recovery
window.

The failure/recovery state is `supported` only because the page separates the
source-supported failure modes (under-exercised path, accidental activation,
feedback cycles, missing visibility) from the Tycho judgment that silent
correctness loss is worse than explicit failure. The alternative state is
`supported` for the same reason: the explicit-error and added-capacity
statements are source-backed, while the preference rule is Tycho guidance. A
reviewer that requires every word of a dimension quote to be source-quoted
should treat both as partial.

The SRE chapters and appendix are public books under CC BY-NC-ND 4.0; only
short excerpts are quoted. The AWS article and Kubernetes page are rolling
documentation; their raw digests are the binding revisions on 2026-10-30. No
load test, outage, autoscaler or cluster was run, and no performance or
availability measurement is claimed.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer
  should check quote-to-claim fit for both dimensions, the Tycho labels for the
  silent-correctness judgment, the hysteresis application and the
  alternative-choice rule, the five revisions, the moved owner-unit lines, the
  metadata patch and the absence of a sufficient or promotion claim.
- The reviewer must use read-only repository access and must not run tests.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- `book/volumes/v11-pattern-atlas/c07-resilience/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
