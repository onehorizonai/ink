# Local Context Templates

Copy the templates in this directory into `.local/context/` and rename them without the `.template` suffix.

Example:

- `.agents/context/templates/profile.template.md` -> `.local/context/profile.md`
- `.agents/context/templates/blog-publishing.local.template.md` -> `.local/context/blog-publishing.local.md`

Rules:

- Keep live personal, company, and workspace-specific context in `.local/context/`.
- Do not commit `.local/context/`.
- Treat these files as starter shapes. Replace placeholder values with your own local data.
