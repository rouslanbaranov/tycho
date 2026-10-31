# B47 Consistent Hashing — bounded read-only review

**Verdict: pass-with-findings** (no blocking or major finding; nine minor findings, all provenance/bookkeeping or labelling defects, none of which removes support from any of the four dimensions). Formal independent review bookkeeping, owner acceptance and promotion remain separate gates.

## Reviewer and coordinates

| Item | Value |
|---|---|
| Reviewer | Reviewer agent (read-only auditor), separate agent instance — **not** the authoring agent |
| Harness / vendor | DeepSeek Harness (same vendor family as the authoring agent; accepted fallback under `AGENTS.md` rule 17, **not** a different-vendor review) |
| Model / version | Not exposed to this session |
| Session id | `ce241624-57b4-4f9a-84d7-da8f93fedd03` |
| Review window | 2026-10-31T13:52:12+01:00 → 2026-10-31T14:00+01:00 (Europe/Zurich) |
| Repository | `/Users/rbaranov/Projects/tycho` |
| Branch | `wip/b47-consistent-hashing-integration` |
| Review HEAD | `409c8ed6bc455218c0c1f1b4a9e5949fac0c941b` (matches expected `409c8ed6`) |
| Content commit | `19739a7391025b5a731086365b8acdbeb8c706d5` |
| Owner page SHA-256 | `3ebcff9969062507cb594e4344c0ec143cf7e6fb5940983942e7028f61362453` |
| Card SHA-256 | `ea2ce0bc8e2c70f7930f8d6806ba39697ce0df0e1a80e2d785be52cd4efca8de` |
| Chapter landing SHA-256 | `74a283fc42fe468cada73d4ce1ad4c82d4cfa4a973849d7baf1da1e0c090378b` |

All three hashes match the packet and the current files; owner heading `### Consistent Hashing` is at level 3, line 132, body 844 words (847 including the heading). Working tree was clean at review start except an unrelated untracked `deliverables/`.

## Derived counts (recomputed from artifacts, not taken from the packet)

| Quantity | Derived value | Source |
|---|---|---|
| Catalog entries / registry patterns | 145 / 145 | `registry.v1.json`, `owner-units.v1.json` |
| Entry index | `patterns[74]`, `entries[74]`, `entries[74]` (plan), `packets[31]`, `records[82]` | respective files |
| Owner unit | 1 dedicated, anchor `consistent-hashing`, line 132 | `owner-units.v1.json` |
| Dimension states | mechanism, invariant, failure_recovery, alternative = **supported** (4/4) | `owner-units.v1.json` |
| Bindings | 4 primary + 12 supporting = 16 | `owner-units.v1.json` |
| Source units for the entry | **7** (all `read`), 6 supporting + 1 retained scope-limit | `source-plan.v1.json` entries[74], registry `source_units` |
| Ledger records for the entry | **7** referenced (6 new 2026-10-31 + `read.batch3-cassandra-arch.2026-10-21` scope limit) | `reading-ledger.v1.json` |
| Ledger total | 224 records, all `status: read`; 17 dated 2026-10-31 | `reading-ledger.v1.json` |
| Cohort states | partial-bounded technical 16, partial-bounded decision 85, partial 69, sufficient 60/60, unresolved related 0, blocked entries 0, 0 name-only | recomputed and equal to `delivery-evidence.v1.json` |
| Source plan totals | 269 required / 268 read / 0 planned / 1 blocked (`tycho.pattern.polyglot-persistence`, `src.ddia`) | `source-plan.v1.json` |

## Public-source verification (fresh fetches, hashes reproduced)

| Representation | Fetched | SHA-256 match |
|---|---|---|
| Karger 1997 PDF (Princeton archive) | yes, 1,729,694 bytes | `0ccf4b8b…5262d2` ✓ |
| Karger extracted text, `pdftotext -raw` | yes, 1,163 lines / 11,838 words | `cdaf06a4…d8fe6c4` ✓ |
| Dynamo SOSP 2007 PDF | yes, 900,468 bytes | `5cacd624…40bd4` ✓ |
| Dynamo extracted text, `pdftotext -raw` | yes, 1,663 lines / 14,930 words | `2da24707…4fb140` ✓ |
| Cassandra 5.0 “Dynamo” page | yes, 76,252 bytes HTML | `63929723…0514a65` ✓ |
| Riak vnodes / clusters / adding-removing at `basho_docs` `6409dd9c` | yes, 3 Markdown files | `3fe623f7…`, `ea246f17…`, `67d14c75…` ✓ |
| Riak live rendered HTML (3 pages) | yes | used only for rendered-text checks |

