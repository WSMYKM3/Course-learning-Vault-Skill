# Checkpoint Reviews and Quizzes

Read this reference for cross-lesson summaries, comprehensive quizzes, targeted review, and lightweight progress updates.

## Checkpoint review

Create a checkpoint only when the user requests one or the source has a clear completed module boundary. Synthesize from the included lesson and canonical nodes; consult raw sources only to resolve a real gap.

A useful checkpoint contains:

- the module's central question and mental model;
- a dependency path showing how major ideas build on one another;
- concise comparisons among easily confused concepts or methods;
- a formula/law map with purpose and applicability, not a bare formula dump;
- representative reasoning patterns or problem-solving procedures;
- common mistakes and a compact one-page review section;
- links to every included lesson and the most important canonical nodes.

Do not repeat whole lesson notes or create duplicate atomic pages. Record the covered lessons in frontmatter and in the body.

## Comprehensive quiz

Infer a balanced assessment from the discipline and stated learning goals. Use only question types that measure relevant understanding:

- retrieval and definition;
- explanation and causal reasoning;
- comparison or boundary cases;
- calculation and unit handling;
- derivation or proof steps;
- interpretation of graphs, data, code, or experimental results;
- transfer to a new scenario.

If the user does not specify quantity or difficulty, create a moderate quiz that covers the scope without mechanically assigning one question per note. Weight central ideas and known weak areas more heavily.

Use this answer form:

```markdown
### 1. Question

> [!success]- 参考答案
> Give the result, essential reasoning, and links such as [[Canonical concept]].
```

For a user who wants to attempt the quiz interactively, withhold the answer section until they respond. Otherwise keep answers collapsed in the note. Never hide required data only inside the answer.

## Targeted review and progress

When the user reports missed questions or confusion:

- explain the misconception using the smallest relevant set of nodes;
- generate focused follow-up questions rather than another broad quiz;
- add the topic to `待复习` and update the related lesson to `待复习` only if the user wants progress recorded;
- mark `已掌握` only after explicit user confirmation, never from note generation or a single correct response.

Progress is intentionally lightweight. Do not create spaced-repetition dates, review algorithms, Anki exports, or plugin-specific fields unless the user expands the scope.
