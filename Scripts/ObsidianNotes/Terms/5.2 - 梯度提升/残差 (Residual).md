---
type: term
course: "Machine Learning and AI with Python"
term_cn: "残差"
term_en: "Residual"
tags:
  - term
  - regression
  - boosting
---

# 残差（Residual）

残差是真实响应值与模型预测值之差：$r_i=y_i-\hat y_i$。正残差表示预测偏低，负残差表示预测偏高；在平方误差梯度提升中，下一棵树会学习当前残差。

相关概念：[[梯度提升 (Gradient Boosting)]]、[[伪残差 (Pseudo-Residual)]]、[[均方误差 (Mean Squared Error)]]

相关公式：[[残差公式 (Residual Formula)]]

相关章节：[[5.2 - 梯度提升]]、[[5.3 - 梯度提升为何有效]]
