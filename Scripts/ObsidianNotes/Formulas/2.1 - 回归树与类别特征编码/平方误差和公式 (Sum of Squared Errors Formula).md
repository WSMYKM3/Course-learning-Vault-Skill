---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "平方误差和公式"
formula_en: "Sum of Squared Errors Formula"
tags:
  - formula
  - regression
---

# 平方误差和公式（Sum of Squared Errors Formula）

$$
\text{SSE}(R_m) = \sum_{i:x_i \in R_m}(y_i - \bar{y}_m)^2
$$

含义：$\bar{y}_m$ 是区域 $R_m$ 中响应变量的平均值，也是回归树在该叶节点的预测值。SSE 把区域内每个样本相对叶节点预测值的误差平方后直接求和。分裂比较时，SSE 比只看均值误差更自然地体现了区域样本数的影响。

例子：如果某个区域的真实值是 $2,4,6$，区域均值为 $\bar{y}_m=4$，则

$$
\text{SSE}(R_m) = (2-4)^2 + (4-4)^2 + (6-4)^2 = 8
$$

相关术语：[[平方误差和 (Sum of Squared Errors)]]、[[均方误差 (Mean Squared Error)]]
