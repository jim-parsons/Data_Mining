# encoding=utf-8
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import numpy as np

# train.csv 包含特诊信息和存活与否的标签
# test.csv  值包含特征信息
train_data = pd.read_csv('data/train.csv')
test_data = pd.read_csv('data/train.csv')


# 使用平均年龄来填充Age中的 nan值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)

# 使用票价的均值填充票价中的 nan 值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)

# 使用登录最多的港口来填充登录港口的 nan 值
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)


# 特征选取
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]

# 特征转换器
dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
print(dvec.feature_names_)


# 构造ID3
# 决策树模型
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(train_features, train_labels)

# 模型预测 & 评估
test_features = dvec.transform(test_features.to_dict(orient='record'))
# 决策树预测
pred_labels = clf.predict(test_features)

# 得到决策树准确率
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
# 得到决策树准确率
print(u'score 准确率为 %.4lf' % acc_decision_tree)


# K 折交叉验证统计决策树准确率
print(u'cross_val_score 准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))
