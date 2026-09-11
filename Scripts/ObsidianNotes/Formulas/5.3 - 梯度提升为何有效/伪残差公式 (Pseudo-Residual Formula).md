---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "伪残差公式"
formula_en: "Pseudo-Residual Formula"
tags:
  - formula
  - optimization
  - boosting
---

# 伪残差公式（Pseudo-Residual Formula）

$$
r_{im}
=-left.
\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}
\right|_{F=F_{m-1}}
$$

含义：$r_{im}$ 是第 $m$ 轮样本 $i$ 的伪残差，即损失函数相对于当前预测值的负梯度。梯度提升训练新弱学习器去近似这些数值。

例子：对半平方误差 $L_i=\frac12(y_i-F(x_i))^2$，负梯度为：

$$
-\frac{\partial L_i}{\partial F(x_i)}
=y_i-F(x_i)
$$

若真实值 $y_i=8$、当前预测 $F(x_i)=6$，则伪残差为 $2$，恰好等于普通残差。若换用其他损失函数，伪残差不一定等于 $y_i-F(x_i)$。

相关术语：[[伪残差 (Pseudo-Residual)]]、[[残差 (Residual)]]、[[损失函数 (Loss Function)]]、[[梯度提升 (Gradient Boosting)]]

相关章节：[[5.3 - 梯度提升为何有效]]
