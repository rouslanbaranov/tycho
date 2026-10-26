# Corrected independent AI review — Tycho #535

**Verdict: reject.** The three blocking findings and five non-blocking findings from the original report remain unchanged.

This correction completes the reporting schema. It does not repeat the original review or introduce new substantive verdicts.

## Schema audit of the original report

The original report is available on disk; this is **not a reconstruction from session memory**.

Original report: [REVIEW_2026-10-26.md](/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/outputs/REVIEW_2026-10-26.md).

Original supporting records: [REVIEW_EVIDENCE_2026-10-26.json](/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/outputs/REVIEW_EVIDENCE_2026-10-26.json).

The report's recomputed SHA-256 matches the value preserved in those supporting records:

`cd4b1da910298e7c8d22b345afc941f9ae347a15f681060e25386d67a1f2c9bd`

“Provided” below means present in the original report or its explicitly linked supporting records. “Missing” identifies an omission addressed in this corrected report.

| Required item | Original status | Exact original evidence or omission |
|---|---|---|
| A: reviewer harness and vendor | Missing | Opening identifies Codex, but does not explicitly identify vendor. |
| A: model name and version | Missing | No model/version field. |
| A: session or run ID | Missing | No session identifier. |
| A: timestamp with time zone | Missing | Opening provides date and Europe/Zurich, without time of day. |
| A: repository path | Provided | “Scope and identity.” |
| A: review checkout HEAD | Provided | “Scope and identity”: `0531e9ce…`. |
| A: B1 evidence HEAD | Provided | “Scope and identity”: `180597e5…`. |
| A: handoff path and commit | Missing | Original handoff path appears, but no explicit handoff-commit field. |
| B: exact unit and claim counts | Provided | “Counts and local checks.” |
| B: list of sampled units | Provided | “Sampling of full units”: 22 rows. |
| B: list of checked claims | Provided | “Passage register”: FS-01 through FS-23. |
| B: exclusions | Provided | “Decision and remaining limits.” |
| C: unit disposition counts | Provided | “Counts and local checks.” |
| C: claim disposition counts | Provided | “Counts and local checks.” |
| C: counts derived or copied | Provided | Explicitly described as recomputed from artifacts. |
| D: one row per claim | Missing | Original table uses additional continuation rows. |
| D: final status per claim | Missing | Passage table does not include registry status. |
| D: source URL/document per claim | Missing | Sources are not consistently mapped into all 23 rows. |
| D: revision/hash per claim | Missing | Supporting JSON contains many hashes, but no complete per-claim table. |
| D: exact section/page/requirement | Provided | “Passage register” and “Mandatory-check decisions.” |
| D: quote or precise absence statement | Missing | Several entries provide summaries without either requested form. |
| D: checked-by-reviewer field | Missing | No explicit yes/no column. |
| D: source-unavailable field | Missing | Availability discussed globally, rather than per claim. |
| E: blocking/non-blocking severity | Missing | Blocking findings explicit; remaining findings labelled “Additional.” |
| E: exact location | Provided | Locations beneath R-01 through R-08. |
| E: evidence | Provided | Finding bodies and supporting source manifest. |
| E: affected claims/units | Provided | Finding bodies and mandatory-check decisions. |
| E: required action | Provided | Finding bodies. |
| F: commands with exit status | Missing | Validator names and aggregate success given; full invocations omitted. |
| F: validators run | Provided | “Counts and local checks”; supporting JSON `checks`. |
| F: hashes recomputed | Provided | Supporting JSON `package_hashes`, `samples`, and `source_manifest`. |
| F: sources actually opened | Provided | Supporting JSON `source_manifest` and `sre_book_search`. |
| F: execution limitations | Provided | Initial dependency/Git failures and unavailable Reviewer preset recorded. |
| G: challenged accepted gaps | Provided | R-01 through R-03 and mandatory-check decisions. |
| G: unavailable sources | Provided | EIP complete chapters and DDIA limits. |
| G: sampling limits | Provided | Sampling section and final limitations. |
| G: explicit partial-review field | Missing | Limits explained, but no explicit `partial` field. |
| H: allowed verdict | Provided | Opening: reject. |
| H: `ai_review: performed` | Missing | No explicit field. |
| H: `sufficient: 0` | Provided | Opening. |
| H: authority exclusions | Provided | Opening and “Decision and remaining limits.” |

## A. Identity and revision

