---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "熵公式"
formula_en: "Entropy Formula"
tags:
  - formula
  - information-theory
---

# 熵公式（Entropy Formula）

$$
H(R_m) = - \sum_{k=1}^{K} p_{mk}\log_2(p_{mk})
$$

含义：$p_{mk}$ 表示区域 $R_m$ 中第 $k$ 类样本所占比例。类别分布越均匀，不确定性越高，熵越大；区域越纯净，熵越接近 $0$。当 $p_{mk}=0$ 时，按惯例令 $p_{mk}\log_2(p_{mk})=0$。

例子：如果某个区域有两个类别，比例分别是 $p_1=0.5$、$p_2=0.5$，则

$$
H(R_m) = -[0.5\log_2(0.5)+0.5\log_2(0.5)] = 1
$$

这表示二分类下类别平均混合时，不确定性较高。

相关术语：[[熵 (Entropy)]]、[[信息论 (Information Theory)]]、[[离散分布 (Discrete Distribution)]]

相关章节：[[1.1.3 - 决策树分割标准]]
