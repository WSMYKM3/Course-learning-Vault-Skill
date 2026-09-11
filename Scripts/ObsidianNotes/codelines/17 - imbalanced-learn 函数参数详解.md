---
course: "Machine Learning and AI with Python"
type: parameter-reference
topic: "imbalanced-learn 函数参数"
tags:
  - code-reference
  - python
  - imbalanced-learn
  - parameters
aliases:
  - imbalanced-learn 参数速查
---

# imbalanced-learn 函数参数详解

返回索引：[[00 - Codelines 索引]]；对应代码：[[15 - 类别不平衡与重采样]]。

## `SMOTE()`

调用形式：`SMOTE(*, sampling_strategy='auto', random_state=None, k_neighbors=5)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `sampling_strategy` | `'auto'` | 控制重采样后的目标类别分布；二分类中默认把少数类增加到与多数类相同数量。 |
| `random_state` | 本例 `2` | 固定生成合成样本时的随机性。 |
| `k_neighbors` | `5` | 寻找少数类近邻时使用的近邻数；也可传兼容的近邻估计器。 |

`sampling_strategy` 还可传浮点比例、目标数量字典、类别字符串策略或返回字典的函数；允许形式会随二分类/多分类任务而不同。

## `RandomUnderSampler()`

调用形式：`RandomUnderSampler(*, sampling_strategy='auto', random_state=None, replacement=False)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `sampling_strategy` | `'auto'` | 控制下采样后的目标类别分布；二分类中默认减少多数类以匹配少数类。 |
| `random_state` | 本例 `2` | 固定被保留的多数类样本。 |
| `replacement` | `False` | 是否允许有放回地抽取多数类样本。 |

## `.fit_resample()`

常用形式：`sampler.fit_resample(X, y, **params)`。

| 参数 | 作用 |
|---|---|
| `X` | 待重采样的二维训练特征，行数必须与 `y` 一致。 |
| `y` | 一维类别标签；测试题用 `np.ravel(y_train)` 保证形状。 |
| `**params` | 新版元数据路由机制可能允许的额外参数；普通调用无需设置。 |

返回 `(X_resampled, y_resampled)`。重采样器只应在训练数据上 `.fit_resample()`；验证集和测试集保持真实类别分布。

## 官方参考

- [SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)
- [RandomUnderSampler](https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.RandomUnderSampler.html)
