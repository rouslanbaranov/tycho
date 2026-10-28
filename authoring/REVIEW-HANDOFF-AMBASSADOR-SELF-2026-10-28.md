# Manual review hand-off — Ambassador and Self-Contained Service

Use this while Codex is rate-limited. Reviewer must be read-only and independent.

- HEAD: 63301736
- Owner units SHA-256: 8b960a3a15edd819a85c7a3f9e6f5fb871d41ff90f4b8fd1c29fe7a9737c4a68
- Source plan SHA-256: 6a669730505a3912669c495e58f97f9d14f1d8bdd401329798ff91db602fa381

## Ambassador

Scope: tycho.pattern.ambassador. Read the owner unit, source plan entry,
read.microsoft-ambassador.2026-10-21, the owner Ambassador section, and
book/volumes/v11-pattern-atlas/c01-application-boundaries/ambassador.md.
Verify four verbatim quotes, card/owner agreement, and moved-page metadata.

## Self-Contained Service

Scope: tycho.pattern.self-contained-service. Read the owner unit, source plan entry,
read.microservices-self-contained.2026-10-21, the owner section, and the c01 card.
Verify response independence, CQRS/Saga replica, collaborator failure, retry
alternative, and at least 120 words.

## Output

Return JSON with verdict/technical/decision/findings/limits. A pass requires no
blocking or major finding. Save the raw report under authoring/ai-reviews and add
its SHA-256 to the index; do not treat a pass as owner acceptance or CI.
