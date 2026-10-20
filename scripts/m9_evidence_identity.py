"""Read-only evidence identity/fingerprint checks, not technical claim review."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_ID = re.compile(r'^evidence\.(m9-[a-z]+[0-9]{2})\.([0-9]+)$')
ROW = re.compile(r'^\| (evidence\.m9-[a-z]+[0-9]{2}\.[0-9]+) \|(.*)$')


def scan_rows(root=ROOT):
    rows = []
    root = Path(root)
    for path in sorted((root / 'sources').glob('*.md')):
        for line in path.read_text().splitlines():
            match = ROW.match(line)
            if match:
                eid, payload = match.groups()
                identity = EVIDENCE_ID.fullmatch(eid)
                rows.append({'path': path.relative_to(root).as_posix(), 'id': eid,
                             'source_id': 'src.' + identity[1],
                             'payload_sha256': hashlib.sha256(payload.encode()).hexdigest()})
    return rows


def validate_rows(expected, actual, sources):
    def indexed(rows):
        result = {(r['path'], r['id']): r for r in rows}
        if len(result) != len(rows):
            raise ValueError('duplicate evidence identity within one document')
        return result
    expected, actual = indexed(expected), indexed(actual)
    if set(expected) != set(actual):
        raise ValueError('evidence definitions lost, added or reminted')
    for key, target in expected.items():
        row = actual[key]
        match = EVIDENCE_ID.fullmatch(row['id'])
        if not match or row['source_id'] != 'src.' + match[1] or row['source_id'] != target['source_id']:
            raise ValueError('evidence source binding changed')
        if row['payload_sha256'] != target['payload_sha256']:
            raise ValueError('evidence payload changed')
        if sources.get(row['source_id']) != target['primary_url']:
            raise ValueError('evidence primary URL changed or missing')
    return {'rows': len(actual), 'identities': len({k[1] for k in actual})}


def validate(root=ROOT):
    root = Path(root)
    fixture = json.loads((root / 'tests/fixtures/m9-evidence-migration-baseline.json').read_text())
    if fixture['schema_version'] != 1:
        raise ValueError('unsupported evidence baseline version')
    sources = {s['id']: s['url'] for s in json.loads((root / 'sources/register.json').read_text())['sources']}
    return validate_rows(fixture['rows'], scan_rows(root), sources)
