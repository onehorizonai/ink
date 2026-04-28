#!/usr/bin/env python3
"""Check prompt guidance for the document MCP metadata/content split."""

from __future__ import annotations

import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GLOBAL_SKILLS_DIR = Path(os.environ.get("ONE_HORIZON_SKILLS_DIR", "/Users/gijs/.agents/skills"))

REPO_GUIDANCE_FILES = [
    ".agents/one-horizon-context-setup/references/context-doc-templates.md",
    ".agents/one-horizon-context-setup/references/mcp-readiness.md",
    ".agents/content-idea-finder/references/workflow.md",
    ".agents/linkedin-social-writer/references/workflow.md",
    ".agents/reddit-social-writer/references/workflow.md",
    ".agents/reddit-research/references/workflow.md",
    ".agents/blog-post-writer/references/workflow.md",
    ".agents/page-brief-builder/references/workflow.md",
    ".agents/content-tone-review/SKILL.md",
    ".agents/content-humanizer/SKILL.md",
    ".agents/website-brief-intake/SKILL.md",
]

OPTIONAL_GLOBAL_SKILL_FILES = [
    GLOBAL_SKILLS_DIR / "manage-documents" / "SKILL.md",
    GLOBAL_SKILLS_DIR / "task-management" / "SKILL.md",
]

BANNED_PHRASES = [
    "find-documents returns full content",
    "find-documents returns full document content",
    "read full document bodies from find-documents",
    "read the full body from find-documents",
]


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"missing checked file: {path}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, path: Path) -> None:
    if needle not in text:
        raise AssertionError(f"{path} is missing required guidance: {needle!r}")


def check_repo_guidance() -> None:
    for relative_path in REPO_GUIDANCE_FILES:
        path = REPO_ROOT / relative_path
        text = read(path)
        require(text, "find-documents", path)
        require(text, "get-document", path)

    contract = read(REPO_ROOT / ".agents/one-horizon-context-setup/references/context-doc-templates.md")
    require(contract, "get-task-details", REPO_ROOT / ".agents/one-horizon-context-setup/references/context-doc-templates.md")


def check_global_skills() -> None:
    for path in OPTIONAL_GLOBAL_SKILL_FILES:
        if not path.exists():
            continue
        text = read(path)
        require(text, "find-documents", path)
        require(text, "get-document", path)
        require(text, "metadata plus `excerpt` only", path)
        if path.parts[-2] == "task-management":
            require(text, "content-document-backed task descriptions", path)
            require(text, "get-task-details", path)


def check_banned_phrases() -> None:
    paths = [REPO_ROOT / relative_path for relative_path in REPO_GUIDANCE_FILES]
    paths.extend(path for path in OPTIONAL_GLOBAL_SKILL_FILES if path.exists())

    for path in paths:
        text = read(path).lower()
        for phrase in BANNED_PHRASES:
            if phrase in text:
                raise AssertionError(f"{path} contains banned guidance: {phrase!r}")


def main() -> None:
    check_repo_guidance()
    check_global_skills()
    check_banned_phrases()
    print("document MCP guidance checks passed")


if __name__ == "__main__":
    main()
