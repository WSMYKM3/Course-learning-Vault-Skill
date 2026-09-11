---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "均方误差公式"
formula_en: "Mean Squared Error Formula"
tags:
  - formula
  - regression
---

# 均方误差公式（Mean Squared Error Formula）

$$
\text{MSE}(R_m) = \frac{1}{n_m}\sum_{i:x_i \in R_m}(y_i - \bar{y}_m)^2
$$

含义：$n_m$ 是区域 $R_m$ 中的样本数，$\bar{y}_m$ 是该区域的响应变量均值。MSE 把区域内每个样本相对叶节点预测值的误差平方后求平均，数值越小表示回归预测越接近真实值。

例子：如果某个区域的真实值是 $2,4,6$，区域均值为 $\bar{y}_m=4$，则

$$
\text{MSE}(R_m) = \frac{(2-4)^2 + (4-4)^2 + (6-4)^2}{3} = \frac{8}{3}
$$

相关术语：[[均方误差 (Mean Squared Error)]]、[[响应变量 (Response Variable)]]
