---
course: "Machine Learning and AI with Python"
type: parameter-reference
topic: "scikit-learn 函数参数"
tags:
  - code-reference
  - python
  - scikit-learn
  - parameters
aliases:
  - scikit-learn 参数速查
---

# scikit-learn 函数参数详解

返回索引：[[00 - Codelines 索引]]；对应代码：[[03 - 数据划分与决策树建模]]、[[05 - Bagging 回归与分类]]、[[06 - 模型评估与特征重要性]]、[[13 - Random Forest 与分类 Bagging]]、[[14 - OOB 误差与 Random Forest 调参]]、[[16 - Gradient Boosting 回归]]。

## `train_test_split()`

调用形式：`train_test_split(*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None)`。

课程调用：

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=44
)
```

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `*arrays` | `X, y` | 一个或多个长度相同的数组；函数用同一组索引同步划分。可传两个，也可传更多。 |
| `test_size` | `0.2` | 浮点数表示测试集比例，整数表示测试样本数。 |
| `train_size` | `None` | 浮点数表示训练比例，整数表示训练样本数；通常与 `test_size` 二选一。 |
| `random_state` | `44` | 随机种子或随机状态对象，用于复现划分。 |
| `shuffle` | `True` | 划分前是否打乱样本。 |
| `stratify` | `None` | 传分类标签时按其类别比例分层抽样。 |

返回值数量是输入数组数量的两倍；传 `X, y` 两个数组会返回 4 个结果。

## `DecisionTreeClassifier()`

```python
DecisionTreeClassifier(
    criterion='gini', splitter='best', max_depth=None,
    min_samples_split=2, min_samples_leaf=1,
    min_weight_fraction_leaf=0.0, max_features=None,
    random_state=None, max_leaf_nodes=None,
    min_impurity_decrease=0.0, class_weight=None,
    ccp_alpha=0.0, monotonic_cst=None,
)
```

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `criterion` | `'gini'` | 切分质量标准；常见值为 `'gini'`、`'entropy'`、`'log_loss'`。 |
| `splitter` | `'best'` | 节点选择最佳切分；`'random'` 从随机候选中选最佳。 |
| `max_depth` | `3`、`2`、`10`、`15` | 最大树深；`None` 表示由其他停止条件决定。 |
| `min_samples_split` | `2` | 内部节点继续切分所需的最小样本数或比例。 |
| `min_samples_leaf` | `1` | 叶节点至少保留的样本数或比例。 |
| `min_weight_fraction_leaf` | `0.0` | 叶节点最小加权样本比例。 |
| `max_features` | `None` | 每次寻找切分时考虑的最大特征数。 |
| `random_state` | `44` 或 `0` | 控制随机行为，便于复现。 |
| `max_leaf_nodes` | `None` | 以最佳优先方式限制叶节点总数。 |
| `min_impurity_decrease` | `0.0` | 不纯度下降达到此阈值才执行切分。 |
| `class_weight` | `None` | 类别权重；可传字典或 `'balanced'`。 |
| `ccp_alpha` | `0.0` | 最小代价复杂度剪枝强度。 |
| `monotonic_cst` | `None` | 可选特征单调约束，支持情况取决于版本和任务。 |

课程中的 `DecisionTreeClassifier(max_depth=3, random_state=44)` 只覆盖两个参数，其余全部采用默认值。

## `DecisionTreeRegressor()`

```python
DecisionTreeRegressor(
    criterion='squared_error', splitter='best', max_depth=None,
    min_samples_split=2, min_samples_leaf=1,
    min_weight_fraction_leaf=0.0, max_features=None,
    random_state=None, max_leaf_nodes=None,
    min_impurity_decrease=0.0, ccp_alpha=0.0, monotonic_cst=None,
)
```

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `criterion` | `'squared_error'` | 回归切分损失；还可选 `'absolute_error'`、`'poisson'`，版本可能支持其他值。 |
| `splitter` | `'best'` | 节点切分策略。 |
| `max_depth` | 本例 `3` | 最大树深。 |
| `min_samples_split` | `2` | 内部节点最小样本数或比例。 |
| `min_samples_leaf` | `1` | 叶节点最小样本数或比例。 |
| `min_weight_fraction_leaf` | `0.0` | 叶节点最小加权样本比例。 |
| `max_features` | `None` | 寻找切分时考虑的特征数。 |
| `random_state` | `None` | 控制随机性。 |
| `max_leaf_nodes` | `None` | 最大叶节点数。 |
| `min_impurity_decrease` | `0.0` | 最小不纯度下降。 |
| `ccp_alpha` | `0.0` | 剪枝强度。 |
| `monotonic_cst` | `None` | 单调约束。 |

## `BaggingRegressor()`

```text
BaggingRegressor(
    estimator=None, n_estimators=10,
    *, max_samples=1.0, max_features=1.0,
    bootstrap=True, bootstrap_features=False,
    oob_score=False, warm_start=False,
    n_jobs=None, random_state=None, verbose=0,
)
```

课程调用：`BaggingRegressor(DecisionTreeRegressor(max_depth=3), n_estimators=30)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `estimator` | 深度 3 的回归树 | 被重复拟合的基估计器；课程用第 1 个位置参数传入。旧版可能称 `base_estimator`。 |
| `n_estimators` | `30` | 集成中基估计器数量。 |
| `max_samples` | `1.0` | 每个基估计器抽取的训练样本数量或比例。 |
| `max_features` | `1.0` | 每个基估计器使用的特征数量或比例。 |
| `bootstrap` | `True` | 样本是否有放回抽样；`False` 是 pasting。 |
| `bootstrap_features` | `False` | 特征是否有放回抽样。 |
| `oob_score` | `False` | 是否用袋外样本估计泛化性能。 |
| `warm_start` | `False` | 再次拟合时是否保留已有估计器并追加。 |
| `n_jobs` | `None` | 并行任务数；`-1` 通常表示使用全部处理器。 |
| `random_state` | `None` | 控制 bootstrap 和基估计器随机性。 |
| `verbose` | `0` | 训练过程的输出详细程度。 |

