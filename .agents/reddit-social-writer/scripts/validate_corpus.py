#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

from storage_common import (
    add_profile_arguments,
    display_path,
    resolve_social_corpus_root,
    resolve_storage_roots,
)

SHARED_SCRIPTS = Path(__file__).resolve().parents[2] / "social-common" / "scripts"
if str(SHARED_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SHARED_SCRIPTS))

from social_validation import iter_corpus_files, validate_social_file  # noqa: E402

SKILL_ROOT, REPO_ROOT = resolve_storage_roots(Path(__file__))

ALLOWED_FORMATS = {"post", "comment-reply"}
FORMAT_BY_FOLDER = {
    "posts": "post",
    "comment-replies": "comment-reply",
}
ALLOWED_ASSET_TYPES = {"none", "image", "video", "link", "poll", "other"}
REQUIRED_FIELDS = ("channel", "format", "published_at", "subreddit", "context", "asset_type")
RECOMMENDED_FIELDS = ("audience", "goal", "topic_tags")
FILENAME_RE = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<seq>\d{2})--reddit--(?P<format>[a-z-]+)--(?P<slug>.+)\.md$",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the published-post corpus for reddit-social-writer.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        help=(
            "Corpus root directory. Defaults to the selected Ink profile's Reddit root, "
            "or content/reddit when no profile config exists."
        ),
    )
    add_profile_arguments(parser)
    return parser.parse_args()


def validate_file(path: Path) -> tuple[list[str], list[str], str | None]:
    return validate_social_file(
        path,
        repo_root=REPO_ROOT,
        filename_re=FILENAME_RE,
        channel="reddit",
        allowed_formats=ALLOWED_FORMATS,
        folder_to_format=FORMAT_BY_FOLDER,
        allowed_asset_types=ALLOWED_ASSET_TYPES,
        required_fields=REQUIRED_FIELDS,
        recommended_fields=RECOMMENDED_FIELDS,
    )


def main() -> int:
    args = parse_args()
    root = (
        args.root
        if args.root
        else resolve_social_corpus_root(repo_root=REPO_ROOT, channel="reddit", profile=args.profile, profile_config=args.profile_config)
    ).resolve()

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
