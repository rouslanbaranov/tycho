# B41 — Immutable infrastructure invariant and failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and alternative were supported;
invariant and failure/recovery were partial. This lane binds both partial
dimensions to public IBM, AWS and HashiCorp pages and labels the digest record
rule and the rebuild-equality test as Tycho. The card remains inline in V11/C10.

## Lane coordinates

- Parent HEAD: `8491390e7dbd3de3849acfa2b0b2dac019e46627` (`8491390e`).
- Branch: `b41-immutable`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b41-immutable`.
- Scope: the owner page `# Immutable Infrastructure` in V08/C03 and the
  inline V11/C10 card `### Immutable Infrastructure`. Single-entry lane; no
  other entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v08-delivery-deployment-and-recovery/
      c03-vms-containers-orchestration-and-serverless/
      immutable-infrastructure.md

- Card path:
  `book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md`.
- Current source register: `src.ibm-immutable-infrastructure` is admitted.
  This lane proposes two new source ids, `src.aws-immutable-infrastructure`
  and `src.hashicorp-immutable-vms`, and a new full-page IBM ledger record
  under the existing IBM source id.
- Baseline line-length and boundary checks pass before and after the edit.

## Candidate evaluation

- IBM, "What is Immutable Infrastructure?" (selected). The retained
  2026-10-21 record documents replacement, externalized state and rollback.
  A 2026-10-30 fetch returned 183,332 bytes and was byte-identical across two
  fetches. The retained record was fetched through a 100,000-character cap and
  cannot be reproduced from the full page; this lane adds a new full-page
  record instead of overwriting it. The page supplies version-controlled,
  tested and reproducible changes, clean-image rollback and redeployment of the
  previous image.
- AWS, "REL08-BP04 Deploy using immutable infrastructure" (selected). It
  directly states reproducibility as a deployment goal, describes replacement
  from a version-controlled configuration, says unmanaged drift should be
  detected and remediated, and keeps the previous working version unchanged
  for rollback.
- HashiCorp, "Create immutable virtual machines" (selected). It binds
  identical machine images to drift prevention, rebuild-and-replace, rollback
  by recreating the previous image from its template, and image metadata that
  records which commit built each image.
- HashiCorp, "Create immutable infrastructure" (examined, not selected). It
  covers drift, identical artifacts and audit trails, but the virtual-machine
  page binds rebuild and rollback more directly.
- HashiCorp, "Create immutable containers" (examined, not selected). Its
  rollback workflow is similar, but the virtual-machine page matches the
  machine-image owner claim and records build ancestry.
- HashiCorp, "Reference artifact metadata" (examined, not selected). It
  describes metadata references but does not use the term digest; it adds no
  binding beyond the selected page.
- IBM "Recovery" is a section of the selected article, not a separate unit.
  The existing AWS blue/green whitepaper is registered for another entry and
  was not re-read for this lane.

## Source binding

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. The binding revision is the SHA-256 of the raw served HTML, the same
convention as the retained records. Source punctuation is preserved in this
note; page prose uses straight apostrophes except where a source fragment is
quoted directly.

### IBM — What is Immutable Infrastructure?

- Source id: `src.ibm-immutable-infrastructure` (existing).
- New record: `read.ibm-immutable.2026-10-30`.
- Retained record: `read.batch5-ibm-immutable.2026-10-21`, revision
  `44075e8bbd9269c29e14d87fa34e51f3efb5593f2e2dbd1a03b925358ae1de72`.
- URL: `https://www.ibm.com/think/topics/immutable-infrastructure`.
- Unit label: "What is Immutable Infrastructure? — IBM (full page,
  2026-10-30)"; unit type `article`; access date 2026-10-30.
