#!/usr/bin/env python3
"""Check Ink profile guidance and script support."""

from __future__ import annotations

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

PROFILE_CONTRACT = ".agents/one-horizon-context-setup/references/ink-profile-contract.md"
PROFILE_TEMPLATE = ".local/templates/ink-profiles.local.template.json"

GUIDANCE_FILES = [
    "AGENTS.md",
    "README.md",
    ".local/README.md",
    ".agents/one-horizon-context-setup/SKILL.md",
    ".agents/one-horizon-context-setup/references/context-doc-templates.md",
    ".agents/one-horizon-context-setup/references/ink-initiative-hierarchy.md",
    ".agents/content-idea-finder/SKILL.md",
    ".agents/content-idea-finder/references/workflow.md",
    ".agents/content-creation-runner/SKILL.md",
    ".agents/content-publishing-runner/SKILL.md",
    ".agents/channel-content-writer/SKILL.md",
    ".agents/channel-content-writer/references/channel-workspace.md",
    ".agents/content-program-builder/SKILL.md",
    ".agents/content-program-runner/SKILL.md",
    "content-programs/README.md",
    ".agents/linkedin-social-writer/SKILL.md",
    ".agents/linkedin-social-writer/references/workflow.md",
    ".agents/reddit-social-writer/SKILL.md",
    ".agents/reddit-social-writer/references/workflow.md",
    ".agents/blog-post-writer/SKILL.md",
    ".agents/blog-post-writer/references/workflow.md",
    ".agents/blog-image-finder/SKILL.md",
    ".agents/blog-image-finder/references/setup.md",
    ".agents/blog-image-uploader/SKILL.md",
    ".agents/blog-image-uploader/references/setup.md",
    ".agents/page-brief-builder/SKILL.md",
    ".agents/page-brief-builder/references/workflow.md",
]

SCRIPT_FILES = [
    ".agents/linkedin-social-writer/scripts/create_draft.py",
    ".agents/linkedin-social-writer/scripts/store_published.py",
    ".agents/linkedin-social-writer/scripts/store_published_batch.py",
    ".agents/linkedin-social-writer/scripts/validate_corpus.py",
    ".agents/reddit-social-writer/scripts/create_draft.py",
    ".agents/reddit-social-writer/scripts/store_published.py",
    ".agents/reddit-social-writer/scripts/store_published_batch.py",
    ".agents/reddit-social-writer/scripts/validate_corpus.py",
]

IMAGE_MCP_FILES = [
    ".agents/blog-image-finder/mcp/image-provider/server.py",
    ".agents/blog-image-uploader/mcp/blog-image-s3/server.py",
]

BANNED_PHRASES_BY_FILE = {
    ".agents/linkedin-social-writer/SKILL.md": [
        "Search `../../content/linkedin/`",
        "Save unpublished drafts in `content/linkedin/drafts/`",
    ],
    ".agents/reddit-social-writer/SKILL.md": [
        "Search `../../content/reddit/`",
        "Save unpublished drafts in `content/reddit/drafts/`",
    ],
    ".agents/blog-post-writer/SKILL.md": [
        "Read `../../.local/context/blog-publishing.local.md`",
        "Save unpublished drafts in `content/blog/drafts/`",
    ],
    ".agents/content-idea-finder/references/workflow.md": [
        "Read `../../../.local/context/blog-publishing.local.md`",
        "Search the LinkedIn corpus in `../../content/linkedin/posts/`",
        "Search the Reddit corpus in `../../content/reddit/posts/`",
    ],
}


