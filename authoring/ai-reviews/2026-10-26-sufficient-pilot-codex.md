# Independent AI review — Tycho #540 sufficient pilot

**Overall verdict: reject promotion of this six-entry pilot at the reviewed snapshot.**
All six technical-sufficiency decisions are reject. Four decision-sufficiency assessments
pass; two pass with findings. None has both required passes, so no entry is recommended
for promotion by this report. `ai_review: performed`; `sufficient: 0`.

## Identity and snapshot

- Reviewer harness/vendor: Codex desktop app / OpenAI.
- Model: GPT-6 family according to session context; exact deployed version unavailable.
- Session ID: `01a17a03-0b7c-7513-87fe-1f3994862b1d`.
- Review timestamp: 2026-10-26T23:51:01+01:00, Europe/Zurich.
- Repository: `/Users/rbaranov/Projects/tycho`.
- Reviewed HEAD: `cf9e02f261d3eeeddd2e3541a5746e5a61500d12`.
- Reviewed branch: `feature/TYCHO-540-raise-pattern-atlas-coverage-from-sufficient-ready-to-sufficient`.
- Pilot baseline: `974de23d33ee0ab122ca1054479994573fdc0ebf`.
- Instruction set: the owner's request and
  `authoring/AI-REVIEW-HANDOFF-SUFFICIENT-PILOT_2026-10-26.md` at the reviewed HEAD.
- Policy: `governance/SUFFICIENT-COVERAGE.md` at the reviewed HEAD.
- Prior involvement: I reviewed #535 evidence and remediation in this same external chat;
  I did not author these six entries or the promotion tooling.

During the review, the original checkout changed externally to branch `main`, HEAD
`0f3ece31252c499a258371978279c2f34ed3663f`. The pilot handoff and manifest are absent there.
It later returned to the pilot branch at `a4975a6b3d1deffc6e13169cb2b1fe909c8d3ed9`.
I did not switch or restore branches. The relevant owner/card/source artifacts and policy
are unchanged between cf9e02f2 and that later commit; new batch/tooling changes are outside
this report. Tests and the formal verdict are pinned to the preserved initial HEAD above.

## Scope and policy application

Read all six named owner units, their atlas-card sections, owner-unit evidence records,
registry entries, the eleven manifest source-unit bindings and ten distinct ledger
records. Recomputed all six owner-page and six card-file hashes. The manifest hashes whole
owner pages and whole chapter card files; it does not hash individual sections separately.
There are five distinct owner files and two distinct card files.

Freshly retrieved the ten public ledger URLs; inspected relevant passages in their HTML
or PDF representations. Also inspected a matching preserved ASVS overview representation.
This is a source-support review, not a full rereading of all documents or the whole atlas.

Technical policy item 2 requires mechanism, invariant, failure/recovery and alternative
to be supported by an admitted source at the recorded revision and scope. Merely finding
those sentences in Tycho does not establish external-source support. Correctly labelling
guidance synthetic satisfies the labelling requirement; it does not satisfy item 2.

Decision sufficiency was assessed separately using the card's required components,
conditional state and source-boundary compatibility. A decision pass does not cancel a
technical rejection or authorize promotion.

## Per-entry decisions

PWF means pass-with-findings. Reject means that dimension does not meet the promotion
policy at this snapshot, not that the pattern is unusable.

| Entry | Technical | Decision | Main reason |
|---|---|---|---|
| Workload Identity / mTLS | reject | PWF | Unsupported alternative; stale card scope note. |
| Dark Launching / Shadow Traffic | reject | pass | Required invariant/containment partly synthetic. |
| RBAC / ABAC | reject | PWF | Synthetic failure guidance and conflicting source scope. |
| Federated Identity | reject | pass | Four-dimension source support not established. |
| Controlled Cutover | reject | pass | No-return/recovery evidence explicitly synthetic. |
| Parallel Run | reject | pass | Alternative and complete invariant lack bound support. |

All six retain `partial-bounded` technical, decision and overall coverage in the registry.
The promotion artifact contains zero promotion records. No premature sufficient state was
found. All cards contain the required components and explicitly conditional decision states.

## Blocking findings

### P540-01 — Source support is overstated in the four-dimension evidence fields