- Representation: HTTP 200, 183,332 bytes, HTTP Date
  2026-10-30T22:09:00Z, Last-Modified 2026-10-30T22:09:00Z, ETag
  `W/"2cab1-65f160b208221-gzip"`; raw HTML SHA-256
  `22bb64044ae882898ff1ceda85658cf2c803a93cbc2cd2b843e36652ac590a14`.
  A second fetch is byte-identical. Extracted text SHA-256
  `2b7f841387e268240154a9d2decb06f312e567a10d91ba4b3e47e51ab1cc32c8`.
- Sections used: "Provisioning with infrastructure as code"; "Recovery".
- Exact quotes:

      All infrastructure changes are then documented in version control systems like Git,
      ensuring they’re tested and reproducible.

      Each update creates a new instance, maintaining a clean image for rollback. The same
      automation tools that provision and deploy can restore previous versions in minutes.
      Teams redeploy the previous image rather than debugging and troubleshooting modified
      servers—greatly reducing the detective work traditionally required when configuration
      management changes fail.

- Representation gap: the retained 2026-10-21 record is a 100,000-character
  truncated representation and its revision is not the full-page digest. The
  new record is the exact full-page revision; the retained record is not
  replaced. This is recorded as a representation gap, not treated as a source
  change.
- Limits: one public article; it does not require a digest format, measure a
  rebuild or prove that a rebuilt image equals the deployed one.

### AWS — REL08-BP04 Deploy using immutable infrastructure

- Source id: `src.aws-immutable-infrastructure` (proposed).
- Proposed record: `read.aws-immutable-infrastructure.2026-10-30`.
- URL (concatenate the two lines):

      https://docs.aws.amazon.com/wellarchitected/latest/framework/
      rel_tracking_change_management_immutable_infrastructure.html

- Unit label: "REL08-BP04 Deploy using immutable infrastructure — AWS
  Well-Architected Framework"; unit type `documentation-page`; access date
  2026-10-30.
- Representation: HTTP 200, 32,762 bytes, HTTP Date 2026-10-30T22:09:38Z,
  Last-Modified 2026-10-30T15:49:55Z, ETag
  `"XI7XaRYf/JCp5wA9BlKtrPe42/U="`; raw HTML SHA-256
  `5023f6f37c78581aeb9040d28ae31774f7e729e2e1f2643e47e56aad5e77e77b`.
  A second fetch is byte-identical. Extracted text SHA-256
  `5ccc56d9a9719a6f4656ff48588a5ac7bb301dd5b80bb582640b9207250e2343`.
- Sections used: "REL08-BP04 Deploy using immutable infrastructure";
  "Drift detection".
- Exact quotes:

      Follow an immutable infrastructure deployment strategy to increase the reliability,
      consistency, and reproducibility in your workload deployments.

      Any type of unmanaged configuration change goes against the notion of immutable
      infrastructure, and should be detected and remediated in order to have a successful
      implementation of immutable infrastructure.

      Safer deployments with fast rollback and recovery processes: Deployments are safer
      because the previous working version is not changed. You can roll back to it if errors
      are detected.

- Limits: one public documentation page; it does not require an artifact digest,
  describe a rebuild test, or measure drift detection.

### HashiCorp — Create immutable virtual machines

- Source id: `src.hashicorp-immutable-vms` (proposed).
- Proposed record: `read.hashicorp-immutable-vms.2026-10-30`.
- URL (concatenate the two lines):

      https://developer.hashicorp.com/well-architected-framework/
      define-and-automate-processes/define/immutable-infrastructure/virtual-machines

- Unit label: "Create immutable virtual machines — HashiCorp Well-Architected
  Framework"; unit type `documentation-page`; access date 2026-10-30.
- Representation: HTTP 200, 176,803 bytes, HTTP Date
  2026-10-30T17:41:27Z, ETag `"10ys8gurzgz3sex"`; no Last-Modified; raw
  HTML SHA-256
  `d5c0484691a4f9b512a72bbdf7c171a937eb71ca1753e823336be1520a3f53d2`.
  A second fetch is byte-identical. Extracted text SHA-256
  `4a125cd5ab68390ab5b8eeeac220de3aedec14aad45f543e085945473c20d774`.
