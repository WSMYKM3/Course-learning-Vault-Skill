---
type: term
course: "Machine Learning and AI with Python"
term_cn: "数据泄漏"
term_en: "Data Leakage"
tags:
  - term
  - evaluation
---

# 数据泄漏（Data Leakage）

数据泄漏是指模型训练过程意外使用了本应只在评估阶段出现的信息，导致评估结果过于乐观。在袋外误差中，每个训练点只由没有见过它的树预测，因此可以降低这类泄漏风险。

相关概念：[[验证集 (Validation Set)]]、[[交叉验证 (Cross-Validation)]]、[[袋外误差 (Out-of-Bag Error)]]

相关章节：[[3.2 - 袋外误差与相关树]]
