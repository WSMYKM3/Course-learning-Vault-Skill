---
course: "Machine Learning and AI with Python"
type: parameter-reference
topic: "Pandas 函数参数"
tags:
  - code-reference
  - python
  - pandas
  - parameters
aliases:
  - Pandas 参数速查
---

# Pandas 函数参数详解

返回索引：[[00 - Codelines 索引]]；对应代码：[[01 - Pandas 数据读取清洗与筛选]]。

## 参数数量怎么看

- `function(required, optional=default)`：无默认值的参数必须提供；有默认值的参数可以省略。
- `/` 前的参数只能按位置传入；`*` 后的参数必须使用 `参数名=值`。
- `*args` 表示可以继续传入多个位置参数；`**kwargs` 表示可以继续传入多个具名参数。

## `pd.read_csv()`

课程代码：

```python
df = pd.read_csv('airquality.csv', index_col=0)
```

### 本行参数逐项拆解

| 参数 | 本例值 | 必需性 | 作用 |
|---|---:|---|---|
| `filepath_or_buffer` | `'airquality.csv'` | 必需 | CSV 文件路径、URL、路径对象或可读取的文件对象；这是第 1 个位置参数。 |
| `index_col` | `0` | 可选，默认 `None` | 指定行索引列；整数 `0` 表示把 CSV 第 1 列作为 DataFrame 索引。也可传列名、列号列表或 `False`。 |

只传一个参数也合法：

```python
df = pd.read_csv('agriland.csv')  # 只指定文件路径，其余参数全部使用默认值
```

### 完整参数形式

```text
pd.read_csv(
    filepath_or_buffer,
    *,
    sep=',', delimiter=None, header='infer', names=None,
    index_col=None, usecols=None, dtype=None, engine=None, converters=None,
    true_values=None, false_values=None,
    skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None,
    na_values=None, keep_default_na=True, na_filter=True, skip_blank_lines=True,
    parse_dates=None, date_format=None, dayfirst=False, cache_dates=True,
    iterator=False, chunksize=None,
    compression='infer', thousands=None, decimal='.', lineterminator=None,
    quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None,
    encoding=None, encoding_errors='strict', dialect=None,
    on_bad_lines='error', low_memory=True, memory_map=False,
    float_precision=None, storage_options=None, dtype_backend=None,
)
```

| 参数组 | 参数 | 作用 |
|---|---|---|
| 分隔与表头 | `sep`, `delimiter` | 指定字段分隔符；通常只设置其中一个。 |
| 分隔与表头 | `header` | 表头所在行；`'infer'` 自动判断，`None` 表示文件没有表头。 |
| 分隔与表头 | `names` | 手动提供列名序列。 |
| 行列选择 | `index_col` | 指定哪一列或哪些列作为行索引。 |
| 行列选择 | `usecols` | 只读取指定列，可传列名列表、列号列表或判断函数。 |
| 行列选择 | `skiprows`, `skipfooter`, `nrows` | 跳过开头行、跳过末尾行或限制读取行数。 |
| 数据类型 | `dtype` | 指定整表或各列的数据类型。 |
| 数据类型 | `converters` | 为指定列提供转换函数；对同一列会优先于 `dtype`。 |
| 布尔值 | `true_values`, `false_values` | 指定哪些文本解析为布尔真或假。 |
| 缺失值 | `na_values` | 增加要识别为缺失值的文本。 |
| 缺失值 | `keep_default_na` | 是否同时保留 Pandas 默认缺失值标记。 |
| 缺失值 | `na_filter` | 是否检测缺失值；确定没有缺失值时关闭可提升性能。 |
| 缺失值 | `skip_blank_lines` | 是否跳过空白行。 |
| 日期 | `parse_dates` | 指定要解析为日期的列。 |
| 日期 | `date_format` | 指定日期格式。 |
| 日期 | `dayfirst` | 含糊日期是否优先按“日/月/年”解释。 |
| 日期 | `cache_dates` | 是否缓存重复日期字符串的解析结果。 |
| 解析器 | `engine` | 选择 C、Python 或 PyArrow 等解析引擎。 |
| 解析器 | `low_memory` | C 引擎是否分块推断类型。 |
| 解析器 | `float_precision` | 控制 C 引擎的浮点数转换精度。 |
| 分块读取 | `iterator` | 是否返回可迭代的 `TextFileReader`。 |
| 分块读取 | `chunksize` | 每块读取的行数；设置后返回分块读取器。 |
| 数字文本 | `thousands`, `decimal` | 指定千位符和小数点字符。 |
| 文本格式 | `skipinitialspace` | 是否忽略分隔符后的空格。 |
| 文本格式 | `lineterminator` | 指定行结束符。 |
| 引号转义 | `quotechar`, `quoting`, `doublequote`, `escapechar` | 控制引号字段与转义字符。 |
| 注释坏行 | `comment` | 指定注释起始字符。 |
| 注释坏行 | `on_bad_lines` | 字段数量错误时选择报错、警告、跳过或自定义处理。 |
| 编码 | `encoding`, `encoding_errors` | 指定文本编码及编码错误处理方式。 |
| 压缩远程 | `compression` | 指定或自动推断 gzip、zip 等压缩格式。 |
| 压缩远程 | `storage_options` | 向远程存储后端传递认证或连接参数。 |
| 其他 | `dialect` | 使用 CSV dialect 一次性覆盖多个解析设置。 |
| 其他 | `memory_map` | 本地文件是否使用内存映射。 |
| 其他 | `dtype_backend` | 选择 NumPy nullable、PyArrow 等返回类型后端。 |