- Sections used: "Why use immutable virtual machines"; "Immutable VM
  workflow".
- Exact quotes:

      Immutable virtual machines prevent drift by deploying identical machine images,
      ensuring every VM across all environments matches your defined configuration exactly.

      Rollback if needed: If the new version causes issues, run packer build with your
      previous Packer template to recreate the old image, then run terraform apply.

      Track image metadata: Use HCP Packer to store metadata about your machine images,
      tracking which Git commit built each image, which environments are running each
      version, and the full ancestry of your image builds.

- Limits: one public documentation page; it describes a rebuild-and-rollback
  workflow but does not require digest equality or measure a rebuild.

## Book edits

### Owner page

- Frontmatter: only `updated_at` moves from 2026-10-29 to 2026-10-30.
  `evidence_scope`, `source_inspection_date`, `content_review` and
  `content_verified_at` are unchanged. The new records are supporting
  bindings, not new `evidence_scope` ids.
- The mechanism sentence, the invariant sentence, the failure sentence and
  the alternative sentence are unchanged. This preserves the existing
  verbatim owner-unit quotes.
- A new invariant paragraph binds AWS reproducibility, version-controlled
  replacement and drift detection/remediation; HashiCorp identical machine
  images and commit metadata; and IBM version control, testing and
  reproducibility. `**Tycho record rule:**` labels the digest as Tycho's
  concrete record identity and states that no source mandates a digest format.
- A new failure paragraph binds HashiCorp rebuilding the previous image,
  redeploying it and recording build ancestry; IBM redeploying the previous
  image and retaining a clean image for rollback; and AWS keeping the previous
  working version for rollback. `**Tycho failure test:**` labels digest
  comparison and rebuild exercise as Tycho, not a source claim.
- The `### Immutable Infrastructure` heading stays at line 44. The page grows
  from 74 to 89 lines. The `## Navigation` heading moves from line 68 to 83.
- Raw SHA-256:
  `731b921ea79587646dffd5903663c36e11674d1bef7caff870e1b5bcbbcb98a1`.
- Historical-view SHA-256:
  `3745c093c2ff1ab8ab4e6b3cb1bb868705aa65c3ad537b8f7c335bae2ad393b2`.
- Base raw SHA-256:
  `49d7ede5a997e84e82a8409a55ef47aca4c80a627d6c9293f42056fcd945f790`;
  base historical-view and directory-baseline SHA-256:
  `6381e3290347e1d978689873e7db5a31cdcd1aabacef531d81402e54359cb0c9`.

### V11/C10 inline card

- `evidence_scope.source_ids` adds `src.aws-immutable-infrastructure` and
  `src.hashicorp-immutable-vms`; `src.ibm-immutable-infrastructure` was
  already declared once and stays once. Other frontmatter is unchanged; the
  card dates were already 2026-10-30.
- **Good-fit conditions** add recorded artifacts, drift detection and
  remediation, and an automated rebuild path.
- **Hard contraindications** add an untestable artifact identity or rebuild
  path.
- **Failure and recovery** now states that a rebuilt image can differ from the
  deployed artifact, requires recorded digests, a tested rebuild path and
  rollback, and binds AWS drift remediation, HashiCorp rebuild/rollback
  metadata and IBM tested/reproducible changes. Rebuilt-versus-deployed digest
  comparison is labelled Tycho guidance.
- **Sources** names the retained and full-page IBM records, the AWS record and
  the HashiCorp record; it states that the units are public documentation, not
  benchmarks.
- The `### Immutable Infrastructure` heading moves from line 217 to 219
  because the two source ids precede it. `### Strangler Fig` moves from 248
  to 260 and later headings shift accordingly. The chapter page is 373 lines.
- Raw SHA-256:
  `309016ce38f537d2e388d0d670220d48173ced170de2f26f4b656d4121fc2f60`.
- Historical-view SHA-256:
  `b11a72829e4ccfe5b75dcf7aa792f4e3670ed7ac786d54edbd615fe83b3558a0`.
