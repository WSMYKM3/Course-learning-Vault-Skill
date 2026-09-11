# Source and Verification Policy

Read this reference whenever interpreting course material, correcting transcription, or adding outside information.

## Source roles

Classify content before writing:

1. **Course content:** claims, examples, notation, and sequence directly supported by the supplied material.
2. **Verified correction:** a meaningful error in transcription, notation, or fact corrected using strong evidence.
3. **Verified supplement:** outside context needed to make an implicit formula, definition, or prerequisite understandable.
4. **Unresolved:** material that remains ambiguous or unsupported.

Keep the course as the teaching spine. Do not silently present categories 2 or 3 as if the instructor said them.

## When to research

Research only when at least one of these applies:

- a transcript error changes the meaning;
- a formula, theorem, technical term, unit, or condition is incomplete or suspicious;
- the user requests verification or broader context;
- high-stakes accuracy requires current authoritative information.

Prefer primary or authoritative sources: official course material, textbooks or publisher material, standards, original papers, official documentation, and recognized institutional references. For technical topics, prefer official documentation or primary literature. Avoid using search-result snippets as evidence.

## How to write verified material

Keep additions concise and close to the affected claim:

```markdown
> [!info] 补充
> Explanation not stated directly in the lesson. [Source title](https://example.org)
```

```markdown
> [!warning] 转写纠正
> The transcript appears to say X; the standard expression is Y. [Source title](https://example.org)
```

Use `待核验` when reliable confirmation is unavailable. Preserve the uncertain original only when useful for explaining the discrepancy.

## Guardrails

- Do not add citations that were not checked.
- Do not broaden a lesson into an unrelated survey.
- Do not replace the course's harmless notation or pedagogy merely because another convention is common.
- Do not treat a disagreement with one outside source as proof that the course is wrong; compare scope, definitions, and assumptions first.
- Record source URLs in the relevant note body. Use the frontmatter `source` field for the actual course materials that generated the note.
