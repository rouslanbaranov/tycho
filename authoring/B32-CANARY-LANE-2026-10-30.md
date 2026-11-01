# B32 — Canary Release invariant and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and failure/recovery were supported;
invariant and alternative were partial. This lane binds the source-supported
parts of both dimensions to Argo Rollouts, Flagger, Google SRE and AWS
blue/green public pages and labels the named separation and choice rules as
Tycho guidance. The metadata patch was exercised in a detached scratch copy:
preflight passes 1/1, owner units, registry, cards, sources, book metadata,
directory migration, decomposition and enrichment pass. The patch is not in the
lane commit; promotion is not claimed or ready.

## Lane coordinates

- Parent HEAD: `3a1f1b8d` (short); the branch was created from that commit.
- Branch: `b32-canary`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b32-canary`.
- Scope: the owner section `### Canary Release` in the V08/C04 owner page and
  the inline V11/C10 card `### Canary Release`. Single-entry lane; no other
  entry, shared owner page, promotion or generated file is changed.
- Owner path (concatenate the two lines):

      book/volumes/v08-delivery-deployment-and-recovery/
      c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md

- Card path:
  `book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md`.
- Card location: inline. No dedicated `canary-release.md` exists. A split is
  an integrator decision; this lane does not create one.

## Candidate evaluation

- Argo Rollouts, "Canary" (existing source `src.argo-rollouts`, record
  `read.batch5-argo-canary.2026-10-21`). Selected for the canary mechanism,
  analysis abort and the rolling-mimic passage. The page does not discuss data
  compatibility or alternatives as decision options.
- Flagger, "Deployment Strategies" (proposed source
  `src.flagger-deployment-strategies`). Selected for the alternative
  dimension: canary, A/B, blue/green and blue/green traffic mirroring, with the
  idempotency condition for mirrored requests. The page does not use the term
  feature flag and does not discuss data compatibility.
- Google SRE Workbook, "Canarying Releases", Chapter 16 (existing source
  `src.sre-workbook`, proposed record `read.sre-workbook-canarying.2026-10-30`).
  Selected for the invariant (shared infrastructure and stateful traffic
  teeing) and for alternatives (feature flags, blue/green cost and rollback).
- AWS, "Blue/Green Deployments on AWS", data best-practices page (proposed
  source `src.aws-blue-green-deployments`). Selected for the invariant: blue
  and green environments share data stores and require backward-compatible
  schema changes. The page is a data-tier section of a whitepaper marked
  historical reference; it is not a canary experiment.
- AWS, "When Blue/Green Deployments Are Not Recommended" (same proposed source,
  candidate, not selected). It adds deployment-aware feature-flag caveats and
  data-synchronization complexity, but no canary-specific alternative or
  data-compatibility test. URL, revision and the exact passages are recorded
  below.
- No selected page tests a canary against an incompatible schema, measures a
  mirrored write, or names the exposure/data separation. The separation, the
  reads-only default and the choice rule are Tycho guidance.

## Source binding

### Argo Rollouts — Canary

- Source id: `src.argo-rollouts` (existing).
- Existing record: `read.batch5-argo-canary.2026-10-21`.
- URL: `https://argoproj.github.io/argo-rollouts/features/canary/`.
- Unit label: "Canary — Argo Rollouts documentation"; unit type
  `documentation-page`; access date 2026-10-21; re-read 2026-10-30.
- Recheck 2026-10-30: HTTP `Last-Modified` 2026-01-21T17:53:31Z; ETag
  `"6971129b-1601e"`; served HTML 90,142 bytes; raw HTML SHA-256
  `925398c1c97a8e700b22ec0354648ae6240b405d73e219f2f3e5ffc286c982e7`,
  equal to the record's `content_sha256`. Canonical text SHA-256 is
  `7a7d4792d91d3dd7ea90c2e199343715c688005507ee36307fc7830f06a10bfb`.
  The record revision is the raw HTML digest, so bindings use
  `925398c1...`.
