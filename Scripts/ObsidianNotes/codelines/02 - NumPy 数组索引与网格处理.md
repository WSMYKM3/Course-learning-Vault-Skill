---
course: "Machine Learning and AI with Python"
type: code-reference
topic: "NumPy 数组索引与网格处理"
tags:
  - code-reference
  - python
  - numpy
  - array
aliases:
  - NumPy codelines
---

# NumPy 数组索引与网格处理

返回索引：[[00 - Codelines 索引]]

本页函数逐参数说明：[[09 - NumPy 函数参数详解]]、[[12 - Python 内置函数与自定义函数参数详解]]。

## 唯一值和最优索引

| 代码行 | 作用 |
|---|---|
| `import numpy as np` | 以别名 `np` 导入 NumPy。 |
| `x1_unique = np.unique(tree_df['x1'].values)` | 提取 `x1` 的已排序唯一值，作为候选分割值。 |
| `idx = np.argmin(gini_scores)` | 返回 Gini 分数最小值所在的索引。 |
| `best_pred = np.argmin([min(gini_x1), min(gini_x2)])` | 比较两个特征的最小 Gini，并返回较优特征的位置。 |
| `best_value = unique_values[idx]` | 用最优索引取出相应候选值。 |
| `threshold = (unique_values[idx] + unique_values[idx + 1]) / 2` | 取最优候选值和下一个唯一值的中点作为切分阈值。 |

> [!warning]
> 使用 `idx + 1` 前要确保最优索引不是数组最后一项；实际搜索切分点时通常不把最大唯一值作为有效候选。

## 生成连续预测点

| 代码行 | 作用 |
|---|---|
| `xrange = np.linspace(x.min(), x.max(), 80)` | 在最小值到最大值之间等距生成 80 个点。 |
| `xrange = np.linspace(x.min(), x.max(), 80).reshape(-1, 1)` | 将等距点转成模型需要的二维单特征矩阵。 |
| `n = np.linspace(1, 250, 250).astype(int)` | 生成从 1 到 250 的整数 bootstrap 数量序列。 |
| `np.arange(x_min, x_max, 0.1)` | 按固定步长生成坐标序列。 |

## 数组形状转换

| 代码行 | 作用 |
|---|---|
| `x1.ravel()` | 将任意维数组按行展开为一维视图。 |
| `class_pred.reshape(xx1.shape)` | 把一维预测结果恢复为坐标网格的二维形状。 |
| `np.array(y_hats)` | 将 Python 列表转换为 NumPy 数组。 |
| `np.mean(predictions, axis=0)` | 沿模型维度求平均，得到每个样本的平均预测。 |
| `np.ravel(y_train)` | 将二维单列标签 `(n, 1)` 展平为多数分类器期望的一维形状 `(n,)`。 |
| `np.round(roc_auc_score(y_test, y_proba), 2)` | 将指标结果四舍五入到两位小数。 |

## 构造二维网格

```python
xx1, xx2 = np.meshgrid(                                      # 将两条一维坐标轴扩展为二维坐标网格
    np.arange(x1_min, x1_max, 0.1),                          # 生成横轴上的候选坐标
    np.arange(x2_min, x2_max, 0.1),                          # 生成纵轴上的候选坐标
)                                                               # 结束 meshgrid 调用
X_plot = np.c_[xx1.ravel(), xx2.ravel()]                     # 将两张坐标网格合并为模型可预测的二维样本矩阵
grid_pred = model.predict(X_plot)                            # 对网格中的每个坐标点预测类别
grid_pred = grid_pred.reshape(xx1.shape)                     # 恢复二维网格形状，供 contourf 绘制
```

`np.meshgrid()` 与 `np.c_[]` 常用于绘制[[决策边界 (Decision Boundary)]]。

## Bootstrap 随机索引

| 代码行 | 作用 |
|---|---|
| `np.arange(y_train.shape[0])` | 生成训练样本的全部行索引。 |
| `resample_indexes = np.random.choice(np.arange(y_train.shape[0]), size=y_train.shape[0])` | 有放回抽取与训练集等长的随机索引。 |
| `X_boot = X_train[resample_indexes]` | 按随机索引构造自助特征集。 |
| `y_boot = y_train[resample_indexes]` | 使用相同索引构造配对的自助标签集。 |

> [!important]
> 特征和标签必须使用同一个 `resample_indexes`，否则样本与标签会错位。