## `BaggingClassifier()`

```text
BaggingClassifier(
    estimator=None, n_estimators=10,
    *, max_samples=1.0, max_features=1.0,
    bootstrap=True, bootstrap_features=False,
    oob_score=False, warm_start=False,
    n_jobs=None, random_state=None, verbose=0,
)
```

课程调用：`BaggingClassifier(estimator=basemodel, n_estimators=1000, random_state=random_state)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `estimator` | `basemodel` | 要在不同随机子集上训练的基分类器；`None` 时通常使用决策树桩。 |
| `n_estimators` | `1000` | 基分类器数量。 |
| `max_samples` | `1.0` | 每个基分类器抽取的样本数或比例。 |
| `max_features` | `1.0` | 每个基分类器抽取的特征数或比例。 |
| `bootstrap` | `True` | 是否对样本进行有放回抽样。 |
| `bootstrap_features` | `False` | 是否对特征进行有放回抽样。 |
| `oob_score` | `False` | 是否用未被当前基模型抽到的样本估计泛化分数。 |
| `warm_start` | `False` | 再次拟合时是否复用已有基估计器并增加新估计器。 |
| `n_jobs` | `None` | 拟合和预测所用并行任务数；`-1` 常表示全部处理器。 |
| `random_state` | `random_state` | 控制样本/特征抽样及基估计器随机种子。 |
| `verbose` | `0` | 训练输出详细程度。 |

## `RandomForestClassifier()`

```text
RandomForestClassifier(
    n_estimators=100, *, criterion='gini', max_depth=None,
    min_samples_split=2, min_samples_leaf=1,
    min_weight_fraction_leaf=0.0, max_features='sqrt',
    max_leaf_nodes=None, min_impurity_decrease=0.0,
    bootstrap=True, oob_score=False, n_jobs=None,
    random_state=None, verbose=0, warm_start=False,
    class_weight=None, ccp_alpha=0.0, max_samples=None,
    monotonic_cst=None,
)
```

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `n_estimators` | `10`、`1000`；默认 `100` | 森林中的树数量。 |
| `criterion` | `'gini'` | 衡量分割质量；分类常用 `'gini'`、`'entropy'`、`'log_loss'`。 |
| `max_depth` | `3`、`10`、`20` | 每棵树的最大深度；`None` 表示由其他停止条件决定。 |
| `min_samples_split` | `2` 或网格 `[2, 5]` | 内部节点继续分割所需的最小样本数或比例。 |
| `min_samples_leaf` | `1`、`5`、`40` | 每个叶节点至少保留的样本数或比例。 |
| `min_weight_fraction_leaf` | `0.0` | 叶节点所需的最小加权样本比例。 |
| `max_features` | `'sqrt'` | 每次寻找最佳分割时随机考虑的特征数量。 |
| `max_leaf_nodes` | `None` | 限制每棵树的最大叶节点数。 |
| `min_impurity_decrease` | `0.0` | 分割所需的最小加权不纯度下降。 |
| `bootstrap` | `True` | 是否为每棵树有放回抽样训练样本。 |
| `oob_score` | 本例 `True` | 是否用袋外样本估计泛化分数；要求 `bootstrap=True`。 |
| `n_jobs` | 本例 `-1` | 并行训练、预测等工作的任务数。 |
| `random_state` | `seed` 等 | 控制样本抽样、特征抽样和其他随机行为。 |
| `verbose` | `0` | 训练输出详细程度。 |
| `warm_start` | 本例 `True` | 再次 `.fit()` 时复用已有森林，以增加树数量。 |
| `class_weight` | `'balanced_subsample'` | 类别权重；该值在每棵树的 bootstrap 样本内重新计算。 |
| `ccp_alpha` | `0.0` | 最小代价复杂度剪枝强度。 |
| `max_samples` | `None` | `bootstrap=True` 时每棵树抽取的样本数或比例。 |
| `monotonic_cst` | `None` | 可选单调约束；支持情况取决于任务和版本。 |

训练后的 `oob_score_` 是袋外评分，测试题使用 `1 - clf.oob_score_` 得到 OOB 错误率。

## `GradientBoostingRegressor()`

```text
GradientBoostingRegressor(
    loss='squared_error', learning_rate=0.1, n_estimators=100,
    subsample=1.0, criterion='friedman_mse', min_samples_split=2,
    min_samples_leaf=1, min_weight_fraction_leaf=0.0,
    max_depth=3, min_impurity_decrease=0.0, init=None,
    random_state=None, max_features=None, alpha=0.9,
    verbose=0, max_leaf_nodes=None, warm_start=False,
    validation_fraction=0.1, n_iter_no_change=None,
    tol=1e-4, ccp_alpha=0.0,
)
```

课程调用：`GradientBoostingRegressor(n_estimators=1000, max_depth=1, learning_rate=0.1)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `loss` | `'squared_error'` | 要优化的回归损失；也可按版本选择绝对误差、Huber、分位数等。 |
| `learning_rate` | `0.1` | 缩放每棵新树的贡献；与 `n_estimators` 存在权衡。 |
| `n_estimators` | `1000` | 顺序执行的 boosting 阶段数。 |
| `subsample` | `1.0` | 每轮拟合使用的训练样本比例；小于 1 时形成 stochastic gradient boosting。 |
| `criterion` | `'friedman_mse'` | 基回归树选择分割的准则。 |
| `min_samples_split` | `2` | 基树内部节点继续分割所需的最小样本数或比例。 |
| `min_samples_leaf` | `1` | 基树叶节点最小样本数或比例。 |
| `min_weight_fraction_leaf` | `0.0` | 基树叶节点最小加权样本比例。 |
| `max_depth` | 本例 `1` | 每个基回归估计器的最大深度。 |
| `min_impurity_decrease` | `0.0` | 基树执行分割所需的不纯度下降。 |
| `init` | `None` | 初始预测估计器；`None` 使用常数初始模型。 |
| `random_state` | `None` | 控制子采样及树分割随机性。 |
| `max_features` | `None` | 基树寻找分割时考虑的最大特征数。 |
| `alpha` | `0.9` | Huber 或 quantile 损失使用的分位数。 |
| `verbose` | `0` | 训练输出详细程度。 |
| `max_leaf_nodes` | `None` | 基树最大叶节点数。 |
| `warm_start` | `False` | 再次拟合时是否继续增加 boosting 阶段。 |
| `validation_fraction` | `0.1` | 启用早停时留作验证的数据比例。 |
| `n_iter_no_change` | `None` | 连续多少轮无改善时早停；`None` 禁用。 |
| `tol` | `1e-4` | 判断早停改善的容差。 |
| `ccp_alpha` | `0.0` | 基树的最小代价复杂度剪枝强度。 |

