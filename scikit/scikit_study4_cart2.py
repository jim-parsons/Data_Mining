# encoding=utf-8
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_boston

# 准备数据集
boston = load_boston()
print(boston.feature_names)

# 获取特征和放假
features = boston.data
prices = boston.target

# 随机抽取33% 的数据作为测试集,其余为训练集
train_features, test_features, train_price, test_price = train_test_split(features, prices, test_size=0.33)

# 创建CART 回归树
dtr = DecisionTreeRegressor()

# 拟合构造CART 回归树
# 将训练集的特征值和结果作为参数进行拟合
dtr.fit(train_features, train_price)

# 预测测试集中的放假
predict_price = dtr.predict(test_features)
print('回归树二乘偏差均值', mean_squared_error(test_price, predict_price))
print('回归树绝对偏差均值', mean_absolute_error(test_price, predict_price))