#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path


def slugify(text: str) -> str:
    slug = text.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "untitled"


def yaml_string(value: str | None) -> str:
    return json.dumps((value or "").strip(), ensure_ascii=False)


def yaml_list(values: list[str] | None) -> str:
    cleaned = [value.strip() for value in (values or []) if value and value.strip()]
    return json.dumps(cleaned, ensure_ascii=False)


def plain(value: str | None, fallback: str = "") -> str:
    return (value or fallback).strip()


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def resolve_storage_roots(script_path: Path) -> tuple[Path, Path]:
    skill_root = script_path.resolve().parent.parent
    repo_root = skill_root.parent.parent
    return skill_root, repo_root


def display_path(path: Path, base: Path) -> str:
    resolved_path = path.resolve(strict=False)
    resolved_base = base.resolve(strict=False)
    try:
        return resolved_path.relative_to(resolved_base).as_posix()
    except ValueError:
        return resolved_path.as_posix()


def render_template(template_text: str, values: dict[str, str]) -> str:
    rendered = template_text
    for key, value in values.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return re.sub(r"\{\{[a-z0-9_]+\}\}", "", rendered)


def read_body(body: str | None, body_file: Path | None, default: str) -> str:
    if body and body_file:
        raise SystemExit("Use either --body or --body-file, not both.")
    if body_file:
        return body_file.read_text(encoding="utf-8").strip()
    if body:
        return body.strip()
    return default


def derive_title(body: str, fallback: str = "Untitled") -> str:
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    if not lines:
        return fallback

    first = lines[0].lstrip("#").strip()
    words = first.split()
    if not words:
        return fallback
    return " ".join(words[:12]).strip()


def normalize_date(value: str | None) -> str:
    if not value:
        return datetime.now().astimezone().date().isoformat()

    text = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return text
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    return datetime.fromisoformat(text).date().isoformat()


def next_sequence_number(folder: Path, date_prefix: str) -> int:
    pattern = re.compile(rf"^{re.escape(date_prefix)}-(\d{{2}})--")
    highest = 0
    for path in folder.glob(f"{date_prefix}-*.md"):
        match = pattern.match(path.name)
        if match:
            highest = max(highest, int(match.group(1)))
    return highest + 1


def build_draft_filename(folder: Path, date_prefix: str, format_name: str, title: str) -> str:
    seq = next_sequence_number(folder, date_prefix)
    return f"{date_prefix}-{seq:02d}--draft--{format_name}--{slugify(title)}.md"


def build_published_filename(
    folder: Path,
    date_prefix: str,
    channel: str,
    format_name: str,
    title: str,
) -> str:
    seq = next_sequence_number(folder, date_prefix)
    return f"{date_prefix}-{seq:02d}--{channel}--{format_name}--{slugify(title)}.md"
