# External-agent task-level evaluation — 2026-10-31

Status: AI answerers and AI judge. Not human review, CI or owner acceptance.

## Setup

- 20 answerable tasks: 10 book, 5 atlas, 5 v12;
- 10 off-topic probes with empty evidence;
- each answerer saw only the question and retrieved evidence;
- a separate judge graded support, citation validity and off-topic abstention.

## Results

| Metric | Value |
|---|---:|
| answerable tasks | 20 |
| answered | 17 |
| abstained | 3 |
| fully supported | 16 |
| partially supported | 1 |
| unsupported | 0 |
| citation-valid tasks | 20 / 20 |
| off-topic abstained | 10 / 10 |
| false abstention | 3 / 20 = 15% |

Task score: 16/20 fully supported, 17/20 answered.

## Observations

- No unsupported answer passed the judge.
- The only partial answer was V4-V008: evidence named resource controls but
  not the explicit queue discipline.
- The three abstentions were V4-B016, V4-B004 and V4-A006; the answerer
  reported truncated or missing mechanism detail.
- Off-topic probes had empty evidence, so abstention was straightforward.

## Limits

- Excerpts were truncated to about 230 characters; some answers and
  abstentions reflect the cut, not the full page.
- The judge is AI-only and saw no gold answer.
- Support is not answer correctness against an external reference.
- No human review, CI, owner acceptance or production benchmark.
