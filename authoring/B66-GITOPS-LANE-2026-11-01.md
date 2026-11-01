# B66 — GitOps failure/recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-11-01. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and invariant were supported;
failure/recovery and alternative were partial. This lane binds both partial
dimensions to OpenGitOps, Argo CD and Flux public documentation, and labels the
controller-outage consequence, the four-failure catalogue and the selection
rule as Tycho guidance. The card remains inline in V11/C10. Label Tycho.

## Lane coordinates

- Parent HEAD: 24e019ce7e1727df74063ee45147fa11d322d7b2 (24e019ce).
- Lane label: Tycho.
- Branch: b66-gitops; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b66-gitops.
- Scope: the owner section "GitOps" in V08/C01, the inline "GitOps" card in
  V11/C10, and this note. Single-entry lane; no other entry, shared JSON,
  promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v08-delivery-deployment-and-recovery/
      c01-ci-cd-architecture-and-artifact-provenance/ci-cd-provenance-and-gitops.md

- Inline card path:
  book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md.
- Exactly three files change: the owner page, the inline card host and this
  note.
- Existing source ids: src.opengitops, src.argocd and src.flux. No new source
  identity is proposed.
- New ledger records proposed: ten, listed below.
- Retained historical record: read.batch5-opengitops.2026-10-21, kept as the
  earlier landing-page context and not the current binding.
- Baseline and final line-length and boundary checks pass.

## Card location

The registry records atlas_owner.chapter = V11/C10 and section gitops for this
pattern, and card-batches.v1.json records no card_path. The C10 chapter landing
already contains the card body, so this lane edits that inline block rather than
creating a dedicated page. The chapter frontmatter evidence_scope.source_ids
and notes are updated because they describe the cards hosted by that page; the
registry, card batches and atlas manifest are left for the integrator.
Precedent: B38, B53, B59, B60, B61, B62, B63 and B64 edited inline card hosts
and their chapter source lists the same way.

The task coordinates name V11/C10 inline card, which matches the registry
entry (edition/patterns/registry.v1.json lines 6192-6231) and the chapter
landing. No discrepancy was found.

## Baseline and gap

edition/patterns/owner-units.v1.json records mechanism as supported, invariant
as supported, failure_recovery as partial and alternative as partial. The
recorded reasons are:

- failure_recovery: "Local representation is landing plus four principles; no
  controller outage or drift recovery." Its quote is "Controller outage, drift,
  repository compromise and stale artifact references are common", and its
  binding is read.batch5-opengitops.2026-10-21, section "Pulled Automatically",
  quote "Software agents automatically pull the desired state declarations from
  the source.", revision
  61eb24afa22a5717ddbbc8941e2c10ec4cc2d3b5d7f6f59a407e1a337ed339fe.
- alternative: "Local representation has no pipeline-driven, manual or
  imperative alternative." Its quote is "A pipeline-driven deployment, manual
  release or imperative operator may be preferable when imperative one-off
  changes dominate or no reconciler owner exists."

The entry records technical_coverage partial-bounded, decision_coverage
partial-bounded and review_state self-checked. The summary records
failure_recovery_supported 91 and alternative_supported 95; the gitops entry
contributes to neither. The registry records technical_owner.state
partial-bounded, atlas_owner.state partial-bounded, coverage technical and
decision partial-bounded, one source unit (OpenGitOps — principles, record
read.batch5-opengitops.2026-10-21) and review_status self-checked.

The base owner page is 139 lines, 1,154 words, SHA-256
510ae871f131566a769caa590ff65f32ba7111fe9d4f3124f38bf6a7edc827ff. The base
owner GitOps section (lines 125-139) is 15 lines, 137 words, SHA-256
da34ac4fb08920d8328ed739262316285055deb410ade3eae8eea467f4c00ebd. The base
chapter landing is 283 lines, 1,207 words, SHA-256
cd6851c86a47986b29594fb99c3a2229f6f1af80df042aa6d6a106fef4784118. The base
card block (lines 162-193) is 32 lines, 149 words, SHA-256
ee855b2d6a8d6c8d300af3a5c8b94356ae9453e6d135cf746dd58359a884b158.

The final owner page is 192 lines, 1,828 words, SHA-256
db4ba0f8d6ef1c773711c8a15e70af8bc9e7d8aafded9fd98dc5405368cb1173. The final
owner GitOps section (lines 125-192) is 68 lines, 811 words, SHA-256
e5a4e6d3c83a7275a9cc343f371c7b9dbaf8e1ae219fe65f3fe3225e46128d1e. The final
chapter landing is 296 lines, 1,346 words, SHA-256
f688f91b82661ca0aefb5885948bbfaea1a075775878ae48208109bf901c0b04. The final
card block (lines 164-206) is 43 lines, 278 words, SHA-256
1dde5372ec19bcdaa87c958f9a48222ef8380f6c35a481a080593d39e7531b58.

The gap was evidential. The owner page and card already named controller
outage, drift, repository compromise, stale artifact references, pipeline
deployment, manual release and imperative operation as Tycho guidance, but no
exact public quote, section and representation hash bound those claims. Shared
metadata still shows 2/4 and partial-bounded until the integrator applies the
proposals below.

## Candidate evaluation

- OpenGitOps, GitOps Principles v1.0.0 (selected). The pinned document states
  the four principles and is the canonical vendor-neutral source; the site's
  landing page is retained as historical context.
- Argo CD, Automated Sync Policy (selected). Documents automatic sync against
  live state, self-heal, prune and manual sync, retry semantics, the rollback
  constraint and the sync interval.