- Sections used: "Canary Deployment Strategy", "Overview", "Mimicking Rolling
  Update", "analysis". The existing mechanism and failure/recovery bindings are
  unchanged.
- Exact quotes used:

      A canary rollout is a deployment strategy where the operator releases a
      new version of their application to a small percentage of the production
      traffic.

      Configure the background Analysis to execute during the rollout. If the
      analysis is unsuccessful the rollout will be aborted.

      If the steps field is omitted, the canary strategy will mimic the rolling
      update behavior.

- Limits: one controller feature page; no data-tier, state or compatibility
  discussion; no benchmark or production observation.

### Flagger — Deployment Strategies

- Proposed source id: `src.flagger-deployment-strategies` (new).
- Proposed record: `read.flagger-deployment-strategies.2026-10-30`.
- Unit URL (official Markdown representation):
  `https://docs.flagger.app/usage/deployment-strategies.md`.
- Human page: `https://docs.flagger.app/usage/deployment-strategies`.
- Unit label: "Deployment Strategies — Flagger documentation"; unit type
  `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET; Markdown representation 20,003 bytes, 481 lines,
  SHA-256
  `2d57c5d5bd950da50cf3fc73e1aff83f84981959e544cd8a40cc25c97d66b745`;
  HTML page 753,515 bytes, canonical text SHA-256
  `2dab10b8e7fa6768f1a31e0f25d9d8ae40bbc5992af269ee10a09da8cb51b350`;
  raw HTML SHA-256
  `2943ab6205094330b2caa6ebb00717e400b8813e13fb89bc6c69c03cce56e3b2`.
  HTTP Date 2026-10-30T16:45:19Z; no Last-Modified or Markdown ETag; the HTML
  ETag is `W/"vdtr2iymbgg53p"`. The binding revision is the raw Markdown
  digest.
- Sections read: "Deployment Strategies", "Canary Release", "A/B Testing",
  "Blue/Green Deployments", "Blue/Green with Traffic Mirroring", "Canary
  Release with Session Affinity".
- Exact quotes used:

      Flagger can run automated application analysis, promotion and rollback
      for the following deployment strategies:

      Traffic Mirroring is a pre-stage in a Canary (progressive traffic
      shifting) or Blue/Green deployment strategy.

      Mirroring should be used for requests that are idempotent or capable of
      being processed twice (once by the primary and once by the canary).

      Reads are idempotent.

      Before using mirroring on requests that may be writes, you should
      consider what will happen if a write is duplicated and handled by the
      primary and canary.

      For Canary releases and A/B testing you'll need a Layer 7 traffic
      management solution like a service mesh or an ingress controller. For
      Blue/Green deployments no service mesh or ingress controller is required.

- Limits: living documentation with no published version identifier or
  Last-Modified; the revision is the Markdown representation, not the rendered
  HTML. It supports mirroring idempotency and the strategy list; it does not
  test a duplicated write or name feature flags.

### Google SRE Workbook — Canarying Releases

- Existing source id: `src.sre-workbook`.
- Proposed record: `read.sre-workbook-canarying.2026-10-30`.
- URL: `https://sre.google/workbook/canarying-releases/`.
- Unit label: "Canarying Releases — The Site Reliability Workbook, Chapter 16";
  unit type `book-chapter`; access date 2026-10-30.
- Access: public HTTPS GET; served HTML 80,800 bytes; raw HTML SHA-256
  `2129ec6fefdb7807073a7877344e7f0409c27e4fde1021d30114a38338fd039f`;
  canonical text SHA-256
  `ee9a392c88b4ce3601952bcb9305fd2b4d69cd63267c77a9df9b47d0c1e19ec9`.
  HTTP Date 2026-10-30T16:45:20Z; no Last-Modified or ETag. The binding
  revision is the raw HTML digest.
- Sections read: the full Chapter 16 body, including "Separating Components
  That Change at Different Rates", "Dependencies and Isolation", "Related
  Concepts", "Blue/Green Deployment" and "Traffic Teeing".
