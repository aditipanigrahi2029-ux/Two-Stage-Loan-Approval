
import subprocess
import sys
import time

backend = subprocess.Popen([
    sys.executable, "-m", "uvicorn",
    "api:app",
    "--host", "127.0.0.1",
    "--port", "8000"
])

frontend = subprocess.Popen([
    sys.executable, "-m", "streamlit",
    "run", "app.py",
    "--server.address=0.0.0.0",
    "--server.port=8501",
    "--server.headless=true"
])

try:
    while True:
        if backend.poll() is not None:
            print("Backend stopped", flush=True)
            break

        if frontend.poll() is not None:
            print("Frontend stopped", flush=True)
            break

        time.sleep(1)

finally:
    for process in [backend, frontend]:
        if process.poll() is None:
            process.terminate()

    for process in [backend, frontend]:
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