Location: `/Users/rbaranov/Projects/tycho/edition/patterns/owner-units.v1.json`,
`technical_evidence` for the six entries beginning at lines 8035, 7621, 7975, 7801,
7741 and 7561 respectively.

Every dimension is marked supported, but several quoted Tycho sentences are explicitly
outside their owner section's declared source boundary, or lack a matching bound source
passage. The evidence reasons sometimes establish only that the section states a rule.
That is insufficient under the policy's technical item 2.

Entry-specific evidence and required action:

1. **Workload Identity / mTLS.**
   Owner: `book/volumes/v09-observability-security-and-operations/`
   `c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md`,
   heading Workload Identity-mTLS, lines 118-140.
   The alternative quote recommends network policy/shared secrets when PKI is unavailable
   and compares operational cost with lateral-movement risk. The bound Istio record
   establishes identity provisioning, rotation, authentication and authorization, not that
   comparative recommendation. The source boundary says other guidance is synthetic.
   Supply source support for the alternative and the complete failure/recovery rule,
   or retain the unsupported dimensions as partial rather than sufficient.

2. **Dark Launching / Shadow Traffic.**
   Owner: `book/volumes/v08-delivery-deployment-and-recovery/`
   `c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md`,
   lines 111-135.
   The invariant requires a side-effect boundary, comparison method, load budget and
   sensitive-data rule. The owner boundary explicitly leaves side-effect suppression,
   measurement method and capacity bounds synthetic. The owner-unit evidence reason also
   acknowledges that limitation while marking the invariant supported. Fowler supports
   hidden invocation and switching it off; Istio supports real mirrored requests and
   discarded responses. They do not establish the complete quoted invariant or containment
   contract. Bind the supported clauses precisely and support or narrow the remainder.

3. **RBAC / ABAC.**
   Owner: `book/volumes/v09-observability-security-and-operations/`
   `c05-identity-authorization-and-threat-modeling/authorization-policy-and-least-privilege.md`,
   lines 107-130.
   The failure/recovery quote relies on role explosion and stale attributes. Lines 128-130
   explicitly classify role-explosion and attribute-freshness guidance as synthetic.
   The primary source-support record is the ASVS record; the NIST record supports
   component separation and policy administration, but the complete deterministic,
   versioned-policy invariant and quoted failure/recovery rule are not established by
   their current bindings. Provide exact source/requirement support per dimension, or
   keep the technical evidence partial. This is not a finding that those topics are
   absent from every possible public standard.

4. **Federated Identity.**
   Owner: the identity-and-isolation page above, Federated Identity, lines 93-116.
   The four supported fields include a compound stale-key/wrong-issuer failure sentence
   and a local-account lifecycle alternative. Current source summaries establish OAuth
   token handling and federation trust-chain/key-rollover mechanics, not the complete
   quoted failure and comparative alternative. A stale key does not by itself establish
   acceptance of a wrong issuer; distinguish validation rejection, compromised retained
   keys and over-broad trust configuration. Bind the relevant source passages to the
   actual claims rather than treating page presence as support.

5. **Controlled Cutover.**
   Owner: `book/volumes/v10-decision-support-and-modernization/`
   `c05-target-architecture-versus-transition-states/cutover-gates.md`, lines 131-150.
   The supported invariant and recovery quotes concern a no-return point and mandatory
   forward repair. The source boundary explicitly leaves general no-return gates and
   fallback execution synthetic. The Spanner record explicitly does not support a formal
   no-return point or fallback execution, and the primary owner-unit source-support
   record is Fowler's contextual Strangler article. The source-backed drain-and-switch
   sequence does not establish the general quoted recovery contract. Narrow the owner
   unit or provide admitted evidence for the missing dimensions.

6. **Parallel Run.**
   Owner: `book/volumes/v10-decision-support-and-modernization/`
   `c05-target-architecture-versus-transition-states/authority-states.md`, lines 130-147.
   MinimumCD supports dual execution, incumbent-only output, mismatch logging and a
   side-effect restriction. The quote additionally requires a divergence owner and names
   canary/shadow traffic as the alternative. The cited guide uses shadowing as a name
   for parallel run and recommends branch by abstraction for side effects or expand and
   contract for shared-schema changes. It does not establish this complete alternative
   quote. The primary source-support field still points to contextual Fowler Strangler.
   Correct the binding and source the alternative and remaining invariant clauses.

