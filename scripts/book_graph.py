#!/usr/bin/env python3
"""Deterministic derived structural graph over canonical Tycho metadata.

The graph is a read-only index. Canonical Markdown, frontmatter and the pattern
registry remain authoritative. No edge is inferred from co-occurrence, a
similarity score or a model; every edge carries its origin and locator.

This module has no network, model or graph-database dependency. Building uses
`route_index.canonical_scan`; querying and auditing use only this module.
"""
from __future__ import annotations

import hashlib
import json
import os
import posixpath
import re
import tempfile
from collections import Counter, defaultdict, deque
from pathlib import Path
from urllib.parse import unquote, urlsplit

GRAPH_VERSION = 1
GRAPH_SCHEMA = "tycho-derived-structural-graph-v1"
EDGE_KINDS = (
    "parent",
    "related",
    "prerequisite",
    "body-link",
    "cites",
    "owns-pattern",
    "has-topic",
)
DOCUMENT_PATH_KINDS = ("parent", "related", "prerequisite", "body-link")
ORIGINS = ("frontmatter", "body", "registry")
NODE_KINDS = ("document", "pattern", "source", "topic")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})[^\r\n]*$")
INLINE = re.compile(r"`[^`\n]*`")
LINK = re.compile(r"(?<!!)\[[^\]\n]{1,1500}\]\(([^)\n]+)\)")


class GraphError(ValueError):
    """Graph input, integrity or query error."""


def require(condition, message):
    if not condition:
        raise GraphError(message)


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False)


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def graph_content_sha256(nodes, edges):
    return digest(canonical_json({"nodes": nodes, "edges": edges}))


def node_sort_key(node):
    return (node.get("kind", ""), node.get("id", ""))


def edge_sort_key(edge):
    return (
        edge.get("kind", ""),
        edge.get("from", ""),
        edge.get("to", ""),
        edge.get("origin", ""),
        edge.get("path", ""),
        edge.get("field") or "",
        edge.get("line") or 0,
        edge.get("anchor") or "",
        edge.get("id", ""),
    )


def edge_id(edge):
    identity = {
        "kind": edge["kind"],
        "from": edge["from"],
        "to": edge["to"],
        "origin": edge["origin"],
        "path": edge["path"],
        "field": edge.get("field"),
        "line": edge.get("line"),
        "anchor": edge.get("anchor"),
    }
    return "edge:" + digest(canonical_json(identity))[:24]


def parse_body_links(text, source_path, document_paths):
    """Return explicit canonical body links and local unresolved issues.

    Only links that resolve to a path in `document_paths` become links.
    External URLs, anchors and local links outside `book/` are ignored.
    Fenced and inline code are excluded. The parser is deliberately lexical,
    not a complete CommonMark implementation.
    """
    links = []
    issues = []
    outside_book = 0
    self_links = 0
    fenced = None
    frontmatter = False
    source_dir = posixpath.dirname(source_path)
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if number == 1 and stripped == "---":
            frontmatter = True
            continue
        if frontmatter:
            if stripped == "---":
                frontmatter = False
            continue
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if fenced is None:
                fenced = (marker[0], len(marker))
            elif marker[0] == fenced[0] and len(marker) >= fenced[1]:
                fenced = None
            continue
        if fenced is not None:
            continue
        visible = INLINE.sub("", line)
        for match in LINK.finditer(visible):
            raw = match.group(1).strip()
            value = raw.split(" ", 1)[0].strip("<>")
            if not value or value.startswith("#"):
                continue
            parts = urlsplit(value)
            if parts.scheme or parts.netloc:
                continue
            target = unquote(parts.path)
            if not target:
                continue
            if target.startswith("/") or "\\" in target or ".git" in target.split("/"):
                issues.append({"path": source_path, "line": number,
                               "reason": "unsafe-local-target", "target": value})
                continue
            combined = posixpath.normpath(posixpath.join(source_dir, target))
            if combined == ".." or combined.startswith("../"):
                outside_book += 1
                continue
            if not combined.startswith("book/"):
                outside_book += 1
                continue
            if combined not in document_paths:
                directory_index = combined.rstrip("/") + "/README.md"
                if directory_index in document_paths:
                    combined = directory_index
                else:
                    issues.append({"path": source_path, "line": number,
                                   "reason": "missing-canonical-target",
                                   "target": value})
                    continue
            if combined == source_path:
                self_links += 1
                continue
            links.append({"source_path": source_path, "target_path": combined,
                          "line": number,
                          "anchor": unquote(parts.fragment) or None})
    return links, issues, outside_book, self_links


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise GraphError("cannot read " + str(path) + ": " + str(exc)) from exc