- Exact quotes used:

      For practical reasons, the canary population and the control may share
      backends, frontends, networks, data stores, and other infrastructure.

      Traffic teeing also doesn’t adequately identify risk in stateful systems;
      copies of traffic may introduce unexpected influences between the
      seemingly independent deployments.

      Feature flag or experiment frameworks like Gertrude, Feature, and
      PlanOut allow you to separate feature launches from binary releases.

      Blue/green deployment maintains two instances of a system: one that is
      serving traffic (green), and another that is ready to serve traffic
      (blue).

      One downside is that this setup uses twice as many resources as a more
      “traditional” deployment.

      In this setup, you are effectively performing a before/after canary
      (discussed earlier).

- Limits: one chapter of a free book under CC BY-NC-ND 4.0; no data store was
  tested; the examples are Google-specific and are not reproduced. It supports
  shared infrastructure and stateful teeing risk, not a data-compatibility
  boundary.

### AWS — Blue/Green Deployments on AWS

- Proposed source id: `src.aws-blue-green-deployments` (new).
- Proposed record: `read.aws-blue-green-data.2026-10-30`.
- Landing URL:
  `https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html`.
- Unit URL (concatenate the two lines):

      https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/
      best-practices-for-managing-data-synchronization-and-schema-changes.html

- Unit label: "Best Practices for Managing Data Synchronization and Schema
  Changes — Blue/Green Deployments on AWS"; unit type `documentation-page`;
  access date 2026-10-30. Publication date 2021-09-29; the whitepaper displays
  a historical-reference banner.
- Access: public HTTPS GET; served HTML 18,886 bytes; raw HTML SHA-256
  `07eaa6ff45ca86872f743c07deb17577761f1216e04a840de89ae9c5bfa99442`;
  canonical text SHA-256
  `6cc6f620bb867f4200ea0323fd939a0925bae30266c715b2ed1e73168a40ee41`.
  HTTP Date 2026-10-30T16:46:22Z; Last-Modified 2026-10-30T15:53:36Z; no
  ETag. The binding revision is the raw HTML digest.
- Sections read: "Best Practices for Managing Data Synchronization and Schema
  Changes" and "Decoupling Schema Changes from Code Changes".
- Exact quotes used:

      Both the blue and green environments need up-to-date data

      Broadly, you accomplish this by having both the green and blue
      environments share the same data stores.

      Structured data stores, such as relational database management systems
      (RDBMS), where the data schema can diverge between the environments,
      typically require additional considerations.

      Database updates must be backward compatible, so the old version of the
      application can still interact with the data.

      After this removal, the earlier application version is no longer
      operational.

- Limits: one data-tier section of a whitepaper marked historical reference;
  it is not a canary experiment and does not test a mirrored write.

### AWS not-recommended page — considered, not selected

- URL (concatenate the two lines):

      https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/
      when-bluegreen-deployments-are-not-recommended.html
- Access 2026-10-30: served HTML 16,870 bytes; raw HTML SHA-256
  `ac4d5323d766321b743c4af33c8022b43296ae196309cd6f29f8fa5f4c3db2b7`;
  canonical text SHA-256
  `9f346800418b4113c631b7d4c3a5fd8cec521144e21a1defd0a24002e18f07cd`.
- Exact passages inspected:

      In some scenarios, sharing a data store isn’t desired or feasible.

      You should consider using feature flags in your application to make it
      deployment aware.

      Making your applications deployment aware introduces additional risk and
      complexity and typically isn’t recommended with blue/green deployments.

- No ledger record or binding is added. The page discusses deployment-aware
  feature flags in blue/green, not canary alternatives, and its data-store
  warning is already covered by the selected data page.

## Book edits

### Owner section

- Frontmatter: only `updated_at` moves to 2026-10-30. `evidence_scope` and
  `content_review` remain byte-identical to the decomposition baseline because
  `validate_decomposition.py` protects them; changing them without an
  authorized metadata revision fails `altered-original-provenance`.
  `source_inspection_date` and `content_verified_at` stay `null`; the page
  keeps its decomposition-era draft review state.
