---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "袋外预测公式"
formula_en: "Out-of-Bag Prediction Formula"
tags:
  - formula
  - ensemble
  - evaluation
---

# 袋外预测公式（Out-of-Bag Prediction Formula）

令 $\mathcal{B}_i=\{b: i \notin S_b\}$ 表示训练时没有包含第 $i$ 个观测值的树集合。分类任务中：

$$
\hat{y}^{\text{OOB}}_i=\operatorname{mode}\{\hat{y}_{ib}: b \in \mathcal{B}_i\}
$$

回归任务中：

$$
\hat{y}^{\text{OOB}}_i=\frac{1}{|\mathcal{B}_i|}\sum_{b\in\mathcal{B}_i}\hat{y}_{ib}
$$

含义：$S_b$ 是第 $b$ 棵树的自助训练样本，$\hat{y}_{ib}$ 是第 $b$ 棵树对第 $i$ 个观测值的预测。袋外预测只使用没有见过该观测值的树。

例子：某个分类样本没有进入第 1、3、5 棵树的训练集，这三棵树分别预测 `阳性, 阴性, 阳性`，则袋外预测为阳性。某个回归样本的袋外树预测为 $6,8,7$，则袋外预测为 $(6+8+7)/3=7$。

相关术语：[[袋外样本 (Out-of-Bag Sample)]]、[[逐点袋外预测 (Pointwise Out-of-Bag Prediction)]]、[[多数投票 (Majority Vote)]]、[[预测平均 (Prediction Averaging)]]
