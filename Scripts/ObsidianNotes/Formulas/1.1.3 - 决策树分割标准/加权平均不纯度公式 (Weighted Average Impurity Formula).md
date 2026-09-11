---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "加权平均不纯度公式"
formula_en: "Weighted Average Impurity Formula"
tags:
  - formula
  - decision-tree
---

# 加权平均不纯度公式（Weighted Average Impurity Formula）

$$
I_{\text{split}} = \sum_{j=1}^{J}\frac{n_j}{n}I(R_j)
$$

含义：$I(R_j)$ 是第 $j$ 个子区域的不纯度，$n_j/n$ 是该子区域在所有样本中的比例。一次分割产生多个区域时，按每个区域的样本数量加权汇总不纯度，用来评价整体分割质量。二叉分裂时，$J=2$。

例子：如果一个二叉分裂产生两个子区域，左侧有 $8$ 个样本、基尼指数 $0.375$，右侧有 $4$ 个样本、基尼指数 $0$，则

$$
I_{\text{split}} = \frac{8}{12}\times 0.375 + \frac{4}{12}\times 0 = 0.25
$$

这个值会和其他候选分裂的加权平均不纯度比较，越低通常越好。

相关术语：[[加权平均不纯度 (Weighted Average Impurity)]]、[[不纯度 (Impurity)]]、[[区域 (Region)]]

相关章节：[[1.1.3 - 决策树分割标准]]
