# Pattern semantic page audit — 2026-10-21

Status: self-checked audit for issue #288. An independent agent review is recorded
separately. This is not independent human technical or editorial review, not sufficient
coverage and not owner acceptance.

## Scope

The audit covers all 419 canonical documents in the current tree: 304 technical pages,
6 decision pages, 97 navigation pages and the 12 V11 atlas pages. Every page has one
record with a content hash, a review date, required checks, findings and a disposition.

## Method

1. Read each page as a bounded page, not as a claim-by-claim source verification.
2. Apply tier-specific checks:
   - technical and decision pages: identity, question, content, evidence, limits and
     internal navigation;
   - navigation pages: identity, inventory, links, status and limits;
   - atlas pages: identity, cards, owner links, nonclaims and links.
3. Record only findings visible in the page, with an exact heading anchor or `page`.
   Each finding needs a remediation or an explicit gate.
4. Bind the record to the reviewed content with the page SHA-256 and recompute it in
   the validator.
5. Classify the page under the disposition and severity rules below.

The method is deliberately bounded: a recorded pass means the required elements were
inspected, not that every sentence was source-verified.

## Disposition and severity rules

- `sound`: no finding; all required checks pass.
- `sound-with-findings`: only low findings, each with a remediation or gate.
- `needs-remediation`: at least one medium or high finding with a concrete remediation.
- `blocked`: at least one finding has an explicit unresolved gate.

Severity:

- `low`: wording, staleness, navigation or duplicate text that does not change a
  mechanism or evidence claim.
- `medium`: missing, contradictory, unsupported or duplicate content that could
  mislead a technical or editorial decision, or an unsupported claim of executed work
  or external judging.
- `high`: fabricated independent human review or owner acceptance, or a central
  mechanism or safety claim contradicted with no bounded remediation.

## Artifacts

- [semantic audit](../edition/patterns/semantic-audit.v1.json);
- [JSON Schema](../schemas/pattern-semantic-audit.v1.schema.json);
- [validator](../scripts/validate_pattern_semantic_audit.py);
- [builder and queue](../scripts/semantic_audit.py);
- [adversarial tests](../tests/test_tycho_semantic_audit.py);
- premerge integration in [premerge_check.py](../scripts/premerge_check.py).

## Coverage and dispositions

| Measure | Value |
|---|---|
| Canonical pages | 419 |
| Technical pages | 304 |
| Decision pages | 6 |
| Navigation pages | 97 |
| Atlas pages | 12 |
| Sound | 278 |
| Sound with bounded findings | 93 |
| Needs remediation | 47 |
| Blocked | 1 |
| Pages with findings | 141 |
| Findings | 166 (118 low, 48 medium, 0 high) |

The blocked page is V11/C06, where Polyglot Persistence remains uncarded because no
technical owner exists. The seven open gates are independent human technical review,
independent human editorial review, owner acceptance, the blocked Polyglot entry and
three deferred page-split decisions.

## Independent agent review

The owner assigned the independent review agent **Reviewer** on 2026-10-21. It reviewed
PR #289 at commit `a0b0b95` and returned **ACCEPT-WITH-FINDINGS** with 17 findings. A
focused re-review found 7 residual findings; all 24 were addressed. See
[the review record](INDEPENDENT-AGENT-REVIEW_2026-10-21.md). This is non-human review and
does not satisfy the independent human review or owner acceptance gates.

## Finding themes

- 81 status findings are mostly retained historical or "proposed" wording in chapter
  source ledgers and older navigation pages that no longer matches the current tree.
- 33 navigation findings identify case or supporting pages with no internal route to
  their parent, a decision guide or a source-read record.
- 16 missing-item findings include pages that promise an original walkthrough or
  transfer limits that the page does not contain.
- 13 contradictory findings include duplicate or mutually inconsistent sections and
  naming or column mismatches in worked examples.
- 11 unsupported findings identify page claims without on-page source linkage.
- 11 duplicate findings restate the same case or claims in two sections.
- One shallow finding records missing inline evidence links in a technical page.

These are bounded editorial findings. They do not revoke the owner's earlier acceptance
of the 69 primary manuscripts; they identify remediation work against the exact pages.

## Remediation and external gates

The 47 `needs-remediation` pages and the other findings remain work items. The audit
records each remediation or gate; it does not claim that all findings were fixed.

- Independent human technical review: open; no named human reviewer.
- Independent human editorial review: open; no named human editor.
- Owner acceptance: open; not recorded.
- Polyglot Persistence: blocked; keep uncarded until an owner exists.
- Three split candidates: deferred with migration gates; no split performed.

Five V11 pages were corrected where the audit confirmed a concrete defect:

- the landing: Phase 5/open-audit wording replaced with Phase 6/recorded-audit wording;
- C01 Self-Contained Service: the owner note now describes only the anchored section;
- C02 Gateway Aggregation: the "does not own aggregation" contradiction was removed;
- C03 Process Manager: the self-referential Routing Slip entry became Idempotent Receiver;
- C08 Causal Ordering: the self-referential entry became Read Replicas.

Each corrected page has a precise correction note in the audit artifact. The remaining
findings are recorded for a bounded remediation task rather than silently fixed.

## Limits

- This is self-checked work plus an independent agent review; it is not human
  verification or owner acceptance.
- The audit records a bounded page reading and does not verify every sentence against
  an external source.
- Page hashes bind the record to the reviewed content; a later page edit invalidates
  the record until it is re-reviewed.
- No release, deployment, hosted retrieval, benchmark or CI result is claimed.
- The 40 non-catalog related labels are recorded as deliberate non-routes, and three
  catalog-index reads are marked intentionally unused; neither is a fabricated route.

## Reproduction

```text
BRANCH=feature/TYCHO-288-audit-all-419-pages-semantically-and-close-residual-atlas-gaps
.venv/bin/python3 scripts/semantic_audit.py --queue /tmp/tycho-semantic-queue
.venv/bin/python3 scripts/semantic_audit.py --reviews /tmp/tycho-semantic-reviews
.venv/bin/python3 scripts/validate_pattern_semantic_audit.py
.venv/bin/python3 scripts/premerge_check.py --branch "$BRANCH" \
  --issue-title '[E17-29] Audit all 419 pages semantically and close residual atlas gaps'
```

The queue and per-page review files are intermediate working data; the committed
artifact is the canonical record. The validator and premerge commands require the
validation dependencies and `.venv/bin/python3`; the system Python does not provide
`jsonschema`.