- Argo CD, Diffing Customization (selected). Documents OutOfSync after a
  successful sync and controller or webhook mutation.
- Argo CD, Best Practices (selected). Documents leaving room for imperativeness
  and pinning Git revisions rather than moving remote bases.
- Argo CD, Security (selected). Documents repository write trust, malicious
  images and prune deletion.
- Argo CD, High Availability (selected). Documents controller polling,
  generated-manifest caching, repo-server failure/retry behavior and the
  largely stateless control plane.
- Flux, Core Concepts (selected). Documents GitOps, reconciliation, manual-edit
  reversion, the reconciliation interval and the Gitless model.
- Flux, Kustomization (selected). Documents drift detection and correction,
  suspension and the retry interval.
- Flux, GitRepository (selected). Documents commit-signature verification with
  trusted keys.
- Flux, Prometheus metrics (selected). Documents controller and resource
  metrics, including readiness.
- OpenGitOps website (examined, retained). Re-fetched 2026-11-01; the four
  principles match the pinned document; the site is moving, so the document is
  the binding revision.
- Argo CD FAQ, Monitoring and Disaster Recovery (examined, not selected). No
  selected statement describes controller-outage behavior; the metrics page
  would duplicate the Flux monitoring unit; disaster recovery covers export and
  import, not reconciliation failure.
- Flux FAQ and Security (examined, not selected). Reconciliation wording
  duplicates Core Concepts and Kustomization; security guidance is about RBAC
  and tenant impersonation, not the failure modes bound here.
- Vendor tutorials and third-party summaries (examined, not selected). They are
  not primary documentation and would add unverified restatements.

No Kubernetes cluster, Argo CD installation, Flux installation, reconciled
application, controller outage, repository compromise or artifact-verification
experiment was performed.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-11-01 (UTC), twice per
representation. Raw bytes were hashed from the served body (no compression was
requested). Where the same bytes were served twice, the table records one
SHA-256; every pair matched. Canonical extraction for HTML: select the main
element, drop script, style, nav, footer, header and aside subtrees, convert
block tags to newlines, strip remaining tags, decode entities, normalize
non-breaking spaces, typographic quotes and dashes to ASCII, remove heading
pilcrows, collapse space runs and blank lines, and strip. The pinned
OpenGitOps Markdown removes inline link targets, emphasis markers and heading
markers before the same whitespace normalization. Character counts include
spaces and newlines; word counts split on whitespace. Quoted fragments below
were checked against the canonical text after whitespace normalization.

### R1 — OpenGitOps, GitOps Principles v1.0.0

- Record: read.opengitops-principles.2026-11-01 (proposed).
- Source: src.opengitops (existing).
- URL: https://raw.githubusercontent.com/open-gitops/documents/v1.0.0/PRINCIPLES.md
- Label/type: "GitOps Principles v1.0.0"; specification document; tag v1.0.0.
- Representation: HTTP/2 200 on 2026-11-01T00:02:19Z and 00:02:20Z;
  995-byte Markdown; ETag
  "3ff9d79fb021438e46cd2c7332b6c5fd474b70116ad632ec34770f6c43d2a0d2";
  raw Markdown SHA-256
  8e72a33d840c0079fd7db54011e173bffd422fc17c1497c096c39c7dc8dced44 on both
  fetches. Canonical text 777 characters / 110 words, SHA-256
  543c25108834b745be6805551e537b64a2a2606ef5e482fb70965ad415447ccb.
- Sections read: the full document, including "Declarative", "Versioned and
  Immutable", "Pulled Automatically" and "Continuously Reconciled".
- Sections not read: the linked GLOSSARY and linked guidance pages.
- Claims supported: Q1-Q4.
- Limits: a short principles document; it states no controller behavior,
  failure mode, recovery procedure or implementation guidance. Licence:
  Creative Commons Attribution 4.0 (LICENSE.md at the same tag).

### R2 — Argo CD, Automated Sync Policy

- Record: read.argocd-auto-sync.2026-11-01 (proposed).
- Source: src.argocd (existing).
- URL: https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/
- Label/type: "Automated Sync Policy — Argo CD"; official documentation, read
  through the moving stable alias.
- Representation: HTTP/2 200 on 2026-11-01T00:02:21Z and 00:02:22Z;
  84,263-byte HTML; Last-Modified Tue, 04 Aug 2026 08:58:04 GMT; ETag
  W/"ff38c1bd00764fb2893de596e76d5bf6"; raw HTML SHA-256
  96dcceaa8ed4d04960e871503f8efb25b78616ca91d2f5b0ac991ed9eab936aa on both
  fetches. Canonical text 5,505 characters / 817 words, SHA-256
  a040e013515b199f0dd55d9a17eed3787c1caa0db350fcfd52742508ffde1311.
- Sections read: the full page, including "Automatic Pruning", "Automatic
  Self-Healing", "Automatic Retry with a limit" and "Automated Sync Semantics".
- Sections not read: linked pages, images and examples outside the page.
- Claims supported: Q5-Q12.
- Limits: vendor documentation for one controller; it describes intended
  behavior, not an outage or failure drill. The stable alias is not a version
  pin; the ETag, Last-Modified and canonical hash pin this representation.

### R3 — Argo CD, Diffing Customization

