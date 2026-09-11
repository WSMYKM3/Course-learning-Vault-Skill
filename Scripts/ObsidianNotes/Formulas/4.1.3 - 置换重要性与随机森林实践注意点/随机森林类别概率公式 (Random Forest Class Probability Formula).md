---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "随机森林类别概率公式"
formula_en: "Random Forest Class Probability Formula"
tags:
  - formula
  - random-forest
  - classification
---

# 随机森林类别概率公式（Random Forest Class Probability Formula）

$$
\hat{P}(Y=c\mid x)=\frac{1}{B}\sum_{b=1}^{B}\hat{P}_b(Y=c\mid x)
$$

含义：$B$ 是森林中的树数量，$\hat{P}_b(Y=c\mid x)$ 是第 $b$ 棵树对样本 $x$ 属于类别 $c$ 的概率估计。随机森林可以把各树的类别概率取平均，得到整体类别概率估计。

例子：三棵树对类别“阳性”的概率估计分别为 $0.8,0.6,1.0$，则随机森林给出的类别概率估计为

$$
\hat{P}(Y=\text{阳性}\mid x)=\frac{0.8+0.6+1.0}{3}=0.8
$$

相关术语：[[类别概率 (Class Probability)]]、[[随机森林 (Random Forest)]]、[[分类任务 (Classification Task)]]
