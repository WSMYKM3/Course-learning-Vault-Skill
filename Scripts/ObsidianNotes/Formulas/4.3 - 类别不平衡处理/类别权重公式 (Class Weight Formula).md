---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "类别权重公式"
formula_en: "Class Weight Formula"
tags:
  - formula
  - imbalanced-data
  - classification
---

# 类别权重公式（Class Weight Formula）

一种常见权重设置为：

$$
w_k=\frac{n}{K\cdot n_k}
$$

含义：$n$ 是总样本数，$K$ 是类别数量，$n_k$ 是第 $k$ 类样本数。样本越少的类别，权重越大。

例子：二分类数据中共有 $100$ 个样本，类别 A 有 $90$ 个，类别 B 有 $10$ 个。则

$$
w_A=\frac{100}{2\times90}\approx0.56,\qquad
w_B=\frac{100}{2\times10}=5
$$

少数类 B 获得更高权重。

相关术语：[[类别加权 (Class Weighting)]]、[[类别不平衡 (Class Imbalance)]]、[[少数类 (Minority Class)]]