def registries(root):
    root = Path(root)
    pattern_path = root / "edition/patterns/registry.v1.json"
    source_path = root / "sources/register.json"
    topic_path = root / "sources/document-topics.json"
    patterns = load_json(pattern_path)
    sources = load_json(source_path)
    topics = load_json(topic_path)
    require(patterns.get("schema_version") == 1, "unsupported pattern registry")
    require(isinstance(patterns.get("patterns"), list), "pattern registry list")
    require(isinstance(sources.get("sources"), list), "source register list")
    require(topics.get("schema_version") == 1, "unsupported topic registry")
    require(isinstance(topics.get("topics"), list), "topic registry list")
    source_by_id = {item["id"]: item for item in sources["sources"]}
    topic_by_id = {item["id"]: item for item in topics["topics"]}
    return (patterns["patterns"], source_by_id, topic_by_id,
            digest(pattern_path.read_text(encoding="utf-8")))


def add_edge(edges, kind, source, target, origin, path, field=None, line=None,
             anchor=None, source_sha256=None):
    require(kind in EDGE_KINDS, "unknown edge kind " + str(kind))
    edge = {
        "kind": kind,
        "from": source,
        "to": target,
        "origin": origin,
        "path": path,
        "field": field,
        "line": line,
        "anchor": anchor,
        "source_sha256": source_sha256,
    }
    edge["id"] = edge_id(edge)
    edges.append(edge)


