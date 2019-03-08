# encoding=utf-8
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn.datasets import load_boston
import pandas as pd

# train.csv 包含特诊信息和存活与否的标签
# test.csv  值包含特征信息

train_data = pd.read_csv('data/train.csv')
test_data = pd.read_csv('data/train.csv')
# 特征选取
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]

# 特征值里面有一些字符串,如Sex, male(0), female(1)
# Embarked有三种可能S,C,Q
# 使用sklearn DictVectorizer将符号转换为数字 0/1

dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))

# dvec = DictVectorizer(sparse=False)
# fit_transform 可将特征向量转化为特征值矩阵.
# train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
# ['Age', 'Embarked=C', 'Embarked=Q', 'Embarked=S', 'Fare', 'Parch', 'Pclass', 'Sex=female', 'Sex=male', 'SibSp']
# ['Age', 'Embarked=C', 'Embarked=Q', 'Embarked=S', 'Fare', 'Parch', 'Pclass', 'Sex=female', 'Sex=male', 'SibSp']

print(dvec.feature_names_)