- Record: read.argocd-diffing.2026-11-01 (proposed).
- Source: src.argocd (existing).
- URL: https://argo-cd.readthedocs.io/en/stable/user-guide/diffing/
- Label/type: "Diffing Customization — Argo CD"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:02:23Z and 00:02:25Z;
  90,399-byte HTML; Last-Modified Tue, 04 Aug 2026 08:58:04 GMT; ETag
  W/"460d4f3967ee389de16b35665a7e41ae"; raw HTML SHA-256
  b211d5eb963dbc77c90b45db2f31bc16727122cc401342db64497d021999c06b on both
  fetches. Canonical text 6,980 characters / 940 words, SHA-256
  0bed4b0a57fc14884b69801d2509727941a01986e49c80407b50ba8e806c4d59.
- Sections read: the full page, including the OutOfSync reasons, "Application
  Level Configuration", "System-Level Configuration" and the drift-detection
  caveats.
- Sections not read: linked Kubernetes issues, source code and images.
- Claims supported: Q13-Q14.
- Limits: it explains why drift is observed and how to ignore fields; it does
  not measure drift frequency or an outage.

### R4 — Argo CD, Best Practices

- Record: read.argocd-best-practices.2026-11-01 (proposed).
- Source: src.argocd (existing).
- URL: https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/
- Label/type: "Best Practices — Argo CD"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:02:26Z and 00:02:27Z;
  76,747-byte HTML; Last-Modified Tue, 04 Aug 2026 08:58:04 GMT; ETag
  W/"3b25a0367841a9e5ed66c2ca49f58a43"; raw HTML SHA-256
  a5f4eda8478efb9565c1c3d6263df11f9bec5e0201acf717a85dd44b815d605a on both
  fetches. Canonical text 3,076 characters / 470 words, SHA-256
  f437ee2827494dc5da1bd1834ebb9479466234f2d52ffe4ea5d581b674653fed.
- Sections read: the full page, including "Separating Config Vs. Source Code
  Repositories", "Leaving Room For Imperativeness" and "Ensuring Manifests At
  Git Revisions Are Truly Immutable".
- Sections not read: linked pages and images.
- Claims supported: Q15-Q17.
- Limits: guidance, not a rule; it does not test a moving base or an
  imperative change.

### R5 — Argo CD, Security

- Record: read.argocd-security.2026-11-01 (proposed).
- Source: src.argocd (existing).
- URL: https://argo-cd.readthedocs.io/en/stable/operator-manual/security/
- Label/type: "Security — Argo CD"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:02:28Z and 00:02:29Z;
  98,339-byte HTML; Last-Modified Tue, 04 Aug 2026 08:58:04 GMT; ETag
  W/"6010a0a566cc80190106c934972b0505"; raw HTML SHA-256
  ac0a86ae4dbbfd379918b9c26f160392afcafc3b9d106deec7eba439ce55ad9f on both
  fetches. Canonical text 14,386 characters / 2,099 words, SHA-256
  fff8363f607b7968fb032a30660cd17c94bf9bfc9cfcbb22263f39653da88c3d.
- Sections read: the full page, including "Git & Helm Repositories",
  "Unauthorized Deployments", "Tool command invocation", "Remote bases and
  helm chart dependencies", "Secrets", "External Cluster Credentials" and
  "Cluster RBAC".
- Sections not read: linked hardening guides, source code and images.
- Claims supported: Q18-Q20.
- Limits: it states trust implications, not an exercised compromise; the page
  does not measure detection or recovery.

### R6 — Argo CD, High Availability

- Record: read.argocd-ha.2026-11-01 (proposed).
- Source: src.argocd (existing).
- URL: https://argo-cd.readthedocs.io/en/stable/operator-manual/high_availability/
- Label/type: "High Availability — Argo CD"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:02:30Z and 00:02:31Z;
  137,513-byte HTML; Last-Modified Tue, 04 Aug 2026 08:58:04 GMT; ETag
  W/"8fd31edc7344d71470625f86fd45b138"; raw HTML SHA-256
  12e0f80b7dba3296e2a8a1479b09517b669a157d5346fb87db698dece24f17ca on both
  fetches. Canonical text 34,719 characters / 4,899 words, SHA-256
  b7656c3fe3d19c8f9300d218059cde6fe04f31d4e71da8f9224a1bdce80e64ad.
- Sections read: the full page, including "Scaling Up", the
  argocd-repo-server and argocd-application-controller subsections, sharding,
  "Monorepo Scaling Considerations" and "Use Fully Qualified Git References".
- Sections not read: linked pages, source code and images.
- Claims supported: Q21-Q25.
- Limits: it describes availability and performance mechanics, not a
  controller-outage drill; it does not state that an outage halts
  reconciliation.

### R7 — Flux, Core Concepts

- Record: read.flux-concepts.2026-11-01 (proposed).
- Source: src.flux (existing).
- URL: https://fluxcd.io/flux/concepts/
- Label/type: "Core Concepts — Flux"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:02:32Z and 00:02:33Z;
  171,673-byte HTML; ETag "5eae9198227298f7113998e902a01e11-ssl"; raw HTML
  SHA-256
  67594741a3590127a6b09320eb824616df3865fd77278535c2b84a5676f30abe on both
  fetches. Canonical text 6,203 characters / 920 words, SHA-256
  dafb61f8bdef5a405d332a184592fc90662acd2accb1904a613950d5f82d7a5b. The page
  carries "Last modified 2026-04-20" (b36fcc8a).
- Sections read: the full page, including "GitOps", "Gitless GitOps", "GitOps
  Toolkit (gotk)", "Sources", "Reconciliation", "Kustomization", "Bootstrap",
  "Continuous Delivery", "Continuous Deployment" and "Progressive Delivery".