These findings do not require implementing every operational control or running a
benchmark. They require honest source support for the dimensions selected for promotion.

### P540-02 — Ledger scope fields contradict one another

Locations in `/Users/rbaranov/Projects/tycho/edition/patterns/reading-ledger.v1.json`:

- NIST record beginning line 5251: sections_read includes Conclusion and appendices,
  while sections_not_read excludes them and read_scope at line 5292 excludes appendices.
- OpenID record beginning line 5297: sections_read includes the full specification,
  sections_not_read excludes many of the same sections, and read_scope at line 5361
  still limits reading to sections 1,3,4,5,11.
- Spanner record beginning line 5366: ten headings are listed as read, while read_scope
  at line 5410 and limitations still describe three sections; What's next is both read
  and excluded.
- MinimumCD record beginning line 5415: eight headings are listed as read, while read_scope
  at line 5459 names six and excludes Next step/Related content.
- ASVS record beginning line 4545: complete-PDF claims coexist with an overview URL,
  overview content hash and a page-only read_scope.

Affected entries: RBAC/ABAC, Federated Identity, Controlled Cutover and Parallel Run.
The records have status read and nonempty hashes, but their exact reading scopes cannot
be determined consistently. Correct the contradictory fields and identify the actual
document representation. A previous package-level pass did not certify this new
sufficiency gate's exact dimension/source bindings.

### P540-03 — Two pinned source hashes were not reproduced; ASVS pins the wrong artifact

Affected records: RFC 9700, Spanner Cutover and ASVS. See the source manifest below.

Seven of ten fresh URL responses match their ledger content hashes. A preserved ASVS
overview also matches its ledger hash, bringing available exact representations to eight.
That overview is not the complete ASVS 5.0.0 PDF used for requirement-level assertions.

RFC 9700's fresh HTML hashes to c00e2234fcd7..., not the recorded 9919d061d40a....
Spanner's fresh response hashes to 4107463035ed..., not 7770d4c9e13b....
These differences are not proof that substantive source text changed: Google HTML can
include changing chrome, and the new RFC representation matches another available cache.
However, an exact expected representation or an explicit normalized-hash comparison to
that expected representation was not established for these two records.

Required action: preserve/reproduce the expected bytes or document the hash domain and
reconcile the relevant source content. Pin the actual ASVS document separately. Do not
silently replace the reviewed source revision when promoting an entry.

## Non-blocking decision-card findings

### P540-04 — Stale scope notes and duplicated source prose

Location: `/Users/rbaranov/Projects/tycho/book/volumes/v11-pattern-atlas/`
`c11-security-operations/README.md`.

- Workload Identity / mTLS, lines 245-249: says all 34 headings were read but still
  refers to eight cited sections without identifying that subset.
- RBAC / ABAC, lines 208-217: describes the old fourteen-heading ASVS overview, while
  the pilot source unit now names the full requirement document; source prose is also
  duplicated across consecutive lines.

Required action: state precisely which representation and subset each note describes,
and remove the duplicate prose. These cards pass the component-presence check but receive
decision PWF until their source notes are reconciled.

The other four decision passes concern conditional editorial decision framing only.
Their source notes label the operational limits rather than claiming measured results.

## Synthetic-only claims and source boundaries

The owner pages mostly label synthetic guidance clearly. The misrepresentation arises
when the owner-unit metadata nevertheless calls the complete quoted dimensions supported.
Examples include dark-launch load/side-effect contracts, RBAC freshness/role explosion,
cutover no-return/forward repair, and comparative alternatives. These are useful design
judgments, but their usefulness is not source evidence.

The workload statement that certificate issuance availability is part of the request path
is explicitly labelled synthetic. It should still be qualified: the Istio source describes
startup provisioning, local delivery of certificates and periodic renewal, not a CA call
for each application request. Labels do not resolve that architectural ambiguity.

Unmeasured costs, thresholds, revocation propagation and recovery guarantees remain
unverified. No local execution or production observation is inferred from the sources.

## Mechanical checks actually run

All tests ran on the isolated copy at
`/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/work/pilot540/tree`.

Interpreter:
`/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/work/venv/bin/python`.

Each script invocation was `<interpreter> -B scripts/<name>.py`.