## `GridSearchCV()`

```text
GridSearchCV(
    estimator, param_grid, *, scoring=None, n_jobs=None,
    refit=True, cv=None, verbose=0, pre_dispatch='2*n_jobs',
    error_score=nan, return_train_score=False,
)
```

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `estimator` | `rf` | 要调参的估计器，必需。 |
| `param_grid` | `{'min_samples_split': [2, 5]}` | 参数名到候选值列表的字典，或多个此类字典组成的列表。 |
| `scoring` | `{'AUC': 'roc_auc'}` | 单个评分器或具名多指标字典。 |
| `n_jobs` | `-1` | 并行评估候选配置的任务数。 |
| `refit` | `'AUC'` | 用哪个指标选择最佳参数，并在全训练集上重训。 |
| `cv` | `None` | 交叉验证折数、切分器或预定义切分；`None` 使用默认策略。 |
| `verbose` | `0` | 搜索过程输出详细程度。 |
| `pre_dispatch` | `'2*n_jobs'` | 控制并行任务的预派发数量和内存占用。 |
| `error_score` | `nan` | 某候选拟合失败时记录的分数；可设 `'raise'`。 |
| `return_train_score` | 本例 `True` | 是否在 `cv_results_` 中保留训练分数。 |

## `.fit()`

常用形式：`fit(X, y, sample_weight=None, **fit_params)`。

