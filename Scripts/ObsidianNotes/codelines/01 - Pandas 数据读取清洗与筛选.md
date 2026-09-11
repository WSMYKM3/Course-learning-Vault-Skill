---
course: "Machine Learning and AI with Python"
type: code-reference
topic: "Pandas 数据读取清洗与筛选"
tags:
  - code-reference
  - python
  - pandas
  - data-cleaning
aliases:
  - Pandas codelines
---

# Pandas 数据读取清洗与筛选

返回索引：[[00 - Codelines 索引]]

本页函数逐参数说明：[[08 - Pandas 函数参数详解]]。

## 读取和查看数据

| 代码行                                               | 作用                     |
| ------------------------------------------------- | ---------------------- |
| `import pandas as pd`                             | 以别名 `pd` 导入 Pandas。    |
| `df = pd.read_csv('agriland.csv')`                | `filepath_or_buffer='agriland.csv'` 指定 CSV 路径；其他参数使用默认值。 |
| `df = pd.read_csv('airquality.csv', index_col=0)` | `filepath_or_buffer='airquality.csv'` 指定路径；`index_col=0` 把第 1 列设为行索引。 |
| `elect_train = pd.read_csv('election_train.csv')` | 将训练数据读取到独立 DataFrame。  |
| `elect_test = pd.read_csv('election_test.csv')`   | 将测试数据读取到独立 DataFrame。  |
| `df.head()`                                       | 查看前 5 行，快速确认列名和数据内容。   |
| `df.head(10)`                                     | 查看前 10 行。              |

> [!tip]
> notebook 中的相对路径以 notebook 的工作目录为基准；若出现 `FileNotFoundError`，先检查当前工作目录。

## 缺失值过滤

| 代码行 | 作用 |
|---|---|
| `df.Ozone.notna()` | 为 `Ozone` 非缺失的行生成布尔掩码。 |
| `df = df[df.Ozone.notna()]` | 仅保留 `Ozone` 不为 `NaN` 的记录。 |

`notna()` 只检查指定列，因此不会因为其他列存在缺失值而删除整行。相关概念：[[缺失数据 (Missing Data)]]。

## 选择特征和响应变量

| 代码行 | 作用 |
|---|---|
| `X = df[['latitude', 'longitude']].values` | 选择两列特征并转换为 NumPy 二维数组。 |
| `y = df['land_type'].values` | 选择单列标签并转换为 NumPy 一维数组。 |
| `x = df[['Ozone']].values` | 用双中括号保留二维特征矩阵形状 `(n_samples, 1)`。 |
| `y = df['Temp']` | 选择 `Temp` 列作为 Pandas Series 响应变量。 |
| `pred_cols = ['minority', 'density', 'hispanic', 'obesity', 'female', 'income', 'bachelor', 'inactivity']` | 用列表集中保存多个特征列名。 |
| `X_train = elect_train[pred_cols]` | 按列名列表构造训练特征矩阵。 |
| `X_test = elect_test[pred_cols]` | 使用同一列名和顺序构造测试特征矩阵。 |
| `y_train = elect_train['won']` | 取训练集的单列标签。 |
| `y_test = elect_test['won']` | 取测试集的单列标签。 |
| `X = df.drop('Outcome', axis=1)` | 删除响应列 `Outcome`，保留其余全部列作为特征 DataFrame。 |
| `X = df.drop('Outcome', axis=1).values` | 删除响应列后再取得二维 NumPy 特征数组。 |
| `y = df[['Outcome']].values` | 用双中括号取得形状为 `(n_samples, 1)` 的二维标签数组。 |

> [!important]
> `df[['Ozone']]` 返回二维 DataFrame，`df['Ozone']` 返回一维 Series。多数 scikit-learn 模型要求 `X` 为二维结构。

## 用比较结果生成二元标签

| 代码行 | 作用 |
|---|---|
| `elect_train['trump'] > elect_train['clinton']` | 逐行比较两列，得到布尔 Series。 |
| `y_train = (elect_train['trump'] > elect_train['clinton']).astype(int)` | 将比较结果从 `True/False` 转换为 `1/0` 训练标签。 |
| `y_test = (elect_test['trump'] > elect_test['clinton']).astype(int)` | 用相同规则生成测试标签。 |

## 条件筛选和区域切分

| 代码行 | 作用 |
|---|---|
| `first_split_df = tree_df[tree_df['x2'] <= x2_threshold]` | 保留满足第一次左分支条件的样本。 |
| `right_region = first_split_df[first_split_df['x1'] > x1_threshold]` | 从父区域中继续筛选右分支。 |
| `left_region = first_split_df[first_split_df['x1'] <= x1_threshold]` | 从父区域中继续筛选左分支。 |
| `tree_df.loc[tree_df['x2'] <= threshold, 'y']` | 用 `.loc` 同时按条件筛行并选择 `y` 列。 |
| `tree_df.loc[tree_df['x2'] <= threshold, 'y'].mode().iloc[0]` | 取得条件区域内出现次数最多的类别。 |
| `left_region['y'].value_counts()` | 统计区域内各类别的样本数。 |

## DataFrame 自助采样

| 代码行 | 作用 |
|---|---|
| `df_new = df.sample(frac=1, replace=True)` | 从 DataFrame 有放回抽取与原数据相同数量的样本。 |
| `y_boot = df_new.land_type.values` | 从自助样本中提取标签数组。 |
| `X_boot = df_new[['latitude', 'longitude']].values` | 从同一自助样本中提取对应特征，保持特征与标签对齐。 |

相关概念：[[自助采样 (Bootstrap Sampling)]]、[[自助数据集 (Bootstrap Dataset)]]、[[有放回抽样 (Sampling with Replacement)]]。

## Notebook 显示设置

| 代码行 | 作用 |
|---|---|
| `pd.set_option('display.width', 100)` | 设置 DataFrame 文本输出的显示宽度。 |
| `pd.set_option('display.max_columns', 20)` | 最多显示 20 列，减少宽表被过早截断。 |
