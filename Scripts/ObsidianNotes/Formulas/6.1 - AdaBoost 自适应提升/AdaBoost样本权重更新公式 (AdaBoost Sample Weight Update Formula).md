---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "AdaBoost 样本权重更新公式"
formula_en: "AdaBoost Sample Weight Update Formula"
tags:
  - formula
  - boosting
  - adaboost
---

# AdaBoost 样本权重更新公式（AdaBoost Sample Weight Update Formula）

$$
w_i^{(t+1)}=
\frac{w_i^{(t)}\exp\!\left(-\alpha_t y_i h_t(x_i)\right)}{Z_t}
$$

含义：$w_i^{(t)}$ 是旧样本权重，$\alpha_t$ 是当前学习器权重，$y_i$ 是真实标签，$h_t(x_i)$ 是预测，$Z_t$ 负责归一化。正确分类时权重乘以 $e^{-\alpha_t}$，错误分类时乘以 $e^{+\alpha_t}$。

例子：某样本原权重为 $0.2$，且 $\alpha_t=0.693$。若预测正确，其未归一化新权重为：

$$
0.2e^{-0.693}\approx0.2(0.5)=0.1
$$

若预测错误，其未归一化新权重为：

$$
0.2e^{0.693}\approx0.2(2)=0.4
$$

归一化前，错误样本的新权重是正确样本的 4 倍；最后还要把所有样本权重同时除以 $Z_t$，使总和为 $1$。

相关术语：[[样本权重 (Sample Weight)]]、[[学习器权重 (Learner Weight)]]、[[AdaBoost (Adaptive Boosting)]]

相关章节：[[6.1 - AdaBoost 自适应提升]]
