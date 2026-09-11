---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "AdaBoost 最终分类器公式"
formula_en: "AdaBoost Final Classifier Formula"
tags:
  - formula
  - boosting
  - adaboost
---

# AdaBoost 最终分类器公式（AdaBoost Final Classifier Formula）

$$
H(x)=\operatorname{sign}\left(\sum_{t=1}^{T}\alpha_t h_t(x)\right)
$$

含义：$h_t(x)\in\{-1,+1\}$ 是第 $t$ 个弱学习器的预测，$\alpha_t$ 是它的投票权。所有加权预测相加后，正号预测 $+1$，负号预测 $-1$。

例子：三个弱学习器的预测为 $+1,-1,+1$，对应权重为 $0.8,0.3,0.2$：

$$
H(x)=\operatorname{sign}\left(0.8-0.3+0.2\right)
=\operatorname{sign}(0.7)=+1
$$

这不是普通多数投票；每个学习器的票数会根据其可靠程度加权。

相关术语：[[AdaBoost (Adaptive Boosting)]]、[[弱学习器 (Weak Learner)]]、[[学习器权重 (Learner Weight)]]

相关章节：[[6.1 - AdaBoost 自适应提升]]
