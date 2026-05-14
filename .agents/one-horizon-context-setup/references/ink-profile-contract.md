# Ink Profile Contract

Use this contract before any Ink workflow resolves One Horizon context, searches planned Ink work, reads local corpus examples, or writes local drafts/corpus entries.

## Profile Config

The local profile registry lives at:

- `.local/context/ink-profiles.local.json`

It is gitignored and machine-local. Use `.local/templates/ink-profiles.local.template.json` as the tracked starter.

Required shape:

```json
{
  "version": 1,
  "selectionMode": "ask_when_multiple",
  "profiles": {
    "one-horizon": {
      "label": "One Horizon",
      "workspaceId": "<one-horizon-workspace-id>",
      "authorName": "<author-name>",
      "authorUserId": "",
      "website": "https://example.com",
      "sourceRepo": "/absolute/path/to/one-horizon-source",
      "contentRoots": {
        "linkedin": "content/linkedin",
        "reddit": "content/reddit",
        "blogDrafts": "content/blog/drafts"
      },
      "blogPublishingConfig": ".local/context/blog-publishing.local.md",
      "imageProviderConfig": ".secrets/one-horizon/image-provider.json",
      "imageUploadConfig": ".secrets/one-horizon/blog-image-s3.json"
    }
  }
}
```

Relative paths are resolved from the Ink repo root. Absolute paths are allowed for external repos or published blog folders. Do not commit the live config or any machine-local IDs, user IDs, personal names, private URLs, or local filesystem paths.

## Resolution Order

1. Use an explicit profile named in the prompt, such as `Use Ink profile Product A`.
2. Use `INK_PROFILE` when set.
3. Load `.local/context/ink-profiles.local.json`.
4. If exactly one profile exists, use it.
5. If multiple profiles exist and none was named, ask which Ink profile to use before continuing.

Do not silently use the One Horizon MCP default workspace when a workflow depends on Ink context. Do not infer the profile from old local context files or published corpus examples.

For non-interactive scripts, `--profile` has the same meaning as an explicit profile in the prompt. If a multi-profile config exists and no profile is supplied, scripts must stop with a clear message instead of choosing a default.

## Workspace and Author Rules

- Resolve One Horizon documents, tasks, and initiatives inside the selected profile's `workspaceId`.
- Resolve the author inside that same workspace.
- Use `authorUserId` when present; otherwise resolve `authorName` with One Horizon member/team tools.
- Author context doc titles remain `Ink Context - {Author Name} - {Doc Type}`, but they are only valid inside the selected workspace.
- The workspace-shared `Ink Context - Trend Sources` document is also per selected workspace.
- Required Ink parent initiatives (`Ink`, `Ink - LinkedIn`, `Ink - Reddit`, `Ink - Blog`, `Ink - Website Briefs`) are per selected workspace.

## Local Content Roots

Each selected profile owns its own local paths:

- `contentRoots.linkedin`: published LinkedIn corpus root; drafts live under `<linkedin>/drafts/`.
- `contentRoots.reddit`: published Reddit corpus root; drafts live under `<reddit>/drafts/`.
- `contentRoots.blogDrafts`: unpublished blog draft root.
- `blogPublishingConfig`: local Markdown file containing that profile's `source_articles_dir`, `publish_output_dir`, `last_confirmed_on`, and optional post-publish commands such as `post_publish_generate_command` and `post_publish_build_command`.
- `imageProviderConfig`: optional local JSON file for image search/download provider credentials, staging folder, and download history.
- `imageUploadConfig`: optional local JSON file for image upload bucket/CDN credentials, object prefix, and upload history.

Image config files belong under ignored local paths such as `.secrets/<profile-id>/`. Do not share one image upload config between profiles unless the profiles intentionally publish to the same bucket/CDN. When multiple profiles exist, image MCP tools must resolve the selected Ink profile before searching, downloading, or uploading images.

Legacy behavior is allowed only when no profile config exists. In that case scripts and old docs may still use `content/linkedin`, `content/reddit`, `content/blog/drafts`, `.local/context/blog-publishing.local.md`, `.secrets/image-provider.json`, and `.secrets/blog-image-s3.json`.

## Profile Bootstrap Source Safety

When setting up a profile from a source repo, use only safe project sources from the selected profile's `sourceRepo` after confirming the profile and target workspace.

Allowed source patterns:

- `README.md`
- `apps/**/README.md`
- `docs/**/*.md`
- public website copy files, such as `apps/**/website/src/app/**`

Do not read `.env*`, `.secrets`, `node_modules`, build outputs, `.turbo`, `.tmp`, private runtime state, or generated dependency folders as setup source material.

Create context docs and Ink parent initiatives in the selected profile workspace only after the normal confirmation summary. Existing docs remain read-only.
