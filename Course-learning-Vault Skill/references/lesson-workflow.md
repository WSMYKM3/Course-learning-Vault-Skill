# Lesson Workflow

Read this reference when converting one or more text-based lessons into Obsidian notes.

## 1. Establish the lesson boundary

- Identify the exact source file or pasted range, course, chapter, and target vault.
- Read adjacent lesson titles or the course map only to establish prerequisites and sequence.
- Do not invent a future-lesson link from an assumed syllabus.
- If multiple transcripts overlap, decide which is primary and record all material sources used.

## 2. Reconstruct the teaching argument

Clean subtitle and speech artifacts without flattening the lesson:

- remove timestamps, non-semantic sound cues, repeated fragments, and empty speaker labels;
- join line-broken sentences and repair obvious transcription substitutions;
- retain examples, caveats, instructor contrasts, and the order required to understand a derivation;
- distinguish a genuine correction from stylistic rewriting.

Create a compact internal outline before writing: learning goals, prerequisite ideas, central question, reasoning sequence, examples, formulas or procedures, limitations, and likely misconceptions.

## 3. Select atomic nodes

Create a standalone node when it is a core course idea, reusable across lessons, likely to be tested, independently searchable, or valuable as a graph junction. Prefer a few strong nodes over exhaustive noun extraction.

Choose the type by learning function:

- **concept:** definition or mental model;
- **formula/law:** symbolic relation whose meaning and use should be recalled independently;
- **method:** repeatable problem-solving or analysis procedure;
- **theorem/proof:** only when statement or reasoning deserves separate study;
- **code/classic example:** only when repeatedly reusable.

Run the canonicalization process in `vault-schema.md` before creating any node.

## 4. Write the lesson

Use this adaptable shape rather than forcing irrelevant headings:

```markdown
# 1.2 中文主题（English Topic）

## 知识节点

核心概念：...
核心公式：...
前置内容：...

## 学习目标

...

## 核心内容

Organized explanation, derivation, examples, comparisons, and limitations.

## 常见误区

Only when the source or subject gives meaningful pitfalls.

## 复习检查

1. Question...

> [!success]- 参考答案
> Answer with the necessary reasoning and links.

## 一句话总结

...
```

Place links inside the explanation as well as in the navigation section. A node list alone does not make a useful knowledge graph.

## 5. Handle mathematics and science precisely

- Use `$...$` for inline math and `$$...$$` for display math.
- Check every command backslash, delimiter, subscript, superscript, sign, and evaluation bar.
- Define symbols near first use and state assumptions or valid domains.
- Preserve units and dimensional consistency when applicable.
- A formula page needs a worked numerical or symbolic example. Use small values that reveal how the formula works.
- If the transcript only implies a standard formula, verify it before adding it and label it as a verified supplement when it was not actually stated in the lesson.

## 6. Build the self-check

Generate a short set proportional to the lesson. Cover the most important learning goals with a subject-appropriate mix of recall, explanation, comparison, calculation, derivation, prediction, or application. Do not force every type into every lesson.

Put each answer in a collapsed standard Obsidian callout. Answers should be sufficient to diagnose understanding: include causality for “why” questions, calculation steps where the step matters, and links back to the relevant nodes.

## 7. Integrate and verify

- Add or update the lesson entry in the course map without changing mastery state.
- Add reciprocal source-lesson links to newly created atomic nodes.
- Link only verified prerequisite or neighboring lessons.
- Re-read rendered Markdown structure and run the audit script.
- If the source has not changed and the requested outputs already exist, report that rather than duplicating them.