| 参数 | 作用 |
|---|---|
| `X` | 形状通常为 `(n_samples, n_features)` 的训练特征。 |
| `y` | 与 `X` 行数一致的标签或连续响应值。 |
| `sample_weight` | 可选的每样本权重；并非所有模型或版本都支持。 |
| `**fit_params` | 某些元估计器允许继续传入额外具名拟合参数。 |

返回拟合后的模型自身。

## `.predict()`

决策树常用形式：`predict(X, check_input=True)`；`BaggingRegressor.predict(X)` 只要求 `X`。

| 参数 | 作用 |
|---|---|
| `X` | 要预测的二维特征矩阵。 |
| `check_input` | 决策树的可选参数，控制是否进行输入验证；Bagging 的公开 `predict` 不提供该参数。 |

返回每个样本的类别或连续预测值。

## `.predict_proba()`

分类器常用形式：`predict_proba(X)`。

- `X` 是要预测的二维特征矩阵。
- 返回形状通常为 `(n_samples, n_classes)`；第 `j` 列对应 `classes_[j]` 的概率。
- 二分类且类别顺序为 `[0, 1]` 时，`predict_proba(X)[:, 1]` 取得正类 1 的概率。

## `.get_params()` 与 `.set_params()`

| 调用 | 参数 | 作用 |
|---|---|---|
| `estimator.get_params(deep=True)` | `deep=True` 同时返回嵌套估计器参数 | 返回参数字典，键名可用于网格搜索。 |
| `estimator.set_params(**params)` | 例如 `n_estimators=i` | 更新一个或多个具名参数，并返回估计器自身。 |

`set_params()` 只修改配置；必须调用 `.fit()` 才会按新配置训练。嵌套参数名使用双下划线，例如 `estimator__max_depth`。

## `.score()`

调用形式：`score(X, y, sample_weight=None)`。

| 参数 | 作用 |
|---|---|
| `X` | 要评分的特征矩阵。 |
| `y` | 对应真实目标。 |
| `sample_weight` | 可选样本权重。 |

分类器返回平均准确率；回归器通常返回 $R^2$，不是 MSE。

## `accuracy_score()`

