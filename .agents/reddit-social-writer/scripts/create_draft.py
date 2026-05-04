#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from storage_common import (
    FORMAT_BY_FOLDER,
    build_draft_filename,
    default_format_template,
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create an unpublished Reddit draft file.")
    parser.add_argument("--format", required=True, choices=sorted(FORMAT_BY_FOLDER))
    parser.add_argument("--title", required=True)
    parser.add_argument("--subreddit", required=True)
    parser.add_argument("--format-template")
    parser.add_argument("--goal")
    parser.add_argument("--audience")
    parser.add_argument("--asset-type", default="none")
    parser.add_argument("--source-brief")
    parser.add_argument("--research-snapshot")
    parser.add_argument("--example-path", action="append")
    parser.add_argument("--body")
    parser.add_argument("--body-file", type=Path)
    return parser.parse_args()


def build_content(root: Path, args: argparse.Namespace, created_at: str, body: str) -> str:
    template_text = load_text(root / "templates" / "storage" / "draft.md")
    default_example_path = f"content/reddit/{FORMAT_BY_FOLDER[args.format]}/replace-with-example.md"
    values = {
        "format_yaml": yaml_string(args.format),
        "created_at_yaml": yaml_string(created_at),
        "title_yaml": yaml_string(args.title),
        "subreddit_yaml": yaml_string(args.subreddit),
        "format_template_yaml": yaml_string(args.format_template or default_format_template(args.format)),
        "goal_yaml": yaml_string(args.goal),
        "audience_yaml": yaml_string(args.audience),
        "asset_type_yaml": yaml_string(args.asset_type),
        "source_brief_yaml": yaml_string(args.source_brief),
        "research_snapshot_yaml": yaml_string(args.research_snapshot),
        "based_on_examples_yaml": yaml_list(args.example_path or [default_example_path]),
        "goal_plain": plain(args.goal),
        "body": body,
    }
    return render_template(template_text, values)


def main() -> int:
    args = parse_args()
    root, repo_root = resolve_storage_roots(Path(__file__))
    drafts_root = repo_root / "content" / "reddit" / "drafts" / FORMAT_BY_FOLDER[args.format]
    drafts_root.mkdir(parents=True, exist_ok=True)

    created_at = datetime.now().astimezone().isoformat(timespec="minutes")
    date_prefix = normalize_date(created_at)
    filename = build_draft_filename(drafts_root, date_prefix, args.format, args.title)
    target = drafts_root / filename

    body = read_body(args.body, args.body_file, "[Draft body goes here]")
    target.write_text(build_content(root, args, created_at, body), encoding="utf-8")
    print(display_path(target, repo_root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
