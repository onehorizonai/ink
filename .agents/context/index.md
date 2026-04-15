# Context Index

`.agents/context/` holds the public contract for how local context works.

Store live runtime context in `.local/context/`, which is gitignored.

Starter files live in `.agents/context/templates/`. Copy only the files you need into `.local/context/`.

Load runtime context progressively.

## Always start here

- `.local/context/profile.md`

## Usually load for business writing

- `.local/context/current-work.md`
- `.local/context/market-context.md`
  Use for product positioning, competitor context, integrations, and partner references.
- `blog-publishing.md`
  Use for the blog path-resolution contract.
- `.local/context/blog-publishing.local.md`
  Use for the active blog source and publish folders. If the file is missing, or if either stored folder is `[unset]` or missing on disk, ask the user and update this local file before continuing.

## Load only when relevant

- `.local/context/work-history.md`
  Use for founder stories, career reflections, credibility, or background-heavy posts.
- `.local/context/personal-interests.md`
  Use for analogies, taste, cultural references, hobbies, music, sports, or human texture when it helps.
- `.local/context/personal-life.md`
  Use only for explicitly personal writing, life updates, reflection posts, or when the brief calls for family, pets, or similar details.

## Rule

Do not load irrelevant personal context into business writing.
