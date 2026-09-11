---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "置换重要性公式"
formula_en: "Permutation Importance Formula"
tags:
  - formula
  - random-forest
  - variable-importance
---

# 置换重要性公式（Permutation Importance Formula）

当评估指标越高越好时：

$$
\operatorname{PI}_j = S - \frac{1}{K}\sum_{k=1}^{K}S_{j,k}^{\text{perm}}
$$

含义：$S$ 是原始验证集或 OOB 表现，$S_{j,k}^{\text{perm}}$ 是第 $k$ 次随机置换特征 $j$ 后的模型表现，$K$ 是重复置换次数。置换后表现下降越多，$\operatorname{PI}_j$ 越大，说明特征越重要。

例子：原始准确率为 $0.86$，打乱某个特征三次后的准确率为 $0.78,0.80,0.79$，平均为 $0.79$，则

$$
\operatorname{PI}_j=0.86-0.79=0.07
$$

相关术语：[[置换重要性 (Permutation Importance)]]、[[变量重要性 (Variable Importance)]]、[[验证集 (Validation Set)]]、[[袋外误差 (Out-of-Bag Error)]]
