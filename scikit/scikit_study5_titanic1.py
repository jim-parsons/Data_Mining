# encoding=utf-8
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_boston
import pandas as pd

# train.csv 包含特诊信息和存活与否的标签
# test.csv  值包含特征信息
train_data = pd.read_csv('data/train.csv')
test_data = pd.read_csv('data/train.csv')
# 数据探索

print(train_data.info())
print("="*20)
print(train_data.describe())
print("="*20)
print("="*20)
print(train_data.describe(include=['O'])) # 查看字符串类型的整体情况
print("="*20)
print(train_data.head())
print("="*20)
print(train_data.tail())


# Age, Fare(船票价格), Cabin 有缺失

# 使用平均年龄来填充Age中的 nan值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)

# 使用票价的均值填充票价中的 nan 值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)

# Cabin 为船舱,有大量缺失值
# Embarked 为登录港口,有少量缺失值
print(train_data['Embarked'].value_counts())
# S    644  占比最多,因而把空值都赋值为S
# C    168
# Q     77


