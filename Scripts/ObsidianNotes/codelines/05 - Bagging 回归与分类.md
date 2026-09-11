---
course: "Machine Learning and AI with Python"
type: code-reference
topic: "Bagging 回归与分类"
tags:
  - code-reference
  - python
  - bagging
  - ensemble-learning
aliases:
  - Bagging codelines
---

# Bagging 回归与分类

返回索引：[[00 - Codelines 索引]]

本页函数逐参数说明：[[09 - NumPy 函数参数详解]]、[[10 - scikit-learn 函数参数详解]]、[[12 - Python 内置函数与自定义函数参数详解]]；Random Forest 对比见 [[13 - Random Forest 与分类 Bagging]]。

相关课程笔记：[[3.1 - 集成学习与袋装法]]、[[3.2 - 袋外误差与相关树]]。

## 使用 BaggingRegressor

| 代码行 | 作用 |
|---|---|
| `from sklearn.ensemble import BaggingRegressor` | 导入 Bagging 回归器。 |
| `from sklearn.tree import DecisionTreeRegressor` | 导入作为基模型的回归树。 |
| `num_bootstraps = 30` | 指定集成中的回归树数量。 |
| `max_depth = 3` | 限制每棵回归树的最大深度。 |
| `model = BaggingRegressor(DecisionTreeRegressor(max_depth=max_depth), n_estimators=num_bootstraps)` | 创建由多棵回归树组成的 Bagging 模型。 |
| `model.fit(x_train, y_train)` | 在训练数据上拟合所有基估计器。 |
| `y_pred = model.predict(x_test)` | 聚合所有基估计器，输出测试集平均预测。 |
| `y_pred1 = model.estimators_[0].predict(x_test)` | 只使用 Bagging 中第一棵树预测，便于与集成结果比较。 |
| `BaggingRegressor(DecisionTreeRegressor(max_depth=3), n_estimators=30, max_samples=0.8, random_state=3)` | 每棵树使用 80% 样本，固定 bootstrap 随机性。 |

## 使用 BaggingClassifier

| 代码行 | 作用 |
|---|---|
| `from sklearn.ensemble import BaggingClassifier` | 导入分类 Bagging 元估计器。 |
| `basemodel = DecisionTreeClassifier(max_depth=20, random_state=144)` | 创建所有 bootstrap 共用的基分类器模板。 |
| `bagging = BaggingClassifier(estimator=basemodel, n_estimators=1000, random_state=144)` | 创建由 1000 棵自助决策树组成的分类集成。 |
| `bagging.fit(X_train, y_train)` | 为每个基模型抽样并完成拟合。 |
| `bagging.predict(X_val)` | 通过基分类器投票输出验证集类别。 |

## 手写分类 Bagging：生成自助数据

| 代码行 | 作用 |
|---|---|
| `predictions = []` | 创建列表，保存每棵树的预测数组。 |
| `for i in range(num_bootstraps):` | 重复训练指定数量的 bootstrap 树。 |
| `resample_indexes = np.random.choice(np.arange(y_train.shape[0]), size=y_train.shape[0])` | 有放回抽取与训练集等长的样本索引。 |
| `X_boot = X_train[resample_indexes]` | 根据索引构造自助特征集。 |
| `y_boot = y_train[resample_indexes]` | 根据相同索引构造自助标签集。 |
| `clf = DecisionTreeClassifier(max_depth=max_depth, random_state=44)` | 创建当前 bootstrap 对应的基分类树。 |
| `clf.fit(X_boot, y_boot)` | 在当前自助数据集上训练基分类树。 |
| `pred = clf.predict(X_to_evaluate)` | 让当前基分类树预测目标样本。 |
| `predictions.append(pred)` | 将当前树的预测加入集成结果列表。 |

## 多数投票

| 代码行 | 作用 |
|---|---|
| `np.mean(predictions, axis=0)` | 对每个样本汇总所有树的平均类别值。 |
| `average_prediction = (np.mean(predictions, axis=0) > 0.5).astype(int)` | 对二分类平均值以 0.5 为阈值进行多数投票，并返回 `0/1`。 |
| `return average_prediction` | 返回 Bagging 的最终类别预测。 |

> [!important]
> 上述平均后阈值法只适用于标签编码为 `0/1` 的二分类问题。多分类问题应统计每个样本预测的众数。

## 完整的手写分类 Bagging 函数

```python
def prediction_by_bagging(X_train, y_train, X_to_evaluate, num_bootstraps):  # 定义自助聚合预测函数
    predictions = []                                                         # 保存每棵树的预测
    for _ in range(num_bootstraps):                                           # 训练指定数量的基模型
        indexes = np.random.choice(                                           # 开始生成随机自助索引
            np.arange(y_train.shape[0]),                                      # 可抽取的训练集行号
            size=y_train.shape[0],                                            # 每次抽取与原训练集等长
        )                                                                       # 结束随机抽样调用
        X_boot = X_train[indexes]                                             # 获取自助特征样本
        y_boot = y_train[indexes]                                             # 获取与特征配对的自助标签
        clf = DecisionTreeClassifier(max_depth=max_depth, random_state=44)    # 创建基分类树
        clf.fit(X_boot, y_boot)                                               # 拟合当前自助样本
        predictions.append(clf.predict(X_to_evaluate))                        # 保存当前树的预测
    return (np.mean(predictions, axis=0) > 0.5).astype(int)                   # 多数投票并返回 0/1 类别
```

相关概念：[[集成学习 (Ensemble Learning)]]、[[基模型 (Base Model)]]、[[聚合 (Aggregation)]]。

## 查看树数量对准确率的影响

```python
n = np.linspace(1, 250, 250).astype(int)                                      # 生成要测试的树数量 1 到 250
acc = []                                                                      # 保存每个树数量对应的准确率
for n_i in n:                                                                 # 逐一测试不同集成规模
    y_pred = prediction_by_bagging(X_train, y_train, X_test, n_i)             # 用 n_i 棵树预测
    acc.append(np.mean(y_pred == y_test))                                     # 计算并保存当前测试准确率
```
