#!/usr/bin/env python3
"""Validate Ink channel taxonomy and channel/format registry coverage."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = REPO_ROOT / ".agents/content-program-builder/references/channel-taxonomy.md"
REGISTRY = REPO_ROOT / ".agents/channel-content-writer/references/channel-format-registry.csv"
PROGRAM_ROOT = REPO_ROOT / "content-programs"
CHANNEL_GUIDE_ROOT = REPO_ROOT / ".agents/channel-content-writer/references/channels"
FORMAT_GUIDE_ROOT = REPO_ROOT / ".agents/channel-content-writer/references/formats"

ALLOWED_ROUTES = {"dedicated-skill", "generic-channel-writer", "manual-handoff"}
PATH_FIELDS = ("family_guides", "channel_guides", "format_guides", "adapter_paths")
SLUG_RE = re.compile(r"^- `([^`]+)`")
TOP_LEVEL_RE = re.compile(r"^[A-Za-z0-9_]+:")

CHANNEL_REQUIRED_HEADINGS = (
    "## Source Guidance",
    "## Native Behavior",
    "## Audience And Context Rules",
    "## Creative Strategy",
    "## Compliance And Risk",
    "## Manual Boundary",
    "## Metrics",
    "## QA Checklist",
    "## Anti-Patterns",
)

FORMAT_REQUIRED_HEADINGS = (
    "## Source Guidance",
    "## Use Cases",
    "## Required Inputs",
    "## Output Shape",
    "## Copy And Creative Rules",
    "## Psychological Levers",
    "## Platform Adaptation",
    "## Variants And Testing",
    "## Review Checklist",
    "## Failure Diagnostics",
    "## Anti-Patterns",
)


class ValidationError(Exception):
    pass


def read_taxonomy_slugs() -> set[str]:
    slugs: set[str] = set()
    for line in TAXONOMY.read_text(encoding="utf-8").splitlines():
        match = SLUG_RE.match(line.strip())
        if match:
            slugs.add(match.group(1))
    if not slugs:
        raise ValidationError(f"{TAXONOMY}: no channel slugs found")
    return slugs


def read_registry() -> dict[str, dict[str, str]]:
    with REGISTRY.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValidationError(f"{REGISTRY}: registry is empty")
    registry: dict[str, dict[str, str]] = {}
    for row in rows:
        slug = (row.get("slug") or "").strip()
        if not slug:
            raise ValidationError(f"{REGISTRY}: row missing slug")
        if slug in registry:
            raise ValidationError(f"{REGISTRY}: duplicate slug {slug}")
        registry[slug] = {key: (value or "").strip() for key, value in row.items()}
    return registry


def split_paths(value: str) -> list[Path]:
    paths: list[Path] = []
    for raw_path in value.split(";"):
        raw_path = raw_path.strip()
        if raw_path:
            paths.append(REPO_ROOT / raw_path)
    return paths


def validate_registry_paths(registry: dict[str, dict[str, str]]) -> None:
    for slug, row in registry.items():
        route = row.get("route", "")
        if route not in ALLOWED_ROUTES:
            raise ValidationError(f"{REGISTRY}: {slug} has invalid route {route!r}")
        if route == "dedicated-skill" and not row.get("adapter_paths"):
            raise ValidationError(f"{REGISTRY}: {slug} uses dedicated-skill but has no adapter_paths")
        if route != "dedicated-skill" and not row.get("family_guides"):
            raise ValidationError(f"{REGISTRY}: {slug} needs at least one family guide")
        if not row.get("format_guides"):
            raise ValidationError(f"{REGISTRY}: {slug} needs at least one format guide or adapter playbook")
        for field in PATH_FIELDS:
            for path in split_paths(row.get(field, "")):
                if not path.exists():
                    raise ValidationError(f"{REGISTRY}: {slug} references missing {field} path {path}")


def validate_guide_templates() -> None:
    for guide_path in sorted(CHANNEL_GUIDE_ROOT.glob("*.md")):
        text = guide_path.read_text(encoding="utf-8")
        missing = [heading for heading in CHANNEL_REQUIRED_HEADINGS if heading not in text]
        if missing:
            relative = guide_path.relative_to(REPO_ROOT)
            raise ValidationError(f"{relative}: missing channel guide headings: {', '.join(missing)}")

    for guide_path in sorted(FORMAT_GUIDE_ROOT.glob("*.md")):
        text = guide_path.read_text(encoding="utf-8")
        missing = [heading for heading in FORMAT_REQUIRED_HEADINGS if heading not in text]
        if missing:
            relative = guide_path.relative_to(REPO_ROOT)
            raise ValidationError(f"{relative}: missing format guide headings: {', '.join(missing)}")


def read_program_channels(program_file: Path) -> list[str]:
    channels: list[str] = []
    in_channels = False
    for line in program_file.read_text(encoding="utf-8").splitlines():
        if line.startswith("channels:"):
            in_channels = True
            continue
        if in_channels and TOP_LEVEL_RE.match(line) and not line.startswith((" ", "\t")):
            break
        if in_channels:
            stripped = line.strip()
            if stripped.startswith("- "):
                channels.append(stripped[2:].strip().strip('"').strip("'"))
    return channels


def validate_program_channels(taxonomy_slugs: set[str]) -> None:
    for program_file in sorted(PROGRAM_ROOT.rglob("program.yaml")):
        for channel in read_program_channels(program_file):
            if channel not in taxonomy_slugs:
                relative = program_file.relative_to(REPO_ROOT)
                raise ValidationError(f"{relative}: unknown channel {channel!r}")


def main() -> int:
    try:
        taxonomy_slugs = read_taxonomy_slugs()
        registry = read_registry()

        registry_slugs = set(registry)
        missing = sorted(taxonomy_slugs - registry_slugs)
        extra = sorted(registry_slugs - taxonomy_slugs)
        if missing:
            raise ValidationError(f"{REGISTRY}: missing slugs: {', '.join(missing)}")
        if extra:
            raise ValidationError(f"{REGISTRY}: slugs not in taxonomy: {', '.join(extra)}")

        validate_registry_paths(registry)
        validate_guide_templates()
        validate_program_channels(taxonomy_slugs)
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"ok: {REGISTRY.relative_to(REPO_ROOT)} covers {len(taxonomy_slugs)} channel slugs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
