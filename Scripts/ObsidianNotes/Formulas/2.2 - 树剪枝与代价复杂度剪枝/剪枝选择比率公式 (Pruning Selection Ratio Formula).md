---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "剪枝选择比率公式"
formula_en: "Pruning Selection Ratio Formula"
tags:
  - formula
  - decision-tree
  - pruning
---

# 剪枝选择比率公式（Pruning Selection Ratio Formula）

$$
g(T,T') = \frac{\operatorname{Err}(T')-\operatorname{Err}(T)}{|T|-|T'|}
$$

含义：$T$ 是当前树，$T'$ 是某个候选剪枝树，分子表示剪枝带来的误差增加，分母表示剪枝减少的叶节点数量。这个比率越小，表示用较小的误差代价换来了较多的复杂度下降。

例子：如果当前树误差为 $0.32$、叶节点数为 $8$，某个候选剪枝树误差为 $0.33$、叶节点数为 $7$，则

$$
g(T,T')=\frac{0.33-0.32}{8-7}=0.01
$$

如果另一个候选剪枝树误差为 $0.36$、叶节点数为 $6$，则

$$
g(T,T'')=\frac{0.36-0.32}{8-6}=0.02
$$

因为 $0.01<0.02$，第一个候选剪枝树在这一步更值得优先考虑。

相关术语：[[树剪枝 (Tree Pruning)]]、[[代价复杂度剪枝 (Cost-Complexity Pruning)]]、[[子树 (Subtree)]]

相关章节：[[2.2 - 树剪枝与代价复杂度剪枝]]