- Base raw SHA-256:
  `74bdb64fe5d10d78acc76e373ae688b3add09089a8c6122045e075b4448d89f6`;
  base historical view:
  `e9dafd6c43ceb511af1510a738c0af0f3b1ba98f68d55ea40aa9e5da5e93f0e1`;
  directory-baseline SHA-256:
  `dffed0a0c31023b87696c64cd838fe8defe739cc06825aff369bd558003c2976`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following changes are not in the lane commit. They were exercised in a
detached scratch copy of this worktree with the two book files plus the source
register, ledger, source plan, registry, owner units, content revision and
atlas manifest. The scratch results are in the Validation section; no scratch
file is part of the lane commit.

### Source register `sources/register.json`

Set `updated` to 2026-10-30; the source count moves from 301 to 303.

- `src.aws-immutable-infrastructure` — title "REL08-BP04 Deploy using
  immutable infrastructure"; category `delivery`; publisher "Amazon Web
  Services"; kind `official-docs`; URL the AWS page above; resolved URL the
  same; topics `["deployment-architecture","software-delivery",
  "immutable-infrastructure","drift"]`; priority `core`; planned use
  "Immutable deployment reproducibility, drift detection and rollback for the
  immutable-infrastructure invariant and failure/recovery dimensions.";
  admission `admitted-for-research`; access
  `public-web-or-author-download`; reading status
  `full-public-page-inspected`; version records the 2026-10-30 access,
  32,762-byte HTML, raw HTML SHA-256 `5023f6f3...`, HTTP Date
  2026-10-30T22:09:38Z, Last-Modified 2026-10-30T15:49:55Z, ETag
  `XI7XaRYf/JCp5wA9BlKtrPe42/U=` (without the surrounding quotes) and the
  absence of a separate version identifier; `access_checked` and
  `content_verified` 2026-10-30; license note "Public AWS documentation;
  cite short excerpts and paraphrase; do not mirror."; verification scope
  names the full page and the sections above, and excludes linked pages and
  images; observed title "REL08-BP04 Deploy using immutable infrastructure -
  AWS Well-Architected Framework".
- `src.hashicorp-immutable-vms` — title "Create immutable virtual
  machines"; category `software-delivery`; publisher "HashiCorp"; kind
  `official-docs`; URL the HashiCorp page above; resolved URL the same;
  topics `["deployment-architecture","software-delivery",
  "immutable-infrastructure","packer"]`; priority `core`; planned use
  "Immutable VM rebuild, rollback and image metadata for the
  immutable-infrastructure failure/recovery dimension."; admission
  `admitted-for-research`; access `public-web-or-author-download`; reading
  status `full-public-page-inspected`; version records the 2026-10-30
  access, 176,803-byte HTML, raw HTML SHA-256 `d5c04846...`, HTTP Date
  2026-10-30T17:41:27Z, ETag `10ys8gurzgz3sex` (without the surrounding
  quotes), no Last-Modified and no separate version identifier;
  `access_checked` and `content_verified` 2026-10-30; license note "Public
  HashiCorp documentation; cite short excerpts and paraphrase; do not mirror.";
  verification scope names the full page and the sections above, and excludes
  linked pages and images; observed title "Create immutable virtual machines |
  Well-Architected Framework | HashiCorp Developer".
- `src.ibm-immutable-infrastructure` — set `reading_status` to
  `full-public-page-inspected`; set `access_checked` and
  `content_verified` to 2026-10-30. Append to `version`: full 183,332-byte
  HTML fetched 2026-10-30; raw HTML SHA-256 `22bb6404...`; HTTP Date and
  Last-Modified 2026-10-30T22:09:00Z; ETag
  `W/"2cab1-65f160b208221-gzip"`; the retained 2026-10-21 fetch was
  truncated at 100,000 characters. Append to `verification_scope`: "Full
  page re-read 2026-10-30 for the invariant and failure/recovery dimensions;
  linked pages and images were not read." Do not change the URL or admission
  state.

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add three records; set `updated` to 2026-10-30. Records move from 200 to 203.
Each record is `status: read`, `reviewer: "Automated authoring agent"`, and
uses the exact URL, label, sections and `content_sha256` below.

