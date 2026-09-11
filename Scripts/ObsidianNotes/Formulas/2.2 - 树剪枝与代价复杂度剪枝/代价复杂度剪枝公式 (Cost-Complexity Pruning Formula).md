---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "代价复杂度剪枝公式"
formula_en: "Cost-Complexity Pruning Formula"
tags:
  - formula
  - decision-tree
  - regularization
---

# 代价复杂度剪枝公式（Cost-Complexity Pruning Formula）

$$
C_{\alpha}(T) = \operatorname{Err}(T) + \alpha |T|
$$

含义：$T$ 表示一棵候选树，$\operatorname{Err}(T)$ 表示这棵树的训练误差或节点误差总量，$|T|$ 表示叶节点数量，$\alpha$ 是控制复杂度惩罚强度的复杂度参数。

例子：如果一棵树的误差为 $0.32$、叶节点数为 $8$，并取 $\alpha=0.2$，则

$$
C_{\alpha}(T)=0.32+0.2\times 8=1.92
$$

若剪枝后误差变为 $0.33$、叶节点数变为 $7$，则

$$
C_{\alpha}(T')=0.33+0.2\times 7=1.73
$$

虽然误差略有增加，但总代价下降，因此在这个 $\alpha$ 下剪枝后的树更优。

相关术语：[[代价复杂度剪枝 (Cost-Complexity Pruning)]]、[[复杂度参数 (Complexity Parameter)]]、[[叶节点 (Leaf Node)]]、[[正则化 (Regularization)]]

相关章节：[[2.2 - 树剪枝与代价复杂度剪枝]]
