#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

from social_storage import display_path


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def load_markdown(path: Path) -> tuple[dict[str, object], str]:
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
                    list_values.append(str(strip_quotes(list_line[4:].strip())))
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


def strip_quotes(value: str) -> object:
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


def validate_social_file(
    path: Path,
    *,
    repo_root: Path,
    filename_re: re.Pattern[str],
    channel: str,
    allowed_formats: set[str],
    folder_to_format: dict[str, str],
    allowed_asset_types: set[str],
    required_fields: tuple[str, ...],
    recommended_fields: tuple[str, ...],
    required_sections: tuple[str, ...] = ("## Published Copy",),
) -> tuple[list[str], list[str], str | None]:
    errors: list[str] = []
    warnings: list[str] = []
    path_label = display_path(path, repo_root)

    filename_match = filename_re.match(path.name)
    if not filename_match:
        errors.append(
            f"{path_label}: filename does not match the expected {channel} corpus pattern",
        )

    try:
        frontmatter, body = load_markdown(path)
    except ValueError as exc:
        return [f"{path_label}: {exc}"], warnings, None

    for field in required_fields:
        value = frontmatter.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path_label}: missing required field '{field}'")

    actual_channel = str(frontmatter.get("channel", "")).strip().lower()
    if actual_channel and actual_channel != channel:
        errors.append(f"{path_label}: channel must be '{channel}', got '{actual_channel}'")

    format_name = str(frontmatter.get("format", "")).strip().lower()
    if format_name and format_name not in allowed_formats:
        errors.append(f"{path_label}: unknown format '{format_name}'")

    expected_format = folder_to_format.get(path.parent.name)
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
    if asset_type and asset_type not in allowed_asset_types:
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

    for field in recommended_fields:
        if field not in frontmatter or frontmatter.get(field) in (None, "", []):
            warnings.append(f"{path_label}: recommended field '{field}' is missing")

    for section in required_sections:
        if section not in body:
            warnings.append(f"{path_label}: missing '{section}' section")

    return errors, warnings, format_name or None


def iter_corpus_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.name.lower() != "readme.md" and path.is_file()
        and "drafts" not in path.relative_to(root).parts
    )
