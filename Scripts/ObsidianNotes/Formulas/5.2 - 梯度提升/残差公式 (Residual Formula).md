---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "残差公式"
formula_en: "Residual Formula"
tags:
  - formula
  - regression
  - boosting
---

# 残差公式（Residual Formula）

$$
r_i=y_i-\hat y_i=y_i-F(x_i)
$$

含义：$y_i$ 是样本 $i$ 的真实响应值，$\hat y_i=F(x_i)$ 是模型预测，$r_i$ 是残差。正残差表示模型预测太低，负残差表示预测太高。

例子：真实值为 $8$，当前模型预测 $6.5$，则：

$$
r=8-6.5=1.5
$$

梯度提升的下一棵树会尝试给这个样本提供正方向修正。

相关术语：[[残差 (Residual)]]、[[梯度提升 (Gradient Boosting)]]、[[响应变量 (Response Variable)]]

相关章节：[[5.2 - 梯度提升]]、[[5.3 - 梯度提升为何有效]]
