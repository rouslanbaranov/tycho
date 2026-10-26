# Focused independent AI re-review — Tycho #535 remediation

**Verdict: reject.** R-04 remains open and its remediation introduced source-scope
misbindings. R-01, R-02, R-06, R-07 and R-08 are resolved in the reviewed scope.
R-03 and R-05 have residual documentation findings described below.

## Identity and revision

- Harness/vendor: Codex desktop app / OpenAI.
- Model: GPT-6 family according to session context; exact deployed version not available.
- Session: `01a17a03-0b7c-7513-87fe-1f3994862b1d`.
- Timestamp: 2026-10-26T22:52:10+01:00, Europe/Zurich.
- Repository: `/Users/rbaranov/Projects/tycho`.
- Branch: `feature/TYCHO-535-read-the-155-pattern-source-plan-units-in-full`.
- Review HEAD: `d10110996429aa7337962fb5cad2b1d6f77b4b32`.
- Original reviewed snapshot / comparison base: `0531e9ce801dc04e8150afa8b92755c6338a55b5`.
- Last substantive remediation commit: `bbe1c0c6454e1ebd1ce387dce5d1957f90009ccf`.
- Earlier B1 evidence HEAD: `180597e52403e3dabb71c50eb92a5b991d6803b8`.
- Prior involvement: I performed the original external review and its reporting correction
  in this same reviewer chat. I did not author the remediation or access authoring-chat
  history. This is a continuation by the prior reviewer, not a fresh reviewer session.

Instruction set: the owner's focused re-review request and
`authoring/AI-REVIEW-HANDOFF-REMEDIATION_2026-10-26.md` at the reviewed HEAD.

The repository's original report was read and its hash recomputed. It matches the supplied
SHA-256 `4e9ed912281f84346dfa11caec0a05b50ef613de461443afb662481f37b0eb90`.
Its path is `authoring/ai-reviews/2026-10-26-full-unit-reading-codex.md`.
The original reject remains historical; this report evaluates the remediation separately.

## Scope

Review R-01 through R-08, changed claim/result records, all 155 source-specific section
bindings, preserved prior scopes, and ACCEPTED/RESOLUTIONS/ALTERNATIVES consistency.
Inspect changed claims FS-01/02/03/06/07/08/09/10/11/12/13/14/15/16/17/18/19/21.
Count all 23 claims without repeating source review of unchanged FS-04/05/20/22/23.

I freshly retrieved the eleven EIP public pattern pages, Routing Slip and Workbook
chapters 2, 3 and 5. Relevant passages were inspected. I rechecked the previously acquired
official EIP chapter PDF hash and passages at printed pp.72, 74 and 77.
All public HTML hashes match the corresponding prior representations, including the three
Workbook chapters. Full URLs and hashes appear in the manifest at the end.

Changed-unit sampling covered at least the five requested units: Layered Architecture,
API Gateway, Resequencer, Failover / Failback and Synthetic Monitoring. Their section
bindings now match. The complete mechanical comparison additionally inspected the ten
mismatched units listed below. This is scope verification, not a new full reading of them.

## Derived counts and required-check results

Counts were computed from JSON artifacts using `collections.Counter`, not copied from
the handoff.

| Unit disposition | Count |
|---|---:|
| full-read | 129 |
| full-read-exact-reuse | 14 |
| partial-read | 1 |
| blocked-current | 11 |
| Total | 155 |

| Claim disposition | Count |
|---|---:|
| partially-supported | 15 |
| unconfirmed | 5 |
| contradicted | 2 |
| resolved | 1 |
| Total | 23 |

| Required check | Result |
|---|---|
| Counts | Pass; both totals and distributions reproduced. |
| FS-21 | Pass; support and remaining uncertainty separated. |
| FS-10 | Pass; concerns supported, universal wording unconfirmed. |
| Eleven EIP records | Pass; each has both nonempty clause arrays. |
| Zero section differences | **Fail: 10 differences, 155 matched entries.** |
| Four narrowed public scopes | Pass; linked_sources is not-read in all four. |
| FS-18 | Pass; mechanism separated from variants/serialization. |
| Workbook chapter range | Pass; results coverage says chapters 1-21. |
| Existing validators | Pass; all eight exit 0 on an isolated copy. |

