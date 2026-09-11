---
name: course-learning-vault
description: Turn course transcripts and text-based learning materials into a structured, linked Obsidian study vault. Use for course setup, lesson notes, canonical concept/formula/method nodes, checkpoint reviews, quizzes, or vault quality audits. Do not use for audio/video transcription, generic note-taking unrelated to a course, or spaced-repetition scheduling.
---

# Course Learning Vault

Build a source-grounded learning system, not a cleaned transcript. Preserve the course's teaching logic while making the result useful for understanding, retrieval, and review in standard Obsidian.

## Route the request

- **Set up a course or vault:** read [references/vault-schema.md](references/vault-schema.md).
- **Turn a transcript or text lesson into notes:** read [references/vault-schema.md](references/vault-schema.md), [references/lesson-workflow.md](references/lesson-workflow.md), and [references/source-policy.md](references/source-policy.md).
- **Create a checkpoint review or quiz:** read [references/vault-schema.md](references/vault-schema.md) and [references/review-and-quiz.md](references/review-and-quiz.md). Also read [references/source-policy.md](references/source-policy.md) if consulting raw or external sources.
- **Audit a vault:** read the audit section of [references/vault-schema.md](references/vault-schema.md), then run `python3 scripts/audit_vault.py <vault>`. Auditing is read-only; do not repair findings unless the user asks.

## Shared workflow

1. Inspect applicable project instructions, the target vault, source materials, and `00 - Course Map.md` when present. Discover facts from files before asking the user.
2. Determine whether this is a new vault or a legacy vault. For a legacy vault, record its existing directory mapping and do not migrate, rename, or reorganize it without an explicit request.
3. Read every existing note that will be updated. Preserve unknown frontmatter fields, user-authored sections, annotations, and links. If safe ownership of existing text is unclear, add a clearly labeled proposal or ask before replacement.
4. Use the source as the teaching spine. Separate course content from verified correction, outside supplementation, and unresolved uncertainty.
5. Reuse canonical nodes before creating new ones. Check filenames, aliases, titles, and both Chinese and English names; do not auto-merge ambiguous terms.
6. Write only standard Markdown, Obsidian WikiLinks, callouts, YAML frontmatter, and MathJax. Do not require community plugins.
7. Update the course map and related links when outputs change. Never mark a lesson or concept as mastered unless the user explicitly reports that state.
8. Run the audit after material changes. Resolve errors caused by the current work and report pre-existing findings separately.

## Defaults

- Treat each course as an independent vault.
- Write in Chinese unless the course map or user requests another language. Preserve standard English terminology in titles or aliases when it improves retrieval; do not invent an English equivalent when none is established.
- Generate a short lesson self-check with collapsible answers. Generate checkpoint reviews and comprehensive quizzes only when requested or when the user accepts a suggestion at a clear module boundary.
- Accept `.txt`, `.md`, pasted text, and subtitle-like transcripts as primary input. Read PDFs, web pages, or notebooks only when relevant and available; do not transcribe audio or video.
- Keep atomic nodes selective. Concepts, formulas/laws, and methods are core types; create theorem, proof, code, or classic-example nodes only when the material benefits from them.

## Safety and stopping rules

- Never modify original course materials.
- Never silently overwrite a note merely because a source changed. Merge deliberately after inspecting both versions.
- Never create facts, formulas, citations, future lesson links, or mastery claims to make the vault look complete.
- External research is for resolving meaningful uncertainty or filling an explicitly requested gap, not for turning every lesson into a broader textbook.