def read(relative_path: str) -> str:
    path = REPO_ROOT / relative_path
    if not path.exists():
        raise AssertionError(f"missing checked file: {relative_path}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, relative_path: str) -> None:
    if needle not in text:
        raise AssertionError(f"{relative_path} is missing required guidance: {needle!r}")


def check_profile_contract() -> None:
    contract = read(PROFILE_CONTRACT)
    require(contract, "selectionMode", PROFILE_CONTRACT)
    require(contract, "ask_when_multiple", PROFILE_CONTRACT)
    require(contract, "workspaceId", PROFILE_CONTRACT)
    require(contract, "contentRoots", PROFILE_CONTRACT)
    require(contract, "contentRoots.channels", PROFILE_CONTRACT)
    require(contract, "blogPublishingConfig", PROFILE_CONTRACT)
    require(contract, "imageProviderConfig", PROFILE_CONTRACT)
    require(contract, "imageUploadConfig", PROFILE_CONTRACT)
    require(contract, "Do not commit the live config", PROFILE_CONTRACT)


def check_template() -> None:
    path = REPO_ROOT / PROFILE_TEMPLATE
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["version"] == 1
    assert data["selectionMode"] == "ask_when_multiple"
    profiles = data["profiles"]
    for profile_id in ("one-horizon", "fit-horizon"):
        profile = profiles[profile_id]
        for key in (
            "label",
            "workspaceId",
            "authorName",
            "website",
            "sourceRepo",
            "contentRoots",
            "blogPublishingConfig",
            "imageProviderConfig",
            "imageUploadConfig",
        ):
            if key not in profile:
                raise AssertionError(f"{path} profile {profile_id!r} is missing {key!r}")
        for channel in ("linkedin", "reddit", "blogDrafts", "channels"):
            if channel not in profile["contentRoots"]:
                raise AssertionError(f"{path} profile {profile_id!r} is missing contentRoots.{channel}")


def check_guidance_files() -> None:
    for relative_path in GUIDANCE_FILES:
        text = read(relative_path)
        if "ink-profile-contract" not in text and "Ink profile" not in text:
            raise AssertionError(f"{relative_path} does not mention Ink profile resolution")

    for relative_path, phrases in BANNED_PHRASES_BY_FILE.items():
        text = read(relative_path)
        for phrase in phrases:
            if phrase in text:
                raise AssertionError(f"{relative_path} still contains stale single-profile guidance: {phrase!r}")


def check_no_sensitive_profile_examples() -> None:
    for relative_path in (PROFILE_CONTRACT, PROFILE_TEMPLATE, "README.md", ".agents/one-horizon-context-setup/SKILL.md"):
        text = read(relative_path)
        if "/Users/" in text:
            raise AssertionError(f"{relative_path} contains a machine-local /Users path")
        if re.search(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", text):
            raise AssertionError(f"{relative_path} contains a real-looking UUID")
        if re.search(r'"workspaceId"\s*:\s*"(?!<)[^"]+"', text):
            raise AssertionError(f"{relative_path} contains a non-placeholder workspaceId example")

    template = json.loads((REPO_ROOT / PROFILE_TEMPLATE).read_text(encoding="utf-8"))
    for profile_id, profile in template["profiles"].items():
        if not profile["workspaceId"].startswith("<"):
            raise AssertionError(f"{PROFILE_TEMPLATE} profile {profile_id!r} has a non-placeholder workspaceId")
        if not profile["authorName"].startswith("<"):
            raise AssertionError(f"{PROFILE_TEMPLATE} profile {profile_id!r} has a non-placeholder authorName")


def check_script_profile_support() -> None:
    shared = read(".agents/social-common/scripts/social_storage.py")
    require(shared, "INK_PROFILE", ".agents/social-common/scripts/social_storage.py")
    require(shared, "ink-profiles.local.json", ".agents/social-common/scripts/social_storage.py")
    require(shared, "resolve_social_corpus_root", ".agents/social-common/scripts/social_storage.py")
    require(shared, "resolve_social_drafts_root", ".agents/social-common/scripts/social_storage.py")

    for relative_path in SCRIPT_FILES:
        text = read(relative_path)
        require(text, "add_profile_arguments(parser)", relative_path)
        require(text, "args.profile", relative_path)
        require(text, "args.profile_config", relative_path)

    for relative_path in IMAGE_MCP_FILES:
        text = read(relative_path)
        require(text, '"profile"', relative_path)
        require(text, '"profile_config"', relative_path)
        require(text, "resolve_ink_profile", relative_path)


def check_blog_unique_date_guidance() -> None:
    required = {
        "AGENTS.md": "Published blog dates must be unique",
        ".agents/blog-post-writer/SKILL.md": "Published blog posts must have a unique `metadata.date`",
        ".agents/blog-post-writer/references/workflow.md": "Reserve the published date",
        ".agents/blog-post-writer/references/corpus-spec.md": "Published blog dates must be unique",
        ".agents/content-publishing-runner/SKILL.md": "published blog date must be unique",
    }
    for relative_path, needle in required.items():
        require(read(relative_path), needle, relative_path)

    corpus_spec = read(".agents/blog-post-writer/references/corpus-spec.md")
    if "If the same date and slug need more than one file, append" in corpus_spec:
        raise AssertionError("corpus spec still allows duplicate published blog dates")


def main() -> None:
    check_profile_contract()
    check_template()
    check_guidance_files()
    check_no_sensitive_profile_examples()
    check_script_profile_support()
    check_blog_unique_date_guidance()
    print("Ink profile guidance checks passed")


if __name__ == "__main__":
    main()
