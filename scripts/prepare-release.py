#!/usr/bin/env python3
"""Import a newer deployed contract; fail on changed contracts without a version bump."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def semver(value):
    if not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', value):
        raise ValueError('Release versions must be stable major.minor.patch values')
    return tuple(map(int, value.split('.')))


def decide(previous, incoming, current):
    target = incoming['info']['version']
    if semver(target) < semver(current):
        raise ValueError('Refusing to release an older API version')
    if target == current:
        if incoming != previous:
            raise ValueError('API contract changed without a version bump')
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source')
    args = parser.parse_args()
    old = json.loads((ROOT / 'spec/openapi.json').read_text())
    current = json.loads((ROOT / 'config/typescript.json').read_text())['npmVersion']
    cmd = [sys.executable, str(ROOT / 'scripts/sync-spec.py')]
    if args.source:
        cmd += ['--source', args.source]
    subprocess.run(cmd, check=True)
    new = json.loads((ROOT / 'spec/openapi.json').read_text())
    changed = decide(old, new, current)
    version = new['info']['version']
    if changed:
        for name, field in [('typescript', 'npmVersion'), ('python', 'packageVersion'), ('go', 'packageVersion')]:
            path = ROOT / f'config/{name}.json'
            data = json.loads(path.read_text())
            data[field] = version
            path.write_text(json.dumps(data, indent=2) + '\n')
        subprocess.run([sys.executable, str(ROOT / 'scripts/generate.py')], check=True)
        subprocess.run(['npm', 'install', '--package-lock-only', '--ignore-scripts', '--prefix', 'typescript'], cwd=ROOT, check=True)
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
            output.write(f'changed={str(changed).lower()}\nversion={version}\n')
    print(f'API {version}: ' + ('prepared release' if changed else 'already current'))


if __name__ == '__main__':
    main()
