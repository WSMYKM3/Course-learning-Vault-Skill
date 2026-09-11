---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "分类错误率公式"
formula_en: "Classification Error Formula"
tags:
  - formula
  - decision-tree
---

# 分类错误率公式（Classification Error Formula）

$$
E(R_m) = 1 - \max_{k} p_{mk}
$$

含义：$p_{mk}$ 表示区域 $R_m$ 中第 $k$ 类样本所占比例。在区域 $R_m$ 中，如果全部预测为多数类，则错误比例等于 $1$ 减去最大类别比例。

例子：如果一个区域里 10 个样本中有 7 个 A 类、3 个 B 类，则最大类别比例是 $0.7$，所以

$$
E(R_m) = 1 - 0.7 = 0.3
$$

这表示把整个区域都预测为 A 类时，会错分约 $30\%$ 的样本。

相关术语：[[分类错误率 (Classification Error Rate)]]、[[多数类 (Majority Class)]]、[[不纯度 (Impurity)]]

相关章节：[[1.1.3 - 决策树分割标准]]
