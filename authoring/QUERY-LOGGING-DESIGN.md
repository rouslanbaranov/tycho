# Query logging design

Status: design only. No logging is implemented or enabled.

## Goals

Support post-enrichment query analysis without collecting raw user text by
default.

## Proposed record

Schema version 1:

- event_id (UUID)
- occurred_at (UTC, RFC 3339)
- query_sha256 (default); raw_query only with explicit opt-in
- search_snapshot
- route_snapshot
- status and basis
- top_paths (up to 10)
- top_scores (rounded)
- latency_ms
- client_id (pseudonymous)
- redaction_version

No page content, credentials, headers or user identifiers are logged.

## Redaction and retention

- Raw query is off by default; hash is salted per deployment.
- Opt-in must be explicit, per client, documented and revocable.
- Default retention: 30 days; aggregates may be retained longer.
- Access: operator-only; export only aggregated counts.
- Never write logs into the repository or generated index.

## Threats

- Query text can contain secrets or personal data; hash-only default reduces
  exposure but does not eliminate inference.
- Log replay must not mutate qrels or ranking.
- A logging failure must not fail search.

## Nonclaims

No logging exists yet; this is not telemetry, CI, human review or sufficient
coverage.

## Implemented subset

The opt-in MCP query log now stores query_sha256 by default. Raw query text is
available only with --query-log-raw. This does not add rotation or retention;
those remain planned.

