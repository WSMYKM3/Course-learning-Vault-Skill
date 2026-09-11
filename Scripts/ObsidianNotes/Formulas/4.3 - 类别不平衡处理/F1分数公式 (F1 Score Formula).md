---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "F1分数公式"
formula_en: "F1 Score Formula"
tags:
  - formula
  - evaluation
  - classification
---

# F1分数公式（F1 Score Formula）

$$
F_1=2\cdot\frac{\operatorname{Precision}\cdot\operatorname{Recall}}{\operatorname{Precision}+\operatorname{Recall}}
$$

含义：F1 分数是[[精确率 (Precision)|精确率]]和[[真正率 (True Positive Rate)|召回率]]的调和平均。它适合用于正类识别重要、类别不平衡明显的分类任务。

例子：如果精确率为 $0.75$，召回率为 $0.60$，则

$$
F_1=2\cdot\frac{0.75\times0.60}{0.75+0.60}
=\frac{0.90}{1.35}\approx0.67
$$

组成公式：[[精确率公式 (Precision Formula)]]、[[真正率公式 (True Positive Rate Formula)]]

相关术语：[[F1分数 (F1 Score)]]、[[精确率 (Precision)]]、[[真正率 (True Positive Rate)|召回率]]、[[类别不平衡 (Class Imbalance)]]