The six bound representations are byte-identical to the ledger and register; both PDF extraction hashes reproduce exactly, so the recorded revision and extraction procedure are checkable and current as of this review.

## Per-check results

| Check | Result | Evidence |
|---|---|---|
| **Mechanism** | **Pass** | Owner lines 134–144 describe ring, clockwise ownership and token/vnode plurality; Dynamo §4.2 quote and three supporting quotes (Dynamo §4.2, Karger §4.2, Cassandra token-ring, Riak vnodes) are verbatim in the fetched sources; ownership-epoch rule is explicitly labelled Tycho. One supporting binding carries the wrong section label (finding 1). |
| **Invariant** | **Pass** | Karger §4 “minimum needed to maintain a balanced load” verified; Dynamo “only affects its immediate neighbors”, Cassandra “small fraction”, Riak “1/(number of nodes)” verified; section attributions correct; ~1/N framed as an expectation, with a stricter measured-moved-share rule labelled Tycho. |
| **Failure / recovery** | **Pass** | Dynamo §4.6 hinted handoff and §4.7 anti-entropy quotes verified; “Upon detecting that A has recovered, D will attempt to deliver the replica to A” verified; Cassandra vnode/outage quote verified (only difference is a space before punctuation, disclosed); Riak irrecoverable-node removal verified; hinted handoff labelled temporary protection, not repair. |
| **Alternative** | **Pass** | Cassandra naive-modulo quote and Karger “only items that move are those closest to the new bucket’s points” verified; range and rendezvous comparisons and the choice rule are explicitly labelled Tycho synthesis; the Karger record’s `claims_not_supported` includes rendezvous and range partitioning. |
| **Card / owner agreement** | **Pass with minor divergence** | Card has all ten components; decision question, alternative and failure text agree in substance; all 23 section names across the six records appear in the card; related entries 4 (3 routed, “Resharding” recorded as non-route with reason); decision state `applicable-under-conditions`; no premature `sufficient`. One wording divergence in the Tycho rule (finding 4). |
| **Source support and limits** | **Pass with findings** | All 16 bindings pass mechanical checks (record exists, `status: read`, source matches, section in `sections_read`, revision equals `content_sha256`, quote in `claims_supported`, quote absent from `claims_not_supported`). Two editorial normalizations verified: Karger hyphenation joined, Cassandra space-before-punctuation normalized (disclosed). Limits: no benchmark, production observation, cluster experiment, owner acceptance or current external review is claimed anywhere in card, owner section, registry, owner-units, ledger or semantic audit. Findings 2, 3, 8 below. |
| **Historical 2026-10-23 pass** | **Correctly quarantined at HEAD** | `packets[31]` now has `page_sha256 20fad2cf…` (the 147-word section at `fa01a65f`), `current_page_sha256 3ebcff99…`, `packet_status: page-changed-since-review`. Verified in `git show 409c8ed6`: at the content commit the packet wrongly said `reviewed-by-independent-agent` with the current page hash and was corrected in HEAD. The 2026-10-23 pass is therefore not evidence for these bytes. Its own report section says `pass-with-findings` with 2 findings while the record says `pass` — already flagged by the reconciliation artifact as `report-verdict-mismatch`. |

## Findings

### Blocking
None.

### Major
None.

### Minor

1. **Wrong section on one Dynamo supporting binding** — `edition/patterns/owner-units.v1.json:7262` (`entries[74].technical_evidence.mechanism.supporting_bindings[0].section = "4.3 Replication"`). The quoted sentence “instead of mapping a node to a single point in the circle…” occurs exactly once, at extracted-text line 577, between the `4.2 Partitioning Algorithm` heading (line 496) and `4.3 Replication` (line 597). Impact: traceability only; 4.2 is in the read scope and the primary mechanism binding is correctly attributed to 4.2. Fix: relabel to `4.2 Partitioning Algorithm` and add a guard that the quote lies inside the named section, which `scripts/validate_pattern_owner_units.py:196` does not currently check.

