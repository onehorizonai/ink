#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any


PROFILE_CONFIG_ENV = "INK_PROFILE_CONFIG"
PROFILE_ENV = "INK_PROFILE"
DEFAULT_PROFILE_CONFIG = Path(".local/context/ink-profiles.local.json")
LEGACY_CONTENT_ROOTS = {
    "linkedin": Path("content/linkedin"),
    "reddit": Path("content/reddit"),
}


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


def add_profile_arguments(parser: Any) -> None:
    parser.add_argument(
        "--profile",
        help="Ink profile id to use. Defaults to INK_PROFILE when set.",
    )
    parser.add_argument(
        "--profile-config",
        type=Path,
        help=(
            "Path to ink-profiles.local.json. Defaults to INK_PROFILE_CONFIG "
            "or .local/context/ink-profiles.local.json."
        ),
    )


def add_program_metadata_arguments(parser: Any) -> None:
    parser.add_argument("--program-id", help="Optional Ink Content Program id.")
    parser.add_argument("--format-id", help="Optional Content Program format id.")
    parser.add_argument("--run-id", help="Optional Content Program run id.")
    parser.add_argument("--campaign-id", help="Optional Content Program campaign id.")


def program_metadata_values(args: Any) -> dict[str, str]:
    return {
        "program_id_yaml": yaml_string(getattr(args, "program_id", None)),
        "format_id_yaml": yaml_string(getattr(args, "format_id", None)),
        "run_id_yaml": yaml_string(getattr(args, "run_id", None)),
        "campaign_id_yaml": yaml_string(getattr(args, "campaign_id", None)),
    }


def _resolve_config_path(repo_root: Path, profile_config: Path | None) -> Path:
    configured = profile_config or (
        Path(os.environ[PROFILE_CONFIG_ENV]) if os.environ.get(PROFILE_CONFIG_ENV) else None
    )
    if configured is None:
        configured = DEFAULT_PROFILE_CONFIG

    configured = configured.expanduser()
    if configured.is_absolute():
        return configured
    return repo_root / configured


def load_profile_config(repo_root: Path, profile_config: Path | None = None) -> dict[str, Any] | None:
    path = _resolve_config_path(repo_root, profile_config)
    if not path.exists():
        return None

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid Ink profile config at {display_path(path, repo_root)}: {exc}") from exc

    if not isinstance(data, dict):
        raise SystemExit(f"Invalid Ink profile config at {display_path(path, repo_root)}: root must be an object.")
    profiles = data.get("profiles")
    if not isinstance(profiles, dict) or not profiles:
        raise SystemExit(
            f"Invalid Ink profile config at {display_path(path, repo_root)}: missing non-empty 'profiles'.",
        )
    return data


def resolve_ink_profile(
    repo_root: Path,
    profile: str | None = None,
    profile_config: Path | None = None,
) -> tuple[str, dict[str, Any]] | None:
    config = load_profile_config(repo_root, profile_config)
    requested = (profile or os.environ.get(PROFILE_ENV) or "").strip()

    if config is None:
        if requested:
            config_path = _resolve_config_path(repo_root, profile_config)
            raise SystemExit(
                (
                    f"Ink profile '{requested}' was requested, but no profile config exists at "
                    f"{display_path(config_path, repo_root)}."
                ),
            )
        return None

    profiles = config["profiles"]
    if requested:
        if requested not in profiles:
            available = ", ".join(sorted(profiles))
            raise SystemExit(f"Unknown Ink profile '{requested}'. Available profiles: {available}.")
        selected = profiles[requested]
        if not isinstance(selected, dict):
            raise SystemExit(f"Invalid Ink profile '{requested}': profile value must be an object.")
        return requested, selected

    if len(profiles) == 1:
        only_id = next(iter(profiles))
        selected = profiles[only_id]
        if not isinstance(selected, dict):
            raise SystemExit(f"Invalid Ink profile '{only_id}': profile value must be an object.")
        return only_id, selected

    available = ", ".join(sorted(profiles))
    raise SystemExit(
        (
            "Multiple Ink profiles are configured. Pass --profile or set INK_PROFILE. "
            f"Available profiles: {available}."
        ),
    )


def resolve_repo_path(repo_root: Path, value: str, *, field_name: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise SystemExit(f"Selected Ink profile is missing '{field_name}'.")

    path = Path(os.path.expandvars(value.strip())).expanduser()
    if path.is_absolute():
        return path
    return repo_root / path


def resolve_social_corpus_root(
    repo_root: Path,
    channel: str,
    profile: str | None = None,
    profile_config: Path | None = None,
) -> Path:
    selected = resolve_ink_profile(repo_root, profile, profile_config)
    if selected is None:
        return repo_root / LEGACY_CONTENT_ROOTS[channel]

    profile_id, profile_data = selected
    roots = profile_data.get("contentRoots")
    if not isinstance(roots, dict):
        raise SystemExit(f"Selected Ink profile '{profile_id}' is missing 'contentRoots'.")
    return resolve_repo_path(repo_root, roots.get(channel, ""), field_name=f"contentRoots.{channel}")


def resolve_social_drafts_root(
    repo_root: Path,
    channel: str,
    profile: str | None = None,
    profile_config: Path | None = None,
) -> Path:
    return resolve_social_corpus_root(repo_root, channel, profile, profile_config) / "drafts"


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
