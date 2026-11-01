# Local HTTP MCP container and client smoke

> Issue [#367](https://github.com/rouslanbaranov/tycho/issues/367), E09-07,
> and evidence issue [#373](https://github.com/rouslanbaranov/tycho/issues/373),
> M5. **Status:** local container plus an authenticated Vercel test deployment,
> 2026-10-24. Not a production service; not independently reviewed; no OAuth,
> per-client authorization, rate limiting or owner acceptance is claimed.
> Vercel supplies TLS and the domain.

## Purpose

[mcp/mcp_http_server.py](../mcp/mcp_http_server.py) wraps the merged
stdio MCP adapter in a read-only HTTP service so client agents and humans can
reach the book, search and MCP tools over the network. The stdio adapter
remains the canonical protocol implementation.

The service is deliberately bounded; it is tested locally and on Vercel:

- modern MCP 2026-07-28 stateless JSON-RPC over `POST /mcp`;
- bearer-token authentication from the environment;
- `GET /search` and `POST /search` for the same section index;
- `GET /book` and `GET /book/<path>` for raw canonical Markdown;
- `GET /health` and `GET /ready` for container readiness;
- no writes to the book, index or query log during requests.

Legacy `initialize` is rejected over HTTP because this wrapper is stateless.
SSE subscriptions, sessions and the legacy handshake remain outside the local
prototype.

```mermaid
flowchart LR
    Agent["Client agent"] -->|"Bearer + POST /mcp"| Service["Tycho HTTP container"]
    Human["Human reader"] -->|"Bearer + GET /book"| Service
    Service --> Adapter["TychoMcpServer"]
    Adapter --> Index["Section FTS snapshot"]
    Adapter --> Book["Canonical book Markdown"]
```

The diagram describes the local prototype, not a deployed production topology.

## Endpoints

| Route | Auth | Purpose |
|---|---|---|
| `GET /health` | no | Liveness only; no book data |
| `GET /ready` | no | Snapshot identity and counts |
| `POST /mcp` | bearer | Modern MCP JSON-RPC |
| `GET /search?q=...` | bearer | Bounded section search |
| `POST /search` | bearer | JSON search arguments |
| `GET /book` | bearer | HTML list of Markdown pages |
| `GET /book/<path>` | bearer | Raw canonical Markdown |

MCP requests may include `MCP-Protocol-Version`, `Mcp-Method` and, for tool
calls, `Mcp-Name`. A mismatch returns HTTP 400 with code `-32020`.

## Security boundary

- `TYCHO_MCP_TOKEN` is required at startup; there is no anonymous MCP,
  search or book access.
- Tokens are compared with `hmac.compare_digest`; they are never logged.
- The container runs as an unprivileged user and the compose profile uses a
  read-only root filesystem plus a small `/tmp` tmpfs.
- Book reads reject absolute paths, `..`, backslashes, symlinks and paths
  outside `book/`.
- The query log is disabled; no request writes the book, index or evidence.
- TLS is not implemented in the process. A terminating proxy or container
  host must provide TLS, request limits, per-client authorization and audit
  retention before any shared deployment.

## Build and run

Set a high-entropy token in the environment; do not commit it:

~~~sh
export TYCHO_MCP_TOKEN='<set-a-long-random-token>'
docker build -f Dockerfile.vercel -t tycho-mcp-local:0.1 .
docker run --rm --read-only --tmpfs /tmp:size=16m \
  -p 8000:8000 -e TYCHO_MCP_TOKEN tycho-mcp-local:0.1
~~~

Or with compose:

~~~sh
TYCHO_MCP_TOKEN='<set-a-long-random-token>' docker compose up --build
~~~

The image builds the section index during `docker build`; the runtime image
contains the book, schema, route index and pattern registry.

## Client smoke

Standard-library client, no SDK required:

~~~sh
TYCHO_MCP_TOKEN="$TYCHO_MCP_TOKEN" .venv/bin/python \
  mcp/tests/smoke/mcp_http_client_smoke.py --url http://<container-host>:8000 \
  --query "retry budget"
~~~

Official SDK client, Python 3.11+ and `mcp==2.3.0` in a separate environment:

~~~sh
TYCHO_MCP_TOKEN="$TYCHO_MCP_TOKEN" \
  /tmp/tycho-mcp-sdk-2.3.0/bin/python mcp/tests/smoke/mcp_http_sdk_smoke.py \
  --url http://<container-host>:8000
~~~

Both smokes exercise discovery, `tools/list`, `tools/call`, `/search` and
a book page. They are transport checks, not agent answer-quality evaluation.

## Measured local evidence - 2026-10-24

| Observation | Value |
|---|---|
| Host runtime | Docker 28.3.2 on macOS |
| Base image | `python:3.12-slim` |
| Image | `tycho-mcp-local:test`, `sha256:b397fef04fb0...`; 264 MB |
| Book and index | 423 documents, 2,753 sections |
| Section snapshot | `f0a80c286a3f6b5bc6db20898389146ea330ffc9a92168df2a65579935325329` |
| Read-only run | `--read-only --tmpfs /tmp:size=16m` |
| Vercel-ready port run | `PORT=8080`; health, standard client and SDK passed |
| Health | HTTP 200, no auth |
| MCP discovery | HTTP 200, modern 2026-07-28 only |
| Tools | 7 at 2026-10-24; 11 in server 0.2.0 |
| Search call | `ok`, 2 results, citation returned |
| HTTP search | `ok`, 2 results |
| Book page | HTTP 200, 10,181 bytes |
| Standard client | exit 0 |
| Official SDK client | protocol 2026-07-28, 7 tools, search `ok`, 2 results |
| Vercel URL | https://tycho-theta.vercel.app |
| Vercel readiness | 423 documents, 2,753 sections, section snapshot `f0a80...` |
| Vercel no-auth boundary | HTTP 401 for /mcp and /search |
| Vercel clients | standard client and mcp 2.3.0 client both exit 0 |

These are single-machine and remote test observations, not a latency, capacity
or security benchmark.

## Vercel compatibility

Vercel's container runtime can deploy an OCI image as an autoscaling Function.
It detects a project-root `Dockerfile.vercel`, serves HTTP on port 80 by
default and honors the `PORT` environment variable. The image uses that
filename and the server reads `PORT` at startup, so the same image is a
candidate for Vercel Functions.

- Set `TYCHO_MCP_TOKEN` in the Vercel project environment.
- Set `PORT=8080` in the Vercel project environment. The image runs as uid
  10001 and does not bind privileged port 80.
- Vercel supplies TLS and the domain; the process still does not implement
  OAuth, per-client authorization or rate limiting.
- Scale-to-zero and cold starts apply. The section index is built into the
  image; there is no persistent `/tmp` or query log.
- The test deployment is live at https://tycho-theta.vercel.app. It uses
  the project environment variables TYCHO_MCP_TOKEN and PORT=8080; the token
  is not recorded here.
- Remote checks passed: health, readiness, no-auth 401 for MCP/search,
  standard-library client and official mcp==2.3.0 client.

See the public Vercel guide
[Running Docker on Vercel](https://vercel.com/kb/guide/docker).

## Update and release model

The deployed image is immutable. A released book or API change produces a new
image and a new Vercel deployment; there is no in-place update of the running
container. Normal merges to `main` do not deploy; the release marker gates the
build.

### Book-only change

1. Edit the Markdown/frontmatter and run the repository book validators.
2. Rebuild the local section index:
   ~~~sh
   .venv/bin/python scripts/section_fts_index.py build --full
   .venv/bin/python scripts/section_fts_index.py check
   ~~~
3. Run the MCP tests:
   ~~~sh
   .venv/bin/python -m unittest discover -s tests \
     -p 'test_tycho_mcp*.py' -v
   ~~~
4. Open a PR and merge it. A normal merge does not deploy. To release,
   update `deployment/vercel-release` in the release PR; the build runs
   `section_fts_index.py build --full` inside `Dockerfile.vercel`, and the
   committed SQLite artifact is not used.
5. Check `/ready` and rerun the remote SDK smoke.

No MCP code or `SERVER_VERSION` change is needed for book-only changes.

### API change

- Update `TOOL_SPECS` and handlers in `mcp/mcp_server.py`, HTTP behavior
  in `mcp/mcp_http_server.py`, and the relevant tests/docs.
- Keep changes additive where possible; removing or renaming a tool, argument
  or response field is breaking for clients.
- Bump `SERVER_VERSION` for a tool/API behavior change. `server/discover`
  and `/health` expose it. The MCP protocol version (`2026-07-28`) is
  independent and changes only with the protocol.
- Test old and new client paths; update the stdlib and SDK smokes.
- Merge the release PR with an updated `deployment/vercel-release`; Vercel
  replaces the deployment atomically after the build succeeds.

### Snapshot semantics and client pinning

The service serves exactly one section snapshot. `/ready` and search
responses expose it, and `tycho_search` accepts a `snapshot` argument.

A client that pins an old snapshot must refresh it after a redeploy; the old
snapshot is not retained. There is no multi-snapshot serving or blue/green
snapshot switch. Treat a snapshot-mismatch response as a signal to re-read
`/ready` and retry against the current snapshot.

### Preview, production and rollback

- Automatic Vercel deployments are limited to `main` by the root
  `vercel.json` policy (`git.deploymentEnabled`). Pushing a feature branch
  does not create a Preview deployment.
- A preview is an explicit owner action. Set Preview `TYCHO_MCP_TOKEN` and
  `PORT=8080`, then deploy the branch from the Vercel dashboard or with an
  authenticated CLI. A manual preview consumes one deployment.
- A merge to `main` creates the production test deployment only when
  `deployment/vercel-release` changes. Other merges skip the build.
- Vercel keeps previous immutable deployments; use Instant Rollback to return
  to a prior image. Rollback restores the old index and API together. Keep
  the live image and at least one rollback candidate when pruning the registry.
- There is no database migration or persistent state to reconcile.

### Deployment budget

The free plan allows 100 deployments per day, and the Hobby container
registry allows 50 images per repository. Main-only preview suppression was
not enough: every merge to `main` still created one deployment and one image.
A burst of merges on 2026-10-25 and 2026-10-26 produced rate-limited failures
and then registry push failures after the repository reached the 50-image cap.

Production builds are now gated by `ignoreCommand` on
`deployment/vercel-release`. A merge that does not change that file is
skipped before the build. A release PR changes the marker and builds once.
This also keeps the per-commit image count under the Hobby repository limit.

The gate is not a preview switch: `git.deploymentEnabled` still disables every
non-`main` branch. Use the explicit preview path above when a preview is
needed. The policy test
`tests/test_tycho_vercel_deployment_policy.py` guards both settings.

See [the release procedure](../deployment/README.md) and the public Vercel
limits for [deployments](https://vercel.com/docs/limits) and
[container images](https://vercel.com/docs/container-registry/limits-and-pricing).

### What the platform does not enforce

- Vercel builds the image but does not run the Python test suite.
- Vercel does not check local index freshness; the image build always rebuilds
  the full index.
- A successful build is not evidence that the API or clients work.
- Vercel does not prune per-commit container images automatically; the Hobby
  registry cap is an owner-managed resource.
- Vercel does not provide a separate audit message for a branch-policy skip;
  verify a skipped build by the absence of a Vercel status on the commit.
- `scripts/premerge_check.py` and the remote smoke remain mandatory release
  gates.

## Tests

~~~sh
.venv/bin/python -m unittest discover -s tests \
  -p 'test_tycho_mcp_http.py' -v
~~~

The four tests cover authentication, discovery, tools/list, tools/call,
search, book files, traversal refusal, readiness, malformed JSON and header
mismatch. The container build and client smokes remain manual evidence.

## Known limitations and next gates

- The service serves one snapshot. A client holding an old snapshot must
  refresh after each redeploy; there is no multi-snapshot retention.
- Renaming or removing a tool or response field has no deprecation window;
  coordinate clients and bump `SERVER_VERSION` for API changes.
- Vercel builds the image but does not run tests or check local index freshness;
  pre-merge tests and the remote smoke are manual gates.
- Vercel provides TLS for the test deployment, but there is no OAuth,
  per-client authorization, rate limiting or durable audit sink. The one
  static bearer token is suitable only for a restricted test.
- The Vercel deployment is a test, not production acceptance; scale-to-zero,
  cold starts and the absence of persistent disk apply.
- No legacy HTTP handshake, sessions, SSE subscriptions, cancellation
  processing or progress forwarding.
- The book route returns raw Markdown; it does not render a reading site.
- Production deployment is release-gated. Content merged without a marker
  change is not served by the test deployment until the next release.
- The Hobby container registry keeps at most 50 images per repository. Old
  images must be deleted before a release when the cap is reached.
- Automatic preview deployments are disabled. Preview testing requires an
  explicit owner action and is not part of the normal issue-branch flow.
- A stable host beyond the Vercel test needs explicit capacity, auth and
  operations decisions. GitHub Pages cannot run it; GitHub Actions runners
  are ephemeral.
- No independent review, human acceptance, CI result or production claim.
  `sufficient: 0`.

## Related records

- [Read-only stdio MCP record](MCP-READ-ONLY-MVP.md)
- [MCP follow-up questions](https://github.com/rouslanbaranov/tycho/issues/362)
- [Service container issue](https://github.com/rouslanbaranov/tycho/issues/367)
- [Update model issue](https://github.com/rouslanbaranov/tycho/issues/377)
- [Vercel deployment policy](https://github.com/rouslanbaranov/tycho/issues/392)
- [Vercel release gate](https://github.com/rouslanbaranov/tycho/issues/475)
- [Agent-facing tool contract](MCP-AGENT-TOOL-CONTRACT.md)
