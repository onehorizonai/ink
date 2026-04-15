#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

from storage_common import display_path, resolve_storage_roots

SKILL_ROOT, REPO_ROOT = resolve_storage_roots(Path(__file__))

ALLOWED_FORMATS = {"post", "comment-reply", "dm", "dm-reply", "repost"}
FORMAT_BY_FOLDER = {
    "posts": "post",
    "comment-replies": "comment-reply",
    "dms": "dm",
    "dm-replies": "dm-reply",
    "reposts": "repost",
}
ALLOWED_ASSET_TYPES = {"none", "image", "carousel", "video", "document", "link", "other"}
REQUIRED_FIELDS = ("channel", "format", "published_at", "context", "asset_type")
RECOMMENDED_FIELDS = ("audience", "goal", "topic_tags")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
FILENAME_RE = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<seq>\d{2})--linkedin--(?P<format>[a-z-]+)--(?P<slug>.+)\.md$",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the published-post corpus for linkedin-social-writer.",
    )
    default_root = REPO_ROOT / "content" / "linkedin"
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help="Corpus root directory. Defaults to content/linkedin at the repo root.",
    )
    return parser.parse_args()


def load_markdown(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = FRONTMATTER_RE.match(content)
    if not match:
        raise ValueError("missing YAML frontmatter")

    frontmatter = parse_frontmatter(match.group(1))

    return frontmatter, content[match.end() :]


def parse_frontmatter(frontmatter_text: str) -> dict[str, object]:
    data: dict[str, object] = {}
    lines = frontmatter_text.splitlines()
    index = 0

    while index < len(lines):
        raw_line = lines[index]
        if not raw_line.strip():
            index += 1
            continue
        if raw_line.startswith((" ", "\t")):
            raise ValueError(f"unexpected indentation on line {index + 1}")
        if ":" not in raw_line:
            raise ValueError(f"invalid frontmatter line {index + 1}: {raw_line}")

        key, raw_value = raw_line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if not key:
            raise ValueError(f"missing key on line {index + 1}")

        if value in {">", "|"}:
            block_lines: list[str] = []
            index += 1
            while index < len(lines):
                block_line = lines[index]
                if block_line.startswith("  "):
                    block_lines.append(block_line[2:])
                    index += 1
                    continue
                if not block_line.strip():
                    block_lines.append("")
                    index += 1
                    continue
                break

            if value == ">":
                collapsed = " ".join(part.strip() for part in block_lines if part.strip())
                data[key] = collapsed
            else:
                data[key] = "\n".join(block_lines).strip()
            continue

        if value == "":
            list_values: list[str] = []
            cursor = index + 1
            while cursor < len(lines):
                list_line = lines[cursor]
                if not list_line.strip():
                    cursor += 1
                    continue
                if list_line.startswith("  - "):
                    list_values.append(strip_quotes(list_line[4:].strip()))
                    cursor += 1
                    continue
                if list_line.startswith((" ", "\t")):
                    raise ValueError(f"unsupported nested value for '{key}' on line {cursor + 1}")
                break

            data[key] = list_values if list_values else ""
            index = cursor
            continue

        data[key] = strip_quotes(value)
        index += 1

    return data


def strip_quotes(value: str) -> str:
    if value.startswith("[") and value.endswith("]"):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            pass
        else:
            if isinstance(parsed, list):
                return parsed
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def validate_datetime(value: str) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False

    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"

    try:
        datetime.fromisoformat(text)
    except ValueError:
        return False

    return True


def validate_file(path: Path) -> tuple[list[str], list[str], str | None]:
    errors: list[str] = []
    warnings: list[str] = []
    path_label = display_path(path, REPO_ROOT)

    filename_match = FILENAME_RE.match(path.name)
    if not filename_match:
        errors.append(
            f"{path_label}: filename must match YYYY-MM-DD-NN--linkedin--format--slug.md",
        )

    try:
        frontmatter, body = load_markdown(path)
    except ValueError as exc:
        return [f"{path_label}: {exc}"], warnings, None

    for field in REQUIRED_FIELDS:
        value = frontmatter.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path_label}: missing required field '{field}'")

    channel = str(frontmatter.get("channel", "")).strip().lower()
    if channel and channel != "linkedin":
        errors.append(f"{path_label}: channel must be 'linkedin', got '{channel}'")

    format_name = str(frontmatter.get("format", "")).strip().lower()
    if format_name and format_name not in ALLOWED_FORMATS:
        errors.append(f"{path_label}: unknown format '{format_name}'")

    expected_format = FORMAT_BY_FOLDER.get(path.parent.name)
    if expected_format and format_name and format_name != expected_format:
        errors.append(
            (
                f"{path_label}: format '{format_name}' does not match parent folder "
                f"'{path.parent.name}'"
            ),
        )
    if filename_match and format_name and filename_match.group("format") != format_name:
        errors.append(
            (
                f"{path_label}: format '{format_name}' does not match filename format "
                f"'{filename_match.group('format')}'"
            ),
        )

    published_at = frontmatter.get("published_at")
    if published_at and not validate_datetime(str(published_at)):
        errors.append(f"{path_label}: published_at must be ISO date or datetime")

    asset_type = str(frontmatter.get("asset_type", "")).strip().lower()
    if asset_type and asset_type not in ALLOWED_ASSET_TYPES:
        errors.append(f"{path_label}: unknown asset_type '{asset_type}'")
    if asset_type and asset_type != "none":
        asset_summary = frontmatter.get("asset_summary")
        if not isinstance(asset_summary, str) or not asset_summary.strip():
            errors.append(
                f"{path_label}: asset_summary is required when asset_type is '{asset_type}'",
            )

    topic_tags = frontmatter.get("topic_tags")
    if topic_tags is not None and (
        not isinstance(topic_tags, list)
        or not all(isinstance(tag, str) and tag.strip() for tag in topic_tags)
    ):
        errors.append(f"{path_label}: topic_tags must be a list of non-empty strings")

    for field in RECOMMENDED_FIELDS:
        if field not in frontmatter or frontmatter.get(field) in (None, "", []):
            warnings.append(f"{path_label}: recommended field '{field}' is missing")

    if "## Published Copy" not in body:
        warnings.append(f"{path_label}: missing '## Published Copy' section")

    return errors, warnings, format_name or None


def iter_corpus_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.name.lower() != "readme.md" and path.is_file()
    )


def main() -> int:
    args = parse_args()
    root = args.root.resolve()

    if not root.exists():
        print(f"[ERROR] Corpus directory not found: {display_path(root, REPO_ROOT)}")
        return 1

    files = iter_corpus_files(root)
    if not files:
        print(f"[OK] No corpus files found yet in {display_path(root, REPO_ROOT)}")
        return 0

    counts: Counter[str] = Counter()
    all_errors: list[str] = []
    all_warnings: list[str] = []

    for path in files:
        errors, warnings, format_name = validate_file(path)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        if format_name:
            counts[format_name] += 1

    for message in all_errors:
        print(f"[ERROR] {message}")
    for message in all_warnings:
        print(f"[WARN] {message}")

    print(f"\nChecked {len(files)} corpus file(s) under {display_path(root, REPO_ROOT)}")
    for format_name in sorted(counts):
        print(f"- {format_name}: {counts[format_name]}")

    if all_errors:
        print("\nCorpus validation failed.")
        return 1

    if all_warnings:
        print("\nCorpus validation passed with warnings.")
        return 0

    print("\nCorpus validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