| Field | Value |
|---|---|
| Reviewer harness | Codex desktop app, using its agent and local execution tools |
| Reviewer vendor | OpenAI |
| Model name | GPT-6 family, as identified by the session's developer context |
| Exact model/version | **not available**; no precise deployed model identifier or version is exposed |
| Session ID | `01a17a03-0b7c-7513-87fe-1f3994862b1d` |
| Session ID evidence | Read from the execution environment's `CODEX_THREAD_ID` |
| Original review date | 2026-10-26, Europe/Zurich |
| Original review exact timestamp | **not available**; the original report did not record time of day |
| Correction timestamp | 2026-10-26T22:28:08+01:00, Europe/Zurich |
| Timestamp evidence | Clock tool returned 2026-10-26 21:28:08 UTC at correction start |
| Repository | `/Users/rbaranov/Projects/tycho` |
| Branch | `feature/TYCHO-535-read-the-155-pattern-source-plan-units-in-full` |
| Original checked HEAD | `0531e9ce801dc04e8150afa8b92755c6338a55b5` |
| Current checkout HEAD | `ec9289ae7dd9a1f179133c46ca9991a59e86055a` |
| B1 evidence HEAD | `180597e52403e3dabb71c50eb92a5b991d6803b8` |
| Current handoff | `/Users/rbaranov/Projects/tycho/authoring/AI-REVIEW-HANDOFF_2026-10-26.md` |
| Current handoff last-changing commit | `ec9289ae7dd9a1f179133c46ca9991a59e86055a` |
| Handoff rename/policy commit | `5afae41a0a0bd7443977cd2cd1ac7fed9542e2bc` |
| Original handoff commit | `0531e9ce801dc04e8150afa8b92755c6338a55b5` |

Current handoff SHA-256:

`13fc97f5ae933787c434fbbaabebe53749adbfa47ffdc0da8c716bba73a156d0`

The current handoff's own “Hand-off/policy commit” field identifies `5afae41a`. Git history establishes that the file was subsequently changed at `74d10b48…` and `ec9289ae…`. These are distinct revision facts.

For this correction, I compared the current package files with the original recorded hashes. The claims, results, three pattern-plan/ledger files, all batch records, ACCEPTED, RESOLUTIONS, and ALTERNATIVES remain byte-identical. The original human-review handoff has been replaced by the AI-review handoff, and the reading contract has changed.

Accordingly, substantive findings retain their original evidence basis. The original validator results belong to the original checked copy; this report does **not** represent them as fresh executions against the current HEAD.

## B. Scope and sampled units

The package contains **155 unit entries** and **23 removed-claim entries**. The original review sampled **22 units across batches 1–21**, including both halves of batch 16.

| Batch | Sampled unit | Passage or scope inspected |
|---|---|---|
| 01 | Database per Service | Storage ownership and cross-service query forces |
| 02 | Presentation Domain Data Layering | Layer responsibilities and Acknowledgements |
| 03 | Static Content Hosting | Direct storage delivery and article headings |
| 04 | Competing Consumers | Single-consumer delivery semantics |
| 05 | Ambassador | Colocated proxy responsibilities |
| 06 | API Gateway | Gateway solution, Known uses, Example application |
| 07 | Event Sourcing | Atomic event storage, replay, related-pattern sections |
| 08 | Deployment Stamps | Independent deployments, capacity and routing sections |
| 09 | Shuffle Sharding | Tenant subsets, guarantees and rollout |
| 10 | Hexagonal Architecture | Domain isolation, implementation and testing sections |
| 11 | OpenID Federation 1.0 | Revocation process and status-data sections |
| 12 | Materialized Views | Persisted results, refresh and actual headings |
| 13 | Cassandra Dynamo Architecture | Token-ring partitioning and article headings |
| 14 | KEDA Documentation Landing | Where to go and links to child documentation |
| 15 | SRE Service Level Objectives | Indicators, objectives and control measures |
| 16a | Argo Canary | Rollout steps, pause and analysis subsection |
| 16b | Raft Overview | Replicated-log and consensus explanation in declared scope |
| 17 | Event-Driven Consumer | Callback mechanics and acknowledgement example |
| 18 | Scatter-Gather | Aggregation and partial-failure examples |
| 19 | Command-side Replica | Read-only replica and staleness |
| 20 | PostgreSQL PITR | Archive chain, recovery steps and timelines |
| 21 | Load Balancing at the Frontend | DNS and virtual-IP balancing |

Twenty sampled raw HTML hashes matched the batch hashes. Static Content Hosting and Deployment Stamps differed; those two samples concern current retrieved content, not a certified identical historical representation.

Checked claims:

`FS-01, FS-02, FS-03, FS-04, FS-05, FS-06, FS-07, FS-08, FS-09, FS-10, FS-11, FS-12, FS-13, FS-14, FS-15, FS-16, FS-17, FS-18, FS-19, FS-20, FS-21, FS-22, FS-23`.

I did **not**:

- Repeat all 143 full or exact-reuse readings.
- Establish exhaustive coverage of every linked article or documentation child.
- Obtain or read the unavailable complete EIP chapters or DDIA book.
- Perform a complete semantic review of all canonical book pages.
- Re-run the original validator suite during this correction.
- Review all intervening governance changes for substantive acceptance.
- Independently reconstruct the author's activity outside the recorded evidence.