| Script/check | Exit |
|---|---:|
| validate_sufficient_pilot.py | 0 |
| validate_sufficient_promotions.py | 0 |
| validate_pattern_owner_units.py | 0 |
| validate_pattern_registry.py | 0 |
| validate_pattern_sources.py | 0 |
| validate_pattern_cards.py | 0 |
| validate_delivery_evidence.py | 0 |
| check_boundary.py | 0 |
| unittest discover -s tests -p test_tycho_sufficient_pilot.py | 0 |

The unittest run executed one test. All 12 owner/card hash comparisons pass.
All eleven source-unit bindings match the source plan on every field represented in the
manifest; the source plan additionally records unit_type. The six owner headings/anchors,
registry identities and card owners align. No promotion records exist.

These successful structural checks do not validate the truth of source-support flags.
The pilot validator explicitly validates inputs without performing content review.

## Limits and next action

This review is bounded to the six pilot entries at cf9e02f2. It does not revisit all
155 reading units, certify whole-book completeness, or assess unrelated promotion-tool
implementation. Source figures, examples and runtime security behaviour were not executed
or independently reproduced. Full source rereading was not claimed.

The checkout changed externally during the run, so a whole-run unchanged-repository
claim would be inaccurate. The reviewer issued no write, checkout, commit, PR or
configuration mutation against the original repository. Working copies and reports
were written outside it. The later checkout/tooling is not a separately tested snapshot.

Retain all six entries as partial-bounded. Correct the dimension/source mappings and
reading-scope metadata, reconcile pinned representations, then request a focused review
of the changed evidence. Do not add promotion records based on this report.

No owner acceptance, CI execution, merge permission or sufficient coverage is claimed.
The author must save this report verbatim and index its hash; the reviewer has not
performed that repository write.

## Public sources inspected

