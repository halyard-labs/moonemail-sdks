#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(root / 'scripts/generate.py')], cwd=root, check=True)
subprocess.run(['git', 'diff', '--exit-code', '--', 'typescript', 'python', 'go'], cwd=root, check=True)
untracked = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard', 'typescript', 'python', 'go'], cwd=root, text=True)
if untracked.strip(): raise SystemExit('Untracked generated files: ' + untracked)