## C. Counts and derivation

These are **stored package dispositions**, not replacement reviewer classifications.

| Unit disposition | Count |
|---|---:|
| full-read | 129 |
| full-read-exact-reuse | 14 |
| partial-read | 1 |
| blocked-current | 11 |
| **Total** | **155** |

| Claim disposition | Count |
|---|---:|
| unconfirmed | 17 |
| contradicted | 3 |
| partially-supported | 2 |
| resolved | 1 |
| **Total** | **23** |

The counts were derived from:

- `/Users/rbaranov/Projects/tycho/edition/patterns/full-unit-reading-plan.v1.json`
- `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/claims.v1.json`

They were recomputed in the original review and again during this correction using `collections.Counter`. They were **not copied from the handoff**.

## D. Per-claim evidence

“Final status” below means the registry's existing final disposition. Recording that status does not endorse it. Reviewer challenges remain in section E.

The hash column uses a unique **12-character prefix of the SHA-256**, identifying the preserved source representation. Full HTML hashes are in the original supporting JSON; full document hashes are recorded in section F.

“Yes” means a relevant passage or bounded absence check was performed, not that the unavailable full book was read.

| Claim | Final status | Source / SHA-256 prefix | Exact locator | Short quote or precise bounded absence statement | Checked-by-reviewer | Unavailable-source note |
|---|---|---|---|---|---|---|
| FS-01 | unconfirmed | [Event Sourcing][p01]; `aade58421e5a` | Solution; Resulting context | Schema evolution and duplicate-handling mechanics were not established by this complete pattern page. | yes | Page available; linked guidance not exhaustively checked. |
| FS-02 | unconfirmed | [Idempotent Consumer][p02]; `3edddaa1959c` | Solution, processed-message transaction paragraph | “rollback the transaction and ignore the message.” Explicit retention/concurrency limits were not established. | yes | Page available; linked articles not exhaustively checked. |
| FS-03 | unconfirmed | [CQRS][p03]; `592b31fe177a` | Solution; Resulting context | “a read-only ‘replica’”. Duplicate/order/failure-handling requirements were not established by this page. | yes | Page available; linked articles not exhaustively checked. |
| FS-04 | contradicted | [Cassandra Overview][p04]; `53c36bff1a21` | Overview; Features; Operating | The complete overview does not explain consistent hashing; that explanation is on the separate Dynamo page. | yes | Overview available. |
| FS-05 | contradicted | [KEDA landing][p05]; `8c704134e53d` | Where to go | “Use the navigation bar on the left”. Detailed scaler, ScaledObject, lag and cooldown mechanics are absent from the landing. | yes | Landing available; linked documentation is a different scope. |
| FS-06 | unconfirmed | [Event-Driven Consumer][p06]; `bdd22eb6db0e`; EIP chapter 3 PDF | RabbitMQ example; printed p.77 | “acknowledges messages automatically on receipt but before processing.” Generic channel-specific semantics remain unconfirmed. | yes | Public example/PDF available; complete book pattern unavailable. |
| FS-07 | unconfirmed | [Request-Reply][p07]; `6d79d9ec15c6` | Asynchronous Callback; crash/restart paragraphs | “re-establishes the caller's context”. The complete correlation/timeout/ambiguous-outcome rule was not established. | yes | Public excerpt available; complete book pattern unavailable. |
| FS-08 | unconfirmed | [Content-Based Router][p08]; `2e1bcb059062` | Solution explanation, configurable-rules paragraph | “a configurable rules engine”. Contract/versioning/testing requirements were not established by the excerpt. | yes | Public excerpt available; complete book pattern unavailable. |
| FS-09 | unconfirmed | [Message Filter][p09]; `899fcd8bbb8d` | Solution explanation | “the message is discarded.” A disposition exists; the claimed audit-boundary requirement remains unconfirmed. | yes | Public excerpt available; complete book pattern unavailable. |
| FS-10 | contradicted | EIP chapter 3, official PDF; `c1e7125dcebf` | Printed pp.72, 74, 77; PDF pages 16, 18, 21 | “channels provide buffering”; “not transactional”. These passages do not demonstrate contradiction of the general concern. | yes | Cited chapter available; contradiction verdict challenged. |
| FS-11 | unconfirmed | [Aggregator][p11]; `15d8640d5ad1` | Completeness conditions: Wait for All; Time Out | “evaluating those responses received within that time limit.” Partial-set handling exists; duplicate handling remains unconfirmed. | yes | Public excerpt available; complete book pattern unavailable. |
| FS-12 | unconfirmed | [Scatter-Gather][p12]; `ed4e25c160ba` | Mulesoft example; Durable Functions example | “Route errors propagate to the Scatter-Gather”. Failure and completion concerns exist; assess remaining clauses separately. | yes | Public examples available; complete book pattern unavailable. |
| FS-13 | unconfirmed | [Durable Subscriber][p13]; `d8697f78f17e` | Solution explanation | “saves messages for an inactive subscriber”. Explicit bounded-retention/replay requirements were not established. | yes | Public excerpt available; complete book pattern unavailable. |
| FS-14 | unconfirmed | [Resequencer][p14]; `cafe3058fa70` | Solution explanation | “internal buffer to store out-of-sequence messages”. Timeout/missing-message policy remains unconfirmed. | yes | Public excerpt available; complete book pattern unavailable. |
| FS-15 | unconfirmed | [Claim Check][p15]; `96395638cbc1` | Solution; enumerated storage/retrieval steps | “Store message data in a persistent store”. Lifetime/access-control obligations remain unconfirmed. | yes | Public excerpt available; complete book pattern unavailable. |
| FS-16 | unconfirmed | [Message Broker][p16]; `ddc6d825aa8a` | Solution; broker hierarchy | “determine the correct destination”. Mediation exists; bridge/protocol-contract mapping remains unconfirmed. | yes | Public excerpt available; complete book pattern unavailable. |
| FS-17 | unconfirmed | [Canonical Data Model][p17]; `02992f61d752` | Solution; translator-count comparison | “produce and consume messages in this common format.” Ownership/version-drift requirements were not established. | yes | Public excerpt available; complete book pattern unavailable. |
| FS-18 | partially-supported | [Routing Slip][p18]; `5e46ed0bbff9`; Process Manager `ac6e6180c5ee` | Routing Slip solution; Process Manager opening comparison | “specifying the sequence of processing steps.” Core per-message path mechanism is supported; “variants” needs clarification. | yes | Public pages available; complete book text unavailable. |
| FS-19 | unconfirmed | [Command-side Replica][p19]; `ef4d815712f4` | Solution; Benefits | “a read-only replica”; “potentially stale”. Bounding staleness/reconciliation remains unconfirmed. | yes | Page available; linked articles not exhaustively checked. |
| FS-20 | unconfirmed | [PostgreSQL PITR][p20]; `0c5f4cb3a63b`; PostgreSQL 18 PDF | §25.3 archive setup, recovery, timelines; whole-PDF phrase search | Exact combined RPO/RTO determinant assertion was not established. Specified objective phrases were absent from the PDF search. | yes | Page and manual representation available. |
| FS-21 | unconfirmed | Workbook [ch.5][sre5] `340f148f65a7`, [ch.2][sre2] `1b02c7f3f640`, [ch.3][sre3] `239b784698c7` | Generating Artificial Traffic; browser-probe SLI example; probe configuration | “A system can synthesize user activity”. The exact term is absent, but substantive mechanism/design support exists. | yes | Public book pages available; whole-book absence conclusion challenged. |
| FS-22 | partially-supported | OWASP ASVS 5.0.0 English PDF; `a2fa1bbe38f1` | Verification levels; V8; V8.4.1; V13.2.2; V13.3.2 | “consumer operations will never affect tenants”. Trust-boundary phrase search returned zero; other identified elements are supported. | yes | Complete matching PDF and CSV available. |
| FS-23 | resolved | [OpenID Federation 1.0][oid]; `4a71afdfbed5` | §11.4; §§8.7.2–8.7.3; §8.4.2 | “does not define a revocation process.” Revoked key/trust-mark status data are separately defined. | yes | Complete matching specification available. |