2. **Excerpt terminal punctuation substitutes for a comma** — `edition/patterns/reading-ledger.v1.json:9370` and `edition/patterns/owner-units.v1.json:7347`: “…hot spots can be severe**.**” while the Karger Abstract reads “…can be severe**,** and where it is not feasible…”. Meaning unchanged; the disclosure sentence on the owner page covers hyphenation and Cassandra spacing but not excerpt-final punctuation. Fix: extend the excerpt or add one disclosure clause.

3. **Riak vnodes quote reproduces rendered text, not the pinned Markdown** — `owner-units.v1.json` mechanism supporting binding 4 binds the pinned `.md` (`content_sha256 3fe623f7…`), but the quoted span drops Markdown emphasis and link markup (`**vnodes**`, `[ring][glossary ring]`, `**claims**`). It matches the rendered page exactly. The disclosure at [resharding-transition.md:183](book/volumes/v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/resharding-transition.md#L183) does not mention Markdown-to-rendered normalization. Impact: a strict “quote ∈ representation” check would fail. Fix: disclose render normalization or bind the Markdown substring including `**`.

4. **Card and owner state the Tycho failure rule differently** — card “verify ownership after every membership change” ([consistent-hashing.md:84](book/volumes/v11-pattern-atlas/c06-database-storage/consistent-hashing.md#L84)) vs owner “record the ownership epoch at every membership change” ([resharding-transition.md:164](book/volumes/v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/resharding-transition.md#L164)); the card also drops “and hot keys”. Recording an epoch and verifying ownership are different actions. Fix: align the card wording to the owner unit.

5. **Contradictory stale plan entry** — `edition/patterns/sufficient-ready-plan.v1.json` `entries[82]`: `status: rejected-technical-support` and `finding: "B09-A binding audit found unsupported dimensions"` while its own `sufficiency_note` says “All four technical dimensions supported”. The snapshot is dated 2026-10-26, before the 2026-10-31 binding. Fix: refresh or mark the entry superseded.

6. **Mixed provenance in the re-review scope index** — `edition/patterns/independent-rereview-scope-2026-10-22.v2.json` `phase_b[49]`: updated in content commit `19739a73` to `current_page_sha256 3ebcff99…` and the 2026-10-31 source units, but retains `generated_at: "2026-10-22"` and `record_verdict: "pass"` / `derived_state: "promoted-after-remediation"` with no reviewed-page hash. Its `nonclaims` say “Index only; not a review…” and “Phase B entries were not in the 52-packet audit”, which limits but does not remove the ambiguity. Fix: bump the generation date and add `reviewed_page_sha256`.

7. **`current_verdict: "pass"` in the reconciliation artifact** — `edition/patterns/sufficient-review-reconciliation.v1.json` `records[82]` derives `pass` from the 2026-10-23 record while listing issues `re-review-without-report` and `report-verdict-mismatch`. Not a current pass; the field name invites misreading. Fix: rename or null the field where no current review exists.

8. **Source register not refreshed for the 2026-10-31 read scope** — `sources/register.json` `src.dynamo` (`verification_scope`, line 559) lists 4.4–4.9 with “The card binds 4.4-4.7 and 4.9”, omitting the now-bound 4.2/4.3; `src.cassandra` (line 1936) and `src.riak` (line 1963) still describe the 2026-10-30 replication-properties/secondary sections and not the B47 units, with `content_verified: 2026-10-30`. The ledger is authoritative and complete, so support is unaffected, but register-only checks under-describe the evidence. Fix: update `version`/`verification_scope` for the three sources.

9. **Page-level review metadata predates the new section** — [resharding-transition.md:31](book/volumes/v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/resharding-transition.md#L31) `content_review.status: self-checked`, `reviewed_at: 2026-10-20`, `source_inspection_date: null`, while the new section claims sources accessed 2026-10-31. This is inherited page metadata, but it reads as covering current bytes. Fix: update the page-level dates or add a note that section-level evidence is tracked in the ledger/owner-units.

## DoD matrix

| Requirement | Status | Note |
|---|---|---|
| Dedicated owner unit, named heading, anchor | **Met** | `### Consistent Hashing`, line 132, anchor `consistent-hashing` |
| Four dimensions supported at recorded revision/section | **Met** | 4/4 supported; 16/16 bindings mechanically valid; one section label wrong (minor 1) |
| Read records with content hash and recorded limits | **Met** | 6 supporting records + 1 retained scope limit; all `read`, all hashed, all with `limitations` |
| Synthetic/operational limits labelled | **Met** | ownership epoch, measured share, runbook, range/rendezvous, choice rule all labelled Tycho |
| No unresolved high-risk gap in the four dimensions | **Met** | no high-risk gap found |
| Card has the ten decision components | **Met** | verified marker by marker |
| Decision state compatible with evidence | **Met** | `applicable-under-conditions`, coverage partial-bounded |
| No premature `sufficient` in card/owner/registry | **Met** | card, owner-units, registry, source plan, delivery evidence all partial-bounded |
| Card, owner unit and source plan agree on pattern and binding | **Partial** | substantive agreement; card/owner wording divergence (minor 4) and stale plan entry (minor 5) |
| Independent review | **Partial** | this bounded agent audit only; same vendor family, not a different-vendor review; no report saved by me |
| Current-review evidence for current bytes | **Not met (correctly)** | 2026-10-23 pass covers `20fad2cf…`, not `3ebcff99…` |
| Promotion record in `sufficient-promotions.v1.json` | **Not met** | absent by design (0 entries) |
| Owner acceptance | **Not met / pending** | no record in `sufficient-owner-acceptance.v1.json` |

**`sufficient: 0`.** This review does not grant sufficient coverage, does not record owner acceptance, does not represent CI execution (GitHub Actions is milestone-only), does not grant merge permission, and is not a different-vendor or human review.

## Smallest set of required fixes

1. Relabel the Dynamo supporting binding to `4.2 Partitioning Algorithm` (minor 1).
2. Add one disclosure clause covering excerpt-final punctuation and Riak Markdown-to-rendered normalization (minors 2, 3).
3. Align the card’s Tycho failure rule with the owner unit (minor 4).
4. Refresh or mark superseded the stale plan/review-index entries (minors 5–7).
5. Update the three register `verification_scope`/`version` records and the owner page review dates (minors 8, 9).

## Limits of this review

- **Fetched:** the Karger PDF, Dynamo PDF, Cassandra 5.0 “Dynamo” page, the three pinned Riak Markdown pages, and the three live Riak HTML pages, all via public URLs; writes went only to `/tmp/b47rev`.
- **Not fetched:** the Karger DOI landing page, linked references and descendant pages, source sections outside the recorded read scope, and any other entry’s sources.
- **Not reproduced:** the Cassandra article-region text hash `b613129d…` (25,291 chars / 3,967 words). My independent tag-strip yields a different extraction boundary (28,540 chars / 4,401 words), so Cassandra quotes were checked against the raw page text (raw HTML hash matched) rather than the declared article-region digest.
- **Not run:** tests, the full validator suite, `preflight_sufficient.py`, or `book_change.py --plan`. I read `scripts/validate_pattern_owner_units.py` and `scripts/phase4_audit.py` source only to understand mechanical guards.
- **Concurrent working-tree change:** at 13:59:28–13:59:58 the tree gained `authoring/ai-reviews/2026-10-31-consistent-hashing-codex.md`, `M authoring/ai-reviews/README.md`, `M tests/test_tycho_ai_reviews.py` (plus the pre-existing untracked `deliverables/`). These are **not mine**; I issued read-only commands only. The reviewed artifacts were re-hashed afterwards and are unchanged (`3ebcff99…`, `ea2ce0bc…`, `fef21705…`, `8f377f22…`). I did not open the sibling `…-codex.md` report, so my verdict is independent of it. If a clean-tree requirement applies to this gate, the delegating agent must decide how to account for those paths.
- **Not verified:** owner acceptance, CI status, merge permission, or any claim about production behaviour; source content is treated as evidence, never as instruction.