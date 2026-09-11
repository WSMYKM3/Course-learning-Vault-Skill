---
course: "Machine Learning and AI with Python"
type: parameter-reference
topic: "Python 内置函数与自定义函数参数"
tags:
  - code-reference
  - python
  - parameters
  - functions
aliases:
  - Python 参数速查
---

# Python 内置函数与自定义函数参数详解

返回索引：[[00 - Codelines 索引]]。

## `min()` 和 `max()`

两种调用形式：

```text
min(iterable, *, key=None, default=...)
min(arg1, arg2, *args, key=None)
```

`max()` 参数规则相同，只是返回最大值。

| 参数 | 作用 |
|---|---|
| `iterable` | 一个可迭代对象，例如 Gini 分数列表。 |
| `arg1, arg2, *args` | 直接比较两个或更多位置参数；`*args` 表示数量可继续增加。 |
| `key` | 比较前应用的函数，例如 `key=len`。 |
| `default` | iterable 为空时的返回值；仅 iterable 形式支持。 |

`max(1e-5, left_1 + left_0)` 比较两个数，确保分母至少为 `1e-5`。

## `range()`

支持三种参数数量：`range(stop)`、`range(start, stop)`、`range(start, stop, step)`。

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `start` | `0` | 起点，包含。 |
| `stop` | 必需 | 终点，不包含。 |
| `step` | `1` | 步长，不能为 0。 |

`range(num_bootstraps)` 只传一个参数，因此从 0 迭代到 `num_bootstraps - 1`。

## `enumerate()`

调用形式：`enumerate(iterable, start=0)`。

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `iterable` | 必需 | 要遍历的可迭代对象。 |
| `start` | `0` | 第一个计数值。 |

返回 `(计数, 元素)` 对；课程用它同时取得分割序号和分割规则。

## `zip()`

调用形式：`zip(*iterables, strict=False)`。

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `*iterables` | 一个或多个可迭代对象 | 把相同位置的元素组合成元组；输入数量可变。 |
| `strict` | `False` | `True` 时输入长度不同会抛错；较新 Python 版本支持。 |

## `sorted()`

调用形式：`sorted(iterable, *, key=None, reverse=False)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `iterable` | `zip(x, y)` | 要排序的可迭代对象；课程中每个元素是 `(x_i, y_i)`。 |
| `key` | `None` | 默认直接比较元素；元组会先比较第一个值，因此按 `x_i` 排序。 |
| `reverse` | `False` | `False` 升序，`True` 降序。 |

`list(zip(*sorted(zip(x, y))))` 会先保持 x/y 配对排序，再将两列拆开。

## `float()`

调用形式：`float(x=0.0)`。

- `float('inf')` 创建正无穷，可用于初始化“当前最小误差”。
- 省略参数时返回 `0.0`；传数字或合规字符串时转换为浮点数。

## 字典 `.items()`

调用形式：`dictionary.items()`，没有参数。

返回字典键值对的动态视图；`for label, errors in error_rate.items():` 会在每轮同时解包键和值。

## `lambda` 排序键

`lambda item: (item[1], -item[0])` 是匿名函数，不是一次立即调用。它接收一个二元组 `item`，返回“误差、负树数量”作为比较键：`min(..., key=...)` 会先选误差更小者，误差相同时选树数量更大者。

## `len()`

调用形式：`len(object)`。

- `object` 是唯一必需参数，必须实现长度协议。
- 返回整数长度，例如分割规则数或特征列数。

## `round()`

调用形式：`round(number, ndigits=None)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `number` | MSE 或准确率 | 要舍入的数字。 |
| `ndigits` | `2` 或 `4` | 保留小数位；省略时返回最接近的整数。可为负数以舍入到十位、百位。 |

## `print()`

调用形式：`print(*objects, sep=' ', end='\n', file=None, flush=False)`。

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `*objects` | 可为 0 个、1 个或多个对象 | 依次转换为文本并输出。 |
| `sep` | 空格 | 多个对象间的分隔文本。 |
| `end` | 换行符 | 输出末尾追加的文本。 |
| `file` | 标准输出 | 输出目标文件对象。 |
| `flush` | `False` | 是否立即刷新输出缓冲区。 |

## 列表 `.append()`

调用形式：`list.append(object)`。

- `object` 是唯一参数，可以是任何 Python 对象。
- 原地把对象添加到列表尾部，返回 `None`。
- `predictions.append(pred)` 会把整条预测数组作为一个元素加入，而不是逐个加入预测值。

## 字典与列表字面量不是函数参数

- `obs = {'x1': x1_i, 'x2': x2_i}` 中冒号左侧是键，右侧是值。
- `splits = [('x2', threshold), ('x1', threshold_2)]` 中每个二元组依次表示特征名和阈值。
- 这些是容器构造语法，不是普通函数调用。