## E. Findings and required actions

These findings retain their original severity and disposition. The requested actions are recommendations; no repository edits were made.

### R-01 — Blocking: FS-21 overlooks substantive Workbook support

**Location:** `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/results.v1.json:51`, also line 52.

**Affected claim:** FS-21.

**Evidence:** The result closes the complete-book search as unconfirmed and identifies only case-study corroboration. Chapter 5 describes artificial user activity and coverage limitations; chapter 2 describes browser probes and measurement coverage; chapter 3 describes probe placement and geographically separate confirmation. See the per-claim row and linked chapters.

**Required action:** Reopen FS-21. Record the available support, identify any editorial synthesis, and distinguish an unsuitable original chapter citation from absence across the complete book. At minimum, evaluate a partially-supported disposition.

### R-02 — Blocking: FS-10's contradiction conclusion is not demonstrated

**Location:** `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/results.v1.json:173`–175; corresponding ledger limitation at `/Users/rbaranov/Projects/tycho/edition/patterns/reading-ledger.v1.json:1573`.

**Affected claim:** FS-10.

**Evidence:** The cited chapter discusses buffering, conditional reordering and nontransactional message loss. These support the identified concerns. They do not demonstrate the opposite of the removed statement. The universal “each stage” wording exceeds the examples' scope.

