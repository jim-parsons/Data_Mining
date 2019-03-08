# coding:utf-8
from sklearn import preprocessing
import numpy as np

# 初始化数据，每一行代表一个样本,每一列代表一个特征
x = np.array([[0., -3., 1.],
              [3., 1., 2.],
              [0., 1., -1.]])

# 将数据进行[0, 1]规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)
print(minmax_x)

x = np.array([[0., -3., 1.],
              [3., 1., 2.],
              [0., 1., -1.]])

# 将数据z-Score 规范化 转化为高斯分布
# z-score 标准化(正太标准化)是基于原始数据的均值（mean）和标准差（standard deviation）进行数据的标准化。将A的原始值x使用z-score标准化到x
# 最后结果为均值为0,方法为1,
scaled_x = preprocessing.scale(x)
print(scaled_x)

x = np.array([[0., -3., 1.],
              [3., 1., 2.],
              [0., 1., -1.]])

# 小数定标规范话
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print(scaled_x)

# exercise
x = np.array([[5000], [16000], [58000]])
min_max_scaler = preprocessing.MinMaxScaler()
print(min_max_scaler.fit_transform(x))