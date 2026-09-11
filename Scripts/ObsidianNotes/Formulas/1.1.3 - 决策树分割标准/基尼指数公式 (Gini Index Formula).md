---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "基尼指数公式"
formula_en: "Gini Index Formula"
tags:
  - formula
  - decision-tree
---

# 基尼指数公式（Gini Index Formula）

$$
G(R_m) = 1 - \sum_{k=1}^{K} p_{mk}^2
$$

含义：$p_{mk}$ 表示区域 $R_m$ 中第 $k$ 类样本所占比例。类别比例越集中，平方和越大，基尼指数越低；类别越混合，基尼指数越高。

例子：如果一个区域中正类比例为 $0.75$、负类比例为 $0.25$，则

$$
G(R_m) = 1 - (0.75^2 + 0.25^2) = 1 - 0.625 = 0.375
$$

如果所有样本都属于同一类，基尼指数就是 $0$。

相关术语：[[基尼指数 (Gini Index)]]、[[不纯度 (Impurity)]]

相关章节：[[1.1.3 - 决策树分割标准]]
