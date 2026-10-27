"""Package existing records without rerunning tests or modifying implementation."""
from pathlib import Path
from datetime import datetime, timezone
import zipfile
import uuid
root = Path(__file__).resolve().parent
out = root / ('evidence_' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S') + '_' + uuid.uuid4().hex[:8] + '.zip')
files = [root/n for n in ('app.py','test_app.py','TASK.md','requirements.txt','pytest.ini','run_tests.py','export_run.py')]
files += list((root/'baseline_logs').rglob('*'))
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in files:
        if p.is_file(): z.write(p,p.relative_to(root))
with zipfile.ZipFile(out) as z:
    for item in z.infolist(): print(item.filename, item.file_size)
print('Archive:',out)
print('Export the OpenHands conversation separately; it is not in this ZIP.')
