---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "平均不纯度下降公式"
formula_en: "Mean Decrease in Impurity Formula"
tags:
  - formula
  - random-forest
  - variable-importance
---

# 平均不纯度下降公式（Mean Decrease in Impurity Formula）

$$
\operatorname{MDI}(t)=\frac{N_t}{N}\left(I(t)-\frac{N_L}{N_t}I(t_L)-\frac{N_R}{N_t}I(t_R)\right)
$$

含义：$t$ 是父节点，$t_L$ 和 $t_R$ 是左右子节点，$N$ 是整棵树训练样本数，$N_t$ 是父节点样本数，$N_L,N_R$ 是左右子节点样本数，$I(\cdot)$ 是节点不纯度。括号内是不纯度下降，$\frac{N_t}{N}$ 让覆盖更多样本的节点贡献更大。

例子：父节点有 $N_t=100$ 个样本，整棵树有 $N=200$ 个样本，父节点基尼指数为 $0.50$。左右子节点各有 $50$ 个样本，基尼指数分别为 $0.20$ 和 $0.30$，则

$$
\operatorname{MDI}(t)=\frac{100}{200}\left(0.50-\frac{50}{100}\times0.20-\frac{50}{100}\times0.30\right)
=0.5\times0.25=0.125
$$

相关术语：[[平均不纯度下降 (Mean Decrease in Impurity)]]、[[不纯度 (Impurity)]]、[[基尼指数 (Gini Index)]]、[[变量重要性 (Variable Importance)]]
