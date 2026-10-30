# Qrels v4 batches

Status: **ten batches complete and merged**; A01–A02 use dedicated card sections
and zero Entry inventory anchors.

Coverage:

- B01–B03 (reworked): 12 volumes and 15 chapter topics together; 12 case-page
  direct answers.
- B04–B06: 5/5, 8/8, 9/12 volumes/chapters.
- A01–A02: 13 and 16 distinct cards across 8 atlas chapters; zero Entry inventory sections.
- V01: 6 V12 chapters; V02: 5 V12 chapters.

B01–B03 content_commit was normalized from `a6d962ce` to `7918391f`;
A01/A02/V01 from `9deabb77`, V02 from `6f6e242d`, all to `7918391f`.
Verification used `git diff -- book edition generated`; no canonical content
changed. No grades changed.

Atlas sections use dedicated card pages; zero `Entry inventory` sections
remain. V12 uses V12 book pages, not individual artifact records.

Final files and validation: [../REPORT.md](../REPORT.md).
