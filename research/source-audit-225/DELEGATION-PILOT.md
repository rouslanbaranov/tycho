# Delegation pilot - reading extraction

**Date:** 2026-10-24. **Verdict:** viable for bounded reading/extraction, with
central validation. Not a substitute for page-level comparison judgment.

## Scope

Four landing-only sources, two reader children, two sources each:

| Record | Source | Lines / words | Agent |
|---|---|---|---|
| R081 | src.otel-collector | 308 / 1,786 | A |
| R082 | src.prometheus-storage | 180 / 2,199 | A |
| R083 | src.prom-alerting | 138 / 343 | B |
| R084 | src.aws-leases-enrichment | 100 / 2,005 | B |

Each child received the local file, exact line/word/hash, a fixed JSON schema,
and instructions to read sequentially, exclude site chrome, label
representation gaps, and write only to `/tmp/pilot6/records/`.

## Results

- **4/4 records passed** line, word and SHA-256 checks after one parent fix.
- **3/4 passed the full schema on first validation.** R081 returned only two
  `tycho_candidates`; the parent added one valid book path, then it passed.
- R083 correctly reported that only 76 of 343 words are technical prose; the
  rest is documentation navigation, pagination and version selector. It did not
  treat chrome as content.
- R084 read all eight sections, excluded only the reader header, and recorded
  that the representation has no byline or figures.
- R081 recorded two capture artifacts without losing prose: a Mermaid/front-
  matter concatenation at line 174 and HTML entities; it also found an internal
  inconsistency (send_batch_size cited but absent from the shown config).
- R082 flagged a measurement nuance: Python whitespace split gives 2,199 words,
  while POSIX wc -w gives 2,210 because 24 non-breaking spaces join tokens in
  the tree diagram. The manifest uses the Python count.
- Parent spot-checks against the local text found no invented mechanisms in
  R082, R083 or R084. The claims matched the source passages.
- Candidates were action-oriented and their paths existed. R084 produced five;
  R082 and R083 produced three; R081 underproduced.

## Quality assessment

**Strong:** evidence fidelity, exact line/word/hash discipline, chrome
separation, source-silence notes, candidate paths, timeliness (both children
returned records within the same short window).

**Weak:** candidate-count compliance is not self-enforcing; one child returned
two instead of three. A parent validator caught it, but the schema must be
checked mechanically on every record.

**Unresolved:** neither child performed independent review, and the parent read
all four sources for calibration, so this pilot does not establish that a
parent can accept delegated records without reading. It establishes that
delegated extraction is usable when the parent validates and spot-checks.

## Implication for book analysis

Delegation is suitable for **reading and evidence extraction**, not for
comparison verdicts. Page-level claims must stay centralized because the parent
needs a consistent baseline anchor, support classification and severity. If
children write book findings directly, the result will be inconsistent
terminology and duplicated or conflicting comparisons.

## Recommended guardrails for scale-up

1. One child per 1-2 finite units; never a whole documentation collection.
2. Fixed manifest with URL, version, file, lines, words and SHA-256.
3. Schema requires 3-6 existing candidates and 6-12 notes; validator rejects
   otherwise.
4. Parent spot-checks at least one claim per record and reads every record with
   a representation gap.
5. Comparisons remain parent/Reviewer work; children only supply source claims.
6. Reviewer samples 10-20% of records and all supplement/partial records.
7. Keep records in a pilot ledger until a batch is accepted; do not inflate the
   canonical reading count from unvalidated output.

## Status

Pilot records are validated but **not merged** into `readings.json`. The
canonical ledger remains 80 records. This report is process evidence, not a new
source reading.
