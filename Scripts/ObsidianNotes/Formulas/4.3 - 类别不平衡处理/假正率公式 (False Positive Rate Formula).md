---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "假正率公式"
formula_en: "False Positive Rate Formula"
tags:
  - formula
  - evaluation
  - classification
---

# 假正率公式（False Positive Rate Formula）

$$
\operatorname{FPR}=\frac{FP}{FP+TN}
$$

含义：$FP$ 是被错误预测为正类的真实负类样本数，$TN$ 是被正确预测为负类的样本数。假正率回答：“所有真实负类中，有多少被模型误报为正类？”它是 ROC 曲线的横轴。

例子：数据中有 $100$ 个真实负类，其中 $10$ 个被误报为正类、$90$ 个被正确预测为负类，则

$$
\operatorname{FPR}=\frac{10}{10+90}=0.10
$$

相关术语：[[假正率 (False Positive Rate)]]、[[假阳性 (False Positive)]]、[[ROC曲线 (Receiver Operating Characteristic Curve)]]、[[AUC (Area Under the Curve)]]
