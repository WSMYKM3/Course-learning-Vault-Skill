---
type: formula
course: "Machine Learning and AI with Python"
formula_cn: "ROC AUC公式"
formula_en: "ROC AUC Formula"
tags:
  - formula
  - evaluation
  - classification
---

# ROC AUC公式（ROC AUC Formula）

ROC 曲线下面积的积分定义为：

$$
\operatorname{AUC}=\int_{0}^{1}\operatorname{TPR}(u)\,du
$$

其中 $u$ 表示假正率 FPR，$\operatorname{TPR}(u)$ 表示相应阈值下的真正率。

对于有限样本，AUC 也可理解为随机抽取一个正类和一个负类时，模型给正类更高评分的概率；并列评分按一半计入：

$$
\operatorname{AUC}
=\frac{1}{n_+n_-}
\sum_{i:y_i=1}\sum_{j:y_j=0}
\left[
\mathbb{1}(s_i>s_j)+\frac{1}{2}\mathbb{1}(s_i=s_j)
\right]
$$

含义：$n_+$ 和 $n_-$ 分别是正类与负类样本数，$s_i$ 是模型给样本的连续正类评分。AUC 越接近 $1$，模型把正类排在负类前面的能力越强。

例子：若一共有 $10$ 个正负样本对，其中 $8$ 对的正类评分更高、没有并列，则 AUC 为 $8/10=0.80$。

计算 ROC AUC 时应传入正类概率或其他连续评分，例如 `predict_proba(X)[:, 1]`。传入硬分类标签只保留一个阈值的结果，无法充分表示模型在所有阈值下的排序能力。

相关术语：[[AUC (Area Under the Curve)]]、[[ROC曲线 (Receiver Operating Characteristic Curve)]]、[[真正率 (True Positive Rate)]]、[[假正率 (False Positive Rate)]]、[[类别概率 (Class Probability)]]
