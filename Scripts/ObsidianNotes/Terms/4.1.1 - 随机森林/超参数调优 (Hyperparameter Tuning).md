---
type: term
course: "Machine Learning and AI with Python"
term_cn: "超参数调优"
term_en: "Hyperparameter Tuning"
tags:
  - term
  - model-selection
  - hyperparameter
---

# 超参数调优（Hyperparameter Tuning）

超参数调优是根据验证表现选择模型训练前配置的过程。在随机森林中，可调参数包括树数量、最大深度、叶节点最小样本数和每次分割考虑的特征数量。

候选配置可以通过独立验证集、交叉验证或袋外误差比较；测试集应保留到模型选择完成后再用于最终评估。

相关概念：[[超参数 (Hyperparameter)]]、[[网格搜索 (Grid Search)]]、[[交叉验证 (Cross-Validation)]]、[[袋外误差 (Out-of-Bag Error)]]、[[验证集 (Validation Set)]]、[[测试集 (Test Set)]]