- Sections not read: linked pages and images.
- Claims supported: Q26-Q30.
- Limits: a concepts page; its "five minutes" default is illustrative and
  configurable; it states no outage behavior.

### R8 — Flux, Kustomization

- Record: read.flux-kustomization.2026-11-01 (proposed).
- Source: src.flux (existing).
- URL: https://fluxcd.io/flux/components/kustomize/kustomizations/
- Label/type: "Kustomization — Flux"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:02:35Z and 00:02:36Z;
  414,533-byte HTML; ETag "af0e7e0b273774b27e5d817e4f942a31-ssl"; raw HTML
  SHA-256
  b85783593ff286c27edd61a635aee206276fb57ef483c9cf0a1a0c062f76adaa on both
  fetches. Canonical text 76,767 characters / 10,166 words, SHA-256
  a9c5aa15a1306a073aca397e7211775077f135e1d291757447b2268bb760cd3d. No
  Last-Modified header or in-page revision marker was served.
- Sections read: the full page, including "Example", "Writing a Kustomization
  spec", "Source reference", "Prune", "Interval", "Retry interval", "Path",
  "Target namespace", "Suspend", "Health checks" and "Dependencies".
- Sections not read: linked API reference pages, source code and images.
- Claims supported: Q31-Q34.
- Limits: it documents controller behavior and configuration, not an outage or
  drift measurement; the page is large and only the named sections were used.

### R9 — Flux, GitRepository

- Record: read.flux-gitrepository.2026-11-01 (proposed).
- Source: src.flux (existing).
- URL: https://fluxcd.io/flux/components/source/gitrepositories/
- Label/type: "Git Repositories — Flux"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:02:37Z and 00:02:39Z;
  287,093-byte HTML; ETag "39aadaa6e32bedbbff9b5009a97c7fd4-ssl"; raw HTML
  SHA-256
  e777c0694ce2b4f5cc7e0bffb70fd386d002c853e51d672190be6de24f462cba on both
  fetches. Canonical text 39,762 characters / 5,235 words, SHA-256
  98680148d8d9f5ad57991ab20953187cb2ca90b0dbd34ea6fae0b583c12dc978. No
  Last-Modified header or in-page revision marker was served.
- Sections read: the full page, including "Artifact", "Secret reference",
  "Verification" and "SSH verification".
- Sections not read: linked API reference pages, source code and images.
- Claims supported: Q35-Q36.
- Limits: signature verification is optional configuration, not an enforced
  default; no key or repository was configured.

### R10 — Flux, Prometheus metrics

- Record: read.flux-monitoring.2026-11-01 (proposed).
- Source: src.flux (existing).
- URL: https://fluxcd.io/flux/monitoring/metrics/
- Label/type: "Flux Prometheus metrics — Flux"; official documentation.
- Representation: HTTP/2 200 on 2026-11-01T00:02:40Z and 00:02:41Z;
  174,714-byte HTML; ETag "37b1eeae940dc54d7f9561617791a3d7-ssl"; raw HTML
  SHA-256
  c77926ad06fbc2e50e8c6cf5fc24dd2abecd0f102d16dbb617be4722e00fbc80 on both
  fetches. Canonical text 7,082 characters / 920 words, SHA-256
  64f28e79497797a2088aed2a3a0cc2e1d00fea20dff408ddb4edd4eed6f30160. The page
  carries "Last modified 2025-05-02" (49b0a264).
- Sections read: the full page, including "Controller metrics", "Resource
  metrics", "Monitoring setup" and "Flux Grafana dashboards".
- Sections not read: the linked example repository, dashboards and images.
- Claims supported: Q37-Q40.
- Limits: it lists metric names and labels; it does not prescribe alerts,
  thresholds or a runbook.

## Selected exact quotes

Quotes reproduce the served prose after the normalization above. Typographic
quotes and dashes are ASCII in this note. Line breaks inside quotes are
editorial wrapping and are not part of the source text. Forty numbered
fragments were checked against the ten canonical representations on 2026-11-01;
40/40 were present. The owner and card use a subset; every fragment used there
was also checked. Q numbers group fragments by source and dimension, not by
page order.

### Mechanism

- Q1, R1, "Pulled Automatically": "Software agents automatically pull the
  desired state declarations from the source."
- Q2, R1, "Versioned and Immutable": "Desired state is stored in a way that
  enforces immutability, versioning and retains a complete version history."
- Q3, R1, "Continuously Reconciled": "Software agents continuously observe
  actual system state and attempt to apply the desired state."
- Q4, R1, "Declarative": "A system managed by GitOps must have its desired
  state expressed declaratively."
- Q5, R2, "Automated Sync Policy": "Argo CD has the ability to automatically
  sync an application when it detects differences between the desired manifests
  in Git, and the live state in the cluster."
- Q6, R2, "Automated Sync Policy": "CI/CD pipelines no longer need direct
  access to the Argo CD API server to perform the deployment."
- Q7, R2, "Automated Sync Policy": "Instead, the pipeline makes a commit and
  push to the Git repository with the changes to the manifests in the tracking
  Git repo."
- Q8, R2, "Automatic Self-Healing": "By default, changes that are made to the
  live cluster will not trigger automated sync."
- Q12, R2, "Automated Sync Semantics": "The automatic sync interval is
  determined by the timeout.reconciliation value in the argocd-cm ConfigMap,
  which defaults to 120s with added jitter of 60s for a maximum period of
  3 minutes."
