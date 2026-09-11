---
type: term
course: "Machine Learning and AI with Python"
term_cn: "置换重要性"
term_en: "Permutation Importance"
tags:
  - term
  - random-forest
  - variable-importance
---

# 置换重要性（Permutation Importance）

置换重要性通过随机打乱某个预测变量的取值，并观察模型在验证集或袋外样本上的表现下降多少来衡量该变量的重要性。表现下降越多，说明模型越依赖该变量。

公式：[[置换重要性公式 (Permutation Importance Formula)]]

相关概念：[[变量重要性 (Variable Importance)]]、[[验证集 (Validation Set)]]、[[袋外误差 (Out-of-Bag Error)]]

相关章节：[[4.1.2 - 随机森林变量重要性与平均不纯度下降]]、[[4.1.3 - 置换重要性与随机森林实践注意点]]
