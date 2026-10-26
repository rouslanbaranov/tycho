"""Focused tests for the derived structural graph and its offline queries."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import book_graph  # noqa: E402


def edge(kind, source, target, origin="frontmatter", path="book/a.md",
         field=None, line=None, anchor=None, source_sha256="a" * 64):
    item = {
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
    item["id"] = book_graph.edge_id(item)
    return item


def document(node_id, path, label, kind="page", sha=None):
    return {"id": node_id, "kind": "document", "label": label,
            "document_kind": kind, "path": path,
            "source_sha256": sha or ("a" * 64)}


def make_graph(nodes, edges):
    nodes = sorted(nodes, key=book_graph.node_sort_key)
    edges = sorted(edges, key=book_graph.edge_sort_key)
    return {
        "schema": book_graph.GRAPH_SCHEMA,
        "graph_version": 1,
        "metadata_version": 1,
        "source_snapshot_sha256": "b" * 64,
        "coverage": "complete",
        "unannotated_paths": [],
        "counts": {},
        "nodes": nodes,
        "edges": edges,
        "content_sha256": book_graph.graph_content_sha256(nodes, edges),
    }


def base_graph():
    nodes = [
        document("doc:a", "book/a.md", "A"),
        document("doc:b", "book/b.md", "B"),
        document("doc:c", "book/c.md", "C"),
        document("doc:d", "book/d.md", "D"),
        {"id": "pattern:p", "kind": "pattern", "label": "P",
         "family": "fam"},
        {"id": "src:s", "kind": "source", "label": "S"},
        {"id": "topic:t", "kind": "topic", "label": "t"},
    ]
    edges = [
        edge("parent", "doc:b", "doc:a", field="parent_id"),
        edge("related", "doc:a", "doc:c",
             field="route_hints.related_ids[0]"),
        edge("body-link", "doc:a", "doc:c", origin="body", line=9,
             anchor="target"),
        edge("body-link", "doc:a", "doc:d", origin="body", line=10),
        edge("prerequisite", "doc:c", "doc:b",
             field="route_hints.prerequisites[0]"),
        edge("cites", "doc:a", "src:s",
             field="evidence_scope.source_ids[0]"),
        edge("has-topic", "doc:a", "topic:t", field="topic_ids[0]"),
        edge("owns-pattern", "pattern:p", "doc:a", origin="registry",
             path="edition/patterns/registry.v1.json",
             field="patterns[0].technical_owner", anchor="owner"),
    ]
    return make_graph(nodes, edges)


class BodyLinkTests(unittest.TestCase):
    def test_filters_code_images_external_and_self(self):
        fence = chr(96) * 3
        inline = chr(96)
        text = ("---\n"
                "title: A\n"
                "---\n"
                "[good](b.md#target)\n"
                "![image](b.md)\n"
                + inline + "[inline](b.md)" + inline + "\n"
                + fence + "\n"
                "[fenced](b.md)\n"
                + fence + "\n"
                "[external](https://example.test/page)\n"
                "[outside](../authoring/note.md)\n"
                "[self](a.md)\n"
                "[missing](missing.md)\n"
                "[directory](sub)\n")
        links, issues, outside, self_links = book_graph.parse_body_links(
            text, "book/a.md",
            {"book/a.md", "book/b.md", "book/sub/README.md"})
        self.assertEqual([(item["target_path"], item["line"], item["anchor"])
                          for item in links],
                         [("book/b.md", 4, "target"),
                          ("book/sub/README.md", 14, None)])
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]["reason"], "missing-canonical-target")
        self.assertEqual(outside, 1)
        self.assertEqual(self_links, 1)

    def test_no_frontmatter_links_are_body_links(self):
        links, issues, outside, self_links = book_graph.parse_body_links(
            "---\nlink: [x](b.md)\n---\n", "book/a.md", {"book/b.md"})
        self.assertEqual(links, [])
        self.assertEqual(issues, [])


class BuildTests(unittest.TestCase):
    def test_build_provenance_and_determinism(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "book").mkdir()
            text_a = "---\ntitle: A\n---\n\n[to B](b.md#owner)\n"
            text_b = "---\ntitle: B\n---\n\n[to A](a.md)\n"
            (root / "book/a.md").write_text(text_a, encoding="utf-8")
            (root / "book/b.md").write_text(text_b, encoding="utf-8")
            scan = {
                "snapshot_sha256": "c" * 64,
                "coverage": "complete",
                "unannotated_paths": [],
                "metadata_version": 1,
                "documents": [
                    {"id": "doc:a", "kind": "page", "path": "book/a.md",
                     "parent_id": None, "related": ["doc:b"],
                     "prerequisites": [], "title": "A",
                     "source_ids": ["src:s"], "topics": ["topic:t"],
                     "sha256": hashlib.sha256(
                         text_a.encode("utf-8")).hexdigest()},
                    {"id": "doc:b", "kind": "page", "path": "book/b.md",
                     "parent_id": "doc:a", "related": [],
                     "prerequisites": ["doc:a"], "title": "B",
                     "source_ids": [], "topics": [],
                     "sha256": hashlib.sha256(
                         text_b.encode("utf-8")).hexdigest()},
                ],
            }
            patterns = [{
                "id": "pattern:p", "catalog_name": "P", "family": "fam",
                "technical_owner": {"document_id": "doc:b",
                                    "path": "book/b.md",
                                    "anchor": "owner", "state": "partial"},
            }]
            graph = book_graph.build_graph(
                root, scan=scan, patterns=patterns,
                source_by_id={"src:s": {"id": "src:s", "title": "S"}},
                topic_by_id={"topic:t": {"id": "topic:t",
                                         "description": "T"}},
                registry_sha256="f" * 64)
            self.assertEqual(graph["counts"]["documents"], 2)
            self.assertEqual(graph["counts"]["edges_by_kind"]["parent"], 1)
            self.assertEqual(graph["counts"]["edges_by_kind"]["body-link"], 2)
            body = [item for item in graph["edges"]
                    if item["kind"] == "body-link"]
            self.assertEqual(body[0]["line"], 5)
            owner = next(item for item in graph["edges"]
                         if item["kind"] == "owns-pattern")
            self.assertEqual(owner["path"],
                             "edition/patterns/registry.v1.json")
            self.assertEqual(owner["field"], "patterns[0].technical_owner")
            second = book_graph.build_graph(
                root, scan=scan, patterns=patterns,
                source_by_id={"src:s": {"id": "src:s", "title": "S"}},
                topic_by_id={"topic:t": {"id": "topic:t",
                                         "description": "T"}},
                registry_sha256="f" * 64)
            self.assertEqual(book_graph.graph_bytes(graph),
                             book_graph.graph_bytes(second))


class QueryTests(unittest.TestCase):
    def test_backlinks_group_and_limit(self):
        graph = base_graph()
        result = book_graph.backlinks(graph, "doc:c", limit=1)
        self.assertEqual(result["counts"]["related"], 1)
        self.assertEqual(result["returned"], 1)
        self.assertTrue(result["truncated"])

    def test_path_direction_and_reverse(self):
        graph = base_graph()
        forward = book_graph.shortest_path(graph, "doc:a", "doc:c",
                                            max_hops=2)
        self.assertEqual(forward["status"], "ok")
        self.assertEqual(forward["hops"], 1)
        backward = book_graph.shortest_path(graph, "doc:c", "doc:a",
                                             max_hops=1)
        self.assertEqual(backward["status"], "no-path")
        undirected = book_graph.shortest_path(graph, "doc:c", "doc:a",
                                               max_hops=2, directed=False)
        self.assertEqual(undirected["status"], "ok")
        self.assertTrue(any(step["reverse"] for step in undirected["steps"]))

    def test_audit_reports_candidates(self):
        graph = base_graph()
        result = book_graph.audit_graph(graph)
        self.assertEqual(result["related"]["asymmetric_peer"], 1)
        self.assertEqual(result["body_links"]["body_only"], 1)
        self.assertEqual(result["prerequisites"]["max_depth"], 1)
        self.assertEqual(result["patterns"]["without_owner"], 0)


class IntegrityTests(unittest.TestCase):
    def test_validate_rejects_dangling_and_hash_tamper(self):
        graph = base_graph()
        book_graph.validate_graph(graph)
        broken = json.loads(json.dumps(graph))
        broken["edges"].append(edge("related", "doc:a", "missing"))
        broken["edges"].sort(key=book_graph.edge_sort_key)
        broken["content_sha256"] = book_graph.graph_content_sha256(
            broken["nodes"], broken["edges"])
        with self.assertRaises(book_graph.GraphError):
            book_graph.validate_graph(broken)
        tampered = json.loads(json.dumps(graph))
        tampered["content_sha256"] = "0" * 64
        with self.assertRaises(book_graph.GraphError):
            book_graph.validate_graph(tampered)

    def test_duplicate_node_rejected(self):
        graph = base_graph()
        graph["nodes"].append(dict(graph["nodes"][0]))
        graph["nodes"].sort(key=book_graph.node_sort_key)
        graph["content_sha256"] = book_graph.graph_content_sha256(
            graph["nodes"], graph["edges"])
        with self.assertRaises(book_graph.GraphError):
            book_graph.validate_graph(graph)


if __name__ == "__main__":
    unittest.main()
