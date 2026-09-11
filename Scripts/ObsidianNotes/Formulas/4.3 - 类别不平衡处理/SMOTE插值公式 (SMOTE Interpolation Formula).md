---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "SMOTE插值公式"
formula_en: "SMOTE Interpolation Formula"
tags:
  - formula
  - imbalanced-data
  - sampling
---

# SMOTE插值公式（SMOTE Interpolation Formula）

$$
\mathbf{x}_{\text{new}}
=\mathbf{x}_i+\lambda\left(\mathbf{x}_{nn}-\mathbf{x}_i\right),
\qquad \lambda\in[0,1]
$$

含义：$\mathbf{x}_i$ 是一个少数类样本，$\mathbf{x}_{nn}$ 是它的一个少数类近邻，$\lambda$ 是区间 $[0,1]$ 内的随机值。新样本位于两者之间，因此 SMOTE 生成的是合成样本，而不是简单复制原样本。

例子：在单特征情形下，若 $x_i=2$、$x_{nn}=6$、$\lambda=0.25$，则

$$
x_{\text{new}}=2+0.25(6-2)=3
$$

相关术语：[[SMOTE (SMOTE)]]、[[过采样 (Oversampling)]]、[[少数类 (Minority Class)]]、[[数值特征 (Numerical Feature)]]
