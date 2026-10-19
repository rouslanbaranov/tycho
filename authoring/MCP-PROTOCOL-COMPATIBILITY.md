# MCP protocol, client capability and transport decision — Tycho

> **Issue #56 / E09-01 / M5, 2026-10-19.** Evidence-based transport and compatibility **design**, not a deployed MCP server, tested external client or authenticated remote instance. Only independently public protocol specifications and Tycho knowledge are in scope.

## Decision: target 2026-07-28; support a bounded legacy client path

The official [MCP specification release, 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) makes MCP stateless **at the protocol level**: `initialize` and `notifications/initialized` have been removed for this revision, the `Mcp-Session-Id` protocol header is absent, and every request carries protocol and client-capability information under `params._meta`. A separate standardized `server/discover` RPC replaces mandatory handshake discovery. The official [2026 transport](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/transports/streamable-http.mdx) uses Streamable HTTP with POST `/mcp`, JSON or request-scoped SSE, and mandatory modern HTTP method/version header consistency. **Do not reuse 2025 session-based assumptions in the new implementation.**

For actual v2 support use a specifically verified, pinned **MCP Python SDK 2.x** and its current `MCPServer` / `streamable_http_app()` API (see [official Python SDK v2 migration](https://py.sdk.modelcontextprotocol.io/whats-new/)). This is a proposed SDK dependency, **not an installed or pinned Tycho runtime**. The official SDK documentation states it can serve modern `2026-07-28` and older 2025-era clients from one application when so configured. Before implementation: pin an exact released SDK version and hashes, read the corresponding server/client API reference, then test the actual minimum intended client versions; names are not a capability contract by themselves.

### Version-by-version compatibility matrix

| Axis | Legacy 2025-11-25 | Current 2026-07-28 | Tycho requirement |
|---|---|---|---|
| Lifecycle | `initialize` → `notifications/initialized` | Per-request metadata, no initialize handshake; optional `server/discover` | SDK-driven version negotiation/fallback, explicit noninteroperable outcome if unsupported |
| Session | Optional `MCP-Session-Id`, possible GET SSE stream and DELETE | **No protocol-level session ID**, no GET/DELETE MCP stream; requests independent | Never require sticky session for modern search/read; legacy only if a verified client truly needs it |
| Transport | Streamable HTTP and stdio supported in relevant SDKs | Streamable HTTP POST, JSON or per-request SSE; stdio where supported | `/mcp` for remote transport, stdio for local integration/evidence tests |
| Metadata | Session/initialize-negotiated capabilities | `params._meta` carries protocol version, client info/capabilities as specified | Validate supported protocol revisions and legal capability assumptions per call |
| HTTP headers | Legacy negotiated `MCP-Protocol-Version`; session if assigned | `MCP-Protocol-Version`, `Mcp-Method` and `Mcp-Name` where method requires it | Validate body/header agreement, reject mismatches; let conformant SDK handle protocol parsing |
| Server capabilities | Negotiated at initialization | `server/discover`, `tools/list`, `resources/list`, `prompts/list` | Advertise **actually implemented** features only; graph tools are excluded and vector tools require independent evidence and acceptance |
| Notifications and subscriptions | Legacy GET SSE/change notifications | Explicit `subscriptions/listen` capability for subscribed notifications; not mandatory for simple read-only tools | No unsolicited notification stream as part of the minimal deployment |
| App state | Protocol session can carry state | Explicit application-generated handle or immutable snapshot ID passed in ordinary tool args | Snapshot/cursor identity must remain independent of TCP connection/server replica |

The change is documented in the [2026-07-28 spec changelog](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx). **MCP server `instructions` or resource onboarding does not make a new core RPC called `onboarding`**. Do not pretend project-defined `tycho.onboard` is a standard MCP method.

## Onboarding and capabilities — one remote entry, standard discovery

Remote address proposed: `https://<approved-host>/mcp` (operator-supplied; **no host exists yet**). Standard discovery for clients on the current protocol is `server/discover`; clients may also call `tools/list` and `resources/list`. An optional, versioned read-only resource `tycho://onboarding/v1` is a **proposed URI convention**, advertised through the standard resources mechanism only after it is implemented. The shared Rocinante specialist can ship onboarding rules alongside its own agent configuration, but it must still discover actual server capabilities/schema and cannot assume a future service is live.

Proposed onboarding payload, not a registered method:
- collection identity: `tycho`, schema version, supported protocol revisions and actual snapshot ID;
- `route → read → verify` instructions and bounded `search`/`read`/`evidence` tool names **only when those handlers exist**;
- exact hard limits per operation, timeouts/cursors and error semantics; missing data/contradictions and source admissibility;
- source independence and rights boundary, no arbitrary filesystem access and no source auto-enrichment;
- client compatibility, token/latency measurement guidance and a stable maintenance route.

The [retrieval contract](models/retrieval-contracts.md) owns stable IDs, snapshot refusal and evidence truth; its `operation` field is **Tycho-internal**, not a guaranteed MCP-standard JSON-RPC method. The MCP adapter will expose schema-described tools such as `tycho_search`/`tycho_read` only when independently implemented and tested in #57; `tools/call` is the standardized method for invoking those tools.

## Remote security, scaling and error behavior

- A network-exposed endpoint **must** authenticate/authorize clients according to deployment policy, validate the `Origin` header, enforce TLS/ingress controls and avoid unrestricted outbound URLs, executable tools or exposed arbitrary paths. Treat client-supplied `snapshot_id` as an untrusted identifier; look it up against published snapshots only.
- Modern stateless protocol means any healthy replica can handle a request **provided all replicas can read the same immutable published Tycho snapshot and enforce the same identity/filter/permissions**. It does **not** automatically solve application-level cursor storage, access control, failed requests or consistency during rolling deployment.
- Reject unsupported protocol versions, malformed metadata/header disagreement and unknown tool names explicitly; do not silently convert a modern request into legacy behavior. Honor the SDK's documented fallback logic: recognize modern structured incompatibility errors before attempting legacy handshake.
- If the network drops mid-request, do not claim cancellation or successful completion without server outcome. Read-only idempotent retrieval may be safely retried using same snapshot but a new request ID; stale snapshot must return a mismatch. No hidden mutation from query.
- All external clients require actual tests: (1) v2 `server/discover` → `tools/list` → `tools/call` with immutable snapshot; (2) a v1 legacy client `initialize` → `tools/list` → `tools/call`; (3) unsupported-version, header/body mismatch, forbidden Origin, auth missing, stale snapshot; (4) proxy/rolling-replica behavior. These are **planned executable integration cases**, NOT test results.

## Current implementation and ownership boundaries

| Capability | State after #56 | Owner |
|---|---|---|
| Protocol revision comparison and standard discovery design | **Specified**, with 2026-07-28 primary links | #56 |
| Exact pinned MCP SDK and client compatibility tests | **Pending**, must be tested when SDK/runtime is installed | #57 implementation gate |
| Section/lexical retrieval engine | Independent partial source and index work; no deployed endpoint claimed | #49–#51 |
| Standard MCP tools/resources/read adapter | **Not implemented by this issue** | #57 |
| Evidence/provenance and decision-method tools | **Not implemented by this issue**; no curated graph tools are planned | #58 |
| Remote deployment, authorization, observability, load testing | **Planned** separate rollout/evaluation scope | later E09 / Rocinante integration |

This decision is intentionally reversible if a client compatibility matrix demonstrates that an older SDK is required. **Only exact-version client/server tests can justify changing the deployment stack**, and no speculative protocol-level onboarding method should be invented. Independent reviewer approval, end-to-end client roundtrip, auth pen-test and a live server are not claimed.
