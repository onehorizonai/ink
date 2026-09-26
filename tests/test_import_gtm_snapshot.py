from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/import_gtm_snapshot.py"
SPEC = importlib.util.spec_from_file_location("import_gtm_snapshot", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RefreshSnapshotTests(unittest.TestCase):
    def test_comparison_ignores_export_timestamp(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            first = Path(temp) / "first"
            second = Path(temp) / "second"
            for directory, timestamp in ((first, "first"), (second, "second")):
                directory.mkdir()
                (directory / "snapshot.md").write_text("same", encoding="utf-8")
                (directory / "snapshot.json").write_text(
                    json.dumps({"exportedAt": timestamp, "version": "1.1.0"}),
                    encoding="utf-8",
                )

            self.assertEqual(MODULE.comparable_snapshot(first), MODULE.comparable_snapshot(second))

    def test_failed_export_preserves_current_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "profile/gtm"
            target.mkdir(parents=True)
            (target / "snapshot.md").write_text("current", encoding="utf-8")

            def fail(_source: Path, output: Path) -> None:
                output.mkdir()
                (output / "snapshot.md").write_text("invalid", encoding="utf-8")
                raise SystemExit("hash mismatch")

            with patch.object(MODULE, "export", fail), self.assertRaises(SystemExit):
                MODULE.refresh(Path(temp) / "source", target)
            self.assertEqual((target / "snapshot.md").read_text(encoding="utf-8"), "current")

    def test_verified_export_replaces_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "profile/gtm"
            target.mkdir(parents=True)
            (target / "snapshot.md").write_text("current", encoding="utf-8")

            def succeed(_source: Path, output: Path) -> None:
                output.mkdir()
                (output / "snapshot.md").write_text("fresh", encoding="utf-8")
                (output / "snapshot.json").write_text("{}", encoding="utf-8")

            with patch.object(MODULE, "export", succeed):
                MODULE.refresh(Path(temp) / "source", target)
            self.assertEqual((target / "snapshot.md").read_text(encoding="utf-8"), "fresh")


if __name__ == "__main__":
    unittest.main()