- Q26, R7, "GitOps": "GitOps is a way of managing your infrastructure and
  applications so that whole system is described declaratively and version
  controlled, and having an automated process that ensures that the deployed
  environment matches the state specified in one or more Git repositories."
- Q27, R7, "Reconciliation": "Reconciliation refers to ensuring that a given
  state (e.g. application running in the cluster, infrastructure) matches a
  desired state declaratively defined somewhere (e.g. a Git repository)."
- Q28, R7, "Kustomization": "The reconciliation runs every five minutes by
  default, but this can be changed with .spec.interval."

### Invariant

- Q9, R2, "Automated Sync Semantics": "Automatic sync will not reattempt a sync
  if the previous sync attempt against the same commit-SHA and parameters had
  failed."
- Q10, R2, "Automated Sync Semantics": "Rollback cannot be performed against an
  application with automated sync enabled."
- Q16, R4, "Ensuring Manifests At Git Revisions Are Truly Immutable": "it is
  possible for manifests to change their meaning from one day to the next."
- Q17, R4, "Ensuring Manifests At Git Revisions Are Truly Immutable": "A better
  version would be to use a Git tag or commit SHA."
- Q35, R9, "Verification": ".spec.verify is an optional field to enable the
  verification of Git commit signatures."
- Q36, R9, "Verification": "Containing the public keys of trusted Git authors."

### Failure and recovery

- Q13, R3, "Diffing Customization": "It is possible for an application to be
  OutOfSync even immediately after a successful Sync operation."
- Q14, R3, "Diffing Customization": "A controller or mutating webhook is
  altering the object after it was submitted to Kubernetes so it differs from
  the one in Git."
- Q9 and Q10, R2, "Automated Sync Semantics", as above.
- Q11, R2, "Automatic Pruning": "To prune the resources, a manual sync can
  always be performed (with pruning checked)."
- Q18, R5, "Git & Helm Repositories": "gaining unauthorized write access to a
  git repository trusted by Argo CD will have serious security implications".
- Q19, R5, "Unauthorized Deployments": "an attacker with access to a trusted git
  repo would be able to affect the Kubernetes resources which are deployed."
- Q20, R5, "Unauthorized Deployments": "an attacker could update the deployment
  manifest deploy malicious container images to the environment, or delete
  resources in git causing them to be pruned in the live environment."
- Q21, R6, "High Availability": "Argo CD is largely stateless."
- Q22, R6, "High Availability": "A set of HA manifests are provided for users
  who wish to run Argo CD in a highly available manner."
- Q23, R6, "argocd-repo-server": "Argo CD assumes by default that manifests only
  change when the repo changes, so it caches the generated manifests (for 24h
  by default)."
- Q24, R6, "argocd-repo-server": "With Kustomize remote bases, or in case a Helm
  chart gets changed without bumping its version number, the expected manifests
  can change even though the repo has not changed."
- Q25, R6, "argocd-application-controller": "The controller polls Git every 3m
  by default."
- Q29, R7, "Kustomization": "If you make any changes to the cluster using
  kubectl edit/patch/delete, they will be promptly reverted. You either suspend
  the reconciliation or push your changes to a Git repository."
- Q31, R8, "Example": "every ten minutes, the Kustomization runs a server-side
  apply dry-run to detect and correct drift inside the cluster."
- Q32, R8, "Interval": "correcting any existing drift in the process."
- Q33, R8, "Suspend": "When a Kustomization is suspended, new Source revisions
  are not applied to the cluster and drift detection/correction is paused."
- Q34, R8, "Retry interval": ".spec.retryInterval is an optional field to
  specify the interval at which to retry a failed reconciliation."
- Q37, R10, "Flux Prometheus metrics": "Flux has native support for Prometheus
  metrics to provide insights into the state of the Flux components."
- Q38, R10, "Flux Prometheus metrics": "These can be used to set up monitoring
  for the Flux controllers."
- Q39, R10, "Resource metrics": "gotk_resource_info provides information about
  the current state of Flux resources."
- Q40, R10, "Resource metrics": "ready shows the readiness of the resource."

### Alternative

- Q6 and Q7, R2, "Automated Sync Policy", as above.
- Q11, R2, "Automatic Pruning", as above.
- Q15, R4, "Leaving Room For Imperativeness": "It may be desired to leave room
  for some imperativeness/automation, and not have everything defined in your
  Git manifests."
- Q30, R7, "Gitless GitOps": "In the Gitless GitOps model, the Flux controllers
  are fully decoupled from Git, relying solely on container registries as the
  source of truth for the desired state of Kubernetes clusters."

## Owner page changes

The owner section "GitOps" is rewritten in three bounded parts and a source
note. The mechanism paragraph keeps the reviewed-intent definition and adds the
OpenGitOps, Argo CD and Flux descriptions. The invariant paragraph keeps the
revert-commit rule and adds the repository-trust and commit-signature
statements. A new "Failure and recovery (Tycho synthesis)" paragraph names the
four failure modes, binds drift, failed-sync retry, rollback, repository write
access, manifest caching and remediation signals, and labels the
controller-outage consequence and the runbook as Tycho guidance. A new
"Alternative (Tycho comparison)" paragraph binds pipeline deployment, manual
sync, imperative changes and the Gitless source model, and labels the selection
rule as Tycho guidance. A new "Sources and limits" paragraph lists the ten
proposed records and the limits.

The owner frontmatter changes updated_at from 2026-10-21 to 2026-11-01. The
owner evidence_scope is unchanged because the page is covered by the
decomposition metadata guard; adding source ids there would require a separate
authorized metadata revision, as in B38.

## Card changes

