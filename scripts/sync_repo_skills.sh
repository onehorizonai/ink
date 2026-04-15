#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Usage: ./scripts/sync_repo_skills.sh [target...]

Sync repo-local skills from .agents/ into every configured app-specific skills directory.

If one or more targets are provided, sync only those targets.

Configured targets:
  - codex

Examples:
  ./scripts/sync_repo_skills.sh
  ./scripts/sync_repo_skills.sh codex
EOF
}

configured_targets() {
  printf '%s\n' "codex"
}

resolve_target_dir() {
  case "$1" in
    codex)
      printf '%s\n' "${CODEX_HOME:-$HOME/.codex}/skills"
      ;;
    *)
      return 1
      ;;
  esac
}

warn_for_target() {
  local target="$1"
  local skill_dir="$2"
  local skill_name="$3"

  case "${target}" in
    codex)
      if [ ! -f "${skill_dir}/agents/openai.yaml" ]; then
        printf 'warn: %s is missing agents/openai.yaml; syncing anyway\n' "${skill_name}" >&2
      fi
      ;;
  esac
}

if [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
  usage
  exit 0
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
agents_dir="${repo_root}/.agents"

if [ ! -d "${agents_dir}" ]; then
  printf 'error: missing agents directory: %s\n' "${agents_dir}" >&2
  exit 1
fi

sync_target() {
  local target_name="$1"
  local target_dir=""
  local linked_count=0
  local existing_count=0

  if ! target_dir="$(resolve_target_dir "${target_name}")"; then
    printf 'error: unsupported sync target: %s\n' "${target_name}" >&2
    printf 'configured targets:\n' >&2
    configured_targets | sed 's/^/  - /' >&2
    exit 1
  fi

  mkdir -p "${target_dir}"

  printf 'sync target: %s -> %s\n' "${target_name}" "${target_dir}"

  for skill_dir in "${agents_dir}"/*; do
    [ -d "${skill_dir}" ] || continue
    [ -f "${skill_dir}/SKILL.md" ] || continue

    skill_name="$(basename "${skill_dir}")"
    target_path="${target_dir}/${skill_name}"

    warn_for_target "${target_name}" "${skill_dir}" "${skill_name}"

    if [ -L "${target_path}" ]; then
      current_target="$(readlink "${target_path}")"
      if [ "${current_target}" = "${skill_dir}" ]; then
        printf 'ok: %s already linked\n' "${skill_name}"
        existing_count=$((existing_count + 1))
        continue
      fi

      printf 'error: %s already points to %s\n' "${target_path}" "${current_target}" >&2
      exit 1
    fi

    if [ -e "${target_path}" ]; then
      printf 'error: %s already exists and is not a symlink\n' "${target_path}" >&2
      exit 1
    fi

    ln -s "${skill_dir}" "${target_path}"
    printf 'linked: %s -> %s\n' "${skill_name}" "${skill_dir}"
    linked_count=$((linked_count + 1))
  done

  printf 'done: %s linked, %s already linked, target %s at %s\n' "${linked_count}" "${existing_count}" "${target_name}" "${target_dir}"
}

if [ $# -eq 0 ]; then
  while IFS= read -r target_name; do
    sync_target "${target_name}"
  done < <(configured_targets)
else
  for target_name in "$@"; do
    sync_target "${target_name}"
  done
fi