**Required action:** Reopen the contradiction finding. Narrow the claim or classify the overgeneralization appropriately. Retain “contradicted” only with an actual incompatible statement or counterexample tied to the intended meaning.

### R-03 — Blocking: grouped EIP closure obscures supported clauses

**Location:** `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/results.v1.json:55`–75; Aggregator limitation at `/Users/rbaranov/Projects/tycho/edition/patterns/reading-ledger.v1.json:1675`.

**Affected claims:** FS-06, FS-11, FS-12, FS-14, FS-15 and FS-16, within the eleven grouped EIP claims.

**Evidence:** Public pages establish acknowledgement mechanics, incomplete-set handling, partial-failure behaviour, buffering, payload storage and broker mediation respectively. Missing full chapters do not remove this available clause-level evidence.

**Required action:** Separate access limitations from claim support. Split composite statements, retain supported clauses, and identify the remaining unconfirmed obligations. Do not promote the original complete conjunctions to fully supported.

### R-04 — Non-blocking: 127 section lists differ between plans

**Location:** `/Users/rbaranov/Projects/tycho/edition/patterns/full-unit-reading-plan.v1.json`, `entries[].sections`; `/Users/rbaranov/Projects/tycho/edition/patterns/source-plan.v1.json`, `entries[].required_units[].sections`.

**Affected units:** 127 matched entries, including Layered Architecture and Failover / Failback.

**Evidence:** Matching by pattern ID, source ID and unit label produced 127 unequal lists. For example, Acknowledgements appears in the corrected Layered Architecture source plan and ledger but not its full-reading-plan section list. The original supporting JSON preserves the complete mismatch list under `scope_mismatches`.

**Required action:** Reconcile the lists or explicitly label the frozen original scope and map final dispositions to corrected ledger scopes. The mismatch alone does not prove incomplete reading.

### R-05 — Non-blocking: acceptance documents contain incompatible statements

**Location:**

- `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/ACCEPTED.md`, items 3 and 7.
- `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/RESOLUTIONS.md:13`.
- `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/ALTERNATIVES.md:44`.

**Affected claims/units:** EIP accepted gaps, especially FS-10 within the FS-06–FS-17 range.

**Evidence:** Earlier prose denies final EIP acceptance while later prose grants it. A range described as unconfirmed includes contradicted FS-10. Another document retains partial statuses where the final plan says blocked.

**Required action:** Mark superseded statements, specify precedence, and enumerate exact claim IDs.

### R-06 — Non-blocking: declared linked-source scope exceeds documented checks

**Location:** `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/claims.v1.json`, `full_source` fields for FS-01, FS-02, FS-03 and FS-19; corresponding results.

**Affected claims:** FS-01, FS-02, FS-03, FS-19.

**Evidence:** Registry scope includes linked articles or guidance, while individual results mainly document pattern-page checks. My page-level checks do not establish exhaustive linked-material absence.

**Required action:** Provide a finite linked-source manifest with revision and passage evidence, or narrow the stated scope.

### R-07 — Non-blocking: absent synonyms do not weaken FS-18's mechanism

**Location:** `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/results.v1.json:84`.

**Affected claim:** FS-18.

**Evidence:** Routing Slip describes a per-message sequence attached to the message. Absence of the literal words “encode” or “path” is not evidence against that paraphrase.

**Required action:** Separate the supported mechanism from uncertainty about “variants” and its relationship to Process Manager. Preserve the full-book access limitation.

### R-08 — Non-blocking: Workbook coverage metadata omits chapter 21

**Location:** `/Users/rbaranov/Projects/tycho/research/full-source-confirmation/results.v1.json:49`.

**Affected unit:** Complete Workbook source representation.

**Evidence:** The official contents include 21 numbered chapters. The result says chapters 1–20. The 34 count concerns web content URLs, not printed pages.

**Required action:** Correct the chapter range and name the representation explicitly.

## F. Checks actually run

### Original validator executions

The following invocations ran against the isolated review copy:

`/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/work/review-tree`

The interpreter was:

`/Users/rbaranov/Documents/Codex/2026-10-26/human-reviewer-human-review-private-tmp/work/venv/bin/python`

Each command had the form:

```text
<interpreter> -B scripts/<validator>.py
```

| Validator | Final exit status |
|---|---:|
| validate_sources | 0 |
| validate_pattern_sources | 0 |
| validate_pattern_cards | 0 |
| validate_pattern_owner_units | 0 |
| validate_pattern_semantic_audit | 0 |
| validate_pattern_atlas | 0 |
| validate_delivery_evidence | 0 |
| validate_edition | 0 |
| check_boundary, additional check | 0 |

Initial attempts failed because validation dependencies were missing, followed by two Git-dependent checks failing because the isolated copy lacked Git metadata. Dependencies and copied metadata resolved those execution failures. The final successful outputs are preserved under `checks` in the supporting JSON.