The handoff does not enumerate validator names or commands. I used the eight-command suite
from the original handoff, plus check_boundary. This interpretation is explicit below.

## R-01 through R-08 disposition

### R-01 — Resolved in this scope

`research/full-source-confirmation/claims.v1.json`, FS-21, now includes supported external
probing, geographic confirmation, browser probes and artificial user activity. The exact
generic definition and combined explicit-design rule remain unconfirmed.
The corresponding result references chapters 2, 3 and 5 instead of claiming that the
complete book lacks the mechanism.

Workbook chapter 2 describes browser probes and measurement limitations. Chapter 3
describes probe placement and geographically separate confirmation. Chapter 5 describes
artificial user activity and coverage limitations. These support the narrower record.
See [chapter 2][sre2], [chapter 3][sre3] and [chapter 5][sre5].

### R-02 — Resolved in this scope

FS-10 is now partially-supported. Both claim/result records distinguish channel buffering,
conditional reordering and loss in a nontransactional filter from the unconfirmed universal
every-stage assertion. The reading-ledger limitation for `read.batch2-pipes.2026-10-21`
was corrected consistently.

The matching [official chapter PDF][eip3], printed pp.72, 74 and 77, supports this narrower
treatment. SHA-256:
`c1e7125dcebfdd9a2b23a922dfbbc9694e5f8048e81e14dc95e2882043ac4f66`.

### R-03 — Substantive record split applied; residual non-blocking finding

The eleven IDs are FS-06, FS-07, FS-08, FS-09, FS-11, FS-12, FS-13, FS-14,
FS-15, FS-16 and FS-17. Each has nonempty `supported_clauses` and
`unconfirmed_clauses`, and the grouped result supplies corresponding clause support.
The original conjunctions are explicitly not accepted as fully supported.

Public-page passages support the narrower pattern facts: acknowledgement timing,
request/reply mechanics, configurable routing, discard disposition, incomplete-set
strategies, route errors, reconnect delivery, buffering, persistent payload storage,
destination routing and canonical-format translation.

**Residual R-03a — non-blocking, medium.**

Location:
`/Users/rbaranov/Projects/tycho/edition/patterns/reading-ledger.v1.json:1675`,
record `read.batch2-aggregator.2026-10-21`, `limitations`.

The limitation still states that no partial-result text is served. The public
[Aggregator page][agg], Time Out strategy, describes making a decision from responses
received before a deadline. The corrected claim already acknowledges incomplete-set
handling, so the ledger's categorical absence statement remains inconsistent.

Required action: replace that categorical absence statement with the distinction between
supported incomplete-set handling and unconfirmed duplicate/general partial-results rules.
This residual does not undo the correctly recorded clause split, but R-03 is not fully
clean across its original evidence locations.

### R-04 — Open; blocking regression in source-specific scope

Locations:

- `/Users/rbaranov/Projects/tycho/edition/patterns/full-unit-reading-plan.v1.json`,
  `entries[].sections` for the ten entries below.
- `/Users/rbaranov/Projects/tycho/edition/patterns/source-plan.v1.json`, corresponding
  `entries[].required_units[].sections`.
- `/Users/rbaranov/Projects/tycho/authoring/AI-REVIEW-HANDOFF-REMEDIATION_2026-10-26.md:23`,
  the claim that zero differences remain.

Comparison used the complete key `(pattern_id, source_id, unit)`. All 155 entries matched
uniquely; ten section lists differ. No missing entry was silently skipped.

| Affected unit/source | Incorrect reading-plan section identity |
|---|---|
| CDC / src.debezium-outbox | PostgreSQL Logical Replication |
| Materialized View / src.postgresql | REFRESH MATERIALIZED VIEW command reference |
| Polyglot Persistence / src.ddia | Fowler Polyglot Persistence article |
| Load Balancing / src.sre-balancing-enrichment | Frontend balancing chapter |
| Cell-Based Architecture / src.microsoft-cloud-patterns | Cell architecture article |
| Parallel Run / src.minimumcd-parallel-run | Strangler Fig article |
| Dark Launching / src.istio-traffic-mirroring | Dark Launching article |
| Controlled Cutover / src.gcp-spanner-cutover | Strangler Fig article |
| Federated Identity / src.openid-federation | OAuth RFC 9700 section list |
| RBAC / ABAC / src.nist-sp-800-162 | ASVS chapter list |

