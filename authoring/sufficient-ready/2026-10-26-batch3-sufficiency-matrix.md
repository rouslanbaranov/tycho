# Batch 3 sufficiency matrix

Date: 2026-10-26. Refs #532. This is not sufficient coverage and not human review.

## Selection

Six application-boundary entries with a dedicated admitted source, all four
owner-unit technical dimensions `supported`, and a reviewed card/owner binding.

## Result

| Entry | Source | Status | Remaining limit |
|---|---|---|---|
| Layered Architecture | Fowler layering | **sufficient-ready** | logical layers are not deployment units |
| Modular Monolith | Monolith First | **sufficient-ready** | module enforcement is build/review discipline |
| Hexagonal Architecture | AWS hexagonal | **sufficient-ready** | adapter mapping overhead |
| Clean / Onion Architecture | Clean Architecture | **sufficient-ready** | DTO boundary and static-check limits |
| DDD / Bounded Context | Fowler bounded context | **sufficient-ready** | language and context ownership |
| Database per Service | microservices pattern page | **sufficient-ready** | cross-service query and consistency |

## Limits

- `sufficient-ready` is a pilot label, not a registry `sufficient` promotion.
- Decision coverage remains `partial-bounded`.
- No human review, CI, owner acceptance or sufficient coverage is claimed.
- Source records were assessed from ledger metadata and owner-unit states, not re-read.