No validator was run against the original project directory.

### Other original commands and operations

| Operation | Execution evidence / result |
|---|---|
| Derive counts with Python `json` and `collections.Counter` | Exit 0; counts in section C |
| Retrieve/extract source HTML | `work/venv/bin/python work/review_sources.py`; exit 0 |
| Fetch and search Workbook content URLs | Python requests/parser script; exit 0; 34 content URLs |
| Extract PostgreSQL manual | `pdftotext -layout /private/tmp/pg18.pdf work/pg18.txt`; exit 0 |
| Render EIP printed pp.72, 74, 77 | `pdftoppm` for PDF pages 16, 18, 21; exit 0 |
| Inspect EIP rendered images | Image-view tool succeeded for all three pages |
| Count ASVS CSV requirements and levels | Python CSV/Counter script; exit 0; 345 requirements |
| Search ASVS trust-boundary variants | Python regex search; exit 0; zero matches |
| Recompute source/package hashes | Python `hashlib.sha256`; exit 0 |
| Compare original project content before/after | Exit 0; 1,946 files unchanged; zero additions/removals |
| Compare Git status before/after original review | Exit 0; unchanged, including pre-existing untracked `deliverables/` |

The PostgreSQL whole-PDF search returned zero whole-word matches for:

`failback`, `RPO`, `RTO`, `recovery point objective`, `recovery time objective`, `restore verification`, `restore drill`, `restore test`.

This establishes phrase absence in that representation, not absence of related concepts.

### Hashes recomputed

Full SHA-256 values for the principal document representations:

| Document | SHA-256 |
|---|---|
| EIP official chapter 3 PDF | `c1e7125dcebfdd9a2b23a922dfbbc9694e5f8048e81e14dc95e2882043ac4f66` |
| PostgreSQL 18 PDF | `9c6af8d2c8f0eda1b05e510bd8028f752162d2f5ce2db405bbf197336ce638d2` |
| ASVS 5.0.0 English PDF | `a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5` |
| ASVS CSV | `98c8fe911b9edb403af8ee05d3ce8201ecac2659e313b053890a62847cdcf680` |
| OpenID complete specification HTML | `4a71afdfbed5755d6704d6a089f450f10aa9914204b283eae5fadee2897d1911` |

These five local hashes were recomputed again during this correction and match the original observations.

The supporting JSON additionally preserves:

- `package_hashes`: 33 evidence-package file hashes.
- `samples`: 22 sampled-unit hashes and exact-match results.
- `source_manifest`: individual retrieved-source URLs and hashes.
- `sre_book_search`: 34 Workbook content-page URLs, hashes and match counts.

### Sources actually opened

The claim sources are individually identified in section D. Additional sampled pages opened were:

- [Database per Service](https://microservices.io/patterns/data/database-per-service.html)
- [Presentation Domain Data Layering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html)
- [Static Content Hosting](https://learn.microsoft.com/en-us/azure/architecture/patterns/static-content-hosting)
- [Competing Consumers](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html)
- [Ambassador](https://learn.microsoft.com/en-us/azure/architecture/patterns/ambassador)
- [API Gateway](https://microservices.io/patterns/apigateway.html)
- [Deployment Stamps](https://learn.microsoft.com/en-us/azure/architecture/patterns/deployment-stamp)
- [Shuffle Sharding](https://cortexmetrics.io/docs/guides/shuffle-sharding/)
- [Hexagonal Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html)
- [Materialized Views](https://www.postgresql.org/docs/current/rules-materializedviews.html)
- [Cassandra Dynamo](https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html)
- [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Argo Canary](https://argoproj.github.io/argo-rollouts/features/canary/)
- [Raft Overview](https://raft.github.io/)
- [Frontend Load Balancing](https://sre.google/sre-book/load-balancing-frontend/)
- [PostgreSQL Failover](https://www.postgresql.org/docs/18/warm-standby-failover.html)
- [Version-pinned PostgreSQL PITR](https://www.postgresql.org/docs/18/continuous-archiving.html)

The Workbook [contents page](https://sre.google/workbook/table-of-contents/) and all 34 linked content URLs were fetched, extracted and searched. The content URLs comprised:

```text
foreword-I, foreword-II, preface, how-sre-relates,
part-I-foundations, implementing-slos, slo-engineering-case-studies,
monitoring, alerting-on-slos, eliminating-toil, simplicity,
part-II-practices, on-call, incident-response, postmortem-culture,
managing-load, non-abstract-design, data-processing,
configuration-design, configuration-specifics, canarying-releases,
part-III-processes, overload, engagement-model, reaching-beyond,
team-lifecycles, organizational-change, conclusion,
slo-document, error-budget-policy, postmortem-analysis,
index, editors, colophon
```

These are paths beneath `https://sre.google/workbook/`. Fetching and searching every page is not a claim that every page was read in full.

### Correction-only checks

The following read-only checks were executed during this correction:

- `git --no-optional-locks -C /Users/rbaranov/Projects/tycho rev-parse HEAD` — exit 0.
- Git history inspection for the AI-review handoff — exit 0.
- Read the current handoff completely — exit 0.
- Recompute the original report hash — exit 0; matches its preserved hash.
- Compare current package hashes with the original records — exit 0 after correcting the comparison script to handle the renamed handoff.
- Recompute both disposition counters — exit 0; unchanged.
- Read `CODEX_THREAD_ID` — exit 0.
- Recompute the five principal document hashes — exit 0.
- Read the clock — succeeded.

The first package-comparison attempt exited 1 when it tried to hash the removed old handoff path. That was a correction-script error, not a project validation failure; the corrected comparison handled missing paths explicitly.

### Not executable or not performed

- Exact original time of day cannot be recovered from a contemporaneous recorded review timestamp.
- Exact deployed model version is not exposed.
- DeepSeek Harness Reviewer preset is unavailable in this environment.
- No borrowed or restricted full-book access was attempted.
- Original validators were not rerun for this reporting correction.
- No CI execution was performed.

## G. Limits and accepted gaps

**This is a partial, targeted review.**

The accepted gaps challenged remain:

1. FS-21's complete-book absence conclusion.
2. FS-10's contradiction classification.
3. Grouped EIP closure that does not retain available clause-level support.

The accepted full-text access limits remain valid limitations of this review:

- Complete EIP Chapter 4+ pattern text was unavailable to me.
- DDIA full text was unavailable to me.
- No missing book passages were inferred from public excerpts.

The DDIA blocked status is internally consistent: its source-plan unit has no completed reading record, and the related public Fowler reading excludes the book. This supports the honesty of the recorded limitation; it cannot prove that no unrecorded activity occurred elsewhere.

The PostgreSQL Failover / Failback partial status remains conservative. Section 26.3 discusses rebuilding a standby on the former primary and role switching. Phrase absence must not be generalized into absence of all recovery-to-redundancy guidance.

The sampling does not establish the completeness of all 143 claimed full/exact readings. Two sample representations differed from historical hashes. Linked-source absence claims remain bounded by R-06.

The current substantive evidence files match the original reviewed package. Changes to handoff/governance material do not constitute a new complete review of current HEAD.

## H. Verdict and authority

**Verdict: reject.**

- `ai_review: performed`
- `human_review: not-performed`
- `sufficient: 0`
- `partial_review: true`

The AI-review flag refers to checks actually performed in the original review and the limited reporting checks described above. It does not imply a fresh complete review of the current checkout.

Required next action: address R-01 through R-03 and resolve the reporting inconsistencies before a focused re-review.

This report provides **no owner acceptance, CI acceptance, merge permission or sufficient coverage**. No repository files were edited during this correction.

[p01]: https://microservices.io/patterns/data/event-sourcing.html
[p02]: https://microservices.io/patterns/communication-style/idempotent-consumer.html
[p03]: https://microservices.io/patterns/data/cqrs.html
[p04]: https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html
[p05]: https://keda.sh/docs/latest/
[p06]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventDrivenConsumer.html
[p07]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html
[p08]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html
[p09]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Filter.html
[p11]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html
[p12]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html
[p13]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DurableSubscription.html
[p14]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/Resequencer.html
[p15]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html
[p16]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBroker.html
[p17]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html
[p18]: https://www.enterpriseintegrationpatterns.com/patterns/messaging/RoutingTable.html
[p19]: https://microservices.io/patterns/data/command-side-replica.html
[p20]: https://www.postgresql.org/docs/current/continuous-archiving.html
[sre5]: https://sre.google/workbook/alerting-on-slos/
[sre2]: https://sre.google/workbook/implementing-slos/
[sre3]: https://sre.google/workbook/slo-engineering-case-studies/
[oid]: https://openid.net/specs/openid-federation-1_0.html

### review-manifest

```json
{
  "name": "review-manifest",
  "issue": 535,
  "identity": {
    "reviewer_harness": "Codex desktop app",
    "reviewer_vendor": "OpenAI",
    "model_family": "GPT-6",
    "exact_model_version": "not available",
    "model_version_limit": "No precise deployed model identifier or version is exposed.",
    "session_id": "01a17a03-0b7c-7513-87fe-1f3994862b1d",
    "session_id_evidence": "CODEX_THREAD_ID",
    "original_review_date": "2026-10-26",
    "original_review_exact_timestamp": "not available",
    "original_timestamp_limit": "No contemporaneous time-of-day field was recorded.",
    "correction_timestamp": "2026-10-26T22:28:08+01:00",
    "timezone": "Europe/Zurich",
    "repository_path": "/Users/rbaranov/Projects/tycho",
    "branch": "feature/TYCHO-535-read-the-155-pattern-source-plan-units-in-full",
    "original_review_checkout_head": "0531e9ce801dc04e8150afa8b92755c6338a55b5",
    "current_review_checkout_head": "ec9289ae7dd9a1f179133c46ca9991a59e86055a",
    "b1_evidence_head": "180597e52403e3dabb71c50eb92a5b991d6803b8",
    "handoff_path": "/Users/rbaranov/Projects/tycho/authoring/AI-REVIEW-HANDOFF_2026-10-26.md",
    "handoff_last_changing_commit": "ec9289ae7dd9a1f179133c46ca9991a59e86055a",
    "handoff_rename_policy_commit": "5afae41a0a0bd7443977cd2cd1ac7fed9542e2bc",
    "handoff_sha256": "13fc97f5ae933787c434fbbaabebe53749adbfa47ffdc0da8c716bba73a156d0",
    "original_report_available": true,
    "reconstructed_from_session_memory": false,
    "original_report_sha256": "cd4b1da910298e7c8d22b345afc941f9ae347a15f681060e25386d67a1f2c9bd"
  },
  "counts": {
    "basis": "Derived from JSON artifacts in the original review and recomputed during correction.",
    "units": {
      "full_read": 129,
      "full_read_exact_reuse": 14,
      "partial_read": 1,
      "blocked_current": 11,
      "total": 155
    },
    "claims": {
      "unconfirmed": 17,
      "contradicted": 3,
      "partially_supported": 2,
      "resolved": 1,
      "total": 23
    },
    "sampled_units": 22,
    "sample_hash_matches": 20,
    "sample_hash_differences": 2,
    "workbook_content_urls_searched": 34
  },
  "sampled_units": [
    {"batch": "01", "unit": "Database per Service"},
    {"batch": "02", "unit": "Presentation Domain Data Layering"},
    {"batch": "03", "unit": "Static Content Hosting"},
    {"batch": "04", "unit": "Competing Consumers"},
    {"batch": "05", "unit": "Ambassador"},
    {"batch": "06", "unit": "API Gateway"},
    {"batch": "07", "unit": "Event Sourcing"},
    {"batch": "08", "unit": "Deployment Stamps"},
    {"batch": "09", "unit": "Shuffle Sharding"},
    {"batch": "10", "unit": "Hexagonal Architecture"},
    {"batch": "11", "unit": "OpenID Federation 1.0"},
    {"batch": "12", "unit": "Materialized Views"},
    {"batch": "13", "unit": "Cassandra Dynamo Architecture"},
    {"batch": "14", "unit": "KEDA Documentation Landing"},
    {"batch": "15", "unit": "SRE Service Level Objectives"},
    {"batch": "16a", "unit": "Argo Canary"},
    {"batch": "16b", "unit": "Raft Overview"},
    {"batch": "17", "unit": "Event-Driven Consumer"},
    {"batch": "18", "unit": "Scatter-Gather"},
    {"batch": "19", "unit": "Command-side Replica"},
    {"batch": "20", "unit": "PostgreSQL PITR"},
    {"batch": "21", "unit": "Load Balancing at the Frontend"}
  ],
  "checked_claim_ids": [
    "FS-01", "FS-02", "FS-03", "FS-04", "FS-05", "FS-06",
    "FS-07", "FS-08", "FS-09", "FS-10", "FS-11", "FS-12",
    "FS-13", "FS-14", "FS-15", "FS-16", "FS-17", "FS-18",
    "FS-19", "FS-20", "FS-21", "FS-22", "FS-23"
  ],
  "findings": {
    "blocking": ["R-01", "R-02", "R-03"],
    "non_blocking": ["R-04", "R-05", "R-06", "R-07", "R-08"],
    "changed_during_correction": false
  },
  "verdict": "reject",
  "ai_review": "performed",
  "human_review": "not-performed",
  "sufficient": 0,
  "partial_review": true,
  "limits": {
    "full_155_unit_reread": false,
    "exhaustive_linked_source_review": false,
    "unavailable_sources": [
      "Complete EIP Chapter 4+ pattern text",
      "DDIA full text"
    ],
    "challenged_gaps": [
      "FS-21 complete-book absence conclusion",
      "FS-10 contradiction classification",
      "Grouped EIP closure obscuring available clause-level support"
    ],
    "validators_rerun_during_correction": false,
    "original_checks_apply_to": "0531e9ce801dc04e8150afa8b92755c6338a55b5",
    "current_substantive_evidence_matches_original_hashes": true,
    "intervening_governance_changes_fully_reviewed": false,
    "reviewer_preset_available": false,
    "repository_edited_during_correction": false,
    "owner_acceptance": false,
    "ci_execution": false,
    "merge_permission": false,
    "sufficient_coverage": false
  }
}
```
