#!/usr/bin/env python3
"""Refresh or check a selected Ink profile's local GTM snapshot."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / ".local/context/ink-profiles.local.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, help="Ink profile ID")
    parser.add_argument(
        "--source-repo",
        type=Path,
        help="Override the profile's sourceRepo for this run",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero when the local snapshot differs from a fresh export",
    )
    return parser.parse_args()


def profile_source(profile: str, override: Path | None) -> Path:
    if override:
        return override.expanduser().resolve()
    try:
        registry = json.loads(PROFILES.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Cannot read {PROFILES.relative_to(ROOT)}: {exc}") from exc
    config = registry.get("profiles", {}).get(profile)
    if not isinstance(config, dict):
        raise SystemExit(f"Unknown Ink profile: {profile}")
    value = config.get("sourceRepo")
    if not isinstance(value, str) or not value.strip():
        raise SystemExit(
            f"Profile {profile!r} has no sourceRepo. Set it locally or pass --source-repo."
        )
    return Path(value).expanduser().resolve()


def export(source: Path, output: Path) -> None:
    script = source / "packages/gtm/scripts/export_snapshot.py"
    if not script.is_file():
        raise SystemExit(f"GTM exporter not found: {script}")
    subprocess.run(
        [sys.executable, str(script), "--audience", "ink", "--output", str(output)],
        cwd=source,
        check=True,
    )


def main() -> int:
    args = parse_args()
    source = profile_source(args.profile, args.source_repo)
    target = ROOT / ".local/context" / args.profile / "gtm"
    if not args.check:
        export(source, target)
        print(f"Ink profile: {args.profile}")
        return 0

    if not (target / "snapshot.md").is_file():
        print(f"STALE: no imported GTM snapshot for {args.profile}", file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory(prefix="ink-gtm-check-") as temp:
        fresh = Path(temp)
        export(source, fresh)
        current = (target / "snapshot.md").read_bytes()
        expected = (fresh / "snapshot.md").read_bytes()
    if current != expected:
        print(f"STALE: refresh GTM for Ink profile {args.profile}", file=sys.stderr)
        return 1
    print(f"CURRENT: Ink GTM snapshot for {args.profile}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
