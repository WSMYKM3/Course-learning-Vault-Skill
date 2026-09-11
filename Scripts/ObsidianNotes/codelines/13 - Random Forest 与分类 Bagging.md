---
course: "Machine Learning and AI with Python"
type: code-reference
topic: "Random Forest 与分类 Bagging"
tags:
  - code-reference
  - python
  - random-forest
  - bagging
  - ensemble-learning
aliases:
  - Random Forest codelines
  - 随机森林代码行
---
·
# Random Forest 与分类 Bagging

返回索引：[[00 - Codelines 索引]]

本页函数逐参数说明：[[10 - scikit-learn 函数参数详解]]；数据选择见 [[01 - Pandas 数据读取清洗与筛选]]。

相关课程笔记：[[3.1 - 集成学习与袋装法]]、[[3.2 - 袋外误差与相关树]]。

## 准备特征和标签

| 代码行 | 作用 |
|---|---|
| `from sklearn.ensemble import RandomForestClassifier, BaggingClassifier` | 导入随机森林分类器和通用分类 Bagging。 |
| `X = df.drop('Outcome', axis=1)` | 删除标签列，保留 DataFrame 形式的全部特征。 |
| `y = df['Outcome']` | 选择一维标签 Series。 |
| `X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.8, random_state=144)` | 用 80% 数据训练，并固定划分结果。 |

## 使用 BaggingClassifier

```python
max_depth = 20                                                   # 统一限制每棵基树的最大深度
n_estimators = 1000                                              # 指定 Bagging 中的树数量
basemodel = DecisionTreeClassifier(                              # 创建要重复训练的基分类器
    max_depth=max_depth,                                         # 限制单棵树复杂度
    random_state=random_state,                                   # 固定基树随机性
)                                                               # 结束基分类器构造
bagging = BaggingClassifier(                                     # 创建分类 Bagging 集成
    estimator=basemodel,                                         # 使用上面的决策树作为基估计器
    n_estimators=n_estimators,                                   # 训练指定数量的基树
    random_state=random_state,                                   # 固定 bootstrap 抽样结果
)                                                               # 结束 Bagging 构造
bagging.fit(X_train, y_train)                                    # 在训练集上拟合集成模型
predictions = bagging.predict(X_val)                             # 聚合所有树并预测验证集类别
acc_bag = round(accuracy_score(y_val, predictions), 2)           # 计算并保留两位小数的准确率
```

| 代码行 | 作用 |
|---|---|
| `bagging.estimators_[0]` | 取得拟合后的第 1 棵基树。 |
| `bagging.estimators_[100]` | 取得拟合后的第 101 棵基树。 |
| `bagging.predict(X_val)` | 对每个样本进行基分类器投票，返回最终类别。 |

> [!note]
> `estimators_` 末尾的下划线表示它是 `.fit()` 后才生成的属性；索引从 `0` 开始。

## 使用 RandomForestClassifier

```python
random_forest = RandomForestClassifier(                          # 创建随机森林分类器
    max_depth=max_depth,                                         # 限制每棵树的最大深度
    n_estimators=n_estimators,                                   # 指定森林中的树数量
    max_features='sqrt',                                         # 每次分割只随机考虑 sqrt(p) 个特征
    random_state=random_state,                                   # 固定抽样和建树随机性
)                                                               # 结束随机森林构造
random_forest.fit(X_train, y_train)                              # 在训练集上拟合森林
predictions = random_forest.predict(X_val)                       # 预测验证集类别
acc_rf = round(accuracy_score(y_val, predictions), 2)            # 计算验证准确率
```

Random Forest 与普通树 Bagging 的关键区别：Random Forest 不仅对样本做 bootstrap，还在每个节点分割时随机抽取候选特征。`max_features='sqrt'` 用来降低树之间的相关性。

## 类别权重

| 代码行 | 作用 |
|---|---|
| `RandomForestClassifier(class_weight='balanced_subsample', ...)` | 每棵树根据自己的 bootstrap 样本类别频率计算反比权重。 |
| `random_forest.fit(X_train, np.ravel(y_train))` | 将形如 `(n, 1)` 的标签压成 `(n,)` 后拟合模型。 |

`class_weight='balanced_subsample'` 只改变训练损失中的类别权重，不会生成或删除样本。SMOTE 和下采样见 [[15 - 类别不平衡与重采样]]。

## 用 dtreeviz 查看集成中的树

```python
tree_in_bagging = bagging.estimators_[0]                         # 从已拟合 Bagging 中取一棵树
viz = dtreeviz.model(                                            # 构造可视化模型包装器
    tree_in_bagging,                                             # 要解释的决策树
    df.iloc[:, :8],                                              # 特征数据
    df['Outcome'],                                               # 目标标签
    feature_names=df.columns[:8],                                # 节点中显示的特征名
    target_name='Diabetes',                                      # 目标变量显示名
    class_names=['No', 'Yes'],                                   # 类别显示名
)                                                               # 结束可视化模型构造
viz.view(                                                        # 渲染树结构
    fontname='monospace', label_fontsize=18,                     # 设置字体和标签字号
    ticks_fontsize=16, scale=1.4,                                # 设置刻度字号和整体缩放
)                                                               # 结束渲染调用
```

`dtreeviz.model()` 的前三个参数依次是模型、特征和目标；特征列的顺序必须与训练模型时一致。