调用形式：`accuracy_score(y_true, y_pred, *, normalize=True, sample_weight=None)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `y_true` | `y_test` | 真实类别。 |
| `y_pred` | `prediction` 或 `y_pred` | 模型预测类别。 |
| `normalize` | `True` | 返回正确比例；`False` 返回正确样本数。 |
| `sample_weight` | `None` | 可选样本权重。 |

## `mean_squared_error()`

调用形式：`mean_squared_error(y_true, y_pred, *, sample_weight=None, multioutput='uniform_average')`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `y_true` | `y_test` | 真实连续响应值。 |
| `y_pred` | `y_pred1` 或 `y_pred` | 回归预测值。 |
| `sample_weight` | `None` | 可选样本权重。 |
| `multioutput` | `'uniform_average'` | 多输出任务如何聚合误差；也可传 `'raw_values'` 或权重数组。 |

## `f1_score()`

调用形式：`f1_score(y_true, y_pred, *, labels=None, pos_label=1, average='binary', sample_weight=None, zero_division='warn')`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `y_true` | `np.ravel(y_val)` | 真实类别标签。 |
| `y_pred` | `predictions` | 预测的硬类别标签。 |
| `labels` | `None` | 指定参与计算的类别及顺序。 |
| `pos_label` | `1` | `average='binary'` 时作为正类的标签。 |
| `average` | `'binary'` | 多分类/多标签时如何聚合各类 F1。 |
| `sample_weight` | `None` | 可选的样本权重。 |
| `zero_division` | `'warn'` | 分母为零时的返回和警告策略；可用值随版本变化。 |

## `roc_auc_score()`

调用形式：`roc_auc_score(y_true, y_score, *, average='macro', sample_weight=None, max_fpr=None, multi_class='raise', labels=None)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `y_true` | `y_test` 或 `np.ravel(y_val)` | 真实类别标签。 |
| `y_score` | 推荐 `predict_proba(X)[:, 1]` | 二分类正类的连续预测分数或概率。 |
| `average` | `'macro'` | 多类或多标签任务如何聚合结果。 |
| `sample_weight` | `None` | 可选样本权重。 |
| `max_fpr` | `None` | 可选最大假阳性率，用于标准化部分 AUC。 |
| `multi_class` | `'raise'` | 多分类时选择 `'ovr'` 或 `'ovo'`；默认要求显式指定。 |
| `labels` | `None` | 指定多分类标签顺序。 |

## `permutation_importance()`

调用形式：`permutation_importance(estimator, X, y, *, scoring=None, n_repeats=5, n_jobs=None, random_state=None, sample_weight=None, max_samples=1.0)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `estimator` | `tree` 或 `forest` | 已拟合且提供评分能力的模型。 |
| `X`, `y` | 完整特征和标签 | 用于计算基准分数及置换后分数的数据。 |
| `scoring` | `None` | 评分器；`None` 使用估计器默认 `.score()`。 |
| `n_repeats` | `5` | 每个特征独立置换的重复次数。 |
| `n_jobs` | `None` | 按特征并行计算的任务数。 |
| `random_state` | `random_state` | 固定列置换结果。 |
| `sample_weight` | `None` | 计算分数时使用的可选样本权重。 |
| `max_samples` | `1.0` | 每轮从 `X` 中用于计算的最大样本数或比例。 |

## `tree.plot_tree()`

```text
tree.plot_tree(
    decision_tree, *, max_depth=None, feature_names=None, class_names=None,
    label='all', filled=False, impurity=True, node_ids=False,
    proportion=False, rounded=False, precision=3, ax=None, fontsize=None,
)
```

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `decision_tree` | `dtree` | 已拟合的决策树模型，必需。 |
| `max_depth` | `None` | 只显示到指定深度；不改变模型本身。 |
| `feature_names` | `None` | 节点中显示的特征名称。 |
| `class_names` | `None` | 分类树的类别名称。 |
| `label` | `'all'` | 哪些节点显示字段标签。 |
| `filled` | 本例 `True` | 是否按类别、纯度或回归值填色。 |
| `impurity` | `True` | 是否显示节点不纯度。 |
| `node_ids` | `False` | 是否显示节点编号。 |
| `proportion` | `False` | 是否用比例而非绝对样本数。 |
| `rounded` | `False` | 是否使用圆角节点框。 |
| `precision` | `3` | 浮点数显示位数。 |
| `ax` | `None` | 指定绘制到哪个 Matplotlib Axes。 |
| `fontsize` | 本例 `6` 或自动 | 节点文字大小。 |

## 训练后属性：没有函数参数

| 属性 | 作用 |
|---|---|
| `model.estimators_` | `BaggingRegressor.fit()` 后生成的基估计器列表；`[0]` 取第一棵树。 |
| `tree_model.feature_importances_` | 树训练后生成的特征重要性数组；顺序与训练特征列一致。 |
| `forest.oob_score_` | 使用袋外样本计算的拟合后评分；需在构造模型时启用 `oob_score=True`。 |
| `grid_search.best_estimator_` | 网格搜索按 `refit` 规则选出并在全训练集重训的最佳估计器。 |
| `result.importances_mean` | 置换重要性在多次重复中的平均分数下降。 |

末尾下划线 `_` 是 scikit-learn 对“拟合后才存在的属性”的命名惯例。

## 官方参考

- [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
- [BaggingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html)
- [BaggingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html)
- [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)
- [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
- [permutation_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html)
- [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
