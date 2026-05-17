#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from storage_common import (
    FORMAT_BY_FOLDER,
    add_profile_arguments,
    add_program_metadata_arguments,
    build_published_filename,
    default_format_template,
    display_path,
    derive_title,
    load_text,
    normalize_date,
    plain,
    program_metadata_values,
    read_body,
    resolve_storage_roots,
    resolve_social_corpus_root,
    render_template,
    yaml_list,
    yaml_string,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Store a published LinkedIn item in the corpus.")
    parser.add_argument("--format", default="post", choices=sorted(FORMAT_BY_FOLDER))
    parser.add_argument("--title")
    parser.add_argument("--format-template")
    parser.add_argument("--published-at")
    parser.add_argument("--context")
    parser.add_argument("--author")
    parser.add_argument("--audience")
    parser.add_argument("--goal")
    parser.add_argument("--topic-tag", action="append")
    parser.add_argument("--asset-type", default="none")
    parser.add_argument("--asset-summary")
    parser.add_argument("--source-url")
    parser.add_argument("--thread-summary")
    parser.add_argument("--outcome-notes")
    parser.add_argument("--body")
    parser.add_argument("--body-file", type=Path)
    add_profile_arguments(parser)
    add_program_metadata_arguments(parser)
    return parser.parse_args()


def build_content(root: Path, args: argparse.Namespace, title: str, published_at: str, body: str) -> str:
    template_text = load_text(root / "templates" / "storage" / f"{args.format}.md")
    format_template = args.format_template or default_format_template(args.format)
    context = args.context or "Stored from shared LinkedIn content."
    outcome_notes = args.outcome_notes or "- Add notes here if relevant."
    values = {
        "published_at_yaml": yaml_string(published_at),
        "title_yaml": yaml_string(title),
        "format_template_yaml": yaml_string(format_template),
        "context_yaml": yaml_string(context),
        "author_yaml": yaml_string(args.author),
        "audience_yaml": yaml_string(args.audience),
        "goal_yaml": yaml_string(args.goal),
        "topic_tags_yaml": yaml_list(args.topic_tag),
        "asset_type_yaml": yaml_string(args.asset_type),
        "asset_summary_yaml": yaml_string(args.asset_summary),
        "source_url_yaml": yaml_string(args.source_url),
        "thread_summary_yaml": yaml_string(args.thread_summary),
        "outcome_notes_yaml": yaml_string(args.outcome_notes),
        **program_metadata_values(args),
        "context_plain": plain(context),
        "format_template_plain": plain(format_template),
        "audience_plain": plain(args.audience),
        "goal_plain": plain(args.goal),
        "asset_type_plain": plain(args.asset_type),
        "asset_summary_plain": plain(args.asset_summary),
        "thread_summary_plain": plain(args.thread_summary),
        "outcome_notes_plain": plain(outcome_notes, "- Add notes here if relevant."),
        "body": body,
    }
    return render_template(template_text, values)


def main() -> int:
    args = parse_args()
    root, repo_root = resolve_storage_roots(Path(__file__))
    body = read_body(args.body, args.body_file, "")
    if not body:
        raise SystemExit("A body is required via --body or --body-file.")

    title = (args.title or derive_title(body, "Shared LinkedIn item")).strip()
    published_at = normalize_date(args.published_at)

    target_dir = resolve_social_corpus_root(
        repo_root,
        "linkedin",
        args.profile,
        args.profile_config,
    ) / FORMAT_BY_FOLDER[args.format]
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / build_published_filename(target_dir, published_at, args.format, title)

    content = build_content(root, args, title, published_at, body)
    target.write_text(content, encoding="utf-8")
    print(display_path(target, repo_root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
