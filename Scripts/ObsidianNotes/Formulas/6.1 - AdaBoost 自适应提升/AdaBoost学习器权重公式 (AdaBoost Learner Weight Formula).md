---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "AdaBoost 学习器权重公式"
formula_en: "AdaBoost Learner Weight Formula"
tags:
  - formula
  - boosting
  - adaboost
---

# AdaBoost 学习器权重公式（AdaBoost Learner Weight Formula）

$$
\alpha_t=\frac{1}{2}\ln\left(\frac{1-\varepsilon_t}{\varepsilon_t}\right)
$$

含义：$\varepsilon_t$ 是第 $t$ 个弱学习器的加权错误率，$\alpha_t$ 是它在最终分类器中的投票权。错误率越低，投票权越高。

例子：若 $\varepsilon_t=0.2$，则：

$$
\alpha_t=\frac{1}{2}\ln\left(\frac{0.8}{0.2}\right)
=\frac{1}{2}\ln(4)
\approx0.693
$$

若 $\varepsilon_t=0.5$，则 $\alpha_t=0$，说明这个学习器与随机猜测相当，对最终预测没有贡献。

相关术语：[[学习器权重 (Learner Weight)]]、[[加权错误率 (Weighted Error Rate)]]、[[AdaBoost (Adaptive Boosting)]]

相关章节：[[6.1 - AdaBoost 自适应提升]]
