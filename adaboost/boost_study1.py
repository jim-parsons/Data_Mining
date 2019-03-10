from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

# 加载数据
data = load_boston()
train_x, test_x, train_y, test_y = train_test_split(data.data, data.target, test_size=0.25, random_state=33)
# 使用AdaBoost模型
regrossor = AdaBoostRegressor()
regrossor.fit(train_x, train_y)
pred_y = regrossor.predict(test_x)
mse = mean_squared_error(test_y, pred_y)
print('房价预测结果: ', pred_y)
print('AdaBoost 均方误差: ', round(mse, 2))

# ======= 使用决策树 =======
dec_regrossor = DecisionTreeRegressor()
dec_regrossor.fit(train_x, train_y)
dec_pre_y = dec_regrossor.predict(test_x)
dec_mse = mean_squared_error(test_y, dec_pre_y)
print('决策树 均方误差: ', round(dec_mse, 2))


# ======= 使用决策树 =======
knn_regrossor = KNeighborsRegressor()
knn_regrossor.fit(train_x, train_y)
knn_pre_y = knn_regrossor.predict(test_x)
knn_mse = mean_squared_error(test_y, knn_pre_y)
print('knn 均方误差:', round(knn_mse, 2))

