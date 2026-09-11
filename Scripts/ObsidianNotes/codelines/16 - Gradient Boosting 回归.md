---
course: "Machine Learning and AI with Python"
type: code-reference
topic: "Gradient Boosting 回归"
tags:
  - code-reference
  - python
  - gradient-boosting
  - regression
  - ensemble-learning
aliases:
  - Boosting 回归 codelines
---

# Gradient Boosting 回归

返回索引：[[00 - Codelines 索引]]

本页函数逐参数说明：[[10 - scikit-learn 函数参数详解]]；数组形状见 [[09 - NumPy 函数参数详解]]。

## 排序并整理单特征数据

```python
x, y = df['Ozone'].values, df['Temp'].values                     # 提取一维特征和响应数组
x, y = list(zip(*sorted(zip(x, y))))                             # 按 x 升序排列，同时保持 x/y 配对
x = np.array(x).reshape(-1, 1)                                  # 将特征恢复为模型要求的二维矩阵
y = np.array(y)                                                  # 将响应转换为一维 NumPy 数组
```

最内层 `zip(x, y)` 先配对，`sorted(...)` 按元组第一个元素 `x` 排序，前面的 `*` 解包排序结果，外层 `zip(...)` 再把 x 与 y 分开。

## 手算一次 Boosting 更新

```python
basemodel = DecisionTreeRegressor(max_depth=1)                   # 创建第一棵回归树桩
basemodel.fit(x, y)                                              # 用真实响应拟合第一棵树
y_pred = basemodel.predict(x)                                   # 得到第一轮预测
residuals = y - y_pred                                          # 计算第一轮残差

residual_tree = DecisionTreeRegressor(max_depth=1)               # 创建拟合残差的第二棵树桩
residual_tree.fit(x, residuals)                                 # 让第二棵树学习第一棵树的错误
y_pred_residuals = residual_tree.predict(x)                     # 预测每个样本的残差修正量

learning_rate = 0.5                                             # 设置每轮修正的缩放系数
y_pred_new = y_pred + learning_rate * y_pred_residuals          # 把缩放后的残差预测加入旧预测
```

对应更新公式：

$$
\hat y^{(2)} = \hat y^{(1)} + \eta h_2(x)
$$

其中 $h_2(x)$ 是残差树的输出，$\eta$ 是学习率。较小学习率通常需要更多树。

## 使用 GradientBoostingRegressor

```python
l_rate = 0.1                                                     # 设置 Boosting 学习率
boosted_model = GradientBoostingRegressor(                       # 创建梯度提升回归器
    n_estimators=1000,                                           # 按顺序训练 1000 棵弱树
    max_depth=1,                                                 # 每棵基树使用深度 1 的树桩
    learning_rate=l_rate,                                        # 缩放每棵新树的贡献
)                                                               # 结束模型构造
boosted_model.fit(x_train, y_train)                              # 在训练集上顺序拟合弱树
y_pred = boosted_model.predict(x_test)                           # 预测测试集连续响应
boost_mse = mean_squared_error(y_test, y_pred)                   # 计算 Boosting 测试 MSE
```

## 与 Bagging 比较

```python
bagging_model = BaggingRegressor(                                # 创建并行聚合的 Bagging 回归器
    DecisionTreeRegressor(max_depth=3),                          # 使用较深回归树作为基模型
    n_estimators=30,                                             # 独立训练 30 棵树
    max_samples=0.8,                                             # 每棵树抽取 80% 训练样本
    random_state=3,                                              # 固定 bootstrap 结果
)                                                               # 结束 Bagging 构造
bagging_model.fit(x_train, y_train)                              # 拟合所有基树
bag_mse = mean_squared_error(                                    # 计算 Bagging 测试 MSE
    y_test, bagging_model.predict(x_test)                        # 比较真实值与聚合预测
)                                                               # 结束 MSE 调用
```

| 方法 | 基模型关系 | 主要目标 |
|---|---|---|
| Bagging | 多棵树大体独立、可并行训练，最后平均 | 主要降低方差。 |
| Gradient Boosting | 后一棵树拟合前一轮剩余误差，必须顺序训练 | 逐步降低当前模型的损失。 |
