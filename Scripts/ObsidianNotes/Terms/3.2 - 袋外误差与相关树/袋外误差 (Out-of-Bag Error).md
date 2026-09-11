---
type: term
course: "Machine Learning and AI with Python"
term_cn: "袋外误差"
term_en: "Out-of-Bag Error"
tags:
  - term
  - ensemble
  - evaluation
---

# 袋外误差（Out-of-Bag Error）

袋外误差是用未被某个自助数据集抽中的样本来评估对应基模型预测表现的方法。因为每次自助采样都会遗漏一部分原始样本，这些遗漏样本可以作为近似验证集，用来估计袋装模型的泛化误差。

公式：[[袋外预测公式 (Out-of-Bag Prediction Formula)]]、[[袋外误差公式 (Out-of-Bag Error Formula)]]

相关概念：[[袋装法 (Bagging)]]、[[自助数据集 (Bootstrap Dataset)]]、[[袋外样本 (Out-of-Bag Sample)]]、[[交叉验证 (Cross-Validation)]]

相关章节：[[3.1 - 集成学习与袋装法]]、[[3.2 - 袋外误差与相关树]]、[[4.1.1 - 随机森林]]