- `read.ibm-immutable.2026-10-30` — source
  `src.ibm-immutable-infrastructure`; label "What is Immutable
  Infrastructure? — IBM (full page, 2026-10-30)"; type `article`; sections
  "What is immutable infrastructure?", "How does immutable infrastructure
  work?", "Provisioning with infrastructure as code", "Deployment through
  CI/CD pipelines", "External data storage", "Recovery", "Benefits of
  immutable infrastructure", "Predictable server state", "Improved horizontal
  scalability", "Enhanced security", "Challenges of immutable
  infrastructure"; content_sha256
  `22bb64044ae882898ff1ceda85658cf2c803a93cbc2cd2b843e36652ac590a14`.
- `read.aws-immutable-infrastructure.2026-10-30` — source
  `src.aws-immutable-infrastructure`; label "REL08-BP04 Deploy using
  immutable infrastructure — AWS Well-Architected Framework"; type
  `documentation-page`; sections "REL08-BP04 Deploy using immutable
  infrastructure", "Benefits of establishing this best practice",
  "Implementation guidance", "Drift detection", "Implementation steps",
  "Resources"; content_sha256
  `5023f6f37c78581aeb9040d28ae31774f7e729e2e1f2643e47e56aad5e77e77b`.
- `read.hashicorp-immutable-vms.2026-10-30` — source
  `src.hashicorp-immutable-vms`; label "Create immutable virtual machines —
  HashiCorp Well-Architected Framework"; type `documentation-page`; sections
  "Create immutable virtual machines", "Why use immutable virtual machines",
  "Build machine images with Packer", "Deploy immutable VMs with Terraform",
  "Query machine images dynamically", "Immutable VM workflow", "HashiCorp
  resources", "Next steps"; content_sha256
  `d5c0484691a4f9b512a72bbdf7c171a937eb71ca1753e823336be1520a3f53d2`.

The retained `read.batch5-ibm-immutable.2026-10-21` record stays unchanged.

### Source plan `edition/patterns/source-plan.v1.json`

Append three units to `tycho.pattern.immutable-infrastructure` after the
existing IBM unit, in this order:

1. IBM full page: label "What is Immutable Infrastructure? — IBM (full page,
   2026-10-30)", type `article`, URL
   `https://www.ibm.com/think/topics/immutable-infrastructure`, record
   `read.ibm-immutable.2026-10-30`, sections equal to that record's
   eleven-entry `sections_read`.
2. AWS: label "REL08-BP04 Deploy using immutable infrastructure — AWS
   Well-Architected Framework", type `documentation-page`, URL the AWS page
   above, record `read.aws-immutable-infrastructure.2026-10-30`, sections
   equal to that record's six-entry `sections_read`.
3. HashiCorp: label "Create immutable virtual machines — HashiCorp
   Well-Architected Framework", type `documentation-page`, URL the HashiCorp
   page above, record `read.hashicorp-immutable-vms.2026-10-30`, sections
   equal to that record's eight-entry `sections_read`.

Set every unit `status` to `read` and `blocked_reason` to `null`.
Replace the entry notes with: "Invariant and failure/recovery bound
2026-10-30 to AWS REL08-BP04, HashiCorp immutable VMs and IBM's full page;
digest recording and rebuild equality remain Tycho."

