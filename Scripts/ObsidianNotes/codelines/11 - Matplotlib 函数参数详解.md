---
course: "Machine Learning and AI with Python"
type: parameter-reference
topic: "Matplotlib 函数参数"
tags:
  - code-reference
  - python
  - matplotlib
  - parameters
aliases:
  - Matplotlib 参数速查
---

# Matplotlib 函数参数详解

返回索引：[[00 - Codelines 索引]]；对应代码：[[07 - Matplotlib 数据与决策边界可视化]]。

Matplotlib 许多函数接受 `**kwargs`。这表示除了签名明确列出的参数，还可传 `color`、`alpha`、`linewidth`、`zorder` 等 Artist 属性；不同图形对象支持的附加属性不完全相同。

## `plt.subplots()`

调用形式：`plt.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, width_ratios=None, height_ratios=None, subplot_kw=None, gridspec_kw=None, **fig_kw)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `nrows` | `1` | 子图行数。 |
| `ncols` | `3` 或默认 `1` | 子图列数。 |
| `sharex`, `sharey` | `False` | 是否共享坐标轴，也可用 `'row'`、`'col'`、`'all'`。 |
| `squeeze` | `True` | 是否压缩返回的 Axes 数组维度。 |
| `width_ratios`, `height_ratios` | `None` | 各列宽度或各行高度比例。 |
| `subplot_kw` | `None` | 传给每个 Axes 的参数字典。 |
| `gridspec_kw` | `None` | 传给网格布局的参数字典。 |
| `**fig_kw` | `figsize=(6, 6)` | 继续传给 Figure；`figsize` 是宽、高英寸数。 |

返回 `(fig, ax)`；多个子图时 `ax` 通常是 Axes 数组。

## `plt.figure()`

常用形式：`plt.figure(num=None, figsize=None, dpi=None, *, facecolor=None, edgecolor=None, frameon=True, clear=False, **kwargs)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `num` | `None` | Figure 编号或名称。 |
| `figsize` | `(10, 8)` 或 `(30, 20)` | 画布宽、高，单位为英寸。 |
| `dpi` | 默认配置值 | 每英寸像素数。 |
| `facecolor`, `edgecolor` | 默认配置值 | Figure 背景色和边框色。 |
| `frameon` | `True` | 是否绘制 Figure 框架。 |
| `clear` | `False` | 复用已有 Figure 时是否先清空。 |
| `**kwargs` | 未使用 | 其他 Figure 属性。 |

## `Axes.scatter()` / `plt.scatter()`

常用形式：`scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, data=None, **kwargs)`。

| 参数 | 本例 | 作用 |
|---|---|---|
| `x` | `tree_df['x1']` 或 `X[:, 0]` | 点的横坐标。 |
| `y` | `tree_df['x2']` 或 `X[:, 1]` | 点的纵坐标。 |
| `s` | `50` | 点面积，单位为 points²；可传标量或逐点数组。 |
| `c` | `tree_df['y']`、`y` 或固定颜色 | 点颜色或用于颜色映射的数值数组。 |
| `marker` | `'.'` | 点形状。 |
| `cmap` | `'rainbow'` 或 `cmap_bold` | 数值 `c` 到颜色的映射。 |
| `norm`, `vmin`, `vmax` | 省略 | 控制数值到颜色范围的标准化。 |
| `alpha` | `0.4` 或 `0.5` | 透明度，范围通常为 0 到 1。 |
| `linewidths` | 省略 | 点边框线宽。 |
| `edgecolors` / `edgecolor` | `'k'` | 点边框颜色；`'k'` 表示黑色。 |
| `label` | `'Trump'` 等 | 通过 `**kwargs` 设置图例文字。 |
| `data` | `None` | 可传具名数据源，让 `x`、`y` 使用字段名。 |

## `Axes.plot()` / `plt.plot()`

调用形式：`plot(*args, scalex=True, scaley=True, data=None, **kwargs)`。

- `*args` 数量可变，常见为 `plot(x, y)`、`plot(x, y, fmt)`，也能一次传多组 `x, y, fmt`。
- `'r+'` 是格式字符串：`r` 表示红色，`+` 表示加号标记。

| 关键字参数 | 本例/默认值 | 作用 |
|---|---|---|
| `label` | `'Model Prediction'` | 图例文字。 |
| `alpha` | `0.5` 或 `0.7` | 透明度。 |
| `linewidth` | `0.5`、`1`、`3` | 线宽。 |
| `color` | 十六进制颜色 | 线条颜色。 |
| `markersize` | `6` | 标记尺寸。 |
| `scalex`, `scaley` | `True` | 是否根据新数据自动缩放坐标轴。 |
| `data` | `None` | 可选具名数据源。 |

## `legend()` 与 `legend_elements()`

`ax.legend(*args, loc='best', title=None, fontsize=None, **kwargs)`：

| 参数 | 本例/默认值 | 作用 |
|---|---|---|
| `*args` | `*scatter.legend_elements()` | 展开为 handles 和 labels；也可省略，让 Matplotlib 自动收集。 |
| `loc` | `'upper right'` 或 `'best'` | 图例位置。 |
| `title` | `'Classes'` | 图例标题。 |
| `fontsize` | `12` | 图例文字大小。 |
| `**kwargs` | 可选 | 还可设置列数、边框、背景、标题字号等。 |