The V11/C10 "GitOps" card keeps its ten contract fields. Good-fit conditions
add repository write access, commit-signature verification and reconciliation
monitoring. Hard contraindications add unverifiable desired-state revisions and
artifact references. Competing alternative and Failure and recovery are
rewritten to name the bound Argo CD and Flux statements and to keep the
selection rule as Tycho synthesis. Sources lists the retained record and the ten
proposed records. The chapter frontmatter adds src.argocd and src.flux to
evidence_scope.source_ids, updates the notes, review date, updated_at and
source_inspection_date. The Technical owner line and the other eleven cards are
unchanged.

## Proposed shared metadata

The lane does not edit any shared JSON. The proposals below are for the
integrator; applying them is what moves the entry from 2/4 to 4/4.

### reading-ledger.v1.json

Add ten records. All use access_date 2026-11-01, access_method "public HTTPS
GET; served representation inspected", reviewer "Automated authoring agent"
and status "read". The content_sha256 values are the canonical-text hashes
above and must match the owner-units revisions.

- read.opengitops-principles.2026-11-01 — src.opengitops; URL as in R1;
  unit_label "OpenGitOps — GitOps Principles v1.0.0"; unit_type
  specification; sections_read as in R1; sections_not_read "linked GLOSSARY and
  guidance pages"; content_sha256
  543c25108834b745be6805551e537b64a2a2606ef5e482fb70965ad415447ccb;
  characters/words 777 / 110; claims_supported Q1-Q4; claims_not_supported
  controller behavior, failure mode, recovery procedure, implementation
  guidance; limitations as in R1.
- read.argocd-auto-sync.2026-11-01 — src.argocd; content_sha256
  a040e013515b199f0dd55d9a17eed3787c1caa0db350fcfd52742508ffde1311;
  5,505 / 817; claims Q5-Q12.
- read.argocd-diffing.2026-11-01 — src.argocd; content_sha256
  0bed4b0a57fc14884b69801d2509727941a01986e49c80407b50ba8e806c4d59;
  6,980 / 940; claims Q13-Q14.
- read.argocd-best-practices.2026-11-01 — src.argocd; content_sha256
  f437ee2827494dc5da1bd1834ebb9479466234f2d52ffe4ea5d581b674653fed;
  3,076 / 470; claims Q15-Q17.
- read.argocd-security.2026-11-01 — src.argocd; content_sha256
  fff8363f607b7968fb032a30660cd17c94bf9bfc9cfcbb22263f39653da88c3d;
  14,386 / 2,099; claims Q18-Q20.
- read.argocd-ha.2026-11-01 — src.argocd; content_sha256
  b7656c3fe3d19c8f9300d218059cde6fe04f31d4e71da8f9224a1bdce80e64ad;
  34,719 / 4,899; claims Q21-Q25.
- read.flux-concepts.2026-11-01 — src.flux; content_sha256
  dafb61f8bdef5a405d332a184592fc90662acd2accb1904a613950d5f82d7a5b;
  6,203 / 920; claims Q26-Q30.
- read.flux-kustomization.2026-11-01 — src.flux; content_sha256
  a9c5aa15a1306a073aca397e7211775077f135e1d291757447b2268bb760cd3d;
  76,767 / 10,166; claims Q31-Q34.
- read.flux-gitrepository.2026-11-01 — src.flux; content_sha256
  98680148d8d9f5ad57991ab20953187cb2ca90b0dbd34ea6fae0b583c12dc978;
  39,762 / 5,235; claims Q35-Q36.
- read.flux-monitoring.2026-11-01 — src.flux; content_sha256
  64f28e79497797a2088aed2a3a0cc2e1d00fea20dff408ddb4edd4eed6f30160;
  7,082 / 920; claims Q37-Q40.

Each record also carries the unit_url, sections_not_read and limitations from
its R subsection, plus the license note "public documentation; cite short
excerpts and paraphrase; do not mirror".

### sources/register.json

- src.opengitops: reading_status full-public-page-inspected; access_checked and
  content_verified 2026-11-01; version "GitOps Principles v1.0.0 at tag v1.0.0;
  raw PRINCIPLES.md 995 bytes, SHA-256
  8e72a33d840c0079fd7db54011e173bffd422fc17c1497c096c39c7dc8dced44; canonical
  text 777 characters / 110 words, SHA-256
  543c25108834b745be6805551e537b64a2a2606ef5e482fb70965ad415447ccb; site
  landing re-fetched 2026-11-01 as historical context, canonical text 2,064
  characters, SHA-256
  3843d6d81260d8a2b0721f5bd3ccfa9ace15d6a41e4d1934a109e216afffa443";
  verification_scope "Full PRINCIPLES.md v1.0.0 read
  2026-11-01: Declarative, Versioned and Immutable, Pulled Automatically and
  Continuously Reconciled. Linked GLOSSARY and guidance pages were not read."
- src.argocd: reading_status full-public-page-inspected; access_checked and
  content_verified 2026-11-01; version "Argo CD documentation read through the
  readthedocs stable alias on 2026-11-01; five pages with Last-Modified
  2026-08-04T08:58:04Z and per-page ETags and canonical hashes recorded in
  authoring/B66-GITOPS-LANE-2026-11-01.md; the alias is not a version pin";
  verification_scope listing Automated Sync Policy, Diffing Customization, Best
  Practices, Security and High Availability, and saying linked pages and images
  were not read.
