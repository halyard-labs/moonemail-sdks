#!/usr/bin/env python3
"""Import only API-key operations from the live contract or an explicit local file."""
import argparse
import json
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--source', help='Local OpenAPI file; otherwise use the deployed service')
args = parser.parse_args()
if args.source:
    source = json.loads(Path(args.source).read_text())
else:
    with urlopen('https://api.moonemail.co/openapi.json', timeout=30) as response:
        source = json.load(response)
if source.get('openapi') != '3.1.0': raise SystemExit('Unexpected contract format')
# Fail closed: include only operations explicitly secured with an API key.
paths = {}
for path, methods in source['paths'].items():
    for method, op in methods.items():
        if path.startswith('/dashboard/') or op.get('x-required-scope') == 'user_session': continue
        if op.get('security') != [{'bearerKey': []}]:
            raise SystemExit(f'Unexpected authentication on {method} {path}')
        paths.setdefault(path, {})[method] = op
source['paths'] = paths
source['info']['title'] = 'Moonemail API'
source['components']['securitySchemes'].pop('userSession', None)
if source['servers'] != [{'url': 'https://api.moonemail.co'}]: raise SystemExit('Unexpected API host')
(ROOT / 'spec/openapi.json').write_text(json.dumps(source, indent=2, ensure_ascii=False) + '\n')
print(f'Imported {sum(map(len, paths.values()))} public operations; review and regenerate before releasing.')
