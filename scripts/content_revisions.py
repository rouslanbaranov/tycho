"""Explicitly authorized content revisions layered over immutable baselines."""
import json
import re
from pathlib import Path

MANIFEST = 'edition/content-revisions.json'
HEX = re.compile(r'^[0-9a-f]{64}$')
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')


def load(root):
    path = Path(root) / MANIFEST
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('schema_version') != 1:
        raise ValueError('content-revision-version')
    revisions = data.get('revisions')
    if not isinstance(revisions, list):
        raise ValueError('content-revision-list')
    for revision in revisions:
        if not isinstance(revision.get('issue'), int) or revision['issue'] < 1:
            raise ValueError('content-revision-issue')
        if not DATE.fullmatch(str(revision.get('authorized_at', ''))):
            raise ValueError('content-revision-date')
        for kind in ('directory_documents', 'source_blocks', 'enrichment_documents',
                     'enrichment_additions', 'enrichment_baselines'):
            entries = revision.get(kind, [])
            if not isinstance(entries, list):
                raise ValueError('content-revision-' + kind)
            seen = set()
            for entry in entries:
                key = entry.get('key', entry.get('path'))
                if not key or key in seen:
                    raise ValueError('content-revision-key')
                seen.add(key)
                for field in ('previous_sha256', 'current_sha256'):
                    if not HEX.fullmatch(str(entry.get(field, ''))):
                        raise ValueError('content-revision-hash')
    return revisions


def authorized(root, kind, key, previous, current):
    for revision in load(root):
        for entry in revision.get(kind, []):
            if entry.get('key', entry.get('path')) != key:
                continue
            if (entry['previous_sha256'] == previous
                    and entry['current_sha256'] == current):
                return True
    return False
