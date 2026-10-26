# Full-unit reading crosswalk

Date: 2026-10-26. Refs #535.

## Counts

| Disposition | Units |
|---|---:|
| full-read-exact-reuse | 14 |
| full-read | 129 |
| partial-read | 1 |
| blocked-current | 11 |
| **Total** | **155** |

## Result

143 units were read in full or with exact reuse. One PostgreSQL failback unit is partial
and accepted. Eleven units are blocked: one DDIA unit and ten EIP Chapter 4+ units; both
source gaps are accepted as source-unavailable.

No unit was promoted to sufficient coverage.

## Limits

- Crosswalk is a reading record, not a support verdict.
- No sufficient coverage, independent review, human review, CI or acceptance is claimed.