def build_graph(root, scan=None, patterns=None, source_by_id=None,
                topic_by_id=None, registry_sha256=None):
    """Build a graph from canonical metadata and explicit body links.

    If `scan` is omitted, route_index.canonical_scan is used. Supplying the
    scan and registries is intended for focused tests; production callers use
    the defaults.
    """
    root = Path(root).resolve()
    if scan is None:
        try:
            from route_index import canonical_scan
        except ImportError as exc:
            raise GraphError("route_index import failed: " + str(exc)) from exc
        scan = canonical_scan(root)
    if patterns is None or source_by_id is None or topic_by_id is None:
        loaded = registries(root)
        if patterns is None:
            patterns = loaded[0]
        if source_by_id is None:
            source_by_id = loaded[1]
        if topic_by_id is None:
            topic_by_id = loaded[2]
        if registry_sha256 is None:
            registry_sha256 = loaded[3]
    require(isinstance(scan, dict), "scan must be a mapping")
    require(scan.get("coverage") == "complete", "graph requires complete coverage")
    require(isinstance(scan.get("documents"), list), "scan documents missing")
    require(HEX64.fullmatch(str(scan.get("snapshot_sha256", ""))),
            "scan snapshot hash invalid")
    if registry_sha256 is None:
        registry_path = root / "edition/patterns/registry.v1.json"
        require(registry_path.is_file(), "pattern registry hash missing")
        registry_sha256 = digest(registry_path.read_text(encoding="utf-8"))
    require(HEX64.fullmatch(registry_sha256), "registry hash invalid")

    documents = scan["documents"]
    by_id = {doc["id"]: doc for doc in documents}
    by_path = {doc["path"]: doc for doc in documents}
    require(len(by_id) == len(documents), "duplicate document ID")
    require(len(by_path) == len(documents), "duplicate document path")

    nodes = []
    edges = []
    issues = []

    for doc in documents:
        nodes.append({
            "id": doc["id"],
            "kind": "document",
            "label": doc["title"],
            "document_kind": doc["kind"],
            "path": doc["path"],
            "source_sha256": doc["sha256"],
        })

    source_ids = sorted({sid for doc in documents for sid in doc["source_ids"]})
    for sid in source_ids:
        require(sid in source_by_id, "unknown source ID " + sid)
        nodes.append({"id": sid, "kind": "source",
                      "label": source_by_id[sid].get("title", sid)})

    topic_ids = sorted({tid for doc in documents for tid in doc["topics"]})
    for tid in topic_ids:
        require(tid in topic_by_id, "unknown topic ID " + tid)
        nodes.append({"id": "topic:" + tid, "kind": "topic", "label": tid})

    for pattern in patterns:
        nodes.append({
            "id": pattern["id"],
            "kind": "pattern",
            "label": pattern["catalog_name"],
            "family": pattern.get("family"),
        })

    for doc in documents:
        if doc["parent_id"] is not None:
            require(doc["parent_id"] in by_id,
                    doc["path"] + ": dangling parent")
            add_edge(edges, "parent", doc["id"], doc["parent_id"],
                     "frontmatter", doc["path"], "parent_id",
                     source_sha256=doc["sha256"])
        for index, target in enumerate(doc["related"]):
            require(target in by_id, doc["path"] + ": dangling related ID")
            add_edge(edges, "related", doc["id"], target, "frontmatter",
                     doc["path"], "route_hints.related_ids[" + str(index) + "]",
                     source_sha256=doc["sha256"])
        for index, target in enumerate(doc["prerequisites"]):
            require(target in by_id, doc["path"] + ": dangling prerequisite ID")
            add_edge(edges, "prerequisite", doc["id"], target, "frontmatter",
                     doc["path"],
                     "route_hints.prerequisites[" + str(index) + "]",
                     source_sha256=doc["sha256"])
        for index, target in enumerate(doc["source_ids"]):
            require(target in source_by_id, doc["path"] + ": unknown source")
            add_edge(edges, "cites", doc["id"], target, "frontmatter",
                     doc["path"],
                     "evidence_scope.source_ids[" + str(index) + "]",
                     source_sha256=doc["sha256"])
        for index, target in enumerate(doc["topics"]):
            require(target in topic_by_id, doc["path"] + ": unknown topic")
            add_edge(edges, "has-topic", doc["id"], "topic:" + target,
                     "frontmatter", doc["path"], "topic_ids[" + str(index) + "]",
                     source_sha256=doc["sha256"])

    body_links = []
    outside_book = 0
    self_links = 0
    for doc in documents:
        text = (root / doc["path"]).read_text(encoding="utf-8")
        require(digest(text) == doc["sha256"],
                doc["path"] + ": changed during graph build")
        links, found_issues, outside, self_count = parse_body_links(
            text, doc["path"], by_path)
        body_links.extend(links)
        issues.extend(found_issues)
        outside_book += outside
        self_links += self_count

    for link in body_links:
        target = by_path[link["target_path"]]
        add_edge(edges, "body-link", by_path[link["source_path"]]["id"],
                 target["id"], "body", link["source_path"],
                 line=link["line"], anchor=link["anchor"],
                 source_sha256=by_path[link["source_path"]]["sha256"])

    unresolved_owners = []
    for index, pattern in enumerate(patterns):
        owner = pattern.get("technical_owner")
        if not isinstance(owner, dict):
            unresolved_owners.append({"pattern_id": pattern["id"],
                                      "reason": "missing-owner"})
            continue
        path = owner.get("path")
        document_id = owner.get("document_id")
        anchor = owner.get("anchor")
        if path not in by_path or by_path[path]["id"] != document_id:
            unresolved_owners.append({"pattern_id": pattern["id"],
                                      "reason": "unresolved-owner",
                                      "path": path})
            continue
        add_edge(edges, "owns-pattern", pattern["id"], document_id,
                 "registry", "edition/patterns/registry.v1.json",
                 "patterns[" + str(index) + "].technical_owner",
                 anchor=anchor, source_sha256=registry_sha256)

    nodes.sort(key=node_sort_key)
    edges.sort(key=edge_sort_key)
    counts = {
        "documents": sum(1 for node in nodes if node["kind"] == "document"),
        "patterns": sum(1 for node in nodes if node["kind"] == "pattern"),
        "sources": sum(1 for node in nodes if node["kind"] == "source"),
        "topics": sum(1 for node in nodes if node["kind"] == "topic"),
        "edges": len(edges),
        "edges_by_kind": dict(sorted(Counter(e["kind"] for e in edges).items())),
        "body_link_issues": len(issues),
        "outside_book_links": outside_book,
        "self_links": self_links,
    }
    graph = {
        "schema": GRAPH_SCHEMA,
        "graph_version": GRAPH_VERSION,
        "metadata_version": scan.get("metadata_version", 1),
        "source_snapshot_sha256": scan["snapshot_sha256"],
        "coverage": scan["coverage"],
        "unannotated_paths": list(scan.get("unannotated_paths", [])),
        "counts": counts,
        "nodes": nodes,
        "edges": edges,
        "body_link_issues": sorted(issues, key=lambda item: (
            item["path"], item["line"], item["reason"], item["target"])),
        "unresolved_pattern_owners": sorted(
            unresolved_owners, key=lambda item: item["pattern_id"]),
        "content_sha256": graph_content_sha256(nodes, edges),
    }
    validate_graph(graph)
    return graph


