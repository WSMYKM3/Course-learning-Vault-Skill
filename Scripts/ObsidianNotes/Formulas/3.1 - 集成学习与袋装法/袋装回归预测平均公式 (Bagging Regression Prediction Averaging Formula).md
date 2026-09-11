---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "袋装回归预测平均公式"
formula_en: "Bagging Regression Prediction Averaging Formula"
tags:
  - formula
  - regression
  - ensemble
---

# 袋装回归预测平均公式（Bagging Regression Prediction Averaging Formula）

$$
\hat{y} = \frac{1}{B}\sum_{b=1}^{B}\hat{y}_b
$$

含义：$B$ 表示基模型数量，$\hat{y}_b$ 表示第 $b$ 个基模型对同一个输入样本的数值预测。回归袋装模型把所有基模型的预测值取平均作为最终预测。

例子：如果 4 棵回归树对同一个样本的预测分别是 $8.0, 9.5, 7.5, 9.0$，则

$$
\hat{y}=\frac{8.0+9.5+7.5+9.0}{4}=8.5
$$

预测平均可以削弱单个模型的锯齿状波动，使整体预测更平滑。

相关术语：[[袋装法 (Bagging)]]、[[预测平均 (Prediction Averaging)]]、[[回归任务 (Regression Task)]]、[[基模型 (Base Model)]]

相关章节：[[3.1 - 集成学习与袋装法]]