`scatter.legend_elements(prop='colors', num='auto', fmt=None, func=lambda x: x, **kwargs)`：

| 参数 | 默认值 | 作用 |
|---|---:|---|
| `prop` | `'colors'` | 按颜色或点大小生成图例。 |
| `num` | `'auto'` | 生成多少个图例项。 |
| `fmt` | `None` | 标签格式化器。 |
| `func` | 恒等函数 | 将内部颜色/大小值转换回显示值。 |
| `**kwargs` | 无 | 传给生成的图例标记。 |

`ax.add_artist(legend)` 只有一个参数：`legend` 是要加入 Axes 的 Artist 对象。

## `Axes.hlines()` 与 `Axes.vlines()`

| 函数 | 必需位置参数 | 可选参数与课程用法 |
|---|---|---|
| `hlines(y, xmin, xmax, colors=None, linestyles='solid', label='', **kwargs)` | `y` 是水平线高度；`xmin/xmax` 是左右端点。 | `color='black'` 颜色；`lw=2` 线宽；`ls=':'` 点线；`label` 图例文字。 |
| `vlines(x, ymin, ymax, colors=None, linestyles='solid', label='', **kwargs)` | `x` 是垂直线位置；`ymin/ymax` 是上下端点。 | 参数规则同上。 |

`lw` 是 `linewidth` 的别名，`ls` 是 `linestyle` 的别名。

## `Axes.contourf()` / `plt.contourf()`

主要形式：`contourf([X, Y,] Z, [levels], *, alpha=None, cmap=None, norm=None, vmin=None, vmax=None, colors=None, extend='neither', **kwargs)`。

| 参数 | 本例/默认值 | 作用 |
|---|---|---|
| `X`, `Y` | `xx1`, `xx2` | 二维坐标网格；可省略，省略时使用数组索引。 |
| `Z` | `class_pred.reshape(xx1.shape)` | 每个网格点的高度或类别值。 |
| `levels` | 省略 | 等高层级数量或具体层级数组。 |
| `alpha` | `0.2` 或 `0.02` | 填充透明度。 |
| `cmap` | `plt.cm.coolwarm` | 数值到颜色的映射。 |
| `norm`, `vmin`, `vmax` | 省略 | 颜色标准化及范围。 |
| `colors` | 省略 | 直接指定颜色时可替代 `cmap`。 |
| `extend` | `'neither'` | 超出 levels 范围的值如何着色。 |
| `zorder` | `-1` | 通过 `**kwargs` 设置绘制层级，使背景位于散点之后。 |

## 标签、标题、刻度和布局

| 调用形式 | 参数说明 |
|---|---|
| `ax.set_xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)` | `xlabel` 是文本；`fontsize=13` 经 `**kwargs` 设置字号；`labelpad` 控制间距；`loc` 控制位置。 |
| `ax.set_ylabel(ylabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)` | 参数规则与横轴标签相同。 |
| `ax.set_title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs)` | `label` 是标题；`loc` 控制左中右；`pad` 是间距；`y` 是垂直位置。 |
| `plt.xticks(ticks=None, labels=None, *, minor=False, **kwargs)` | 设置刻度位置、标签、主/次刻度及文字属性；只传 `fontsize=12` 会修改已有刻度。 |
| `plt.yticks(...)` | 参数规则与 `xticks` 相同。 |
| `plt.xlim(left=None, right=None, *, emit=True, auto=False, xmin=None, xmax=None)` | 设置或读取横轴范围；课程的无参数调用只读取当前范围。 |
| `plt.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)` | 设置总边距、行间距、列间距和布局矩形。 |
| `plt.show(*args, **kwargs)` | 显示 Figure；交互后端可接受 `block` 等参数。 |

## `ListedColormap()`

调用形式：`ListedColormap(colors, name='from_list', N=None)`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `colors` | 两个十六进制颜色 | 颜色列表，必需。 |
| `name` | `'from_list'` | 颜色映射名称。 |
| `N` | `None` | 映射长度；与颜色数不同会截断或重复扩展。 |

## Pandas 的 `.plot()`

课程调用：`feature_importance.plot(kind='barh', color='steelblue')`。

| 参数 | 本例/默认值 | 作用 |
|---|---:|---|
| `kind` | `'barh'` | 图类型；这里是水平条形图。 |
| `color` | `'steelblue'` | 图形颜色。 |
| `ax` | 默认当前 Axes | 可指定绘制到哪个 Matplotlib Axes。 |
| `figsize` | 默认配置值 | 可直接设置画布尺寸。 |
| `title` | `None` | 可直接设置标题。 |
| `legend` | 依图类型决定 | 是否显示图例。 |
| `**kwargs` | 可选 | 继续传给底层 Matplotlib 绘图函数。 |

## `plt.rcParams` 配置赋值

`plt.rcParams['figure.figsize'] = (12, 8)` 不是函数调用：

- `'figure.figsize'` 是配置键。
- `(12, 8)` 是默认 Figure 宽、高，单位为英寸。
- 它会影响后续没有显式传 `figsize` 的图。

## 官方参考

- [Matplotlib pyplot API](https://matplotlib.org/stable/api/pyplot_summary.html)
- [Matplotlib API reference](https://matplotlib.org/stable/api/index.html)