def graph_bytes(graph):
    return (json.dumps(graph, sort_keys=True, indent=2, ensure_ascii=False)
            + "\n")


def write_graph(path, graph):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = graph_bytes(graph)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                     prefix=path.name + ".", delete=False) as handle:
        handle.write(data)
        temporary = Path(handle.name)
    os.replace(temporary, path)
    os.chmod(path, 0o644)
    return len(data.encode("utf-8"))


def validate_graph(graph):
    require(isinstance(graph, dict), "graph must be an object")
    require(graph.get("schema") == GRAPH_SCHEMA, "unsupported graph schema")
    require(graph.get("graph_version") == GRAPH_VERSION,
            "unsupported graph version")
    require(HEX64.fullmatch(str(graph.get("source_snapshot_sha256", ""))),
            "invalid source snapshot hash")
    nodes = graph.get("nodes")
    edges = graph.get("edges")
    require(isinstance(nodes, list) and isinstance(edges, list),
            "graph nodes/edges missing")
    node_ids = [node.get("id") for node in nodes]
    require(all(isinstance(item, str) and item for item in node_ids),
            "invalid node ID")
    require(len(set(node_ids)) == len(node_ids), "duplicate node ID")
    require(all(node.get("kind") in NODE_KINDS for node in nodes),
            "invalid node kind")
    require(nodes == sorted(nodes, key=node_sort_key), "nodes are not sorted")
    edge_ids = [edge.get("id") for edge in edges]
    require(all(isinstance(item, str) and item for item in edge_ids),
            "invalid edge ID")
    require(len(set(edge_ids)) == len(edge_ids), "duplicate edge ID")
    require(edges == sorted(edges, key=edge_sort_key), "edges are not sorted")
    known = set(node_ids)
    for edge in edges:
        require(edge.get("kind") in EDGE_KINDS, "invalid edge kind")
        require(edge.get("origin") in ORIGINS, "invalid edge origin")
        require(edge.get("from") in known, "dangling edge source")
        require(edge.get("to") in known, "dangling edge target")
        require(isinstance(edge.get("path"), str) and edge["path"],
                "edge path missing")
        require(HEX64.fullmatch(str(edge.get("source_sha256", ""))),
                "edge provenance hash missing")
    require(graph.get("content_sha256") == graph_content_sha256(nodes, edges),
            "graph content hash mismatch")
    return graph


def load_graph(path):
    return validate_graph(load_json(path))


def node_map(graph):
    return {node["id"]: node for node in graph["nodes"]}


def _group_counts(items, key):
    return dict(sorted(Counter(key(item) for item in items).items()))


