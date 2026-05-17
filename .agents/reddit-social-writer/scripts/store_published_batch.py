#!/usr/bin/env python3
"""Store multiple published Reddit items in one call.

Posts are read from a file (--posts-file) or stdin, separated by a
configurable delimiter (default: |). All metadata flags are applied
uniformly to every post in the batch.
"""
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
    derive_title,
    display_path,
    load_text,
    normalize_date,
    plain,
    program_metadata_values,
    render_template,
    resolve_social_corpus_root,
    resolve_storage_roots,
    yaml_list,
    yaml_string,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Store multiple published Reddit items in the corpus.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--posts-file", type=Path, help="File containing posts separated by --separator.")
    parser.add_argument("--separator", default="|", help="Delimiter between posts (default: |). Use '---' for triple-dash.")
    parser.add_argument("--format", default="post", choices=sorted(FORMAT_BY_FOLDER))
    parser.add_argument("--subreddit", required=True)
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
    parser.add_argument("--based-on-research")
    parser.add_argument("--discussion-prompt")
    add_profile_arguments(parser)
    add_program_metadata_arguments(parser)
    return parser.parse_args()


def read_posts(args: argparse.Namespace) -> list[str]:
    if args.posts_file:
        raw = args.posts_file.read_text(encoding="utf-8")
    elif not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        raise SystemExit("Provide posts via --posts-file or stdin.")

    sep = "---" if args.separator == "---" else args.separator
    posts = [p.strip() for p in raw.split(sep)]
    return [p for p in posts if p]


def build_content(root: Path, args: argparse.Namespace, title: str, published_at: str, body: str) -> str:
    template_text = load_text(root / "templates" / "storage" / f"{args.format}.md")
    format_template = args.format_template or default_format_template(args.format)
    context = args.context or "Stored from shared Reddit content."
    outcome_notes = args.outcome_notes or "- Add notes here if relevant."
    values = {
        "subreddit_yaml": yaml_string(args.subreddit),
        "subreddit_plain": plain(args.subreddit),
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
        "based_on_research_yaml": yaml_string(args.based_on_research),
        "discussion_prompt_yaml": yaml_string(args.discussion_prompt),
        **program_metadata_values(args),
        "context_plain": plain(context),
        "format_template_plain": plain(format_template),
        "audience_plain": plain(args.audience),
        "goal_plain": plain(args.goal),
        "asset_type_plain": plain(args.asset_type),
        "asset_summary_plain": plain(args.asset_summary),
        "thread_summary_plain": plain(args.thread_summary),
        "based_on_research_plain": plain(args.based_on_research),
        "discussion_prompt_plain": plain(args.discussion_prompt),
        "outcome_notes_plain": plain(outcome_notes, "- Add notes here if relevant."),
        "body": body,
    }
    return render_template(template_text, values)


def main() -> int:
    args = parse_args()
    root, repo_root = resolve_storage_roots(Path(__file__))
    posts = read_posts(args)

    if not posts:
        raise SystemExit("No posts found after splitting.")

    published_at = normalize_date(args.published_at)
    target_dir = resolve_social_corpus_root(
        repo_root,
        "reddit",
        args.profile,
        args.profile_config,
    ) / FORMAT_BY_FOLDER[args.format]
    target_dir.mkdir(parents=True, exist_ok=True)

    errors = 0
    for i, body in enumerate(posts, 1):
        title = derive_title(body, "Shared Reddit item").strip()
        target = target_dir / build_published_filename(target_dir, published_at, args.format, title)
        try:
            content = build_content(root, args, title, published_at, body)
            target.write_text(content, encoding="utf-8")
            print(f"[{i:02d}] {display_path(target, repo_root)}")
        except Exception as exc:
            print(f"[{i:02d}] ERROR: {exc}", file=sys.stderr)
            errors += 1

    print(f"\n{len(posts) - errors} stored, {errors} errors.")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