- The mechanism paragraph and the existing unit terms are retained.
- The invariant paragraph now states the separation, quotes the Google SRE
  shared-infrastructure and AWS up-to-date-data/backward-compatible-schema
  passages, labels the separation and the reads-only default as Tycho
  guidance, and keeps the shared-state and sample-size cautions.
- The alternative paragraph now states the Flagger idempotency condition,
  labels suppressing writes as Tycho guidance, records the AWS shared-data
  account, cites Google SRE feature flags and Argo's rolling mimic, and keeps
  the canary fit condition. The source boundary lists all four records and
  their revisions.
- The heading stays at line 149; the page is 198 lines.
- Raw SHA-256:
  `563ad00279cffc891078d0fddf74af80b235acf9a530d902d2fe69cbdcfed493`.
- Historical-view SHA-256:
  `8cf72d3d91c71c6534a859f789f6e93d5d6aa21881b517e23fab49a8b68ccb6a`.

### V11/C10 inline card

- Frontmatter adds `src.flagger-deployment-strategies`, `src.sre-workbook` and
  `src.aws-blue-green-deployments` to `evidence_scope.source_ids`. The card
  review, update and inspection dates move to 2026-10-30.
- **Good-fit conditions** now require mirrored traffic to be read-only or
  idempotent.
- **Hard contraindications** now reject mirrored writes that cannot be made
  idempotent.
- **Competing alternative** now names traffic mirroring, blue/green, feature
  flags and rolling deployment and states the reversal conditions.
- **Failure and recovery** now names the duplicated-write and shared-data
  boundary failures and points to the owner source checks.
- **Sources** names the existing Argo record and the three proposed records.
- The heading moves from line 145 to line 148 because of the three added source
  ids. The chapter page is 402 lines.
- Raw SHA-256:
  `8b48f39fc4c95f798bc950e85e0c321e2a288512fda6550dd18fc85d69cf1006`.
- Historical-view SHA-256:
  `0d3f9c94f6b23dca832585cd5be3044b9000b70d87c98063fb62700f179b6e0b`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was exercised in a detached
scratch copy of this worktree with the two book files plus the source register,
ledger, source plan, registry, owner units, card batches and content revision.
The scratch results are in the Validation section; no scratch file is part of
the lane commit.

### Source register `sources/register.json`

Add two source records. Set `updated` to 2026-10-30. The source count moves
from 288 to 290.

- `src.flagger-deployment-strategies` — title "Deployment Strategies";
  category "delivery"; publisher "Flux project"; kind "official-docs"; URL
  `https://docs.flagger.app/usage/deployment-strategies`; resolved URL
  `https://docs.flagger.app/usage/deployment-strategies.md`; topics
  `["deployment", "progressive-delivery", "canary", "blue-green", "traffic-mirroring"]`;
  priority "core"; planned use "Canary, A/B, blue/green and traffic-mirroring
  strategies, including idempotency conditions for mirrored requests.";
  admission "admitted-for-research"; access "public-web-or-author-download";
  reading status "full-public-page-inspected"; version records the 2026-10-30
  access, raw Markdown SHA-256 `2d57c5d5...`, HTML canonical text SHA-256
  `2dab10b8...`, and the absence of a published version or Last-Modified;
  `access_checked` and `content_verified` 2026-10-30; license note "Public
  Flagger documentation; cite short excerpts and paraphrase; do not mirror.";
  verification scope names the full Markdown page and excludes linked pages and
  controller behavior; observed title "Deployment Strategies | Flagger".