Concrete anchors in the full-reading plan:

- Line 1887: Debezium Outbox Event Router entry; its sections name Logical Replication.
- Line 2807: blocked DDIA entry; its sections now name the Fowler article.
- Line 4626: OpenID entry; its sections now name OAuth security BCP material.
- Line 4801: NIST ABAC entry; its sections now name ASVS chapters.

Comparison with `0531e9ce` and `bbe1c0c6^` shows all ten lists were changed by remediation. For example,
the Debezium entry previously had the correct Outbox/Configuration/Example list, and the
blocked DDIA entry previously had an empty list. This is new source-scope misattribution,
not merely the earlier missing-heading problem. That new evidence makes the residual
blocking even though the original R-04 was non-blocking.

The 130 `planned_sections` snapshots do preserve their respective pre-remediation values;
preservation is not the failure. The replacement `sections` must be corrected separately
for every source unit within a pattern.

Required action: bind replacement scopes by the full unit identity, not just the pattern;
retain the preserved prior scopes; verify exactly 155 comparisons, zero unmatched entries
and zero section differences. Add a check that detects sibling-source substitution.

### R-05 — Mostly reconciled; residual non-blocking finding

ACCEPTED and ALTERNATIVES no longer disagree about the ten blocked units versus
clause-level claim support. The earlier incompatible acceptance statements were removed.

**Residual R-05a — non-blocking, low.**

Location:
`/Users/rbaranov/Projects/tycho/research/full-source-confirmation/RESOLUTIONS.md:13`–14.

The FS-06-to-FS-17 range still includes FS-10 while assigning the whole range
`clause-level-support; chapter-4-unavailable`. FS-10's chapter is available and its actual
claim detail is `clause-level-support; universal-wording-unconfirmed`.

Required action: enumerate the eleven Chapter 4+ IDs and record FS-10 separately. The
shared partially-supported classification is no longer contradictory, but the source
availability description still is.

### R-06 — Resolved in this scope

FS-01, FS-02, FS-03 and FS-19 now limit `full_source` to the complete named pattern page,
explicitly put linked guidance/articles outside scope, and set `linked_sources: not-read`.
This resolves the original scope-overstatement finding without asserting new reading.

### R-07 — Resolved in this scope

FS-18 and its result support the per-message sequence mechanism while keeping variants,
serialization detail and the broader Process Manager relationship unconfirmed.
Literal-word absence is no longer used as adverse evidence. The [Routing Slip page][slip]
supports the recorded mechanism. This does not confirm any particular serialization.

### R-08 — Resolved in this scope

The FS-21 result coverage now says chapters 1-21. The public Workbook navigation includes
chapter 21. Its 34-page description refers to web content pages, not printed pagination.

## Executed checks

Execution copy:
`/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/work/rereview-e11839d2/tree`.

Interpreter:
`/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/work/venv/bin/python`.

Each validator command was `<interpreter> -B scripts/<name>.py`, with its working
directory set to that isolated copy. Matching Git metadata was copied into the copy.
No validator or dependency installation modified the original repository.

| Command script | Exit |
|---|---:|
| scripts/validate_sources.py | 0 |
| scripts/validate_pattern_sources.py | 0 |
| scripts/validate_pattern_cards.py | 0 |
| scripts/validate_pattern_owner_units.py | 0 |
| scripts/validate_pattern_semantic_audit.py | 0 |
| scripts/validate_pattern_atlas.py | 0 |
| scripts/validate_delivery_evidence.py | 0 |
| scripts/validate_edition.py | 0 |
| scripts/check_boundary.py | 0 |
| Complete source-specific section comparison, requiring zero differences | **1** |

Additional executed checks, all exit 0: Git HEAD/baseline resolution, original-report
SHA-256, artifact counts, four narrowed scope fields, eleven nonempty clause-array pairs,
prior-scope preservation comparison, source retrieval/extraction and EIP PDF hash check.

