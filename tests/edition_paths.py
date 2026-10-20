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


def read_original_manuscript(path):
    """Keep original research assertions across the explicitly split payload.

    This does not concatenate editorial additions or turn navigation pages into
    claim evidence. Link-resolution tests still inspect real destination files.
    """
    import sys
    sys.path.insert(0, str(ROOT / 'scripts'))
    from decompose_chapters import extract_blocks
    manifest = json.loads((ROOT / 'edition/decomposition-manifest.json').read_text())
    key = canonical_path(path).relative_to(ROOT).as_posix()
    record = next((r for r in manifest['source_bodies'] if r['source_path'] == key), None)
    if record is None:
        return canonical_path(path).read_text(encoding='utf-8')
    blocks = {}
    for target in {r['target'] for r in record['sections']}:
        blocks.update(extract_blocks((ROOT / target).read_text()))
    return ''.join(blocks[(record['source_id'], r['index'])]
                   for r in sorted(record['sections'], key=lambda r: r['index']))
