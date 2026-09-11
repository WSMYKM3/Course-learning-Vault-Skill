---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "平方误差减少量公式"
formula_en: "Sum of Squared Error Reduction Formula"
tags:
  - formula
  - regression
  - decision-tree
---

# 平方误差减少量公式（Sum of Squared Error Reduction Formula）

$$
\Delta \text{SSE} = \text{SSE}(R) - \sum_{j=1}^{J}\text{SSE}(R_j)
$$

含义：原区域的平方误差和减去分裂后各子区域平方误差和之和，得到这次分裂带来的回归拟合改进。二叉分裂时，$J=2$。

例子：如果父区域的 $\text{SSE}(R)=20$，分裂后左区域 $\text{SSE}(R_1)=5$、右区域 $\text{SSE}(R_2)=3$，则

$$
\Delta \text{SSE} = 20 - (5+3) = 12
$$

减少量越大，说明这次分裂越能降低回归误差。

相关术语：[[平方误差和 (Sum of Squared Errors)]]、[[回归树 (Regression Tree)]]、[[区域 (Region)]]