def backlinks(graph, node_id, kinds=None, limit=50):
    require(node_id in node_map(graph), "node not found: " + node_id)
    if kinds:
        unknown = set(kinds) - set(EDGE_KINDS)
        require(not unknown, "unknown edge kind: " + ", ".join(sorted(unknown)))
    selected = [edge for edge in graph["edges"]
                if edge["to"] == node_id and (not kinds or edge["kind"] in kinds)]
    selected.sort(key=lambda edge: (edge["from"], edge["kind"], edge["path"],
                                    edge.get("field") or "",
                                    edge.get("line") or 0, edge["id"]))
    labels = node_map(graph)
    result = {
        "snapshot": graph["source_snapshot_sha256"],
        "content_sha256": graph["content_sha256"],
        "node": {"id": node_id, "kind": labels[node_id]["kind"],
                 "label": labels[node_id]["label"]},
        "counts": _group_counts(selected, lambda edge: edge["kind"]),
        "returned": min(len(selected), limit),
        "truncated": len(selected) > limit,
        "backlinks": [],
    }
    for edge in selected[:limit]:
        result["backlinks"].append({
            "from": edge["from"],
            "from_label": labels[edge["from"]]["label"],
            "kind": edge["kind"],
            "origin": edge["origin"],
            "path": edge["path"],
            "field": edge.get("field"),
            "line": edge.get("line"),
            "anchor": edge.get("anchor"),
        })
    return result


def _adjacency(graph, kinds, directed):
    require(all(kind in EDGE_KINDS for kind in kinds), "unknown edge kind")
    adjacency = defaultdict(list)
    for edge in graph["edges"]:
        if edge["kind"] not in kinds:
            continue
        adjacency[edge["from"]].append((edge["to"], edge, False))
        if not directed:
            adjacency[edge["to"]].append((edge["from"], edge, True))
    for node_id in adjacency:
        adjacency[node_id].sort(key=lambda item: (
            item[0], item[1]["kind"], item[1]["origin"], item[1]["path"],
            item[1].get("field") or "", item[1].get("line") or 0,
            item[1].get("anchor") or "", item[1]["id"]))
    return adjacency


def shortest_path(graph, start, goal, max_hops=4, kinds=DOCUMENT_PATH_KINDS,
                  directed=True):
    labels = node_map(graph)
    require(start in labels, "start node not found: " + start)
    require(goal in labels, "goal node not found: " + goal)
    require(1 <= max_hops <= 10, "max_hops must be 1..10")
    require(kinds, "at least one edge kind is required")
    if start == goal:
        return {"snapshot": graph["source_snapshot_sha256"],
                "content_sha256": graph["content_sha256"],
                "status": "ok", "hops": 0, "nodes": [start], "steps": []}
    adjacency = _adjacency(graph, kinds, directed)
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        current, steps = queue.popleft()
        if len(steps) >= max_hops:
            continue
        for neighbor, edge, reverse in adjacency.get(current, []):
            if neighbor in visited:
                continue
            next_steps = steps + [{
                "from": edge["to"] if reverse else edge["from"],
                "to": neighbor,
                "kind": edge["kind"],
                "origin": edge["origin"],
                "path": edge["path"],
                "field": edge.get("field"),
                "line": edge.get("line"),
                "anchor": edge.get("anchor"),
                "reverse": reverse,
            }]
            if neighbor == goal:
                node_ids = [start] + [step["to"] for step in next_steps]
                return {"snapshot": graph["source_snapshot_sha256"],
                        "content_sha256": graph["content_sha256"],
                        "status": "ok", "hops": len(next_steps),
                        "nodes": node_ids, "steps": next_steps}
            visited.add(neighbor)
            queue.append((neighbor, next_steps))
    return {"snapshot": graph["source_snapshot_sha256"],
            "content_sha256": graph["content_sha256"],
            "status": "no-path", "hops": None, "nodes": [], "steps": [],
            "max_hops": max_hops}


def _ancestor_map(graph):
    parents = {}
    for edge in graph["edges"]:
        if edge["kind"] == "parent":
            parents[edge["from"]] = edge["to"]
    return parents


def _is_ancestor(child, ancestor, parents):
    seen = set()
    current = child
    while current in parents and current not in seen:
        seen.add(current)
        current = parents[current]
        if current == ancestor:
            return True
    return False