## 课程自定义函数

### `get_total_gini(predictor_values, pred_name, df)`

| 参数 | 作用 |
|---|---|
| `predictor_values` | 当前特征的候选分割值数组。 |
| `pred_name` | 当前特征在 DataFrame 中的列名字符串。 |
| `df` | 包含特征列和标签列 `y` 的当前父区域数据。 |

三个参数都没有默认值，调用时必须全部提供。返回与候选值等长的加权 Gini 列表。

### `get_threshold(unique_values, gini_scores)`

| 参数 | 作用 |
|---|---|
| `unique_values` | 已排序的唯一特征值。 |
| `gini_scores` | 与唯一值一一对应的加权 Gini。 |

两个参数都必需。返回最优候选值与下一个唯一值的中点。

### `report_splits(x1_unique, x2_unique, x1_total_gini, x2_total_gini)`

| 参数 | 作用 |
|---|---|
| `x1_unique`, `x2_unique` | 两个特征各自的候选值。 |
| `x1_total_gini`, `x2_total_gini` | 两个特征各候选值对应的 Gini。 |

四个参数都必需。函数打印最佳特征和候选值，不显式返回结果。

### `get_split_labels(splits)`

| 参数 | 作用 |
|---|---|
| `splits` | `[(特征名, 阈值), ...]` 列表；可包含一条或多条顺序分割规则。 |

返回字典列表，每个字典含当前分割左右区域的多数类。

### `predict_class(x1, x2, splits)`

| 参数 | 作用 |
|---|---|
| `x1`, `x2` | 形状一致的特征数组或坐标网格。 |
| `splits` | 按执行顺序排列的 `(特征名, 阈值)` 规则列表。 |

返回展平的一维类别预测数组。

### `prediction_by_bagging(X_train, y_train, X_to_evaluate, num_bootstraps)`

| 参数 | 作用 |
|---|---|
| `X_train` | 用于 Bootstrap 的二维训练特征。 |
| `y_train` | 与训练特征逐行对应的标签。 |
| `X_to_evaluate` | 要获得最终集成预测的二维特征。 |
| `num_bootstraps` | 自助样本和基分类树数量，应为正整数。 |

返回所有树多数投票后的 `0/1` 类别数组。

### `plot_boundary(df, model_1, model_2)`

这是 `exe11/helper.py` 提供的课程辅助函数，而不是标准库函数。

| 参数 | 作用 |
|---|---|
| `df` | 用于绘制样本点和确定坐标范围的数据。 |
| `model_1`, `model_2` | 两个已拟合分类器，用于比较决策边界。 |

三个参数都必需；具体绘制细节由课程的 `helper.py` 实现。

### `plot_feature_importance(model1, model2, X, y)`

这是 `exe43/helper.py` 提供的 MDI 特征重要性比较函数。

| 参数 | 作用 |
|---|---|
| `model1` | 已拟合的单棵决策树，需提供 `feature_importances_`。 |
| `model2` | 已拟合的随机森林，需提供 `feature_importances_`。 |
| `X` | 带列名的特征 DataFrame，用于 y 轴标签和特征顺序。 |
| `y` | 课程 helper 保留的必需位置参数；当前函数体没有使用它。 |

### `plot_permute_importance(result1, result2, X, y)`

这是 `exe43/helper.py` 提供的置换重要性比较函数。

| 参数 | 作用 |
|---|---|
| `result1` | 单树的 `permutation_importance()` 返回对象。 |
| `result2` | 随机森林的 `permutation_importance()` 返回对象。 |
| `X` | 带列名的特征 DataFrame，用于 y 轴标签和排序。 |
| `y` | 课程 helper 保留的必需位置参数；当前函数体没有使用它。 |

## `PrettyTable()` 与 `.add_row()`

课程用法：

```python
pt = PrettyTable()
pt.field_names = ['Max Depth', 'Features', 'Train Accuracy', 'Test Accuracy']
pt.add_row([2, len(pred_cols), round(train_acc, 4), round(test_acc, 4)])
```

| 调用/属性 | 参数说明 |
|---|---|
| `PrettyTable(field_names=None, **kwargs)` | `field_names` 可在构造时提供表头；`**kwargs` 可设置对齐、边框和样式等选项。课程无参数创建空表。 |
| `pt.field_names = [...]` | 属性赋值，不是函数；列表长度决定列数。 |
| `pt.add_row(row, divider=False)` | `row` 是一行数据，长度必须匹配列数；`divider=True` 可在该行后添加分隔线。 |

## 官方参考

- [Python built-in functions](https://docs.python.org/3/library/functions.html)
