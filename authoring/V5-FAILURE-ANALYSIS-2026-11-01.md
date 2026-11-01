# v5 citation and atlas failure analysis — 2026-11-01

Status: AI-only analysis of the completed 50-question v5 holdout. No human
review; no book/atlas changes.

## Citation-invalid answers

Ten results were marked citation-invalid:

Q150, Q154, Q158, Q166, Q174, Q179, Q180, Q185, Q191, Q197.

Mechanical check against the indexed section keys:

- every citation resolves to an indexed section;
- zero bad section keys;
- each answer is missing 5-8 of the precomputed required_evidence anchors;
- two judge passes mostly agree that the substantive citations are valid.

The judges conflated two different contracts:

1. citation validity: every citation resolves and supports a claim;
2. required-evidence coverage: the precomputed anchor list appears.

Only the first belongs in citation_valid. The second is a separate coverage
metric. The current v5 result therefore understates citation validity.

## Atlas failures

Only Q175 of 12 atlas questions passed.

- 11 of 12 failed on core coverage, usually one missing core claim;
- 3 were also marked citation-invalid only because required anchors were absent;
- no bad citation keys were found;
- failures cluster on extra claims (contraindications, RFC/storage rule, BFF
  release coupling, stale routing, sloppy quorum, index lifecycle).

The atlas layer was reached for some answers, but the claim sets ask for more
than the concise answer admits. A 5-core-claim rubric with a 150-220 word
answer creates a structural coverage ceiling. This is a rubric problem first,
not evidence that atlas search is broken.

## Required corrections

1. Split citation_valid from required_evidence_coverage in the judge schema.
2. Limit core claims to 3 per question; move the rest to optional.
3. For atlas questions, require an explicit atlas card or owner page in the
   evidence map, not just any book section.
4. Restore full v3 answers for the next holdout; concise v3 fixed length but
   compressed away core claims.
5. Generate a new v6 corpus and compare only within v6.

## Limits

- analysis is based on judge outputs, not a human adjudication;
- citation support was judged without reading evidence;
- v5 is consumed and must not be tuned for a new score.
