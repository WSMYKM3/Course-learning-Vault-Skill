---
course: "Machine Learning and AI with Python"
type: code-reference
topic: "Matplotlib 数据与决策边界可视化"
tags:
  - code-reference
  - python
  - matplotlib
  - visualization
  - decision-boundary
aliases:
  - Matplotlib codelines
---

# Matplotlib 数据与决策边界可视化

返回索引：[[00 - Codelines 索引]]

本页函数逐参数说明：[[11 - Matplotlib 函数参数详解]]；网格函数见 [[09 - NumPy 函数参数详解]]。

## 创建画布和坐标轴

| 代码行 | 作用 |
|---|---|
| `import matplotlib.pyplot as plt` | 导入 Matplotlib 绘图接口。 |
| `fig, ax = plt.subplots(figsize=(6, 6))` | 创建一个 6×6 英寸的画布和坐标轴对象。 |
| `fig, axes = plt.subplots(1, 3, figsize=(16, 4))` | 创建一行三列的子图，用于并排比较模型。 |
| `plt.figure(figsize=(10, 8))` | 创建指定尺寸的当前画布。 |
| `plt.rcParams['figure.figsize'] = (12, 8)` | 设置后续图形的默认尺寸。 |

## 散点图和类别颜色

| 代码行 | 作用 |
|---|---|
| `scatter = ax.scatter(tree_df['x1'], tree_df['x2'], c=tree_df['y'], cmap='rainbow')` | 按类别值为二维样本着色。 |
| `ax.scatter(X[:, 0], X[:, 1], c=y, s=50, edgecolor='k', cmap=cmap_bold)` | 绘制带黑色边框的分类散点。 |
| `plt.scatter(df.loc[y == 1, 'x1'], df.loc[y == 1, 'x2'], label='Class 1')` | 只绘制类别 1 的样本。 |
| `plt.scatter(df.loc[y == 0, 'x1'], df.loc[y == 0, 'x2'], label='Class 0')` | 只绘制类别 0 的样本。 |

## 根据散点自动生成图例

```python
legend = ax.legend(                                      # 创建图例对象
    *scatter.legend_elements(),                          # 从散点颜色中自动提取类别标记
    loc='upper right',                                   # 把图例放在右上角
    title='Classes',                                     # 设置图例标题
)                                                           # 结束 legend 调用
ax.add_artist(legend)                                    # 将图例固定到坐标轴，避免后续 legend 调用覆盖
```

## 绘制树的分割线

| 代码行 | 作用 |
|---|---|
| `ax.hlines(x2_threshold, xmin=0, xmax=500, color='black', lw=2, ls=':')` | 绘制水平分割线，表示按 `x2` 切分。 |
| `ax.vlines(x1_threshold, ymin=0, ymax=x2_threshold, color='black', lw=2, ls=':')` | 绘制有限范围的垂直分割线，表示子区域内按 `x1` 切分。 |
| `ax.legend()` | 显示带有 `label` 的绘图元素。 |

## 绘制决策区域

```python
xx1, xx2 = np.meshgrid(                                  # 构造覆盖数据范围的二维坐标网格
    np.arange(tree_df['x1'].min() - 5, tree_df['x1'].max() + 5, 1),  # 横轴网格点
    np.arange(tree_df['x2'].min() - 5, tree_df['x2'].max() + 5, 1),  # 纵轴网格点
)                                                               # 结束 meshgrid 调用
class_pred = predict_class(xx1, xx2, splits)             # 对每个网格点预测类别
ax.contourf(                                              # 用填充等高线显示不同预测区域
    xx1,                                                  # 网格横坐标
    xx2,                                                  # 网格纵坐标
    class_pred.reshape(xx1.shape),                        # 与网格形状一致的类别矩阵
    alpha=0.2,                                            # 使用透明背景，避免遮住样本点
    zorder=-1,                                            # 把决策区域放到散点图后面
    cmap=plt.cm.coolwarm,                                 # 设置区域颜色映射
)                                                           # 结束 contourf 调用
```

相关概念：[[预测空间 (Prediction Space)]]、[[决策边界 (Decision Boundary)]]。

## 绘制多棵 Bagging 回归树

```python
for estimator in model.estimators_:                      # 遍历 Bagging 中的每一棵基回归树
    estimator_pred = estimator.predict(xrange)            # 在连续横轴点上预测当前树的分段结果
    plt.plot(                                             # 绘制当前树的预测曲线
        xrange, estimator_pred,                           # 使用横轴点和当前树预测值
        alpha=0.5, linewidth=0.5, color='#ABCCE3',        # 使用细而透明的浅色线
    )                                                       # 结束当前树曲线的 plot 调用
y_pred = model.predict(xrange)                            # 计算所有树聚合后的平均预测
plt.plot(xrange, y_pred, linewidth=3, color='#50AEA4')    # 用粗线突出显示 Bagging 模型预测
```

## 标题、坐标轴和输出

| 代码行 | 作用 |
|---|---|
| `ax.set_xlabel('x1', fontsize=13)` | 设置当前坐标轴的横轴标签。 |
| `ax.set_ylabel('x2', fontsize=13)` | 设置当前坐标轴的纵轴标签。 |
| `ax.set_title('Decision regions', fontsize=14)` | 设置当前子图标题。 |
| `plt.xlabel('Number of trees', fontsize=16)` | 设置 pyplot 当前图的横轴标签。 |
| `plt.ylabel('Accuracy', fontsize=16)` | 设置 pyplot 当前图的纵轴标签。 |
| `plt.tight_layout()` | 自动调整边距，减少标题或标签被裁切。 |
| `plt.show()` | 渲染并显示当前图形。 |

## 自定义离散颜色

| 代码行 | 作用 |
|---|---|
| `from matplotlib.colors import ListedColormap` | 导入离散颜色映射类。 |
| `cmap_bold = ListedColormap(['#F7345E', '#80C3BD'])` | 为两种类别创建高饱和度颜色映射。 |
| `cmap_light = ListedColormap(['#FFF4E5', '#D2E3EF'])` | 为决策区域创建浅色背景映射。 |
