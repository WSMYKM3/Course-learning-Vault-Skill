---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "代理分割相似度公式"
formula_en: "Surrogate Split Similarity Formula"
tags:
  - formula
  - decision-tree
  - missing-data
---

# 代理分割相似度公式（Surrogate Split Similarity Formula）

$$
\operatorname{sim}(s,s')=\frac{1}{n}\sum_{i=1}^{n}\mathbb{1}\left(d_s(x_i)=d_{s'}(x_i)\right)
$$

含义：$s$ 是主分割，$s'$ 是候选代理分割，$d_s(x_i)$ 表示样本 $x_i$ 在分割 $s$ 下进入左子节点还是右子节点。相似度越高，说明候选代理分割越能模仿主分割。

例子：在 5 个样本中，候选代理分割有 4 个样本的左右去向与主分割一致，则

$$
\operatorname{sim}(s,s')=\frac{4}{5}=0.8
$$

相关术语：[[代理分割 (Surrogate Split)]]、[[主分割 (Primary Split)]]、[[缺失数据 (Missing Data)]]
