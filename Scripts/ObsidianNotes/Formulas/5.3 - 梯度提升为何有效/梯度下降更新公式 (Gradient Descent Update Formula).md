---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "梯度下降更新公式"
formula_en: "Gradient Descent Update Formula"
tags:
  - formula
  - optimization
---

# 梯度下降更新公式（Gradient Descent Update Formula）

$$
\mathbf{w}_{t+1}
=\mathbf{w}_t-\eta\nabla_{\mathbf{w}}L(\mathbf{w}_t)
$$

含义：$\mathbf{w}_t$ 是当前参数，$L$ 是损失函数，$\nabla L$ 是当前梯度，$\eta$ 是学习率。减去梯度的一小部分，就是沿局部下降最快的方向更新。

例子：令 $L(w)=(w-3)^2$，从 $w_0=0$ 开始，梯度为 $L'(0)=2(0-3)=-6$。若 $\eta=0.1$：

$$
w_1=0-0.1(-6)=0.6
$$

$w$ 从 $0$ 向最小点 $3$ 移动，且损失从 $9$ 降到 $(0.6-3)^2=5.76$。

相关术语：[[梯度下降 (Gradient Descent)]]、[[损失函数 (Loss Function)]]、[[学习率 (Learning Rate)]]

相关章节：[[5.3 - 梯度提升为何有效]]
