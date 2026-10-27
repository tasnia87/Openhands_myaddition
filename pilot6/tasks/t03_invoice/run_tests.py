"""Raw-output pilot recorder. Run this file as a Python process, never source it."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parent
run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '_' + uuid.uuid4().hex[:8]
logs = ROOT / 'baseline_logs' / run_id
logs.mkdir(parents=True, exist_ok=False)
# Explicit files only: no environment secrets or Git credentials are archived.
tracked = ['app.py', 'test_app.py', 'TASK.md', 'requirements.txt', 'pytest.ini', 'run_tests.py', 'export_run.py']
def snapshot(label):
    dest = logs / label
    dest.mkdir()
    hashes = {}
    for name in tracked:
        p = ROOT / name
        if p.is_file():
            data = p.read_bytes()
            (dest / name).write_bytes(data)
            hashes[name] = hashlib.sha256(data).hexdigest()
    return hashes

def git_output(args):
    try:
        r = subprocess.run(['git', *args], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
        return r.stdout.decode('utf-8', errors='replace') if r.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None

meta = {'task': ROOT.name, 'condition': 'raw', 'run_id': run_id,
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'python': sys.version, 'platform': platform.platform(),
        'cwd': str(ROOT), 'git_commit': git_output(['rev-parse', 'HEAD']),
        'before_sha256': snapshot('before'), 'completed': False,
        'pytest_plugin_autoload': False, 'timeout_seconds': 120}
command = [sys.executable, '-m', 'pytest', 'test_app.py', '-c', str(ROOT / 'pytest.ini'), '--color=no']
meta['command'] = command
(logs / 'metadata.json').write_text(json.dumps(meta, indent=2), encoding='utf-8')
diff = git_output(['diff', '--binary', 'HEAD', '--', '.'])
if diff is not None:
    (logs / 'before.patch').write_text(diff, encoding='utf-8')
env = os.environ.copy()
env['PYTEST_DISABLE_PLUGIN_AUTOLOAD'] = '1'
env['PYTHONIOENCODING'] = 'utf-8'
for name in ('PYTEST_ADDOPTS', 'PYTEST_PLUGINS'):
    env.pop(name, None)
start = time.monotonic()
code = 125
try:
    result = subprocess.run(command, cwd=ROOT, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=120)
    output, code = result.stdout, result.returncode
    meta['completed'] = True
except subprocess.TimeoutExpired as exc:
    output = exc.stdout or b''
    code = 124
    meta['error'] = 'test process timed out'
except OSError as exc:
    output = b''
    meta['error'] = str(exc)
(logs / 'pytest_output.txt').write_bytes(output)
(logs / 'exit_code.txt').write_text(str(code)+'\n', encoding='utf-8')
meta.update(exit_code=code, duration_seconds=time.monotonic()-start,
            finished_utc=datetime.now(timezone.utc).isoformat(), after_sha256=snapshot('after'))
(logs / 'metadata.json').write_text(json.dumps(meta, indent=2), encoding='utf-8')
# Same bytes are saved and delivered; the agent platform may apply its own limits.
sys.stdout.buffer.write(output)
sys.stdout.buffer.flush()
print('\n[Recorder] exit_code=' + str(code) + '; logs=' + str(logs), flush=True)
# Exits this child Python process, not OpenHands' persistent shell.
raise SystemExit(code if code >= 0 else 1)
