---
course: "Machine Learning and AI with Python"
type: code-reference-index
tags:
  - code-reference
  - python
  - codelines
aliases:
  - Codelines
  - Python 代码行索引
---

# Codelines 索引

这里汇总 `Scripts/Test` 当前可见 notebook 中可复用的功能性代码。整理时忽略 `.ipynb_checkpoints`、`.local/share/Trash`，并对 scaffold、run 等重复版本去重。

## 主题导航

- [[01 - Pandas 数据读取清洗与筛选]]：读取 CSV、查看数据、处理缺失值、选择列、条件筛选和自助采样。
- [[02 - NumPy 数组索引与网格处理]]：唯一值、最优索引、数组变形、网格、拼接和随机索引。
- [[03 - 数据划分与决策树建模]]：训练测试集划分、分类树训练、预测、评分和树结构可视化。
- [[04 - 手算 Gini 与递归分割]]：二分类 Gini、加权 Gini、阈值中点、区域多数类和手写预测。
- [[05 - Bagging 回归与分类]]：`BaggingRegressor`、手写 bootstrap、多数投票和单个估计器访问。
- [[06 - 模型评估与特征重要性]]：准确率、MSE、类别计数、特征重要性和结果表格。
- [[07 - Matplotlib 数据与决策边界可视化]]：散点图、图例、分割线、网格预测和决策区域。
- [[13 - Random Forest 与分类 Bagging]]：分类 Bagging、随机特征、类别权重和集成树访问。
- [[14 - OOB 误差与 Random Forest 调参]]：袋外误差、warm start、参数选择和网格搜索。
- [[15 - 类别不平衡与重采样]]：F1、ROC AUC、类别加权、SMOTE 和随机下采样。
- [[16 - Gradient Boosting 回归]]：手算残差更新、梯度提升回归及与 Bagging 的比较。

## 函数参数详解

- [[08 - Pandas 函数参数详解]]：读取、查看、转换、计数、采样和显示配置。
- [[09 - NumPy 函数参数详解]]：唯一值、最优索引、数列、形状、网格、均值和随机抽样。
- [[10 - scikit-learn 函数参数详解]]：数据划分、树模型、Bagging、训练、预测、评分和指标。
- [[11 - Matplotlib 函数参数详解]]：画布、散点、折线、图例、分割线、等高区域和标签。
- [[12 - Python 内置函数与自定义函数参数详解]]：内置函数及课程自定义函数。
- [[17 - imbalanced-learn 函数参数详解]]：SMOTE、RandomUnderSampler 和训练集重采样。

## 来源 notebook

- `Scripts/Test/exe11/dt_classifier_scaffold.ipynb`
- `Scripts/Test/exe12/visualize_dt_scaffold.ipynb`
- `Scripts/Test/exe21/decision_tree_from_scratch.ipynb`
- `Scripts/Test/exe31/overfitting_bagging.ipynb`
- `Scripts/Test/exe32/bagging-classification-scaffold.ipynb`
- `Scripts/Test/exe41/tree_correlation.ipynb`
- `Scripts/Test/exe42/hyper_tuning.ipynb`
- `Scripts/Test/exe43/feature_importance.ipynb`
- `Scripts/Test/exe44/rf_imbalance_challenge.ipynb`
- `Scripts/Test/exe51/Boosting_Regressor.ipynb`

## 阅读约定

- 表格中的每一行都是一条可单独检索的代码行，并附有作用说明。
- 完整函数使用 Python 代码块展示；每一条关键语句都带中文行内注释。
- `参数名=默认值` 表示可省略的参数；`*args` 表示可变数量的位置参数，`**kwargs` 表示可变数量的具名参数。
- 示例变量名来自课程 notebook，复制到其他项目时需要替换为自己的 DataFrame、列名和模型名。

相关课程笔记：[[1.1.3 - 决策树分割标准]]、[[2.1 - 回归树与类别特征编码]]、[[3.1 - 集成学习与袋装法]]。
