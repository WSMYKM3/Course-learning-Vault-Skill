#!/usr/bin/env python3
"""Behavior tests for audit_vault.py."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from audit_vault import audit


class AuditVaultTests(unittest.TestCase):
    def write(self, root: Path, relative: str, content: str) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_valid_small_vault(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(
                root,
                "00 - Course Map.md",
                """---
type: course-map
course_id: demo
course: Demo
output_language: zh-CN
lesson_dir: Lessons
concept_dir: Concepts
formula_dir: Formulas
---
# Demo

课程：[[Lessons/1 - Motion]]
""",
            )
            self.write(
                root,
                "Lessons/1 - Motion.md",
                """---
type: lesson
course: Demo
chapter: 1
topic: Motion
source: lecture.txt
---
# Motion
## 知识节点
[[Concepts/Velocity]]
## 学习目标
Understand velocity.
## 复习检查
Why?
## 一句话总结
Motion changes position.
""",
            )
            self.write(
                root,
                "Concepts/Velocity.md",
                """---
type: concept
course: Demo
aliases:
  - 速度
---
# Velocity
Related lesson: [[Lessons/1 - Motion]]
""",
            )
            (root / "lecture.txt").write_text("source", encoding="utf-8")
            report = audit(root)
            self.assertEqual(report["summary"]["error"], 0)

    def test_detects_links_duplicates_and_latex(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "A/Entropy.md", "---\ntype: concept\ncourse: Demo\n---\n# Entropy\n")
            self.write(root, "B/Entropy.md", "---\ntype: concept\ncourse: Demo\n---\n# Entropy\n")
            self.write(
                root,
                "Formula.md",
                """---
type: formula
course: Demo
---
# Formula
$$
r=-left.x
$$
例子：1。
[[Missing Node]]
""",
            )
            report = audit(root)
            codes = {issue["code"] for issue in report["issues"]}
            self.assertIn("duplicate-basename", codes)
            self.assertIn("unresolved-link", codes)
            self.assertIn("latex-backslash", codes)

    def test_detects_missing_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "Loose.md", "# Loose\n")
            report = audit(root)
            self.assertIn("missing-frontmatter", {issue["code"] for issue in report["issues"]})

    def test_ignores_double_brackets_inside_code(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(
                root,
                "Code.md",
                """---
type: code-reference
course: Demo
---
# Code
`df[['inline']]`
```python
df[['fenced']]
```
""",
            )
            report = audit(root)
            self.assertNotIn("unresolved-link", {issue["code"] for issue in report["issues"]})


if __name__ == "__main__":
    unittest.main()
