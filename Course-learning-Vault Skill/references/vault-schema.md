# Vault Schema

Read this reference when initializing a course, creating any note, adopting a legacy vault, or interpreting audit results.

## New-vault layout

```text
00 - Course Map.md
Lessons/
Concepts/
Formulas/
Methods/
Reviews/
Quizzes/
```

Create `Theorems/`, `Proofs/`, `Code/`, or `Examples/` only when the course actually needs those node types. Do not create empty extension folders.

## Course map: configuration and dashboard

`00 - Course Map.md` is both the human-facing home page and the configuration source of truth. For a new vault, use these path defaults:

```yaml
---
type: course-map
course_id: "stable-lowercase-course-id"
course: "Course title"
provider: "Provider or instructor"
output_language: "zh-CN"
term_language: "en"
lesson_dir: "Lessons"
concept_dir: "Concepts"
formula_dir: "Formulas"
method_dir: "Methods"
review_dir: "Reviews"
quiz_dir: "Quizzes"
source_roots:
  - "../Sources"
tags:
  - course-map
---
```

Omit unknown optional values rather than inventing them. Keep `course_id` stable after creation. The body should contain:

- a short course purpose and source description;
- a lesson table with status and links;
- links to concept, formula, and method indexes or their folders;
- checkpoint review and quiz links;
- a small `待复习` section based only on user-reported difficulty.

Use lesson statuses `未开始`, `学习中`, `待复习`, and `已掌握`. Change them only from explicit user feedback.

## Legacy adoption

Do not reorganize an existing vault. Create or update its course map with the observed paths. For the existing Machine Learning vault, the compatible mapping is:

```yaml
lesson_dir: "."
concept_dir: "Terms"
formula_dir: "Formulas"
method_dir: "Methods"
review_dir: "Reviews"
quiz_dir: "Quizzes"
code_dir: "codelines"
```

Existing metadata such as `lesson-note`, `term`, `term_cn`, `term_en`, `formula_cn`, and `formula_en` remains valid. Apply the normalized schema below to newly created vaults; do not bulk-convert legacy notes unless asked.

## Common metadata

Use the smallest relevant subset. Preserve user-defined properties.

```yaml
---
type: lesson
course_id: "course-id"
course: "Course title"
chapter: "1.2"
topic: "Topic"
source:
  - "relative/or/descriptive/source"
aliases:
  - "Optional alternative title"
tags:
  - course-topic
---
```

Atomic nodes use `type: concept`, `formula`, or `method`, plus `course_id`, `course`, `name_cn`, optional `name_en`, `aliases`, `source_lessons`, and focused tags. Extension types use `theorem`, `proof`, `code-reference`, or `classic-example`.

Reviews use `type: checkpoint-review`, `course_id`, `course`, `scope`, and `lessons`. Quizzes use `type: quiz`, `course_id`, `course`, `scope`, and optional `difficulty`.

Do not put WikiLinks inside YAML values. Link notes in the Markdown body.

## Note contracts

### Lesson

Name: `章节号 - 中文主题.md` when a chapter number exists.

Required behavior:

- state learning objectives;
- organize the explanation around the lesson's reasoning, not transcript chronology alone;
- include a `知识节点` or legacy `Graph View 节点` section;
- link canonical concepts, formulas, and methods in context;
- explain important limitations or misconceptions;
- end with a short self-check, collapsible answers, and one-sentence summary.

### Concept

Name: `中文概念 (English Term).md` when both names are established.

Include a concise definition, intuitive explanation, boundaries or common confusion when useful, related nodes, and source lessons. Do not turn every noun into a concept page.

### Formula or law

Name: `中文公式名 (English Name).md` when both names are established.

Include:

- a display MathJax formula;
- symbol definitions and units or dimensions when relevant;
- assumptions, domain, and applicability;
- at least one small worked example close to the formula;
- related concepts, methods, and source lessons.

### Method

Include the problem it solves, when to use it, inputs and outputs, the essential procedure, limitations, one representative example, and related nodes. Put implementation-specific code in `Code/` only when it is independently reusable.

### Extension nodes

- **Theorem:** statement, assumptions, interpretation, consequences, related proof.
- **Proof:** target statement, prerequisites, proof strategy, essential steps, fragile step or common mistake.
- **Classic example:** prompt, reasoning, solution, transferable lesson. Create only when repeated reference justifies a standalone page.

## Links and canonicalization

Before creating a node:

1. Search exact filename and title.
2. Search YAML aliases and normalized Chinese/English names.
3. Inspect plausible candidates in context.
4. Reuse a single clear match and add a missing alias if safe.
5. If two meanings differ, keep both and disambiguate their filenames. If equivalence is uncertain, flag it rather than merging.

Use `[[Canonical title|display text]]`. If a basename is ambiguous, use a path-qualified link such as `[[Concepts/Entropy (Information Theory)|熵]]`.

Do not link ordinary repeated words. Link the first meaningful occurrence in a section and any place where navigation adds real value.

## Non-destructive updates

- Read the entire existing note before editing it.
- Preserve unknown frontmatter and user-added sections.
- Match and update sections by heading only when their purpose is unambiguous.
- Do not remove a note because it is no longer referenced.
- For large or uncertain rewrites, present the intended changes before replacing content.

## Audit contract

Run:

```bash
python3 <skill-dir>/scripts/audit_vault.py <vault-path>
python3 <skill-dir>/scripts/audit_vault.py <vault-path> --json
```

The audit checks note metadata, required note sections, source paths that look file-like, unresolved and ambiguous WikiLinks, duplicate basenames or aliases, orphans, course-map coverage, math delimiter balance, and suspicious missing LaTeX backslashes. It never modifies the vault.

Treat findings as evidence to inspect, not automatic permission to repair. Some orphan, source, and LaTeX warnings can be intentional.
