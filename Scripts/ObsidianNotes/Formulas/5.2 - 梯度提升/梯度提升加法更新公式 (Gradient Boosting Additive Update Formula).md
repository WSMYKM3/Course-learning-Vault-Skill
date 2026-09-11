---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "梯度提升加法更新公式"
formula_en: "Gradient Boosting Additive Update Formula"
tags:
  - formula
  - boosting
  - gradient-boosting
---

# 梯度提升加法更新公式（Gradient Boosting Additive Update Formula）

$$
F_m(x)=F_{m-1}(x)+\lambda h_m(x)
$$

含义：$F_{m-1}$ 是加入本轮弱学习器之前的整体模型，$h_m$ 是本轮用来近似负梯度或残差的弱学习器，$\lambda$ 是学习率，$F_m$ 是更新后的整体模型。

例子：旧模型对某样本预测 $6$，新树预测该样本需要修正 $2$，学习率为 $0.25$，则：

$$
F_m(x)=6+0.25(2)=6.5
$$

新树虽然建议修正 $2$，本轮实际只加入 $0.5$，使学习过程更保守。

相关术语：[[梯度提升 (Gradient Boosting)]]、[[加法模型 (Additive Model)]]、[[学习率 (Learning Rate)]]、[[弱学习器 (Weak Learner)]]

相关章节：[[5.2 - 梯度提升]]、[[5.3 - 梯度提升为何有效]]
