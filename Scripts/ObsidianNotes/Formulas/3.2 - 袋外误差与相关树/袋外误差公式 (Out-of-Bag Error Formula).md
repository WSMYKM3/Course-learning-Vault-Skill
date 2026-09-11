---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "袋外误差公式"
formula_en: "Out-of-Bag Error Formula"
tags:
  - formula
  - ensemble
  - evaluation
---

# 袋外误差公式（Out-of-Bag Error Formula）

分类任务中：

$$
\text{OOB Error}=\frac{1}{n}\sum_{i=1}^{n}\mathbb{1}\left(\hat{y}^{\text{OOB}}_i \ne y_i\right)
$$

回归任务中：

$$
\text{OOB Error}=\frac{1}{n}\sum_{i=1}^{n}\left(y_i-\hat{y}^{\text{OOB}}_i\right)^2
$$

含义：$n$ 是训练样本数量，$\hat{y}^{\text{OOB}}_i$ 是第 $i$ 个样本的袋外预测，$y_i$ 是真实值。分类时统计预测错误比例，回归时统计平均平方误差。

例子：分类任务中 5 个样本的逐点袋外预测错了 1 个，则 OOB Error 为 $1/5=0.2$。回归任务中 3 个样本的平方误差为 $1,4,0$，则 OOB Error 为 $(1+4+0)/3=5/3$。

相关术语：[[袋外误差 (Out-of-Bag Error)]]、[[逐点袋外误差 (Pointwise Out-of-Bag Error)]]、[[分类任务 (Classification Task)]]、[[回归任务 (Regression Task)]]
