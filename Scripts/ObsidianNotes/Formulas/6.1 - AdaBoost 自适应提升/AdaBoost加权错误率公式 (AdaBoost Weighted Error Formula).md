---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "AdaBoost 加权错误率公式"
formula_en: "AdaBoost Weighted Error Formula"
tags:
  - formula
  - boosting
  - adaboost
---

# AdaBoost 加权错误率公式（AdaBoost Weighted Error Formula）

$$
\varepsilon_t=\sum_{i=1}^{n} w_i^{(t)}\,\mathbf{1}\!\left(y_i\neq h_t(x_i)\right)
$$

含义：$w_i^{(t)}$ 是第 $t$ 轮中样本 $i$ 的权重，$h_t(x_i)$ 是弱学习器的预测。指示函数在预测错误时为 $1$，正确时为 $0$，所以 $\varepsilon_t$ 就是所有错分样本的当前权重之和。

例子：4 个样本的权重为 $0.1,0.2,0.3,0.4$。若第 2、4 个样本被错分，则：

$$
\varepsilon_t=0.2+0.4=0.6
$$

这说明该学习器在当前权重分布下比随机猜测还差，不能把“错了 2 个，共 4 个”直接当作 $0.5$，因为样本并不等权。

相关术语：[[加权错误率 (Weighted Error Rate)]]、[[样本权重 (Sample Weight)]]、[[弱学习器 (Weak Learner)]]

相关章节：[[6.1 - AdaBoost 自适应提升]]