返回值通常是 `DataFrame`；设置 `iterator=True` 或 `chunksize` 后返回 `TextFileReader`。

## `DataFrame.head()`

调用形式：`df.head(n=5)`。

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `n` | `5` | 返回前 `n` 行；负数表示返回除最后 `abs(n)` 行之外的所有行。 |

`df.head()` 使用默认 5 行；`df.head(10)` 明确传入 `n=10`。

## `DataFrame.drop()`

课程调用：`df.drop('Outcome', axis=1)`。

常用形式：`df.drop(labels=None, *, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `labels` | `'Outcome'` | 要删除的标签；与 `axis=1` 组合表示删除列。 |
| `axis` | 本例 `1` | `0`/`'index'` 删除行，`1`/`'columns'` 删除列。 |
| `index` | `None` | 直接按行标签删除，可替代 `labels` 与 `axis=0`。 |
| `columns` | `None` | 直接按列名删除；`df.drop(columns='Outcome')` 语义更清楚。 |
| `level` | `None` | MultiIndex 中指定要匹配的层级。 |
| `inplace` | `False` | 默认返回新 DataFrame，不修改原对象。 |
| `errors` | `'raise'` | 标签不存在时抛错；`'ignore'` 会忽略不存在的标签。 |

## `Series.notna()`

调用形式：`df.Ozone.notna()`。

- 没有参数。
- 返回与原 Series 等长的布尔 Series：非缺失值为 `True`，缺失值为 `False`。

## `Series.astype()`

常见调用形式：`series.astype(dtype, copy=True, errors='raise')`；较新 Pandas 版本可能调整 `copy` 的默认策略。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `dtype` | 本例 `int`，必需 | 目标数据类型；DataFrame 还可传 `{列名: 类型}` 字典。 |
| `copy` | 常见默认 `True` | 是否复制底层数据；具体复制行为也受 Pandas 版本影响。 |
| `errors` | `'raise'` | 转换失败时抛错；`'ignore'` 表示保留原对象。 |

## `Series.mode()`

调用形式：`series.mode(dropna=True)`。

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `dropna` | `True` | 是否忽略缺失值后再计算众数。 |

可能有多个并列众数，所以返回 Series；`.iloc[0]` 取第一个结果。

## `Series.sum()`

调用形式：`series.sum(axis=0, skipna=True, numeric_only=False, min_count=0, **kwargs)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `axis` | `0` | Series 只有一个数据轴；通常不用设置。 |
| `skipna` | `True` | 是否忽略缺失值。 |
| `numeric_only` | `False` | 是否只包含数值、布尔类型。 |
| `min_count` | `0` | 至少需要多少个非缺失值才返回结果，否则返回缺失值。 |
| `**kwargs` | 未使用 | 为兼容 NumPy 接口保留的额外参数。 |

