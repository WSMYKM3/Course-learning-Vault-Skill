---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "均方误差减少量公式"
formula_en: "Mean Squared Error Reduction Formula"
tags:
  - formula
  - regression
  - decision-tree
---

# 均方误差减少量公式（Mean Squared Error Reduction Formula）

$$
\operatorname{Gain}(R)=\Delta(R)=\operatorname{MSE}(R)-\frac{N_1}{N}\operatorname{MSE}(R_1)-\frac{N_2}{N}\operatorname{MSE}(R_2)
$$

含义：在回归树中，可以把分类树中的不纯度下降替换为均方误差减少量。$R$ 是父区域，$R_1$ 和 $R_2$ 是分裂后的两个子区域，$N$ 是父区域样本数，$N_1$ 和 $N_2$ 是两个子区域样本数。增益越大，说明这次分裂越能降低预测误差。

例子：假设父区域 $R$ 有 6 个响应值：$2,4,6,8,10,12$，其均值为 $7$，所以

$$
\operatorname{MSE}(R)=\frac{(2-7)^2+(4-7)^2+(6-7)^2+(8-7)^2+(10-7)^2+(12-7)^2}{6}=\frac{35}{3}
$$

如果分裂成 $R_1=\{2,4,6\}$ 和 $R_2=\{8,10,12\}$，两个子区域的均方误差都是 $\frac{8}{3}$，且 $N_1=N_2=3$，则

$$
\operatorname{Gain}(R)=\frac{35}{3}-\frac{3}{6}\times\frac{8}{3}-\frac{3}{6}\times\frac{8}{3}=9
$$

如果预设阈值是 $5$，因为 $9>5$，这次分裂值得保留；如果增益低于阈值，就可以停止继续分裂。

相关术语：[[均方误差 (Mean Squared Error)]]、[[回归树 (Regression Tree)]]、[[区域 (Region)]]、[[阈值 (Threshold)]]

相关章节：[[2.1 - 回归树与类别特征编码]]