def audit_graph(graph):
    labels = node_map(graph)
    edges = graph["edges"]
    documents = [node for node in graph["nodes"] if node["kind"] == "document"]
    parents = _ancestor_map(graph)
    related = {(edge["from"], edge["to"]) for edge in edges
               if edge["kind"] == "related"}
    asymmetric = []
    for edge in edges:
        if edge["kind"] != "related":
            continue
        source, target = edge["from"], edge["to"]
        if _is_ancestor(source, target, parents) or _is_ancestor(target, source,
                                                                parents):
            continue
        if (target, source) not in related:
            asymmetric.append({"from": source, "to": target,
                               "from_label": labels[source]["label"],
                               "to_label": labels[target]["label"]})
    body_pairs = {(edge["from"], edge["to"]) for edge in edges
                  if edge["kind"] == "body-link"}
    body_only = [{"from": source, "to": target,
                  "from_label": labels[source]["label"],
                  "to_label": labels[target]["label"]}
                 for source, target in sorted(body_pairs - related)]
    related_only = sorted(related - body_pairs)

    prerequisites = defaultdict(set)
    for edge in edges:
        if edge["kind"] == "prerequisite":
            prerequisites[edge["from"]].add(edge["to"])
    cycles = []
    state = {}
    depth = {}

    def visit(node_id, stack):
        if state.get(node_id) == 2:
            return depth.get(node_id, 0)
        if state.get(node_id) == 1:
            cycles.append(stack + [node_id])
            return 0
        state[node_id] = 1
        parents_set = prerequisites.get(node_id, set())
        if not parents_set:
            result = 0
        else:
            result = 1 + max((visit(parent, stack + [node_id])
                              for parent in sorted(parents_set)), default=0)
        state[node_id] = 2
        depth[node_id] = result
        return result

    for doc in documents:
        visit(doc["id"], [])
    deepest = max(depth.items(), key=lambda item: item[1]) if depth else (None, 0)
    chapters = sorted((node for node in documents
                       if node["document_kind"] == "chapter"),
                      key=lambda node: node["path"])
    sequential = 0
    for previous, current in zip(chapters, chapters[1:]):
        if prerequisites.get(current["id"]) == {previous["id"]}:
            sequential += 1

    owner_counts = Counter(edge["to"] for edge in edges
                           if edge["kind"] == "owns-pattern")
    pattern_ids = {node["id"] for node in graph["nodes"]
                   if node["kind"] == "pattern"}
    owned_patterns = {edge["from"] for edge in edges
                      if edge["kind"] == "owns-pattern"}
    concentration = [
        {"document": did, "label": labels[did]["label"], "patterns": count}
        for did, count in sorted(owner_counts.items(),
                                 key=lambda item: (-item[1], item[0]))[:10]
    ]

    navigation_kinds = {"related", "prerequisite", "body-link",
                        "owns-pattern"}
    incoming = Counter(edge["to"] for edge in edges
                       if edge["kind"] in navigation_kinds)
    outgoing = Counter(edge["from"] for edge in edges
                       if edge["kind"] in navigation_kinds)
    no_incoming = [{"id": doc["id"], "label": doc["label"],
                    "path": doc["path"]}
                   for doc in documents if incoming[doc["id"]] == 0]
    no_outgoing = [{"id": doc["id"], "label": doc["label"],
                    "path": doc["path"]}
                   for doc in documents if outgoing[doc["id"]] == 0]

    parallel = Counter((edge["kind"], edge["from"], edge["to"])
                       for edge in edges)
    parallel = {key: count for key, count in parallel.items() if count > 1}
    body_parallel = {key: count for key, count in parallel.items()
                     if key[0] == "body-link"}
    other_parallel = {key: count for key, count in parallel.items()
                      if key[0] != "body-link"}

    body_issues = graph.get("body_link_issues", [])
    unresolved = graph.get("unresolved_pattern_owners", [])
    return {
        "snapshot": graph["source_snapshot_sha256"],
        "content_sha256": graph["content_sha256"],
        "counts": {
            "nodes": len(graph["nodes"]),
            "documents": len(documents),
            "patterns": len(pattern_ids),
            "edges": len(edges),
        },
        "dangling_edges": [],
        "link_scope": {
            "outside_book_links": graph.get("counts", {}).get(
                "outside_book_links", 0),
            "self_links": graph.get("counts", {}).get("self_links", 0),
        },
        "body_link_issues": {
            "count": len(body_issues),
            "samples": body_issues[:20],
        },
        "unresolved_pattern_owners": {
            "count": len(unresolved),
            "samples": unresolved[:20],
        },
        "related": {
            "edges": sum(1 for edge in edges if edge["kind"] == "related"),
            "asymmetric_peer": len(asymmetric),
            "samples": asymmetric[:20],
        },
        "body_links": {
            "edges": sum(1 for edge in edges if edge["kind"] == "body-link"),
            "body_only": len(body_only),
            "samples": body_only[:20],
            "related_only": len(related_only),
            "related_only_samples": [
                {"from": labels[source]["label"],
                 "to": labels[target]["label"]}
                for source, target in related_only[:20]
            ],
        },
        "prerequisites": {
            "edges": sum(1 for edge in edges
                         if edge["kind"] == "prerequisite"),
            "max_depth": deepest[1],
            "deepest": ({"id": deepest[0], "label": labels[deepest[0]]["label"]}
                        if deepest[0] else None),
            "sequential_chapter_transitions": sequential,
            "cycles": len(cycles),
            "cycle_samples": cycles[:5],
        },
        "patterns": {
            "without_owner": len(pattern_ids - owned_patterns),
            "without_owner_samples": sorted(pattern_ids - owned_patterns)[:20],
            "owner_concentration": concentration,
        },
        "documents": {
            "no_navigation_incoming": no_incoming,
            "no_navigation_outgoing": no_outgoing,
        },
        "parallel_edges": {
            "body_link_parallel_pairs": len(body_parallel),
            "other": len(other_parallel),
            "other_samples": [
                {"kind": key[0], "from": key[1], "to": key[2],
                 "count": count}
                for key, count in sorted(other_parallel.items())[:20]
            ],
        },
        "notice": "Findings are candidates for review, not errors or fixes.",
    }


