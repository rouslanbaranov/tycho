"""Resolve historical manuscript test targets through the reviewed migration.

Assertions about sources, diagrams and arithmetic remain unchanged; only the
physical path and the corresponding relative navigation destination change.
"""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIGRATION = json.loads((ROOT / 'edition/migration.json').read_text())
MOVES = {r['old_path']: r['new_path'] for r in MIGRATION['documents']}


def canonical_path(path):
    path = Path(path)
    key = path.relative_to(ROOT).as_posix()
    return ROOT / MOVES.get(key, key)


def relative_link(source, target):
    return os.path.relpath(canonical_path(target), canonical_path(source).parent).replace(os.sep, '/')
