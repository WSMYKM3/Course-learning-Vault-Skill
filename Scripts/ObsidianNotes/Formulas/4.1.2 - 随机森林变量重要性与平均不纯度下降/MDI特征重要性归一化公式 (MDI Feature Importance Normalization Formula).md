---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "MDI特征重要性归一化公式"
formula_en: "MDI Feature Importance Normalization Formula"
tags:
  - formula
  - random-forest
  - variable-importance
---

# MDI特征重要性归一化公式（MDI Feature Importance Normalization Formula）

单棵树内归一化：

$$
\operatorname{FI}_{j,T}^{\text{norm}}=
\frac{\operatorname{FI}_{j,T}}{\sum_{k=1}^{p}\operatorname{FI}_{k,T}}
$$

随机森林层面平均：

$$
\operatorname{FI}_{j}^{\text{forest}}=
\frac{1}{B}\sum_{b=1}^{B}\operatorname{FI}_{j,T_b}^{\text{norm}}
$$

含义：$\operatorname{FI}_{j,T}$ 是特征 $j$ 在单棵树 $T$ 中所有节点 MDI 贡献的总和，$p$ 是特征数量，$B$ 是森林中的树数量。先把单棵树内所有特征贡献归一化，再对森林中的树取平均。

例子：某棵树中三个特征的未归一化重要性分别为 $0.2,0.1,0.7$，总和为 $1.0$，因此归一化后仍为 $0.2,0.1,0.7$。如果另一棵树中特征 $1$ 的归一化重要性是 $0.4$，两棵树中特征 $1$ 的森林平均重要性为 $(0.2+0.4)/2=0.3$。

相关术语：[[平均不纯度下降 (Mean Decrease in Impurity)]]、[[变量重要性 (Variable Importance)]]、[[随机森林 (Random Forest)]]
