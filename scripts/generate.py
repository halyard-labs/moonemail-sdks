#!/usr/bin/env python3
"""Generate clients from the checked-in PUBLIC contract. No network spec fetch here."""
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = '7.26.0'

def generator_document(source):
    doc = copy.deepcopy(source)
    # typescript-fetch loses primitive anyOf unions. String and array are disjoint,
    # so oneOf is equivalent here. Leave nullable/overlapping unions untouched.
    def visit(value):
        if isinstance(value, dict):
            variants = value.get('anyOf', [])
            if len(variants) == 2 and {s.get('type') for s in variants} == {'string', 'array'}:
                value['oneOf'] = value.pop('anyOf')
            for child in value.values(): visit(child)
        elif isinstance(value, list):
            for child in value: visit(child)
    visit(doc)
    return doc

def main():
    cli = os.environ.get('OPENAPI_GENERATOR', 'openapi-generator-cli')
    version = subprocess.check_output([cli, 'version'], text=True).strip()
    if version != VERSION: raise SystemExit(f'Expected generator {VERSION}, got {version}')
    doc = json.loads((ROOT / 'spec/openapi.json').read_text())
    if any(p.startswith('/dashboard') for p in doc['paths']):
        raise SystemExit('Refusing to generate dashboard APIs')
    with tempfile.TemporaryDirectory() as scratch:
        scratch = Path(scratch)
        spec = scratch / 'openapi.json'
        spec.write_text(json.dumps(generator_document(doc), indent=2) + '\n')
        for language, generator in [('typescript', 'typescript-fetch'), ('python', 'python'), ('go', 'go')]:
            output = scratch / language
            subprocess.run([cli, 'generate', '-i', str(spec), '-g', generator,
                '-c', str(ROOT / f'config/{language}.json'), '-o', str(output),
                '--global-property', 'apiTests=false,modelTests=false'], check=True, stdout=subprocess.DEVNULL)
            for name in ['.openapi-generator', '.openapi-generator-ignore', 'git_push.sh', '.travis.yml', '.github']:
                target = output / name
                if target.is_dir(): shutil.rmtree(target)
                elif target.exists(): target.unlink()
            if language == 'typescript':
                p = output / 'package.json'
                package = json.loads(p.read_text())
                package.update(author='Halyard Labs Pty Ltd', description='Official Moonemail JavaScript and TypeScript client',
                    files=['dist', 'README.md', 'LICENSE'], engines={'node': '>=22'})
                package.pop('module', None)
                package['scripts'] = {'build': 'tsc', 'prepack': 'npm run build'}
                package['devDependencies']['typescript'] = '5.9.3'
                package['repository']['directory'] = 'typescript'
                p.write_text(json.dumps(package, indent=2) + '\n')
                (output / 'src/index.ts').write_text((output / 'src/index.ts').read_text() + "\nexport * from './moonemail';\n")
            if language == 'python':
                # Generator 7.26 emits string comparisons for boolean enum literals.
                # Keep the literal check, but compare actual booleans (covered by wire tests).
                for model in (output / 'moonemail/models').glob('*.py'):
                    text = model.read_text().replace("if value not in set(['true']):", 'if value is not True:').replace("if value not in set(['false']):", 'if value is not False:')
                    model.write_text(text)
                p = output / 'pyproject.toml'
                p.write_text(p.read_text().replace('{name = "OpenAPI Generator Community",email = "team@openapitools.org"}',
                    '{name = "Halyard Labs Pty Ltd",email = "support@moonemail.co"}').replace('readme = "README.md"', 'readme = "README.md"\nlicense = "MIT"\nlicense-files = ["LICENSE"]'))
                p = output / 'moonemail/__init__.py'
                p.write_text(p.read_text() + '\nfrom moonemail.client import Moonemail\n')
            shutil.copytree(ROOT / 'overlays' / language, output, dirs_exist_ok=True)
            shutil.copy2(ROOT / 'LICENSE', output / 'LICENSE')
            destination = ROOT / language
            # Preserve only dependency caches/lockfiles, never stale generated source.
            preserved = ['node_modules', 'package-lock.json'] if language == 'typescript' else []
            for name in preserved:
                if (destination / name).exists(): shutil.move(str(destination / name), str(output / name))
            if destination.exists(): shutil.rmtree(destination)
            shutil.move(str(output), str(destination))
    print('Generated TypeScript, Python and Go SDKs.')

if __name__ == '__main__': main()
