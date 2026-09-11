---
type: term
course: "Machine Learning and AI with Python"
term_cn: "网格搜索"
term_en: "Grid Search"
tags:
  - term
  - model-selection
  - hyperparameter
---

# 网格搜索（Grid Search）

网格搜索先为一个或多个超参数列出候选值，再评估这些候选值的笛卡尔积。它通常结合交叉验证为每组配置计算评分，并按指定指标选择最佳配置。

网格搜索只能比较给定网格中的候选值；网格越大，计算成本通常越高。最终测试集不应参与搜索或参数选择。

相关概念：[[超参数调优 (Hyperparameter Tuning)]]、[[超参数 (Hyperparameter)]]、[[交叉验证 (Cross-Validation)]]、[[验证集 (Validation Set)]]、[[测试集 (Test Set)]]