课程中布尔 Series 的 `.sum()` 会把 `True` 当作 1，从而统计满足条件的样本数。

## `Series.value_counts()`

调用形式：`series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)`。

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `normalize` | `False` | `False` 返回次数，`True` 返回比例。 |
| `sort` | `True` | 是否按出现次数排序。 |
| `ascending` | `False` | 是否按升序排列次数。 |
| `bins` | `None` | 对数值数据分箱后再计数；传整数表示箱数。 |
| `dropna` | `True` | 是否排除缺失值。 |

## `DataFrame.sample()`

课程调用：`df.sample(frac=1, replace=True)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `n` | `None` | 指定抽取多少行；不能与 `frac` 同时使用。 |
| `frac` | 本例 `1` | 按原数据比例抽样；`1` 表示抽取与原数据相同数量。 |
| `replace` | 本例 `True` | 是否有放回抽样；Bootstrap 要设为 `True`。 |
| `weights` | `None` | 为各行提供非均匀抽样权重。 |
| `random_state` | `None` | 固定随机抽样结果。 |
| `axis` | `None` | 抽样轴；常用 `axis=0` 抽行、`axis=1` 抽列。 |
| `ignore_index` | `False` | 是否把结果索引重置为 `0...n-1`。 |

`n` 与 `frac` 都省略时默认抽取 1 行。

## `pd.Series()`

课程调用：`pd.Series(dt3.feature_importances_, index=pred_cols, name='importance')`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `data` | `dt3.feature_importances_` | Series 的数据。 |
| `index` | `pred_cols` | 每个值对应的索引标签，长度必须匹配。 |
| `dtype` | `None` | 可选的数据类型。 |
| `name` | `'importance'` | Series 名称。 |
| `copy` | `None` | 是否复制输入数据。 |

## `Series.sort_values()`

调用形式：`series.sort_values(axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `axis` | `0` | Series 只有一个轴。 |
| `ascending` | 本例 `False` | `False` 从大到小，`True` 从小到大。 |
| `inplace` | `False` | 是否原地修改。 |
| `kind` | `'quicksort'` | 排序算法。 |
| `na_position` | `'last'` | 缺失值放开头还是末尾。 |
| `ignore_index` | `False` | 是否重置排序后的索引。 |
| `key` | `None` | 排序前应用的向量化转换函数。 |

## `pd.set_option()`

调用形式：`pd.set_option(*args)`，参数按 `配置名, 值` 成对出现。

| 参数 | 本例 | 作用 |
|---|---|---|
| `pat` | `'display.width'` 或 `'display.max_columns'` | 配置项名称或唯一匹配模式。 |
| `value` | `100` 或 `20` | 配置项的新值。 |

可以一次传一对，也可继续传多对，例如 `pd.set_option('display.width', 100, 'display.max_columns', 20)`。它修改当前会话配置，不返回数据。

## `.loc[]`、`.iloc[]`、`[]` 与 `.values`

这些是索引器或属性，不是普通函数，因此没有圆括号参数。

| 语法 | “参数”位置 | 作用 |
|---|---|---|
| `df[columns]` | `columns` 可为单个列名、列名列表或布尔行掩码 | 单列名返回 Series；列名列表返回 DataFrame；布尔掩码筛选行。 |
| `df.loc[row_selector, column_selector]` | 逗号前选择行，逗号后选择列 | 按标签或布尔条件选择；任一侧都可用 `:` 表示全部。 |
| `series.iloc[position]` | `position` 是从 0 开始的位置、切片或位置数组 | 按整数位置选择；课程的 `.iloc[0]` 取第一个众数。 |
| `series.values` / `df.values` | 无参数 | 取底层 NumPy 数组；现代代码也可用 `.to_numpy()`。 |

`tree_df.loc[condition, 'y']` 中，`condition` 是行选择器，`'y'` 是列选择器。

## 官方参考

- [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [Pandas API reference](https://pandas.pydata.org/docs/reference/index.html)
