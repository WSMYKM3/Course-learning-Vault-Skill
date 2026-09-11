---
type: term
course: "Machine Learning and AI with Python"
term_cn: "AUC"
term_en: "Area Under the Curve"
tags:
  - term
  - evaluation
  - classification
---

# AUC（Area Under the Curve）

AUC 通常指 ROC 曲线下的面积，用于总结分类器在不同阈值下真正率和假正率之间的权衡。类别不平衡或错误代价不同的任务中，AUC 常比单一准确率更有参考价值。

计算 ROC AUC 时应使用正类概率或其他连续评分。硬分类标签只表示一个阈值下的结果，不能充分描述模型跨阈值的排序能力。

公式：[[ROC AUC公式 (ROC AUC Formula)]]

相关概念：[[ROC曲线 (Receiver Operating Characteristic Curve)]]、[[真正率 (True Positive Rate)]]、[[假正率 (False Positive Rate)]]、[[类别概率 (Class Probability)]]、[[类别不平衡 (Class Imbalance)]]

相关章节：[[4.3 - 类别不平衡处理]]