- `src.aws-blue-green-deployments` — title "Blue/Green Deployments on AWS";
  category "delivery"; publisher "Amazon Web Services"; kind "official-docs";
  URL `https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html`;
  resolved URL the data best-practices page above; topics
  `["deployment", "blue-green", "data-compatibility", "schema-evolution"]`;
  priority "core"; planned use "Blue/green environment boundary and data-tier
  compatibility, including shared data stores and schema-change order.";
  admission "admitted-for-research"; access "public-web-or-author-download";
  reading status "full-public-page-inspected"; version records the 2021-09-29
  publication date, historical-reference banner, 2026-10-30 access, data page
  raw HTML SHA-256 `07eaa6ff...`, canonical text SHA-256 `6cc6f620...` and
  Last-Modified 2026-10-30T15:53:36Z; `access_checked` and
  `content_verified` 2026-10-30; license note "Public AWS whitepaper; cite
  short excerpts and paraphrase; do not mirror."; verification scope covers
  the two named sections and excludes the rest of the whitepaper; observed
  title "Best Practices for Managing Data Synchronization and Schema Changes -
  Blue/Green Deployments on AWS".

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add three records. Set `updated` to 2026-10-30. Records move from 165 to 168.

- `read.flagger-deployment-strategies.2026-10-30` — source
  `src.flagger-deployment-strategies`; unit label "Deployment Strategies —
  Flagger documentation"; type `documentation-page`; access date 2026-10-30;
  access method records the Markdown and HTML revisions, HTTP Date, raw
  Markdown digest `2d57c5d5...`, canonical HTML digest `2dab10b8...` and the
  absence of Last-Modified/ETag on the Markdown representation; sections as
  listed above; `content_sha256` `2d57c5d5...`; status `read`; reviewer
  "Automated authoring agent".
- Claims supported: the strategy list; traffic mirroring as a canary/blue-green
  pre-stage; primary response returned and canary response discarded; the
  idempotency/duplicated-write condition; Layer 7 requirement for canary and
  A/B but not blue/green.
- Claims not supported: feature-flag behavior; data compatibility or schema
  behavior; implementation behavior or production observation; linked pages.
- Limits: living page with no published version identifier; revision is the
  Markdown representation, not rendered HTML; mirroring behavior was not
  tested.
- `read.sre-workbook-canarying.2026-10-30` — source `src.sre-workbook`; unit
  label "Canarying Releases — The Site Reliability Workbook, Chapter 16"; type
  `book-chapter`; access date 2026-10-30; access method records the raw HTML
  digest `2129ec6f...`, canonical text digest `ee9a392c...`, 80,800 bytes
  and HTTP Date; sections as listed above; `content_sha256` `2129ec6f...`;
  status `read`; reviewer "Automated authoring agent".
- Claims supported: canary/control shared infrastructure; stateful traffic
  teeing risk; feature flags separating launches from binary releases;
  blue/green's two instances, router rollback and double resource cost;
  canarying as a partial, time-limited deployment.
- Claims not supported: a data-compatibility test; implementation behavior;
  linked chapters; universal applicability of the examples.
- Limits: one chapter under CC BY-NC-ND 4.0; no data store tested; examples are
  Google-specific and not reproduced.
- `read.aws-blue-green-data.2026-10-30` — source
  `src.aws-blue-green-deployments`; unit label "Best Practices for Managing
  Data Synchronization and Schema Changes — Blue/Green Deployments on AWS";
  type `documentation-page`; access date 2026-10-30; access method records the
  18,886-byte HTML, raw digest `07eaa6ff...`, canonical digest
  `6cc6f620...`, HTTP Date and Last-Modified; sections as listed above;
  `content_sha256` `07eaa6ff...`; status `read`; reviewer "Automated
  authoring agent".
- Claims supported: both environments need up-to-date data; shared data stores;
  schema divergence needs extra consideration; backward-compatible database
  updates; deletive schema changes make the earlier version non-operational.
- Claims not supported: a canary-specific data test; implementation behavior;
  the rest of the whitepaper; linked material.
- Limits: one section of a whitepaper marked historical reference; not a canary
  test; examples are AWS-specific and not reproduced.

### Source plan `edition/patterns/source-plan.v1.json`

Append three units to `tycho.pattern.canary-release` after the existing Argo
unit:

- `src.flagger-deployment-strategies`: unit "Deployment Strategies — Flagger
  documentation", type `documentation-page`, URL
  `https://docs.flagger.app/usage/deployment-strategies.md`, the six sections
  above, status `read`, record `read.flagger-deployment-strategies.2026-10-30`.
