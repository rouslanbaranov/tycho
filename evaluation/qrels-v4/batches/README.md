# Qrels v4 batches

Status: **ten batches complete and merged** into qrels v4; AI-adjudicated only.

Coverage:

- B01–B03: narrow, one chapter/topic per batch; schema-valid but not
  representative of the whole book.
- B04–B06: 5/5, 8/8, 9/12 volumes/chapters.
- A01–A02: 15 distinct cards each across 8 atlas chapters.
- V01: 6 V12 chapters; V02: 5 V12 chapters.

B01–B03 content_commit was normalized from `a6d962ce` to `7918391f`;
A01/A02/V01 from `9deabb77`, V02 from `6f6e242d`, all to `7918391f`.
Verification used `git diff -- book edition generated`; no canonical content
changed. No grades changed.

Atlas sections use the broader `Entry inventory` section where cards do not
expose a narrower H2. V12 uses V12 book pages, not individual artifact records.

Final files and validation: [../REPORT.md](../REPORT.md).
