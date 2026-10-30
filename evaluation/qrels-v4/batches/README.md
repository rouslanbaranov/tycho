# Qrels v4 batches — provisional

Status: **provisional**, not final qrels v4.

B01–B03 are validated by `validate_qrels_v4.py` (15 book queries each), but
their coverage is narrow: each batch is concentrated in one chapter/topic.
Codex reported this explicitly. Do not merge them as a representative final set
without coverage review or rework.

B04–B06 are validated; B04 spans 5 volumes/5 chapters, B05 8/8, B06 9/12.

`content_commit` for B01–B03 was normalized from `a6d962ce` to `7918391f`
after verifying with `git diff -- book edition generated` that canonical content
and indexes did not change between the commits. No grades changed.

Remaining batches: A01–A02, V01–V02.

Final merge is allowed only after all ten batches pass and coverage is reviewed.
