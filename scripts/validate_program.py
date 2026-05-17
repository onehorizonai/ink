#!/usr/bin/env python3
"""Validate Ink content program packs.

The validator intentionally supports the small YAML subset used by Ink's
`program.yaml` files so the repo does not need a new runtime dependency.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PROGRAM_KEYS = {
    "id",
    "name",
    "status",
    "summary",
    "visibility",
    "goals",
    "channels",
    "routes",
    "cadence",
    "formats",
    "kpis",
}

REQUIRED_FILES = {
    "README.md",
    "program.yaml",
    "workflow.md",
    "calendar.csv",
    "performance.csv",
}

REQUIRED_DIRS = {
    "formats",
    "prompts",
    "assets",
    "examples",
    "runs",
}

CALENDAR_COLUMNS = {
    "planned_date",
    "run_id",
    "format_id",
    "channel",
    "status",
    "campaign_id",
    "theme",
    "asset_brief",
    "copy_brief",
    "one_horizon_url",
    "publish_url",
    "notes",
}

PERFORMANCE_COLUMNS = {
    "published_date",
    "run_id",
    "format_id",
    "channel",
    "publish_url",
    "impressions",
    "reach",
    "engagements",
    "likes",
    "comments",
    "shares",
    "saves",
    "clicks",
    "followers_delta",
    "notes",
}

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TOP_LEVEL_RE = re.compile(r"^([A-Za-z0-9_]+):(?:\s*(.*))?$")


class ValidationError(Exception):
    pass


def discover_programs(paths: list[Path]) -> list[Path]:
    programs: list[Path] = []
    for raw_path in paths:
        path = raw_path if raw_path.is_absolute() else REPO_ROOT / raw_path
        if path.is_file():
            if path.name != "program.yaml":
                raise ValidationError(f"{path}: expected a program.yaml file")
            programs.append(path.parent)
            continue
        if not path.exists():
            raise ValidationError(f"{path}: path does not exist")
        if (path / "program.yaml").exists():
            programs.append(path)
            continue
        programs.extend(sorted(p.parent for p in path.rglob("program.yaml")))
    return sorted(set(programs))


def parse_top_level_yaml(path: Path) -> tuple[dict[str, str], dict[str, list[str]]]:
    values: dict[str, str] = {}
    sections: dict[str, list[str]] = {}
    current_key = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        match = TOP_LEVEL_RE.match(line)
        if match and not line.startswith((" ", "\t")):
            current_key = match.group(1)
            values[current_key] = (match.group(2) or "").strip().strip('"')
            sections[current_key] = []
            continue
        if current_key:
            sections[current_key].append(line)
    return values, sections


def require_columns(path: Path, required: set[str]) -> None:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration as exc:
            raise ValidationError(f"{path}: CSV is empty") from exc
    columns = {column.strip() for column in header}
    missing = sorted(required - columns)
    if missing:
        raise ValidationError(f"{path}: missing columns: {', '.join(missing)}")


def section_has_item(sections: dict[str, list[str]], key: str, field: str | None = None) -> bool:
    lines = sections.get(key, [])
    if field is None:
        return any(line.strip().startswith("- ") for line in lines)
    needle = f"- {field}:"
    nested_needle = f"{field}:"
    return any(line.strip().startswith(needle) or line.strip().startswith(nested_needle) for line in lines)


def section_field_values(sections: dict[str, list[str]], key: str, field: str) -> list[str]:
    values: list[str] = []
    needles = (f"- {field}:", f"{field}:")
    for line in sections.get(key, []):
        stripped = line.strip()
        if not stripped.startswith(needles):
            continue
        _, raw_value = stripped.split(":", 1)
        value = raw_value.strip().strip('"').strip("'")
        if value:
            values.append(value)
    return values


def validate_program(program_dir: Path) -> None:
    program_file = program_dir / "program.yaml"
    values, sections = parse_top_level_yaml(program_file)

    missing_keys = sorted(REQUIRED_PROGRAM_KEYS - set(values))
    if missing_keys:
        raise ValidationError(f"{program_file}: missing keys: {', '.join(missing_keys)}")

    program_id = values["id"]
    if not SLUG_RE.match(program_id):
        raise ValidationError(f"{program_file}: id must be a lowercase slug")
    if program_dir.name != program_id:
        raise ValidationError(f"{program_file}: id must match directory name '{program_dir.name}'")

    for key in REQUIRED_PROGRAM_KEYS:
        if not values.get(key) and not any(line.strip() for line in sections.get(key, [])):
            raise ValidationError(f"{program_file}: {key} must not be empty")

    for key in ("goals", "channels", "kpis"):
        if not section_has_item(sections, key):
            raise ValidationError(f"{program_file}: {key} must contain at least one list item")
    if not section_has_item(sections, "routes", "id"):
        raise ValidationError(f"{program_file}: routes must contain at least one route id")
    if "uses:" not in "\n".join(sections.get("routes", [])):
        raise ValidationError(f"{program_file}: each program needs at least one route uses value")
    if not section_has_item(sections, "formats", "id"):
        raise ValidationError(f"{program_file}: formats must contain at least one format id")
    if "route:" not in "\n".join(sections.get("formats", [])):
        raise ValidationError(f"{program_file}: formats must reference routes with route")
    route_ids = set(section_field_values(sections, "routes", "id"))
    format_routes = section_field_values(sections, "formats", "route")
    missing_route_ids = sorted(route for route in format_routes if route not in route_ids)
    if missing_route_ids:
        raise ValidationError(
            f"{program_file}: formats reference missing route ids: {', '.join(missing_route_ids)}"
        )

    for filename in REQUIRED_FILES:
        if not (program_dir / filename).is_file():
            raise ValidationError(f"{program_dir}: missing {filename}")
    for dirname in REQUIRED_DIRS:
        if not (program_dir / dirname).is_dir():
            raise ValidationError(f"{program_dir}: missing {dirname}/")

    if not list((program_dir / "formats").glob("*.md")):
        raise ValidationError(f"{program_dir}: formats/ must contain at least one Markdown file")
    if not list((program_dir / "prompts").glob("*.md")):
        raise ValidationError(f"{program_dir}: prompts/ must contain at least one Markdown file")

    require_columns(program_dir / "calendar.csv", CALENDAR_COLUMNS)
    require_columns(program_dir / "performance.csv", PERFORMANCE_COLUMNS)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Ink content program packs.")
    parser.add_argument(
        "paths",
        nargs="*",
        default=["content-programs"],
        help="Program directories, program.yaml files, or roots containing program packs.",
    )
    args = parser.parse_args()

    try:
        programs = discover_programs([Path(path) for path in args.paths])
        if not programs:
            raise ValidationError("no program.yaml files found")
        for program in programs:
            validate_program(program)
            print(f"ok: {program.relative_to(REPO_ROOT) if program.is_relative_to(REPO_ROOT) else program}")
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
