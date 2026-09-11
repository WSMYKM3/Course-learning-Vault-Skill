---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "随机森林特征子集经验规则公式"
formula_en: "Random Forest Feature Subset Heuristic Formula"
tags:
  - formula
  - random-forest
---

# 随机森林特征子集经验规则公式（Random Forest Feature Subset Heuristic Formula）

分类任务常用：

$$
m_{\text{try}} \approx \sqrt{p}
$$

回归任务常用：

$$
m_{\text{try}} \approx \frac{p}{3}
$$

含义：$p$ 表示全部预测变量数量，$m_{\text{try}}$ 表示随机森林在每个分裂节点随机抽取并参与候选分裂搜索的预测变量数量。这些公式是调参起点，不是必须固定的理论最优值。

例子：如果分类任务有 $p=16$ 个预测变量，可以先尝试 $m_{\text{try}}\approx\sqrt{16}=4$。如果回归任务有 $p=12$ 个预测变量，可以先尝试 $m_{\text{try}}\approx 12/3=4$。

相关术语：[[随机森林 (Random Forest)]]、[[预测变量 (Predictor)]]、[[预测变量子集 (Predictor Subset)]]、[[超参数 (Hyperparameter)]]
