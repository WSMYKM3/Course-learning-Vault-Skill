---
course: "Machine Learning and AI with Python"
type: parameter-reference
topic: "NumPy 函数参数"
tags:
  - code-reference
  - python
  - numpy
  - parameters
aliases:
  - NumPy 参数速查
---

# NumPy 函数参数详解

返回索引：[[00 - Codelines 索引]]；对应代码：[[02 - NumPy 数组索引与网格处理]]。

## `np.unique()`

调用形式：`np.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None, *, equal_nan=True, sorted=True)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `ar` | `tree_df['x1'].values`，必需 | 要去重的输入数组。 |
| `return_index` | `False` | 是否同时返回每个唯一值第一次出现的位置。 |
| `return_inverse` | `False` | 是否返回可用于重建原数组的反向索引。 |
| `return_counts` | `False` | 是否同时返回每个唯一值的出现次数。 |
| `axis` | `None` | `None` 先展平；指定轴时沿该轴寻找唯一子数组。 |
| `equal_nan` | `True` | 是否把多个 NaN 合并为一个唯一值。 |
| `sorted` | `True` | 是否排序结果；较旧 NumPy 版本可能没有此参数。 |

## `np.argmin()`

调用形式：`np.argmin(a, axis=None, out=None, *, keepdims=False)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `a` | `gini_scores`，必需 | 要搜索最小值位置的数组。 |
| `axis` | `None` | 在展平数组中搜索；整数表示沿指定轴搜索。 |
| `out` | `None` | 可选的结果输出数组。 |
| `keepdims` | `False` | 是否保留被压缩的轴。 |

## `np.linspace()`

调用形式：`np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0, *, device=None)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `start` | `x.min()` 或 `1` | 序列起点。 |
| `stop` | `x.max()` 或 `250` | 序列终点。 |
| `num` | `80` 或 `250` | 生成多少个等距值，不是步长。 |
| `endpoint` | `True` | 是否包含 `stop`。 |
| `retstep` | `False` | 是否同时返回实际步长。 |
| `dtype` | `None` | 指定输出类型；默认自动推断。 |
| `axis` | `0` | 起止值为数组时，沿哪个轴放置样本。 |
| `device` | `None` | Array API 设备参数，普通 NumPy 通常不设置。 |

## `np.arange()`

可传 1、2 或 3 个主要位置参数：

```python
np.arange(stop)               # start=0、step=1
np.arange(start, stop)        # step=1
np.arange(start, stop, step)  # 三者全部指定
```

完整形式：`np.arange([start,] stop[, step], dtype=None, *, device=None, like=None)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `start` | `x_min`；省略时为 `0` | 半开区间起点，包含该值。 |
| `stop` | `x_max`，必需 | 半开区间终点，不包含该值。 |
| `step` | `0.1` 或 `1`；默认 `1` | 相邻值间隔。 |
| `dtype` | `None` | 输出数据类型。 |
| `device` | `None` | Array API 设备参数。 |
| `like` | `None` | 允许兼容数组类型接管创建过程。 |

浮点步长可能累积误差；需要固定点数时优先使用 `linspace()`。

## `.reshape()`

课程调用：`array.reshape(-1, 1)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `shape` | `(-1, 1)` | 新形状；`-1` 让 NumPy 自动推断行数，`1` 指一列。也可写成一个元组参数。 |
| `order` | `'C'` | `'C'` 按行优先，`'F'` 按列优先，`'A'` 根据内存布局决定。 |
| `copy` | 通常 `None` | 是否允许或强制复制；支持情况随 NumPy 版本变化。 |

元素总数不能改变。

## `np.ravel()` 与 `.ravel()`

调用形式：`np.ravel(a, order='C')` 或 `array.ravel(order='C')`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `a` | `y_train` | 仅函数形式需要；指定要展平的数组状输入。 |
| `order` | `'C'` | 展平顺序，可选 `'C'`、`'F'`、`'A'`、`'K'`。 |

它尽量返回视图，无法返回视图时才复制。

## `np.round()`

调用形式：`np.round(a, decimals=0, out=None)`；别名为 `np.around()`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `a` | ROC AUC 数值 | 要舍入的标量或数组。 |
| `decimals` | 本例 `2` | 保留的小数位；负数可舍入到十位、百位。 |
| `out` | `None` | 可选的结果输出数组，形状必须匹配。 |

标量输入通常返回 NumPy 标量；它与 Python 内置 `round()` 的边界行为和返回类型不一定完全相同。

## `ndarray.astype()`

调用形式：`array.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `dtype` | 本例 `int`，必需 | 目标数组元素类型。 |
| `order` | `'K'` | 返回数组的内存顺序。 |
| `casting` | `'unsafe'` | 允许的数据类型转换安全级别。 |
| `subok` | `True` | 是否保留 ndarray 子类。 |
| `copy` | `True` | 是否总是返回新数组；允许时设 `False` 可复用输入。 |

