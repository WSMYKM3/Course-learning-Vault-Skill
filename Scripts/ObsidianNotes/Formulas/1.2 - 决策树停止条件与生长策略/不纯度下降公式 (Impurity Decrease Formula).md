---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "不纯度下降公式"
formula_en: "Impurity Decrease Formula"
tags:
  - formula
  - decision-tree
---

# 不纯度下降公式（Impurity Decrease Formula）

$$
\Delta I = I(R) - \sum_{j=1}^{J}\frac{n_j}{n}I(R_j)
$$

含义：$I(R)$ 是父区域的不纯度，$R_j$ 是分裂后的第 $j$ 个子区域，$n_j/n$ 是该子区域的样本权重。原区域的不纯度减去分裂后子区域的加权平均不纯度，得到这次分割带来的纯度提升。

例子：如果父区域基尼指数为 $0.48$，分裂成两个子区域，样本数分别为 $6$ 和 $4$，两个子区域基尼指数分别为 $0.20$ 和 $0.30$，则

$$
\Delta I = 0.48 - \left(\frac{6}{10}\times 0.20 + \frac{4}{10}\times 0.30\right)
= 0.48 - 0.24 = 0.24
$$

不纯度下降越大，说明这次分裂越有效。

相关术语：[[不纯度下降 (Impurity Decrease)]]、[[加权平均不纯度 (Weighted Average Impurity)]]、[[区域 (Region)]]
