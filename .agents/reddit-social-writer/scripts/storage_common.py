#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

SHARED_SCRIPTS = Path(__file__).resolve().parents[2] / "social-common" / "scripts"
if str(SHARED_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SHARED_SCRIPTS))

from social_storage import (  # noqa: E402
    build_draft_filename as _build_draft_filename,
    build_published_filename as _build_published_filename,
    derive_title,
    display_path,
    load_text,
    normalize_date,
    plain,
    read_body,
    render_template,
    resolve_storage_roots,
    yaml_list,
    yaml_string,
)

CHANNEL = "reddit"
FORMAT_BY_FOLDER = {
    "post": "posts",
    "comment-reply": "comment-replies",
}


def build_draft_filename(folder: Path, date_prefix: str, format_name: str, title: str) -> str:
    return _build_draft_filename(folder, date_prefix, format_name, title)


def build_published_filename(folder: Path, date_prefix: str, format_name: str, title: str) -> str:
    return _build_published_filename(folder, date_prefix, CHANNEL, format_name, title)


def default_format_template(format_name: str) -> str:
    if format_name == "post":
        return "discussion-post"
    if format_name == "comment-reply":
        return "discussion-reply"
    return ""