- `src.sre-workbook`: unit "Canarying Releases — The Site Reliability
  Workbook, Chapter 16", type `book-chapter`, URL
  `https://sre.google/workbook/canarying-releases/`, the full section list
  above, status `read`, record `read.sre-workbook-canarying.2026-10-30`.
- `src.aws-blue-green-deployments`: unit "Best Practices for Managing Data
  Synchronization and Schema Changes — Blue/Green Deployments on AWS", type
  `documentation-page`, the data page URL above, the two sections, status
  `read`, record `read.aws-blue-green-data.2026-10-30`.

Replace the entry notes with: "Canary mechanism and failure/recovery use Argo
Rollouts; the invariant uses AWS shared-data-store and backward-compatible-
schema guidance plus Google SRE shared-infrastructure and stateful-teeing
limits; the alternative uses Flagger mirroring idempotency plus Google SRE
feature flags/blue-green and the Argo rolling mimic. The reads-only default,
data-compatibility separation and alternative-choice rule remain Tycho
guidance."

Set `updated` to 2026-10-30. Summary: `required_units` 202 -> 205;
`read_units` 201 -> 204; `ledger_records` 165 -> 168. Recompute
`registry_sha256` after saving the registry; the scratch serialization
produced
`bc8d5f8f368e73756e6952e9fca49b4e390317cd6d6e3028ecb51961b92c96bc`,
but the authoritative value is the SHA-256 of the saved registry file.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.canary-release`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to
  `partial-bounded`. Keep `atlas_owner.state` and `coverage.decision` at
  `partial-bounded`.
- Replace `source_units` with, in order: the existing Argo "Canary — Argo
  Rollouts documentation"; Flagger "Deployment Strategies — Flagger
  documentation"; Google SRE "Canarying Releases — The Site Reliability
  Workbook, Chapter 16"; AWS "Best Practices for Managing Data Synchronization
  and Schema Changes — Blue/Green Deployments on AWS". All four have status
  `read`.
- Replace `notes` with: "Invariant and alternative bound 2026-10-30 to Argo
  Rollouts, Flagger, Google SRE and AWS blue/green evidence; the reads-only
  mirroring default, the exposure/data separation and the alternative-choice
  rule remain Tycho guidance. Coverage partial-bounded; no promotion."
- Keep `review_status` `self-checked`. The registry pattern entry has no
  `updated_at` field in the current schema; do not add one.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.canary-release`:

- Keep `owner.line` at 149, the heading and the four `unit_terms` unchanged.
- Invariant:
  - `state`: `supported`.
  - `quote`: "The exposure slice is not a data-compatibility boundary."
  - `reason`: "Google SRE says the canary population and the control may
    share backends, frontends, networks, data stores and other infrastructure,
    and that traffic teeing does not adequately identify risk in stateful
    systems. AWS says both blue and green environments need up-to-date data,
    share the same data stores, and require backward-compatible schema updates.
    The claim that exposure is not a data-compatibility boundary, and the
    reads-only default, are Tycho guidance."
  - `binding`: `src.aws-blue-green-deployments`, record
    `read.aws-blue-green-data.2026-10-30`, section "Best Practices for
    Managing Data Synchronization and Schema Changes", quote "Broadly, you
    accomplish this by having both the green and blue environments share the
    same data stores.", revision `07eaa6ff...`.
  - Supporting bindings: Google SRE "Dependencies and Isolation" quote "For
    practical reasons, the canary population and the control may share
    backends, frontends, networks, data stores, and other infrastructure.";
    Google SRE "Traffic Teeing" quote "Traffic teeing also doesn’t adequately
    identify risk in stateful systems; copies of traffic may introduce
    unexpected influences between the seemingly independent deployments.";
    AWS "Decoupling Schema Changes from Code Changes" quote "Database updates
    must be backward compatible, so the old version of the application can
    still interact with the data.".