The scope-comparison failure is independent of the validator passes. Those validators
did not detect these ten cross-file differences. The edition output retains 423 canonical
documents, content snapshot `30154704ea6e4844c7ea0c7bab3c07b4e0f6f7baf4f9e003f052a7969b19c5e9`
and route snapshot `06b80bd6b82ddc5080b2342ae329233497daac0066625e489ff465a0723c009c`.

## Limits and authority

This is a focused partial re-review. It does not repeat the 155-unit reading, certify
all full-read/exact-reuse records, or review all canonical book content. The ten scope
failures are documentary binding failures; they do not prove that the underlying source
readings never happened.

Complete EIP Chapter 4+ and DDIA full text remain unavailable. No restricted, borrowed or
substitute full-book material was used. Existing public-source representations were used
only at their declared scope. A pattern-context fact in `supported_clauses` does not
establish every requirement in the original removed claim.

`ai_review: performed`; `sufficient: 0`.
No owner acceptance, CI execution, merge permission or sufficient coverage is claimed.
The author, not this reviewer, must preserve this report in the repository and index it.

[sre2]: https://sre.google/workbook/implementing-slos/
[sre3]: https://sre.google/workbook/slo-engineering-case-studies/
[sre5]: https://sre.google/workbook/alerting-on-slos/
[agg]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html
[slip]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RoutingTable.html
[eip3]:
https://www.enterpriseintegrationpatterns.com/docs/EnterpriseIntegrationPatterns_HohpeWoolf_ch03.pdf

## review-manifest

Final integrity check after the owner's announced handoff-only update: 1,951 project
files unchanged, zero additions/removals; Git status and HEAD unchanged. The pre-existing
untracked deliverables directory remains. The reviewer made no repository changes.

