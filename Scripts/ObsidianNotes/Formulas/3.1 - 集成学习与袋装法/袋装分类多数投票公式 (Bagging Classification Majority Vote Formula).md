---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "袋装分类多数投票公式"
formula_en: "Bagging Classification Majority Vote Formula"
tags:
  - formula
  - classification
  - ensemble
---

# 袋装分类多数投票公式（Bagging Classification Majority Vote Formula）

$$
\hat{y} = \operatorname{mode}\{\hat{y}_1,\hat{y}_2,\dots,\hat{y}_B\}
$$

含义：$B$ 表示基模型数量，$\hat{y}_b$ 表示第 $b$ 个基模型的类别预测。分类袋装模型把所有基模型的预测做多数投票，票数最多的类别就是最终预测。

例子：如果 5 棵树对同一个 MRI 扫描的预测分别是 `阳性, 阳性, 阴性, 阳性, 阴性`，则阳性有 3 票、阴性有 2 票，所以

$$
\hat{y}=\operatorname{mode}\{\text{阳性},\text{阳性},\text{阴性},\text{阳性},\text{阴性}\}=\text{阳性}
$$

相关术语：[[袋装法 (Bagging)]]、[[多数投票 (Majority Vote)]]、[[分类任务 (Classification Task)]]、[[基模型 (Base Model)]]

相关章节：[[3.1 - 集成学习与袋装法]]
