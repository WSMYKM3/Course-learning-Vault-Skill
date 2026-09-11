---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "精确率公式"
formula_en: "Precision Formula"
tags:
  - formula
  - evaluation
  - classification
---

# 精确率公式（Precision Formula）

$$
\operatorname{Precision}=\frac{TP}{TP+FP}
$$

含义：$TP$ 是被正确预测为正类的样本数，$FP$ 是被错误预测为正类的样本数。精确率回答：“模型预测为正类的样本中，有多少确实是正类？”假阳性越多，精确率越低。

例子：模型预测出 $40$ 个正类，其中 $30$ 个是真正类、$10$ 个是假阳性，则

$$
\operatorname{Precision}=\frac{30}{30+10}=0.75
$$

相关术语：[[精确率 (Precision)]]、[[假阳性 (False Positive)]]、[[F1分数 (F1 Score)]]、[[类别不平衡 (Class Imbalance)]]