```json
{
  "name": "review-manifest",
  "reviewer_harness": "Codex desktop app",
  "reviewer_vendor": "OpenAI",
  "model_family": "GPT-6",
  "exact_model_version": "not available",
  "session_id": "01a17a03-0b7c-7513-87fe-1f3994862b1d",
  "timestamp": "2026-10-26T22:52:10+01:00",
  "timezone": "Europe/Zurich",
  "repository": "/Users/rbaranov/Projects/tycho",
  "review_head": "d10110996429aa7337962fb5cad2b1d6f77b4b32",
  "reviewed_snapshot": "0531e9ce801dc04e8150afa8b92755c6338a55b5",
  "last_substantive_remediation_commit": "bbe1c0c6454e1ebd1ce387dce5d1957f90009ccf",
  "original_report_sha256": "4e9ed912281f84346dfa11caec0a05b50ef613de461443afb662481f37b0eb90",
  "verdict": "reject",
  "ai_review": "performed",
  "sufficient": 0,
  "scope": "Focused remediation R-01 through R-08; not a repeat of the full reading",
  "counts": {
    "unit_counts": {
      "full-read-exact-reuse": 14,
      "full-read": 129,
      "blocked-current": 11,
      "partial-read": 1
    },
    "claim_counts": {
      "unconfirmed": 5,
      "contradicted": 2,
      "partially-supported": 15,
      "resolved": 1
    },
    "flat_units": 155,
    "unmatched": [],
    "section_diffs": [
      [
        "tycho.pattern.change-data-capture-cdc",
        "src.debezium-outbox",
        "Outbox Event Router — Debezium documentation"
      ],
      [
        "tycho.pattern.materialized-view",
        "src.postgresql",
        "Materialized Views — PostgreSQL documentation"
      ],
      [
        "tycho.pattern.polyglot-persistence",
        "src.ddia",
        "Designing Data-Intensive Applications — polyglot persistence"
      ],
      [
        "tycho.pattern.load-balancing",
        "src.sre-balancing-enrichment",
        "Load Balancing in the Datacenter — public chapter"
      ],
      [
        "tycho.pattern.cell-based-architecture",
        "src.microsoft-cloud-patterns",
        "Deployment Stamps — pattern page"
      ],
      [
        "tycho.pattern.parallel-run",
        "src.minimumcd-parallel-run",
        "Parallel Run — MinimumCD Practice Guide"
      ],
      [
        "tycho.pattern.dark-launching-shadow-traffic",
        "src.istio-traffic-mirroring",
        "Istio Mirroring task page"
      ],
      [
        "tycho.pattern.controlled-cutover",
        "src.gcp-spanner-cutover",
        "Perform cutover from MySQL (Spanner)"
      ],
      [
        "tycho.pattern.federated-identity",
        "src.openid-federation",
        "OpenID Federation 1.0 — Final Specification"
      ],
      [
        "tycho.pattern.rbac-abac",
        "src.nist-sp-800-162",
        "NIST SP 800-162 — Guide to Attribute Based Access Control"
      ]
    ],
    "planned_sections_count": 130
  },
  "findings": {
    "blocking": [
      "R-04 source-specific scope regression"
    ],
    "non_blocking": [
      "R-03a Aggregator ledger absence statement",
      "R-05a FS-10 included in Chapter 4+ range"
    ]
  },
  "resolved_in_scope": [
    "R-01",
    "R-02",
    "R-06",
    "R-07",
    "R-08"
  ],
  "checked_changed_claim_ids": [
    "FS-01",
    "FS-02",
    "FS-03",
    "FS-06",
    "FS-07",
    "FS-08",
    "FS-09",
    "FS-10",
    "FS-11",
    "FS-12",
    "FS-13",
    "FS-14",
    "FS-15",
    "FS-16",
    "FS-17",
    "FS-18",
    "FS-19",
    "FS-21"
  ],
  "sampled_changed_units": [
    "Layered Architecture",
    "API Gateway",
    "Resequencer",
    "Failover / Failback",
    "Synthetic Monitoring"
  ],
  "mismatched_units": [
    {
      "pattern_id": "tycho.pattern.change-data-capture-cdc",
      "source_id": "src.debezium-outbox",
      "unit": "Outbox Event Router — Debezium documentation"
    },
    {
      "pattern_id": "tycho.pattern.materialized-view",
      "source_id": "src.postgresql",
      "unit": "Materialized Views — PostgreSQL documentation"
    },
    {
      "pattern_id": "tycho.pattern.polyglot-persistence",
      "source_id": "src.ddia",
      "unit": "Designing Data-Intensive Applications — polyglot persistence"
    },
    {
      "pattern_id": "tycho.pattern.load-balancing",
      "source_id": "src.sre-balancing-enrichment",
      "unit": "Load Balancing in the Datacenter — public chapter"
    },
    {
      "pattern_id": "tycho.pattern.cell-based-architecture",
      "source_id": "src.microsoft-cloud-patterns",
      "unit": "Deployment Stamps — pattern page"
    },
    {
      "pattern_id": "tycho.pattern.parallel-run",
      "source_id": "src.minimumcd-parallel-run",
      "unit": "Parallel Run — MinimumCD Practice Guide"
    },
    {
      "pattern_id": "tycho.pattern.dark-launching-shadow-traffic",
      "source_id": "src.istio-traffic-mirroring",
      "unit": "Istio Mirroring task page"
    },
    {
      "pattern_id": "tycho.pattern.controlled-cutover",
      "source_id": "src.gcp-spanner-cutover",
      "unit": "Perform cutover from MySQL (Spanner)"
    },
    {
      "pattern_id": "tycho.pattern.federated-identity",
      "source_id": "src.openid-federation",
      "unit": "OpenID Federation 1.0 — Final Specification"
    },
    {
      "pattern_id": "tycho.pattern.rbac-abac",
      "source_id": "src.nist-sp-800-162",
      "unit": "NIST SP 800-162 — Guide to Attribute Based Access Control"
    }
  ],
  "checks": [
    {
      "command": "validate_sources.py",
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
      "command": "validate_pattern_owner_units.py",
      "exit_status": 0
    },
    {
      "command": "validate_pattern_semantic_audit.py",
      "exit_status": 0
    },
    {
      "command": "validate_pattern_atlas.py",
      "exit_status": 0
    },
    {
      "command": "validate_delivery_evidence.py",
      "exit_status": 0
    },
    {
      "command": "validate_edition.py",
      "exit_status": 0
    },
    {
      "command": "check_boundary.py",
      "exit_status": 0
    },
    {
      "command": "source-specific section comparison, require zero mismatches",
      "exit_status": 1
    }
  ],
  "artifact_hashes": {
    "authoring/AI-REVIEW-HANDOFF-REMEDIATION_2026-10-26.md": "999199edbd6af154654f58972ebe2d9be8f29c6201e1b050ff3c77fdede6b7f7",
    "research/full-source-confirmation/claims.v1.json": "750115ff6f406a6f9e8fb9bfc38872bfa1a80728f2bf5d4d107246502d620efc",
    "research/full-source-confirmation/results.v1.json": "86b58651522b4a9cf7e5e042734a331f0d9f757ea05e23f467ec546bfcadceea",
    "edition/patterns/full-unit-reading-plan.v1.json": "c4bafe8d2c2d2dcd8c443cc0591ea665dc2122e4ca90ce04682772f49a20add0",
    "edition/patterns/source-plan.v1.json": "30f5a6bc84eca684193d045815f457218d6bf1d430887b8f9b7f8c3ca98873c1"
  },
  "public_sources": [
    {
      "id": "FS-06",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventDrivenConsumer.html",
      "sha256": "bdd22eb6db0ea6606a9ff53c93d17750b2977ec7f0a25120467a49c532c446d0",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-07",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html",
      "sha256": "6d79d9ec15c68a7547682feb84c4adaea407795c64a69c98b6fed273eb2cea5f",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-08",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html",
      "sha256": "2e1bcb059062a373d4a86319925c989b73ec891cebffe089608b4e48bc69256c",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-09",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/Filter.html",
      "sha256": "899fcd8bbb8d91b9a0985314998a4707c1b4e0b34aa79a2821149c861d53db2c",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-11",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html",
      "sha256": "15d8640d5ad149a0e54a23c4cfe4a84c0abdcec421de2f9eb301daf21d708f58",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-12",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html",
      "sha256": "ed4e25c160ba5c6c908b79de8011ba8f69c26c40ccd92f7612903029b7db78e6",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-13",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/DurableSubscription.html",
      "sha256": "d8697f78f17e355548692ad6ed8459e2fe3932ab1119d7b613c029774e0f2139",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-14",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/Resequencer.html",
      "sha256": "cafe3058fa70fe3bda25f83941e1ac604875e172d2388f6a334c7ff84327f42f",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-15",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html",
      "sha256": "96395638cbc1165642bdff681ec21a2862359e68f88f59cb7a2b5b2ad4753fb5",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-16",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBroker.html",
      "sha256": "ddc6d825aa8a17ef30a18ff8178085022c9424432a6082947f9f7983826f79ca",
      "access_date": "2026-10-26"
    },
    {
      "id": "FS-17",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html",
      "sha256": "02992f61d7529d80300b901e152622f0e876669b52f49d035dba00745a2405f8",
      "access_date": "2026-10-26"
    },
    {
      "id": "routing-slip",
      "url": "https://www.enterpriseintegrationpatterns.com/patterns/messaging/RoutingTable.html",
      "sha256": "5e46ed0bbff9cbd9b7d56986a778230fcbffd4de408735b71e34b93b428844cd",
      "access_date": "2026-10-26"
    },
    {
      "id": "sre2",
      "url": "https://sre.google/workbook/implementing-slos/",
      "sha256": "1b02c7f3f640d92ca4357ba3e088fdbd6766274118afac934bede95ea9ea23e9",
      "access_date": "2026-10-26"
    },
    {
      "id": "sre3",
      "url": "https://sre.google/workbook/slo-engineering-case-studies/",
      "sha256": "239b784698c71e06a421f0c28c4315577b6f4a0e6e3489f0c8a3671462763174",
      "access_date": "2026-10-26"
    },
    {
      "id": "sre5",
      "url": "https://sre.google/workbook/alerting-on-slos/",
      "sha256": "340f148f65a7a92596c65f0a44828cbc1bcf165291cccf2c33a2b57673dd30b3",
      "access_date": "2026-10-26"
    }
  ],
  "integrity": {
    "files_before": 1951,
    "files_after": 1951,
    "changed": [],
    "added": [],
    "removed": [],
    "git_status_unchanged": true,
    "git_status": "?? deliverables/\n",
    "head_unchanged": true
  },
  "limits": [
    "Full 155-unit reading not repeated",
    "Complete EIP Chapter 4+ unavailable",
    "DDIA full text unavailable",
    "No owner acceptance, CI, merge permission or sufficient coverage"
  ]
}
```
