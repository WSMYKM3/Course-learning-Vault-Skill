---
type: term
course: "Machine Learning and AI with Python"
term_cn: "袋外样本"
term_en: "Out-of-Bag Sample"
tags:
  - term
  - ensemble
  - evaluation
---

# 袋外样本（Out-of-Bag Sample）

袋外样本是指在某次自助采样中没有被抽入对应训练集的原始观测值。对使用该自助样本训练出的模型来说，这些观测值没有参与训练，因此可以用于估计该模型的未见数据表现。

相关概念：[[自助采样 (Bootstrap Sampling)]]、[[自助数据集 (Bootstrap Dataset)]]、[[袋外误差 (Out-of-Bag Error)]]

相关章节：[[3.2 - 袋外误差与相关树]]
