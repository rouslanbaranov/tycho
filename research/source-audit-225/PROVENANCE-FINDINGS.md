# Provenance findings

Bounded findings discovered while reading pages for comparison evidence. They do not
authorize edits to the book under #225.

## Non-public source cited by a page

- `book/volumes/v01-requirements-and-architecture/c01-problem-framing/...` is not the
  affected page.
- Affected page: a top-level Netflix case-study page on Java platform convergence.
- The page cites record **R058**, which the audit ledger records as
  `excluded-from-scope`: a non-public internal team site not retrieved by this audit. The page itself asserts an earlier access date, which editorial review must resolve.
- No text from that site was read or used in any comparison. The page is assessed
  only for the readable part; claims resting on this source remain unresolved.
- No employer name, URL, internal terminology or source text is reproduced here.

## Required follow-up

1. Editorial review must verify whether the page's citation can be replaced by an
   admissible public source or removed.
2. Do not treat claims resting on that source as evidence until remediation; the
   page comparisons based on full R045/R020 remain usable.
3. Re-check sibling case-study pages for citations to excluded records before assessing
   them.

## Decision page claims inspection of blocked sources

- Comparison **C373** covers a decision page that says two named sources and a third
  source were inspected and admitted for bounded first-party claims.
- On 2026-10-25 both Spotify Engineering pages were retrieved in full. R043 and R044
  are now full-scoped-text-read, so the page statement matches the ledger.
- The remaining gap is metadata: the page evidence_scope.source_ids is empty and
  source_inspection_date is null. This is classified as qualified, not contradicted.

## Owner-accepted source limitations

Seven case pages are recorded as owner-accepted source limitations. Each cites at
least one blocked or non-public record; they are not verified pages. The former
Java-platform and Java 21 pinning gaps were closed by C404-C413.
