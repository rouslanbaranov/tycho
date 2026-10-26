# Dark Launching / Shadow Traffic — source integration

Date: 2026-10-26. Refs #532. Status: integrated; not sufficient.

## Sources

- `src.fowler-dark-launching`: 387-word bliki entry, hash
`3e39819c496dd5b8ee803eb43688992aa16814b9e9cd751214cf23c64c6a31bb`.
- `src.istio-traffic-mirroring`: task page, hash
`dc18301fbbca9d374536e582e055c60b5594014d2fe88d4e0763b551de51765e`.

## Content changes

The owner note now distinguishes hidden dark-launch invocation from request
mirroring. The card cites both records. The source boundary states that hidden
invocation, load assessment, flag rollback, old/new comparison, mirroring, shadow
host rewrite and fire-and-forget responses are supported. Measurement method,
side-effect suppression and capacity bounds remain synthetic.

## Verification

PASS: source plan, source catalogue, pattern cards and atlas. The packet set now has
six page-changed entries, including this owner page; a fresh Reviewer decision is
required before rebinding.

## Limits

Istio's served YAML manifests are misnested because of a documented template bug;
the raw Markdown was not read. No local reproduction. No sufficient coverage claim.