- Alternative:
  - `state`: `supported`.
  - `quote`: "Traffic mirroring is safe only when requests are idempotent or
    can be processed twice".
  - `reason`: "Flagger lists canary, A/B, blue/green and blue/green
    mirroring, and says mirroring should be used only for requests that are
    idempotent or can be processed twice because a duplicated write can hit
    both versions. Google SRE describes feature flags that separate feature
    launches from binary releases and blue/green that uses twice the resources;
    Argo notes a canary without steps mimics a rolling update. The reads-only
    default and the choice rule are Tycho guidance."
  - `binding`: `src.flagger-deployment-strategies`, record
    `read.flagger-deployment-strategies.2026-10-30`, section "Blue/Green with
    Traffic Mirroring", quote "Mirroring should be used for requests that are
    idempotent or capable of being processed twice (once by the primary and
    once by the canary).", revision `2d57c5d5...`.
  - Supporting bindings: Google SRE "Separating Components That Change at
    Different Rates" quote "Feature flag or experiment frameworks like
    Gertrude, Feature, and PlanOut allow you to separate feature launches from
    binary releases."; Google SRE "Blue/Green Deployment" quote "One downside
    is that this setup uses twice as many resources as a more “traditional”
    deployment."; Argo "Mimicking Rolling Update" quote "If the steps field is
    omitted, the canary strategy will mimic the rolling update behavior.";
    AWS "Best Practices for Managing Data Synchronization and Schema Changes"
    quote "Both the blue and green environments need up-to-date data".
- `source_support`: primary Argo record
  `read.batch5-argo-canary.2026-10-21`; add auxiliary Flagger
  `read.flagger-deployment-strategies.2026-10-30`, Google SRE
  `read.sre-workbook-canarying.2026-10-30` and AWS
  `read.aws-blue-green-data.2026-10-30` with revisions `2d57c5d5...`,
  `2129ec6f...` and `07eaa6ff...`.
- Set `technical_coverage` to `partial-bounded`.
- Set `decision_evidence.competing_alternative` to "Traffic mirroring,
  blue/green, feature flags or rolling deployment. Reverse the choice when
  canary analysis cost exceeds risk reduction, the cohort cannot be isolated,
  or writes make mirroring unsafe."
- Set `notes` to: "Invariant and alternative bound 2026-10-30 to AWS
  data-tier, Flagger mirroring, Google SRE canarying and the existing Argo
  record; the reads-only default and alternative-choice rule remain Tycho
  guidance. Coverage partial-bounded; no promotion."

In `shared_pages`, for the owner page listed under Lane coordinates, set
`bounded_entries` from 0 to 1. Keep `decision` `deepen`.

Summary counters: `invariant_supported` 68 -> 69;
`alternative_supported` 67 -> 68; `technical_partial_bounded` 19 -> 20;
`technical_partial` 81 -> 80. No other counter changes.

### Card registration `edition/patterns/card-batches.v1.json`

Add `card_path`:
`book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md` to the
`tycho.pattern.canary-release` entry. Keep `ledger_record`
`read.batch5-argo-canary.2026-10-21`. The card remains inline; no split is
performed.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B32 canary invariant and alternative source binding; no promotion or owner
acceptance." The historical-view hashes are:

- Owner path previous `b2d4eba1...` (migration baseline), current
  `8cf72d3d...`.
- Card path previous `dffed0a0...` (migration baseline), current
  `0d3f9c94...`.

Leave `source_blocks`, `enrichment_documents`, `enrichment_additions` and
`enrichment_baselines` empty. The owner page is retained and no split is
performed. The previous hashes are migration baselines, not the latest
content-revision current hashes.

### Derived artifacts and review metadata

The book edit changes one canonical page and one atlas chapter. The source
register gains two records, so regenerate `sources/CATALOG.md` with
`python3 scripts/source_catalog.py` (scratch count 290). The registry and
source plan changes make `validate_edition.py` report `edition-index-stale`
and `validate_pattern_atlas.py` report `atlas-registry-hash`. These are
derived-hash refreshes for batch end: the affected route index, atlas
coverage/census, reverse-map, sufficient-workflow and semantic-audit artifacts
are regenerated once. Do not treat a stale derived hash as a lane content
failure.