def format_backlinks(result):
    lines = [
        "Backlinks for " + result["node"]["id"] + " (" + result["node"]["label"] + ")",
        "Snapshot: " + result["snapshot"],
        "Counts: " + ", ".join(kind + "=" + str(count)
                                for kind, count in result["counts"].items()),
    ]
    for item in result["backlinks"]:
        location = item["path"]
        if item["line"]:
            location += ":" + str(item["line"])
        elif item["field"]:
            location += " [" + item["field"] + "]"
        lines.append("  " + item["kind"] + " <- " + item["from_label"]
                     + " (" + location + ")")
    if result["truncated"]:
        lines.append("  truncated; increase --limit for more")
    return "\n".join(lines)


def format_path(result):
    if result["status"] == "no-path":
        return "No path within " + str(result.get("max_hops")) + " hops."
    lines = ["Path: " + str(result["hops"]) + " hop(s)",
             "Snapshot: " + result["snapshot"]]
    for step in result["steps"]:
        suffix = " [reverse traversal]" if step["reverse"] else ""
        location = step["path"]
        if step["line"]:
            location += ":" + str(step["line"])
        lines.append("  " + step["from"] + " -> " + step["to"]
                     + " [" + step["kind"] + "]" + suffix
                     + " (" + location + ")")
    return "\n".join(lines)


def format_audit(result):
    lines = [
        "Derived graph audit",
        "Snapshot: " + result["snapshot"],
        "Nodes: " + str(result["counts"]["nodes"])
        + ", edges: " + str(result["counts"]["edges"]),
        "Related: " + str(result["related"]["edges"]) + " edges, "
        + str(result["related"]["asymmetric_peer"]) + " asymmetric peer",
        "Body links: " + str(result["body_links"]["edges"]) + " edges, "
        + str(result["body_links"]["body_only"]) + " body-only",
        "Prerequisites: max depth " + str(result["prerequisites"]["max_depth"])
        + ", " + str(result["prerequisites"]["sequential_chapter_transitions"])
        + " sequential chapter transitions",
        "Patterns without owner: " + str(result["patterns"]["without_owner"]),
        "Unresolved body links: " + str(result["body_link_issues"]["count"])
        + ", unresolved pattern owners: "
        + str(result["unresolved_pattern_owners"]["count"]),
        "Documents without navigation incoming: "
        + str(len(result["documents"]["no_navigation_incoming"]))
        + ", without navigation outgoing: "
        + str(len(result["documents"]["no_navigation_outgoing"])),
        result["notice"],
    ]
    return "\n".join(lines)