- src.flux: reading_status full-public-page-inspected; access_checked and
  content_verified 2026-11-01; version "Flux documentation fetched 2026-11-01;
  four pages with per-page ETags and canonical hashes recorded in the lane
  note; Core Concepts carries Last modified 2026-04-20 and Prometheus metrics
  Last modified 2025-05-02; Kustomization and GitRepository served no revision
  marker"; verification_scope listing the four pages, and saying linked API
  references, source code and images were not read.

### source-plan.v1.json

Replace the single required_units entry for tycho.pattern.gitops with the ten
units below, in R1-R10 order, each with source_id, unit label, unit_type,
exact R URL, sections list, status read, read_record_id and blocked_reason
null. Then update the summary and notes:

- required_units 356 -> 365; read_units 355 -> 364; ledger_records
  317 -> 327; updated 2026-11-01.
- notes: "OpenGitOps principles v1.0.0, Argo CD reconciliation, drift,
  security and availability, and Flux concepts, drift, verification and
  metrics bound 2026-11-01; no runtime test or promotion."

### owner-units.v1.json

Keep the owner document id, path, heading, anchor, level and line 125. Keep
unit_kind dedicated; add unit terms "drift owner", "commit signature" and
"manifest cache" if the integrator wants them. Technical evidence:

- mechanism: state supported, claim quote unchanged: "GitOps treats a
  versioned desired-state repository as reviewed intent." Reason: OpenGitOps
  requires declarative, versioned and automatically pulled desired state;
  Argo CD compares manifests in Git with live state; Flux describes an
  automated process that matches the deployed environment to the repository.
  Primary binding: src.opengitops, record
  read.opengitops-principles.2026-11-01, section "Pulled Automatically",
  quote Q1, revision 543c2510.... Supporting: Q2 and Q4 (same record), Q5
  (record read.argocd-auto-sync.2026-11-01, revision a040e013...) and Q26
  (record read.flux-concepts.2026-11-01, revision dafb61f8...).
- invariant: state supported, claim quote unchanged: "Rollback is a revert
  commit, which needs a linear, reviewable history and an immutable artifact
  reference." Reason: OpenGitOps requires versioned and immutable desired
  state; Argo CD disables rollback under automated sync and recommends a Git
  tag or commit SHA; Flux can verify commit signatures against trusted keys.
  Primary binding: src.opengitops, section "Versioned and Immutable", quote
  Q2, revision 543c2510.... Supporting: Q10 (record
  read.argocd-auto-sync.2026-11-01), Q17 (record
  read.argocd-best-practices.2026-11-01, revision f437ee28...), Q35 and Q36
  (record read.flux-gitrepository.2026-11-01, revision 98680148...).
- failure_recovery: state supported. Claim quote: "Controller outage, drift,
  repository compromise and stale artifact references are the common failures:
  reconciliation is periodic and controller-driven, a green sync does not prove
  convergence, failed syncs are not retried against the same revision, and a
  trusted repository is a deployment path." Reason: Argo CD can be OutOfSync
  immediately after a successful sync because a controller or webhook changes
  the object; automated sync does not reattempt the same failed revision and
  cannot roll back while enabled; the repo-server caches generated manifests
  and remote bases can change without a repo change; write access to a trusted
  repository lets an attacker deploy malicious images or prune live resources;
  Flux reverts direct cluster edits and pauses drift correction only when
  suspended. Primary binding: src.argocd, record
  read.argocd-diffing.2026-11-01, section "Diffing Customization", quote Q13,
  revision 0bed4b0a.... Supporting: Q14 (same record), Q9, Q10 and Q11
  (record read.argocd-auto-sync.2026-11-01), Q23, Q24 and Q25 (record
  read.argocd-ha.2026-11-01, revision b7656c3f...), Q18-Q20 (record
  read.argocd-security.2026-11-01, revision fff8363f...), Q29 (record
  read.flux-concepts.2026-11-01) and Q40 (record
  read.flux-monitoring.2026-11-01, revision 64f28e79...). The controller-outage
  consequence and the runbook are Tycho guidance; no selected page states that
  an outage halts reconciliation.
- alternative: state supported. Claim quote: "A pipeline that applies directly
  remains a valid deployment model, a manual sync remains available for
  pruning, and an imperative change is sometimes deliberate:". Reason: Argo CD
  says automatic sync removes the pipeline's need for direct API access and
  that the pipeline instead commits to Git; a manual sync remains available;
  Argo CD recommends leaving room for imperativeness; Flux documents a
  registry-backed Gitless model. Primary binding: src.argocd, record
  read.argocd-auto-sync.2026-11-01, section "Automated Sync Policy", quote Q6,
  revision a040e013.... Supporting: Q7 and Q11 (same record), Q15 (record
  read.argocd-best-practices.2026-11-01) and Q30 (record
  read.flux-concepts.2026-11-01). The selection rule is Tycho guidance; the
  sources document options, not a preference.

Other owner-units fields:

- technical_coverage partial-bounded (all four dimensions supported but no
  promotion, so the schema-derived value remains partial-bounded);
  decision_coverage partial-bounded; review_state self-checked.
- notes: "Four dimensions bound 2026-11-01 to OpenGitOps principles v1.0.0,
  Argo CD auto-sync, diffing, best practices, security and high availability,
  and Flux concepts, Kustomization, GitRepository and Prometheus metrics; the
  controller-outage consequence and selection rule remain Tycho; coverage
  partial-bounded; no promotion."
- source_support: primary ledger_record read.opengitops-principles.2026-11-01,
  source_id src.opengitops, unit_type specification, status read,
  card_citation true; auxiliary entries for the nine Argo CD and Flux records.
