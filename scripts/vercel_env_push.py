"""Push .env production variables to linked Vercel project."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT / ".env"

# User-requested keys; FLASK_SECRET_KEY is what config.py reads.
KEYS = [
    "USE_SQLITE",
    "STORAGE_BACKEND",
    "SUPABASE_URL",
    "SUPABASE_KEY",
    "SUPABASE_DB_URL",
    "SUPABASE_STORAGE_BUCKET",
    "FLASK_SECRET_KEY",
    "VERCEL",
]

ALIASES = {
    "SECRET_KEY": "FLASK_SECRET_KEY",
}


def load_env(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def main() -> int:
    env = load_env(ENV_FILE)
    env.setdefault("VERCEL", "1")
    env.setdefault("USE_SQLITE", "0")
    env.setdefault("STORAGE_BACKEND", "supabase")
    env.setdefault("SUPABASE_STORAGE_BUCKET", "property-media")

    if env.get("FLASK_SECRET_KEY") and not env.get("SECRET_KEY"):
        env["SECRET_KEY"] = env["FLASK_SECRET_KEY"]

    targets = list(KEYS)
    if "SECRET_KEY" not in targets:
        targets.append("SECRET_KEY")

    for key in targets:
        src = ALIASES.get(key, key)
        val = env.get(key) or env.get(src)
        if not val:
            print(f"skip {key} (missing in .env)")
            continue
        proc = subprocess.run(
            "npx vercel env add " + key + " production --force --yes",
            input=val,
            text=True,
            cwd=str(ROOT),
            capture_output=True,
            shell=True,
        )
        if proc.returncode != 0:
            print(proc.stderr or proc.stdout)
            return proc.returncode
        print(f"set {key}=production")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