Summary: `required_units` 241 -> 244; `read_units` 240 -> 243;
`blocked_units` stays 1; `ledger_records` 200 -> 203. Recompute
`registry_sha256` after saving the registry; the scratch serialization
produced
`ce103091c2ba1248e4dce5479487081e94a3f428759354701e6e47c200f7cebc`,
but the authoritative value is the SHA-256 of the saved registry file. Refresh
`route_index_snapshot` from the rebuilt route index; the scratch route build
produced
`afe5cc87eb64c08a918b35ba15b534cdd7c32b9f563ab9c2840012d31f68512b`.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.immutable-infrastructure`:

- Set `technical_owner.state` to `partial-bounded`; keep
  `atlas_owner.state` at `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to `partial-bounded`;
  keep `coverage.decision` at `partial-bounded`.
- Append the three units above to `source_units` after the existing IBM unit,
  in the source-plan order, all with status `read`; the unit labels must
  equal the plan labels.
- Replace `notes` with the source-plan notes plus "Coverage partial-bounded;
  no promotion."
- Keep `review_status` `self-checked`. The registry pattern entry has no
  `updated_at` field in the current schema; do not add one.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.immutable-infrastructure`:

- Keep `owner.line` at 44, the heading, document id and unit terms unchanged.
- Invariant: set `state: supported`; keep the existing `quote` ("Every
  running instance must be reproducible from a recorded artifact digest, and
  drift must be detected rather than tolerated."). Reason: "AWS describes
  version-controlled replacement and reproducibility and states that unmanaged
  drift should be detected and remediated; HashiCorp deploys identical machine
  images and describes recording build metadata; IBM documents changes as
  tested and reproducible. The digest is Tycho's recording rule, labelled in
  the page."
  Primary binding `src.aws-immutable-infrastructure`, record
  `read.aws-immutable-infrastructure.2026-10-30`, section "REL08-BP04 Deploy
  using immutable infrastructure", quote "Follow an immutable infrastructure
  deployment strategy to increase the reliability, consistency, and
  reproducibility in your workload deployments.", revision `5023f6f3...`.
  Supporting bindings: AWS drift quote "Any type of unmanaged configuration
  change goes against the notion of immutable infrastructure, and should be
  detected and remediated in order to have a successful implementation of
  immutable infrastructure.", same record, section "Drift detection", same
  revision; HashiCorp "Immutable virtual machines prevent drift by deploying
  identical machine images, ensuring every VM across all environments matches
  your defined configuration exactly.", `src.hashicorp-immutable-vms`,
  record `read.hashicorp-immutable-vms.2026-10-30`, section "Why use
  immutable virtual machines", revision `d5c04846...`; IBM "All
  infrastructure changes are then documented in version control systems like
  Git, ensuring they’re tested and reproducible.", existing IBM source id,
  record `read.ibm-immutable.2026-10-30`, section "Provisioning with
  infrastructure as code", revision `22bb6404...`.
- Failure/recovery: set `state: supported`; keep the existing `quote` ("A
  rebuilt image that no longer matches the deployed artifact turns replacement
  into an uncontrolled change; record digests and test the rebuild path.").
  Reason: "HashiCorp describes rebuilding the previous image, redeploying it
  and recording build metadata; IBM redeploys the previous image and describes
  tested, reproducible changes; AWS keeps the previous working version
  unchanged for rollback. Comparing rebuilt and deployed digests is Tycho's
  failure test, labelled in the page." Primary binding
  `src.hashicorp-immutable-vms`, record
  `read.hashicorp-immutable-vms.2026-10-30`, section "Immutable VM
  workflow", quote "Rollback if needed: If the new version causes issues, run
  packer build with your previous Packer template to recreate the old image,
  then run terraform apply.", revision `d5c04846...`. Supporting bindings:
  HashiCorp "Track image metadata: Use HCP Packer to store metadata about your
  machine images, tracking which Git commit built each image, which
  environments are running each version, and the full ancestry of your image
  builds.", same record and section, same revision; IBM recovery quote "Each
  update creates a new instance, maintaining a clean image for rollback. The
  same automation tools that provision and deploy can restore previous
  versions in minutes. Teams redeploy the previous image rather than debugging
  and troubleshooting modified servers—greatly reducing the detective work
  traditionally required when configuration management changes fail.",
  `src.ibm-immutable-infrastructure`, record
  `read.ibm-immutable.2026-10-30`, section "Recovery", revision
  `22bb6404...`; IBM change/reproducibility quote from "Provisioning with
  infrastructure as code", same record and revision; AWS rollback quote
  "Safer deployments with fast rollback and recovery processes: Deployments
  are safer because the previous working version is not changed. You can roll
  back to it if errors are detected.", record
  `read.aws-immutable-infrastructure.2026-10-30`, section "REL08-BP04 Deploy
  using immutable infrastructure", revision `5023f6f3...`.
- `source_support`: keep `read.batch5-ibm-immutable.2026-10-21` as the
  primary record and add auxiliary entries for
  `read.ibm-immutable.2026-10-30` (`22bb6404...`),
  `read.aws-immutable-infrastructure.2026-10-30` (`5023f6f3...`) and
  `read.hashicorp-immutable-vms.2026-10-30` (`d5c04846...`).
- Set `technical_coverage` to `partial-bounded`. Set `notes` to:
  "Invariant and failure/recovery bound 2026-10-30 to AWS REL08-BP04,
  HashiCorp immutable VMs and IBM's full page. Digest recording and rebuild
  equality remain Tycho. Coverage partial-bounded; no promotion or
  acceptance."
- The card's competing alternative and decision state are unchanged, so
  `decision_evidence.competing_alternative` and `decision_state` stay
  unchanged.
- Summary counters: `invariant_supported` 73 -> 74;
  `failure_recovery_supported` 67 -> 68; `technical_partial_bounded` 16 ->
  17; `technical_partial` 75 -> 74. `technical_sufficient` stays 54.

### Card registration `edition/patterns/card-batches.v1.json`

No card-path or ledger-record change is required; the card remains inline in
V11/C10 and keeps `read.batch5-ibm-immutable.2026-10-21` as its primary
record. If a later promotion is prepared, add `card_path`:
`book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md`.
The sufficient preflight currently stops only at `card_path missing or
absent`; all evidence checks pass in the scratch patch.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B41 immutable infrastructure invariant and failure/recovery source binding;
no promotion or owner acceptance." Use these historical-view hashes:

- Owner path, previous:
  `6381e3290347e1d978689873e7db5a31cdcd1aabacef531d81402e54359cb0c9`;
  current:
  `3745c093c2ff1ab8ab4e6b3cb1bb868705aa65c3ad537b8f7c335bae2ad393b2`.
- Card path, previous (directory baseline):
  `dffed0a0c31023b87696c64cd838fe8defe739cc06825aff369bd558003c2976`;
  current:
  `b11a72829e4ccfe5b75dcf7aa792f4e3670ed7ac786d54edbd615fe83b3558a0`.
- Also add an `enrichment_documents` entry for the owner page's historical
  path `book/volumes/v08/c03/immutable-infrastructure.md`, previous
  `6381e329...`, current `3745c093...`. This is required by
  `validate_enrichment.py`; the page is a registered new enrichment document.
- Leave `source_blocks`, `enrichment_additions` and
  `enrichment_baselines` empty.

Raw file hashes for reference:
`731b921ea79587646dffd5903663c36e11674d1bef7caff870e1b5bcbbcb98a1`
(owner) and
`309016ce38f537d2e388d0d670220d48173ced170de2f26f4b656d4121fc2f60`
(card).

### Atlas manifest `edition/atlas-manifest.json`

Set the V11/C10 document `sha256` to
`309016ce38f537d2e388d0d670220d48173ced170de2f26f4b656d4121fc2f60` and
`registry_sha256` to the new registry file hash
(`ce103091...` in the scratch serialization).

### Frontmatter and evidence scope

The lane leaves the owner page's `evidence_scope`,
`source_inspection_date` and `content_review` unchanged. The new records are
supporting bindings, not new `evidence_scope` ids; this also keeps
`validate_enrichment.py`'s expected owner source list unchanged. The card
gains the two source ids listed above because preflight requires every binding
source to be declared on the card. If the integrator also wants the new
records in the owner `evidence_scope.source_ids`, treat it as a separate
change: update `edition/enrichment-manifest.json`, recompute both
historical-view hashes and the content revision, and re-run the decomposition
and enrichment validators.

### Derived artifacts and review metadata

The book edit changes one canonical owner page and one atlas chapter. The
source register gains two ids, the ledger gains three records, and the source
plan, registry, owner units, content revision and atlas manifest change.
Refresh once at batch end: route index, page census, coverage/reverse map,
phase 4, delivery-evidence counts, edition inventory and the source catalogue
(`python3 scripts/source_catalog.py`). The semantic audit records a hash
change for both pages and requires re-review; do not treat a stale derived
hash as a lane content failure or update the semantic-audit sha without
review.

## Validation

Checker output in the lane worktree after the two book edits:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still required.

Owner-section quote audit: every quoted fragment in the added invariant and
failure/recovery paragraphs is a whitespace-normalized substring of the IBM,
AWS and HashiCorp pages listed above. The Tycho-labelled sentences are not
presented as source quotes.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_pattern_cards.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_registry.py` — PASS; 145 entries.
- `python3 scripts/validate_pattern_owner_units.py` — PASS; 145 entries
  (the metadata still records the two dimensions as partial, and both quotes
  remain verbatim).
