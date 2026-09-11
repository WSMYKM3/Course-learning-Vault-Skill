---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "真正率（召回率）公式"
formula_en: "True Positive Rate (Recall) Formula"
tags:
  - formula
  - evaluation
  - classification
aliases:
  - 召回率公式
  - Recall Formula
---

# 真正率（召回率）公式（True Positive Rate / Recall Formula）

$$
\operatorname{Recall}=\operatorname{TPR}=\frac{TP}{TP+FN}
$$

含义：$TP$ 是被正确预测为正类的样本数，$FN$ 是被错误预测为负类的真实正类样本数。真正率也称召回率，回答：“所有真实正类中，模型成功找出了多少？”

例子：数据中有 $50$ 个真实正类，模型正确找出 $30$ 个、漏掉 $20$ 个，则

$$
\operatorname{Recall}=\frac{30}{30+20}=0.60
$$

相关术语：[[真正率 (True Positive Rate)]]、[[假阴性 (False Negative)]]、[[F1分数 (F1 Score)]]、[[ROC曲线 (Receiver Operating Characteristic Curve)]]
