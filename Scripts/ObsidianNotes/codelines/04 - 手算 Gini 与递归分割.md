---
course: "Machine Learning and AI with Python"
type: code-reference
topic: "手算 Gini 与递归分割"
tags:
  - code-reference
  - python
  - decision-tree
  - gini
aliases:
  - Gini codelines
---

# 手算 Gini 与递归分割

返回索引：[[00 - Codelines 索引]]

本页函数逐参数说明：[[09 - NumPy 函数参数详解]]、[[12 - Python 内置函数与自定义函数参数详解]]。

## 统计分割两侧的类别数

| 代码行 | 作用 |
|---|---|
| `left_1 = ((df[pred_name] <= val) & (df['y'] == 1)).sum()` | 统计阈值左侧类别 1 的样本数。 |
| `left_0 = ((df[pred_name] <= val) & (df['y'] == 0)).sum()` | 统计阈值左侧类别 0 的样本数。 |
| `right_1 = ((df[pred_name] > val) & (df['y'] == 1)).sum()` | 统计阈值右侧类别 1 的样本数。 |
| `right_0 = ((df[pred_name] > val) & (df['y'] == 0)).sum()` | 统计阈值右侧类别 0 的样本数。 |
| `N_left = max(1e-5, left_1 + left_0)` | 计算左侧总数，并用极小值防止除零。 |
| `N_right = max(1e-5, right_1 + right_0)` | 计算右侧总数；两个类别数量必须相加。 |

## Gini 计算代码行

| 代码行 | 作用 |
|---|---|
| `gini_left = 1 - (left_1 / N_left)**2 - (left_0 / N_left)**2` | 计算左子节点 Gini 不纯度。 |
| `gini_right = 1 - (right_1 / N_right)**2 - (right_0 / N_right)**2` | 计算右子节点 Gini 不纯度。 |
| `N_total = N_left + N_right` | 计算父区域总样本数。 |
| `weighted_gini = (N_left / N_total) * gini_left + (N_right / N_total) * gini_right` | 按左右节点样本占比计算加权 Gini。 |
| `total_gini.append(weighted_gini)` | 保存当前候选阈值的加权 Gini。 |

相关公式：[[基尼指数公式 (Gini Index Formula)]]；左右节点的加权方式见本页代码。

## 完整的候选阈值评分函数

```python
def get_total_gini(predictor_values, pred_name, df):                         # 定义函数：评估一个特征的所有候选值
    total_gini = []                                                          # 保存每个候选值的加权 Gini
    for val in predictor_values:                                             # 依次尝试每个候选分割值
        left_1 = ((df[pred_name] <= val) & (df['y'] == 1)).sum()              # 左侧类别 1 数量
        left_0 = ((df[pred_name] <= val) & (df['y'] == 0)).sum()              # 左侧类别 0 数量
        N_left = max(1e-5, left_1 + left_0)                                  # 左侧总样本数并防止除零
        gini_left = 1 - (left_1 / N_left) ** 2 - (left_0 / N_left) ** 2       # 左侧 Gini

        right_1 = ((df[pred_name] > val) & (df['y'] == 1)).sum()              # 右侧类别 1 数量
        right_0 = ((df[pred_name] > val) & (df['y'] == 0)).sum()              # 右侧类别 0 数量
        N_right = max(1e-5, right_1 + right_0)                                # 右侧总样本数并防止除零
        gini_right = 1 - (right_1 / N_right) ** 2 - (right_0 / N_right) ** 2  # 右侧 Gini

        N_total = N_left + N_right                                           # 父区域总样本数
        weighted_gini = (                                                    # 开始计算左右节点的加权平均
            (N_left / N_total) * gini_left                                   # 左侧 Gini 乘左侧权重
            + (N_right / N_total) * gini_right                               # 加上右侧 Gini 乘右侧权重
        )                                                                       # 结束加权 Gini 表达式
        total_gini.append(weighted_gini)                                     # 保存当前候选值的结果
    return total_gini                                                        # 返回全部候选值的加权 Gini
```

## 找到阈值

```python
def get_threshold(unique_values, gini_scores):                 # 根据候选值和对应 Gini 选择阈值
    idx = np.argmin(gini_scores)                               # 找出最低 Gini 的位置
    threshold = (unique_values[idx] + unique_values[idx + 1]) / 2  # 取相邻值中点，避免切在样本值上
    return threshold                                           # 返回最终切分阈值
```

> [!warning]
> 中点公式末尾必须有 `/ 2`。如果只把两个值相加，阈值可能大于区域最大值，使一个子区域为空。

## 为左右区域指定多数类

```python
left_label = region.loc[region[pred] <= threshold, 'y'].mode().iloc[0]   # 取左区域的多数类
right_label = region.loc[region[pred] > threshold, 'y'].mode().iloc[0]   # 取右区域的多数类
region = region[region[pred] <= threshold]                               # 后续示例继续沿左分支向下切分
```

> [!warning]
> 调用 `.mode().iloc[0]` 前应确认区域不为空，否则会出现 `IndexError`。

## 按手写分割规则预测

```python
obs = {'x1': x1_i, 'x2': x2_i}                              # 把一个样本的特征保存为按名称访问的字典
for n_split, (pred, threshold) in enumerate(splits):         # 按顺序应用每条树分割规则
    if obs[pred] <= threshold:                               # 判断样本是否进入当前左分支
        if n_split == len(splits) - 1:                       # 若已到最后一次分割
            y_hats.append(split_labels[n_split]['left'])     # 使用最后左叶节点的类别
    else:                                                    # 样本进入当前右分支
        y_hats.append(split_labels[n_split]['right'])         # 使用当前右叶节点的类别
        break                                                # 已到叶节点，停止继续检查规则
```