- `python3 scripts/validate_pattern_sources.py` — PASS; 240 read; 200
  ledger records (the lane changes no source metadata).
- `python3 scripts/validate_book_metadata.py` — FAIL unknown source ID for
  the card's two new source ids; integrator register work.
- `python3 scripts/validate_pattern_atlas.py` — FAIL
  `atlas-document-sha` in the lane tree.
- `python3 scripts/validate_decomposition.py` — PASS.
- `python3 scripts/validate_enrichment.py` — FAIL
  `enrichment-new-document-drift` until the content revision is applied.
- `python3 scripts/validate_directory_migration.py` — FAIL
  `directory-baseline-payload-drift` until the content revision is applied.

In the detached scratch copy with the metadata patch above:

    PASS: source plan 145 entries; 243 read; 203 ledger records
    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: 303 source records, mandatory IDs, cross-references and catalogue
    freshness after one source_catalog.py regeneration
    PASS: 494 documents, structural metadata and registry references
    PASS: atlas V11 11 chapters, 71 documents, 145 patterns
    PASS: directory migration; 494 canonical documents
    PASS: decomposition; 739 preserved source blocks, 174 new question pages
    PASS: enrichment; explicit membership and byte conservation
    FAIL: sufficient preflight for tycho.pattern.immutable-infrastructure
    - card_path missing or absent

The full unit suite was not run; batch-end tests remain with the integrator.

## Limits

The binding uses three public pages. They describe version-controlled
replacement, reproducibility, drift detection and remediation, rebuild,
rollback and build metadata. None observes this page's service, mandates a
digest format, proves that a rebuilt artifact equals the deployed one, or
measures a recovery window.

The invariant and failure/recovery dimensions are `supported` only because
the page separates the source-supported claims (versioned artifacts,
reproducibility, drift detection, rebuild, rollback, metadata) from the Tycho
judgments that a digest is the record identity and that rebuild equality must
be tested. A reviewer that requires every word of either dimension quote to be
source-quoted should treat both as partial.

The IBM full-page record is new because the retained record is a truncated
representation; the retained record is not overwritten. No build, deployment,
drift detection or rollback was run. The pages are living documentation; their
raw digests are the binding revisions on 2026-10-30.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer
  should check quote-to-claim fit for both dimensions, the Tycho record rule
  and failure test, the three revisions, the IBM representation gap, the
  unchanged owner-unit line and moved card anchor, the metadata patch and the
  absence of a sufficient or promotion claim.
- The reviewer must use read-only repository access and must not run tests.
- Owner acceptance, promotion, CI and merge permission are not claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- `book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