- [Istio security](https://istio.io/latest/docs/concepts/security/): identity provisioning,
  certificate management and authentication/authorization sections.
- [Fowler Dark Launching](https://martinfowler.com/bliki/DarkLaunching.html): full article.
- [Istio mirroring](https://istio.io/latest/docs/tasks/traffic-management/mirroring/):
  mirror mechanism, examples and source limitations.
- [ASVS overview](https://owasp.org/www-project-application-security-verification-standard/):
  current redirect and matching preserved overview; complete PDF not represented by its hash.
- [NIST SP 800-162](https://doi.org/10.6028/NIST.SP.800-162): relevant ABAC and policy sections.
- [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html): relevant token/issuer/audience rules.
- [OpenID Federation](https://openid.net/specs/openid-federation-1_0.html): validation/rollover.
- [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html): article context.
- [Spanner cutover](https://docs.cloud.google.com/spanner/docs/mysql-perform-cutover):
  prechecks, drain, verification and switch.
- [MinimumCD Parallel Run](https://beyond.minimumcd.org/docs/foundations/evolutionary-coding/parallel-run/):
  mechanism, comparison, pitfalls and alternatives.

## review-manifest

```json
{
  "name": "review-manifest",
  "issue": 540,
  "harness": "Codex desktop app",
  "vendor": "OpenAI",
  "model_family": "GPT-6",
  "exact_model_version": "not available",
  "session_id": "01a17a03-0b7c-7513-87fe-1f3994862b1d",
  "timestamp": "2026-10-26T23:51:01+01:00",
  "timezone": "Europe/Zurich",
  "repository": "/Users/rbaranov/Projects/tycho",
  "review_head": "cf9e02f261d3eeeddd2e3541a5746e5a61500d12",
  "review_branch": "feature/TYCHO-540-raise-pattern-atlas-coverage-from-sufficient-ready-to-sufficient",
  "pilot_baseline": "974de23d33ee0ab122ca1054479994573fdc0ebf",
  "verdict": "reject",
  "ai_review": "performed",
  "sufficient": 0,
  "promotions": 0,
  "per_entry": [
    {
      "pattern_id": "tycho.pattern.workload-identity-mtls",
      "technical": "reject",
      "decision": "pass-with-findings"
    },
    {
      "pattern_id": "tycho.pattern.dark-launching-shadow-traffic",
      "technical": "reject",
      "decision": "pass"
    },
    {
      "pattern_id": "tycho.pattern.rbac-abac",
      "technical": "reject",
      "decision": "pass-with-findings"
    },
    {
      "pattern_id": "tycho.pattern.federated-identity",
      "technical": "reject",
      "decision": "pass"
    },
    {
      "pattern_id": "tycho.pattern.controlled-cutover",
      "technical": "reject",
      "decision": "pass"
    },
    {
      "pattern_id": "tycho.pattern.parallel-run",
      "technical": "reject",
      "decision": "pass"
    }
  ],
  "findings": {
    "blocking": [
      "P540-01 source-support overstatement",
      "P540-02 contradictory reading scopes",
      "P540-03 unreconciled source representations"
    ],
    "non_blocking": [
      "P540-04 stale and duplicated source notes"
    ]
  },
  "artifact_sha256": {
    "authoring/AI-REVIEW-HANDOFF-SUFFICIENT-PILOT_2026-10-26.md": "605da4187a66019c202be767bc92aa9db451248bb97243261b49d6f1ac1bc11e",
    "governance/SUFFICIENT-COVERAGE.md": "efe256029be3995a9a5238d335a03ceaaeec5464183113fdf12d27ea97f84c8d",
    "research/sufficient-pilot-540/manifest.json": "3d5ad3e19d28a2dcc212819fc1d7ace6c7e65f178fa6f112ef6ea6958a007666",
    "edition/patterns/owner-units.v1.json": "60901dc89dfad1456e70f851fb72027d92669c11725f5bc4544b72b773c5f455",
    "edition/patterns/reading-ledger.v1.json": "7c014b58551beeb75c8b345f482fd6fe446a3fd3eeaf8073c2ca81531c97e655",
    "edition/patterns/source-plan.v1.json": "30f5a6bc84eca684193d045815f457218d6bf1d430887b8f9b7f8c3ca98873c1",
    "edition/patterns/registry.v1.json": "17177bf1c79789a4cc0c664f1883875e4261c049012af000e3c7863fa3853a97"
  },
  "owner_and_card_hash_checks": [
    {
      "pattern_id": "tycho.pattern.workload-identity-mtls",
      "path": "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md",
      "sha256": "41462a8c2c148e93cd602b969b0021113263ffb434243218a5c53c0792461bbd",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.workload-identity-mtls",
      "path": "book/volumes/v11-pattern-atlas/c11-security-operations/README.md",
      "sha256": "9587d94c3755fcab3f00c3e71448f74316372dd72d4e2f142d104d6f311f16fa",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.dark-launching-shadow-traffic",
      "path": "book/volumes/v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md",
      "sha256": "5c95bf668a8c503a5308b1b218950038082a5a5a78ec9a047e424475481f9b91",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.dark-launching-shadow-traffic",
      "path": "book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md",
      "sha256": "db101e283a93ae0e56276d146f3faeffe1d443e683b40c2367f2cd426393f665",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.rbac-abac",
      "path": "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/authorization-policy-and-least-privilege.md",
      "sha256": "26eb70ddf183185cc1cf48ca5f8b23017d652d1c8c5b16342fa2efe0a62b447d",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.rbac-abac",
      "path": "book/volumes/v11-pattern-atlas/c11-security-operations/README.md",
      "sha256": "9587d94c3755fcab3f00c3e71448f74316372dd72d4e2f142d104d6f311f16fa",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.federated-identity",
      "path": "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md",
      "sha256": "41462a8c2c148e93cd602b969b0021113263ffb434243218a5c53c0792461bbd",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.federated-identity",
      "path": "book/volumes/v11-pattern-atlas/c11-security-operations/README.md",
      "sha256": "9587d94c3755fcab3f00c3e71448f74316372dd72d4e2f142d104d6f311f16fa",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.controlled-cutover",
      "path": "book/volumes/v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/cutover-gates.md",
      "sha256": "c9dc734d942a08082c0e739586337b3ec847b8c9728d3be249d59642c25844d3",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.controlled-cutover",
      "path": "book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md",
      "sha256": "db101e283a93ae0e56276d146f3faeffe1d443e683b40c2367f2cd426393f665",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.parallel-run",
      "path": "book/volumes/v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/authority-states.md",
      "sha256": "5e9c621043bed2fc250d9c8c254b1161beb20f7d820b8cca7fc43b5e637552bb",
      "match": true
    },
    {
      "pattern_id": "tycho.pattern.parallel-run",
      "path": "book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md",
      "sha256": "db101e283a93ae0e56276d146f3faeffe1d443e683b40c2367f2cd426393f665",
      "match": true
    }
  ],
  "source_bindings": [
    {
      "pattern_id": "tycho.pattern.workload-identity-mtls",
      "units": 1,
      "shared_fields_match": true
    },
    {
      "pattern_id": "tycho.pattern.dark-launching-shadow-traffic",
      "units": 2,
      "shared_fields_match": true
    },
    {
      "pattern_id": "tycho.pattern.rbac-abac",
      "units": 2,
      "shared_fields_match": true
    },
    {
      "pattern_id": "tycho.pattern.federated-identity",
      "units": 2,
      "shared_fields_match": true
    },
    {
      "pattern_id": "tycho.pattern.controlled-cutover",
      "units": 2,
      "shared_fields_match": true
    },
    {
      "pattern_id": "tycho.pattern.parallel-run",
      "units": 2,
      "shared_fields_match": true
    }
  ],
  "public_source_retrievals": [
    {
      "record_id": "read.batch6-istio.2026-10-21",
      "url": "https://istio.io/latest/docs/concepts/security/",
      "expected_sha256": "0291fb8211b0215a91fe1c2bf389db7b3cdb6fffd57605f13fb4e6b402eb66e4",
      "sha256": "0291fb8211b0215a91fe1c2bf389db7b3cdb6fffd57605f13fb4e6b402eb66e4",
      "match": true,
      "final_url": "https://istio.io/latest/docs/concepts/security/",
      "bytes": 158607,
      "status": 200
    },
    {
      "record_id": "read.fowler-dark-launching.2026-10-26",
      "url": "https://martinfowler.com/bliki/DarkLaunching.html",
      "expected_sha256": "3e39819c496dd5b8ee803eb43688992aa16814b9e9cd751214cf23c64c6a31bb",
      "sha256": "3e39819c496dd5b8ee803eb43688992aa16814b9e9cd751214cf23c64c6a31bb",
      "match": true,
      "final_url": "https://martinfowler.com/bliki/DarkLaunching.html",
      "bytes": 15000,
      "status": 200
    },
    {
      "record_id": "read.batch7-istio-mirroring.2026-10-26",
      "url": "https://istio.io/latest/docs/tasks/traffic-management/mirroring/",
      "expected_sha256": "dc18301fbbca9d374536e582e055c60b5594014d2fe88d4e0763b551de51765e",
      "sha256": "dc18301fbbca9d374536e582e055c60b5594014d2fe88d4e0763b551de51765e",
      "match": true,
      "final_url": "https://istio.io/latest/docs/tasks/traffic-management/mirroring/",
      "bytes": 121117,
      "status": 200
    },
    {
      "record_id": "read.batch6-asvs.2026-10-21",
      "url": "https://owasp.org/www-project-application-security-verification-standard/",
      "expected_sha256": "34fcc53aa30ea62fbc75c0ad5473d1284b6f6f0653feffefb20abfa00367355a",
      "sha256": "47af8a63b622878d9b84d9366c0123cc41d06b48445130f2e535c4cfd56dee76",
      "match": false,
      "final_url": "https://asvs.owasp.org",
      "bytes": 25827,
      "status": 200
    },
    {
      "record_id": "read.nist-sp-800-162.2026-10-26",
      "url": "https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf",
      "expected_sha256": "ea90ee967a7011c8de5cfaffe0820d157167edefdea5fc2a84af730af4295cd7",
      "sha256": "ea90ee967a7011c8de5cfaffe0820d157167edefdea5fc2a84af730af4295cd7",
      "match": true,
      "final_url": "https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf",
      "bytes": 1863313,
      "status": 200
    },
    {
      "record_id": "read.batch6-rfc9700.2026-10-21",
      "url": "https://www.rfc-editor.org/rfc/rfc9700.html",
      "expected_sha256": "9919d061d40a97886ca866b51c69389b6c81c65cd4b979056c14fdbebfcf622a",
      "sha256": "c00e2234fcd79581bc29669c60d693afaa42f67d9205bddee848f757ae975419",
      "match": false,
      "final_url": "https://www.rfc-editor.org/rfc/rfc9700.html",
      "bytes": 261599,
      "status": 200
    },
    {
      "record_id": "read.openid-federation.2026-10-26",
      "url": "https://openid.net/specs/openid-federation-1_0.html",
      "expected_sha256": "4a71afdfbed5755d6704d6a089f450f10aa9914204b283eae5fadee2897d1911",
      "sha256": "4a71afdfbed5755d6704d6a089f450f10aa9914204b283eae5fadee2897d1911",
      "match": true,
      "final_url": "https://openid.net/specs/openid-federation-1_0.html",
      "bytes": 782171,
      "status": 200
    },
    {
      "record_id": "read.fowler-strangler.2026-10-21",
      "url": "https://martinfowler.com/bliki/StranglerFigApplication.html",
      "expected_sha256": "ac274ebe2a36e7553e9f1923e7fbfbc3ff52504c542eec5353127ffba335989e",
      "sha256": "ac274ebe2a36e7553e9f1923e7fbfbc3ff52504c542eec5353127ffba335989e",
      "match": true,
      "final_url": "https://martinfowler.com/bliki/StranglerFigApplication.html",
      "bytes": 20366,
      "status": 200
    },
    {
      "record_id": "read.gcp-spanner-cutover.2026-10-26",
      "url": "https://docs.cloud.google.com/spanner/docs/mysql-perform-cutover",
      "expected_sha256": "7770d4c9e13b041d68bb4f211e619d05ae3878d2d352c95ed1e09e1190e67390",
      "sha256": "4107463035edba1b128d079583542c7465cebe629992975e44ecb327f267798c",
      "match": false,
      "final_url": "https://docs.cloud.google.com/spanner/docs/mysql-perform-cutover",
      "bytes": 249075,
      "status": 200
    },
    {
      "record_id": "read.minimumcd-parallel-run.2026-10-26",
      "url": "https://beyond.minimumcd.org/docs/foundations/evolutionary-coding/parallel-run/",
      "expected_sha256": "e8cf036da19b3f03456a0eb2aa735d1f8d6a738a46449f451a509395d95fc832",
      "sha256": "e8cf036da19b3f03456a0eb2aa735d1f8d6a738a46449f451a509395d95fc832",
      "match": true,
      "final_url": "https://beyond.minimumcd.org/docs/foundations/evolutionary-coding/parallel-run/",
      "bytes": 399292,
      "status": 200
    }
  ],
  "additional_matching_source": {
    "record_id": "read.batch6-asvs.2026-10-21",
    "representation": "Preserved overview HTML",
    "sha256": "34fcc53aa30ea62fbc75c0ad5473d1284b6f6f0653feffefb20abfa00367355a",
    "complete_asvs_pdf": false
  },
  "checks": [
    {
      "command": "validate_sufficient_pilot.py",
      "exit_status": 0
    },
    {
      "command": "validate_sufficient_promotions.py",
      "exit_status": 0
    },
    {
      "command": "validate_pattern_owner_units.py",
      "exit_status": 0
    },
    {
      "command": "validate_pattern_registry.py",
      "exit_status": 0
    },
    {
      "command": "validate_pattern_sources.py",
      "exit_status": 0
    },
    {
      "command": "validate_pattern_cards.py",
      "exit_status": 0
    },
    {
      "command": "validate_delivery_evidence.py",
      "exit_status": 0
    },
    {
      "command": "check_boundary.py",
      "exit_status": 0
    },
    {
      "command": "unittest discover -s tests -p test_tycho_sufficient_pilot.py",
      "exit_status": 0
    }
  ],
  "limits": [
    "No full atlas or 155-unit review",
    "Relevant source passages checked, not complete rereading of all documents",
    "No runtime/security reproduction",
    "Original checkout changed externally during review",
    "New tooling at a4975a6b is not covered by these cf9e02f2 test results",
    "No owner acceptance, CI or merge permission"
  ],
  "repository_changes_by_reviewer": false,
  "external_checkout_observations": [
    {
      "branch": "main",
      "head": "0f3ece31252c499a258371978279c2f34ed3663f"
    },
    {
      "branch": "feature/TYCHO-540-raise-pattern-atlas-coverage-from-sufficient-ready-to-sufficient",
      "head": "a4975a6b3d1deffc6e13169cb2b1fe909c8d3ed9"
    }
  ]
}
```
