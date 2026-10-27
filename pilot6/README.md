# OpenHands synthetic debugging pilot
Six independently runnable tasks. Each folder has its own TASK.md, app.py,
test_app.py, requirements.txt, pytest.ini, run_tests.py, and export_run.py.
Use Python 3.13 and pytest 8.3.5 where possible. Record actual versions.
Run one task at a time; do not run pytest from this repository root.
The recorder displays raw feedback, disables unrelated third-party pytest plugin
autoloading, and uses default traceback formatting. It has a 120-second per-test-command
timeout. The overall conversation budget must be enforced separately.
This repository does NOT implement concise or structured feedback yet.