- decision_evidence.competing_alternative: the new card text; decision_state
  applicable-under-conditions; card_components 10; atlas_section gitops.
- Summary: failure_recovery_supported 91 -> 92; alternative_supported
  95 -> 96. No other counter changes; technical_partial_bounded stays 15 and
  technical_partial stays 51.

### registry.v1.json

For tycho.pattern.gitops: keep technical_owner.state partial-bounded and
atlas_owner.state partial-bounded; keep coverage technical, decision and
overall partial-bounded; replace source_units with the ten records above, all
status read; keep review_status self-checked, confidence high and the V11/C10
atlas owner. Replace notes with "Four dimensions bound 2026-11-01 to
OpenGitOps principles v1.0.0, Argo CD reconciliation, drift, security and
availability, and Flux concepts, drift, verification and monitoring; coverage
partial-bounded; no promotion." The entry has no updated_at field, so none is
added.

### card-batches.v1.json

No change. The card remains inline in V11/C10, so card_path stays absent and
ledger_record stays read.batch5-opengitops.2026-10-21 for the historical record.
After the integrator adds the new records, preflight will still report
card_path missing until a card_path is registered; that is an integration
step, not a lane failure.

### content-revisions.json and derived artifacts

Add one issue-540 revision with authorized_at 2026-11-01 and authorization
"B66 GitOps failure/recovery and alternative source binding; no promotion or
owner acceptance." Raw hashes for reference:

- Owner path: previous
  510ae871f131566a769caa590ff65f32ba7111fe9d4f3124f38bf6a7edc827ff; current
  db4ba0f8d6ef1c773711c8a15e70af8bc9e7d8aafded9fd98dc5405368cb1173.
- Card path: previous
  cd6851c86a47986b29594fb99c3a2229f6f1af80df042aa6d6a106fef4784118; current
  f688f91b82661ca0aefb5885948bbfaea1a075775878ae48208109bf901c0b04.

The revision record must use the repository's historical-view hashing, not
these raw hashes; recompute both before saving. The book edit changes one
canonical owner page and one atlas chapter, so the atlas manifest (new V11/C10
chapter SHA-256 f688f91b..., new owner SHA-256 db4ba0f8...), route index,
edition inventory and the coverage, census, reverse-map, semantic-audit and
delivery artifacts are stale. Refresh them once at batch end; do not treat a
stale derived hash as a lane content failure.

## Verification

Commands run in
/Users/rbaranov/Projects/tycho-worktrees/b66-gitops:

- python3 scripts/check_markdown_line_length.py
  Result: PASS: V11 prose <=100; 145 exact owner-link exceptions.
- python3 scripts/check_boundary.py
  Result: PASS: configured lexical boundary checks; independent-origin review
  still required.
- Quote check: 40 named passages and fragments checked against the ten
  canonical representations; 40/40 present after whitespace normalization.
- python3 scripts/validate_book_metadata.py
  Result: PASS; 517 documents, complete coverage, 17 topics.
- python3 scripts/validate_pattern_cards.py
  Result: PASS; 11 batches, 145 entries.
- python3 scripts/validate_sources.py
  Result: PASS; 340 source records.
- python3 scripts/validate_enrichment.py
  Result: PASS; explicit membership and byte conservation.
- python3 scripts/validate_decomposition.py
  Result: PASS; 69 chapters, 739 source blocks, 839 fragment routes.
- python3 scripts/validate_pattern_owner_units.py
  Result: FAIL: owner-units-quote-not-verbatim: tycho.pattern.gitops:
  failure_recovery. This is the expected consequence of the no-shared-JSON
  constraint: the owner-units entry still holds the superseded claim quote and
  the partial states.
- python3 scripts/preflight_sufficient.py --pattern tycho.pattern.gitops
  Result: FAIL: failure_recovery and alternative state partial; card_path
  missing or absent. Expected until the proposed metadata is applied.
- python3 scripts/validate_pattern_atlas.py
  Result: FAIL: atlas-document-sha. Expected because the chapter and owner
  hashes changed and the derived manifest was not refreshed.

git status before this note: exactly the owner page and the V11/C10 landing.

No full unit suite was run. The lane is a content slice; the batch-end suite is
the integrator's step.

## Limits

- Coverage and review are self-checked. No independent AI review, owner
  acceptance, promotion, CI result or production observation is claimed.
- The binding is documentation only. No Kubernetes cluster, Argo CD
  installation, Flux installation, controller outage, repository compromise,
  drift injection or signature-verification test was performed.
- No selected page states that a controller outage halts reconciliation. The
  pages document periodic polling, the largely stateless control plane and HA
  manifests; the causal consequence is Tycho guidance and is labelled in the
  owner page.
- Argo CD documentation was read through the moving stable alias. The ETag,
  Last-Modified and canonical hash pin the 2026-11-01 representation, but the
  alias may serve different text later.
- Flux Kustomization and GitRepository served no Last-Modified header or
  in-page revision marker; only the ETag and canonical hash pin those
  representations.
- The owner page narrows "manual release" to the manual-sync capability that
  Argo CD documents; a separate manual release process is not bound by a
  selected page.
- The Gitless model is a source-model alternative, not a pipeline, manual or
  imperative deployment alternative; it is reported separately in the owner
  page and is not used to claim the deployment alternative.
- The card remains inline in V11/C10; this lane did not create a second card.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- the card path book/volumes/v11-pattern-atlas/c10-deployment-modernization/
  README.md.

No shared JSON, promotion, test or generated file is in the lane commit.