`np.linspace(...).astype(int)` 把等距浮点结果转为整数；`(mean > 0.5).astype(int)` 把布尔投票转为 `0/1`。

## `np.array()`

调用形式：`np.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0, *, like=None)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `object` | `y_hats`，必需 | 要转换的列表、元组或数组状对象。 |
| `dtype` | `None` | 指定元素类型。 |
| `copy` | 依版本默认策略 | 是否复制输入。 |
| `order` | `'K'` | 内存布局顺序。 |
| `subok` | `False` | 是否保留 ndarray 子类。 |
| `ndmin` | `0` | 返回数组至少具有多少维。 |
| `like` | `None` | 允许兼容数组实现接管创建过程。 |

## `np.mean()`

调用形式：`np.mean(a, axis=None, dtype=None, out=None, keepdims=False, *, where=True)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `a` | `predictions`，必需 | 要计算平均值的数组。 |
| `axis` | 本例 `0` | 跨不同模型对同一样本求平均；`None` 表示所有元素一起平均。 |
| `dtype` | `None` | 指定累加和结果类型。 |
| `out` | `None` | 可选的结果输出数组。 |
| `keepdims` | `False` | 是否保留被聚合的轴。 |
| `where` | `True` | 用布尔条件选择参与平均的元素。 |

## `np.meshgrid()`

调用形式：`np.meshgrid(*xi, copy=True, sparse=False, indexing='xy')`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `*xi` | 两个 `np.arange(...)` 数组 | 一个或多个一维坐标数组；`*` 表示数量可变。 |
| `copy` | `True` | 是否复制输出网格。 |
| `sparse` | `False` | 是否返回节省内存的稀疏网格。 |
| `indexing` | `'xy'` | `'xy'` 使用笛卡尔绘图习惯；`'ij'` 使用矩阵索引习惯。 |

传两个坐标数组返回两个二维网格；传三个则返回三个三维网格。

## `np.random.choice()`

调用形式：`np.random.choice(a, size=None, replace=True, p=None)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `a` | `np.arange(y_train.shape[0])` | 一维候选数组；也可传整数 `n`，表示从 `0...n-1` 抽取。 |
| `size` | `y_train.shape[0]` | 输出样本形状；整数表示抽多少个。 |
| `replace` | 默认 `True` | 是否有放回；课程虽未显式写出，但默认值正好符合 Bootstrap。 |
| `p` | `None` | 每个候选值的抽样概率；`None` 表示均匀抽样。 |

现代写法可先创建 `rng = np.random.default_rng(seed)`，再调用 `rng.choice(...)`。

## `np.c_[]`

`np.c_[xx1.ravel(), xx2.ravel()]` 不是普通函数，而是索引拼接语法：

- 第 1 个逗号项生成结果第 1 列。
- 第 2 个逗号项生成第 2 列。
- 可以继续增加逗号项，拼接更多列。
- 各输入沿拼接方向必须具有兼容长度。

## 数组方法 `.min()` 与 `.max()`

常用形式：`array.min(axis=None, out=None, keepdims=False, initial=None, where=True)`，`.max()` 参数相同。

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `axis` | `None` | 沿哪个轴求最小/最大；`None` 搜索所有元素。 |
| `out` | `None` | 可选输出数组。 |
| `keepdims` | `False` | 是否保留被聚合的轴。 |
| `initial` | `None` | 参与比较的初始值。 |
| `where` | `True` | 选择参与比较的元素。 |

## `.shape` 属性

`array.shape` 不是函数，没有参数；它返回各维长度组成的元组。`y_train.shape[0]` 取第 0 维，即样本数。

## 官方参考

- [NumPy array creation routines](https://numpy.org/doc/stable/reference/routines.array-creation.html)
- [NumPy array manipulation routines](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)
