---
course: "Machine Learning and AI with Python"
type: code-reference
topic: "OOB 误差与 Random Forest 调参"
tags:
  - code-reference
  - python
  - random-forest
  - oob-error
  - hyperparameter-tuning
  - grid-search
aliases:
  - Random Forest 调参 codelines
---

# OOB 误差与 Random Forest 调参

返回索引：[[00 - Codelines 索引]]

本页函数逐参数说明：[[10 - scikit-learn 函数参数详解]]、[[12 - Python 内置函数与自定义函数参数详解]]。

## 使用预测概率计算 ROC AUC

```python
vanilla_rf = RandomForestClassifier(random_state=seed)           # 创建使用默认超参数的基线森林
vanilla_rf.fit(X_train, y_train)                                 # 拟合训练数据
y_proba = vanilla_rf.predict_proba(X_test)[:, 1]                 # 取每个样本属于正类 1 的概率
auc = np.round(roc_auc_score(y_test, y_proba), 2)                # 计算 ROC AUC 并保留两位小数
```

| 代码行 | 作用 |
|---|---|
| `X_train.shape[0]` | 读取训练样本数。 |
| `X_train.shape[1]` | 读取训练特征数。 |
| `predict_proba(X_test)[:, 1]` | 从两列类别概率中选择正类概率；二分类 ROC AUC 应优先使用此值。 |

## 追踪树数量与 OOB 误差

```python
clf = RandomForestClassifier(                                    # 创建可逐步增加树数量的森林
    warm_start=True,                                             # 后续 fit 保留已有树并继续增加
    oob_score=True,                                              # 计算袋外样本评分
    min_samples_leaf=40,                                         # 每个叶节点至少保留 40 个样本
    max_depth=10,                                                # 限制树深
    random_state=seed,                                           # 固定随机性
)                                                               # 结束模型构造
error_rate = {}                                                  # 保存“树数量 -> OOB 误差”映射
for i in range(150, 501):                                        # 依次尝试 150 到 500 棵树
    clf.set_params(n_estimators=i)                               # 更新当前森林的树数量
    clf.fit(X_train.values, y_train.values)                      # 拟合或扩展森林
    error_rate[i] = 1 - clf.oob_score_                           # 将 OOB 正确率转为 OOB 错误率
```

> [!important]
> `oob_score=True` 只有在 `bootstrap=True` 时可用。`warm_start=True` 下只能增加 `n_estimators`，不要在同一模型上把树数量调小。

## 同时比较叶节点大小

```python
ensemble_clfs = [                                                # 建立要比较的模型列表
    (1, RandomForestClassifier(                                  # 第一个候选模型
        warm_start=True, min_samples_leaf=1,                     # 叶节点至少 1 个样本
        oob_score=True, max_depth=10, random_state=seed,         # 启用 OOB 并固定其他配置
    )),                                                          # 结束第一个候选
    (5, RandomForestClassifier(                                  # 第二个候选模型
        warm_start=True, min_samples_leaf=5,                     # 叶节点至少 5 个样本
        oob_score=True, max_depth=10, random_state=seed,         # 使用相同的其余配置
    )),                                                          # 结束第二个候选
]                                                               # 结束候选模型列表
error_rate = OrderedDict((label, []) for label, _ in ensemble_clfs)  # 按候选值保存误差轨迹
for label, clf in ensemble_clfs:                                 # 遍历每个叶节点大小与模型
    for i in range(min_estimators, max_estimators + 1):          # 遍历候选树数量
        clf.set_params(n_estimators=i)                           # 设置当前树数量
        clf.fit(X_train.values, y_train.values)                  # 训练当前配置
        error_rate[label].append((i, 1 - clf.oob_score_))        # 保存树数量和 OOB 误差二元组
```

## 从误差记录中选择最佳配置

```python
best_error = float('inf')                                        # 用正无穷初始化当前最佳误差
best_num_estimators = 0                                          # 初始化最佳树数量
best_leaf = None                                                  # 初始化最佳叶节点大小
for label, clf_err in error_rate.items():                        # 遍历每组叶节点大小及其误差轨迹
    num_estimators, error = min(                                 # 找到该组误差最低的记录
        clf_err, key=lambda item: (item[1], -item[0])            # 误差相同时偏向更多树
    )                                                            # 结束 min 调用
    if error < best_error:                                       # 若当前组优于之前结果
        best_error = error                                       # 更新最低误差
        best_num_estimators = num_estimators                     # 保存相应树数量
        best_leaf = label                                        # 保存相应叶节点大小
```

## 使用 GridSearchCV

```python
rf = RandomForestClassifier(                                     # 创建供网格搜索使用的基础模型
    n_jobs=-1, n_estimators=best_num_estimators,                 # 并行训练并使用已筛出的树数量
    oob_score=True, max_features='sqrt',                         # 启用 OOB 并随机抽取候选特征
    min_samples_leaf=best_leaf, random_state=seed,               # 使用已筛出的叶大小并固定随机性
)                                                               # 结束基础模型构造
param_grid = {'min_samples_split': [2, 5]}                       # 指定要搜索的分割样本数
scoring = {'AUC': 'roc_auc'}                                     # 为评分指标命名并选择 ROC AUC
grid_search = GridSearchCV(                                      # 创建交叉验证网格搜索器
    rf, param_grid,                                              # 传入模型和参数网格
    scoring=scoring, refit='AUC',                                # 按 AUC 选择并重训最佳模型
    return_train_score=True, n_jobs=-1,                          # 保留训练分数并并行搜索
)                                                               # 结束网格搜索构造
results = grid_search.fit(X_train, y_train)                      # 对所有候选执行交叉验证
best_rf = results.best_estimator_                                # 读取已在全训练集重训的最佳模型
```

| 代码行 | 作用 |
|---|---|
| `estimators_rf.get_params()` | 返回当前估计器全部参数字典。 |
| `clf.set_params(n_estimators=i)` | 用参数名更新估计器并返回估计器自身。 |
| `results.best_estimator_` | 取得按 `refit` 指标选出的最佳已拟合模型。 |
| `results.best_params_` | 取得最佳候选参数字典。 |
| `results.cv_results_` | 取得每个候选配置的交叉验证详细结果。 |
