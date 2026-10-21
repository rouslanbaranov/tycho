# Pattern semantic page audit — 2026-10-21

Status: self-checked audit for issue #288. It is not independent technical or editorial
review, not sufficient coverage and not owner acceptance.

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
5. Classify the page as `sound`, `sound-with-findings`, `needs-remediation` or
   `blocked` under the rules in the artifact.

The method is deliberately bounded: a recorded pass means the required elements were
inspected, not that every sentence was source-verified.

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
| Sound with bounded findings | 100 |
| Needs remediation | 40 |
| Blocked | 1 |
| Pages with findings | 141 |
| Findings | 166 (118 low, 48 medium, 0 high) |

The blocked page is V11/C06, where Polyglot Persistence remains uncarded because no
technical owner exists. The seven open gates are independent technical review,
independent editorial review, owner acceptance, the blocked Polyglot entry and three
deferred page-split decisions.

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

The 40 `needs-remediation` pages and the other findings remain work items. The audit
records each remediation or gate; it does not claim that all findings were fixed.

- Independent technical review: open; no named reviewer.
- Independent editorial review: open; no named reviewer.
- Owner acceptance: open; not recorded.
- Polyglot Persistence: blocked; keep uncarded until an owner exists.
- Three split candidates: deferred with migration gates; no split performed.

The V11 landing and four V11 cards were corrected where the audit confirmed a concrete
contradiction or self-reference. The remaining findings are recorded for a bounded
remediation task rather than silently fixed.

## Limits

- This is agent self-review; it is not independent verification or acceptance.
- The audit records a bounded page reading and does not verify every sentence against
  an external source.
- Page hashes bind the record to the reviewed content; a later page edit invalidates
  the record until it is re-reviewed.
- No release, deployment, hosted retrieval, benchmark or CI result is claimed.
- The 40 non-catalog related labels are recorded as deliberate non-routes, and three
  catalog-index reads are marked intentionally unused; neither is a fabricated route.

## Reproduction

```text
python3 scripts/semantic_audit.py --queue /tmp/tycho-semantic-queue
python3 scripts/semantic_audit.py --reviews /tmp/tycho-semantic-reviews
python3 scripts/validate_pattern_semantic_audit.py
python3 scripts/premerge_check.py --branch feature/TYCHO-288-... --issue-title ...
```

The queue and per-page review files are intermediate working data; the committed
artifact is the canonical record.