The 2026-10-25 agent review recorded in
`edition/patterns/sufficient-candidates.v1.json` predates this edit and no
longer covers the changed owner page or card bytes. The book/atlas independent
review gate applies; do not update the recorded hash without a fresh review.
The prior review is historical evidence, not acceptance of this lane.

## Validation

Checker output in the lane worktree after the two book edits:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_registry.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_sources.py` — PASS; 201 read; 165 ledger
  records.
- `python3 scripts/validate_pattern_owner_units.py` — FAIL
  `owner-units-quote-not-verbatim: tycho.pattern.canary-release: alternative`
  because the existing metadata still carries the old alternative quote;
  integrator work.
- `python3 scripts/validate_book_metadata.py` — FAIL unknown source ID for the
  card's new source ids; integrator register work.
- `python3 scripts/validate_decomposition.py` — PASS; 739 preserved source
  blocks and 174 new question pages.
- `python3 scripts/validate_enrichment.py` — PASS; explicit membership and byte
  conservation.
- `python3 scripts/validate_directory_migration.py` — FAIL
  `directory-baseline-payload-drift` until the content revision is applied.
- `python3 scripts/validate_edition.py` — FAIL
  `directory-baseline-payload-drift` in the lane tree.
- `python3 scripts/validate_pattern_atlas.py` — FAIL
  `atlas-document-sha` in the lane tree.
- `python3 scripts/validate_sources.py` — PASS before this note is added;
  after the note is added it fails `unknown source reference` for the
  proposed source ids because the register records are not in the lane commit.
  That is integrator work, not a lane content failure.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.canary-release` — FAIL: invariant and alternative still
  partial and `card_path` missing; integrator metadata work.

In the detached scratch copy with the metadata patch above:

    PASS: tycho.pattern.canary-release
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: source plan 145 entries; 204 read; 168 ledger records
    PASS: 290 source records, mandatory IDs, cross-references and catalogue
    freshness
    PASS: 484 documents, structural metadata and registry references
    PASS: directory migration; 484 canonical documents, 339 moved documents
    PASS: decomposition; 739 preserved source blocks, 174 new question pages
    PASS: enrichment; explicit membership and byte conservation

The scratch tree still fails `validate_edition.py` (`edition-index-stale`)
and `validate_pattern_atlas.py` (`atlas-registry-hash`); these are
derived-hash refreshes for batch end, not lane content failures. The full unit
suite is not run; batch-end tests remain with the integrator.

## Limits

The binding uses four public pages. The sources describe canary mechanics,
mirroring idempotency, shared infrastructure, data-store sharing, schema
backward compatibility, feature flags and blue/green cost. None tests a canary
against an incompatible schema, measures a mirrored write, or proves that a
shared store is safe. The owner section and card label the exposure/data
separation, the reads-only default and the alternative-choice rule as Tycho
guidance. The `invariant` state is `supported` only because the claim
separates the source-supported shared-store and stateful-teeing evidence from
the Tycho exposure/data separation; a reviewer that requires every word to be
source-quoted should treat the dimension as partial instead. The
`alternative` state is `supported` only because the claim separates the
source-supported mirroring idempotency and strategy list from the Tycho
reads-only and choice rules; a reviewer that requires the rule itself to be
source-quoted should treat the dimension as partial instead.

The Flagger source is a living page represented by its official Markdown; the
HTML canonical digest includes rendered page content. The Google SRE chapter is
CC BY-NC-ND 4.0 and its examples are Google-specific. The AWS data page is part
of a whitepaper marked historical reference and is not a canary experiment. The
AWS not-recommended page was inspected but is not a binding unit.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer should
  check quote-to-claim fit for each dimension, the Tycho labels for the
  exposure/data separation, the reads-only mirroring default and the
  alternative-choice rule, the four revisions, the AWS not-recommended
  candidate, the metadata patch and the absence of a sufficient or promotion
  claim.
- The reviewer must use read-only repository access and must not run tests.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- the card path
  `book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
