# encoding=utf-8
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeClassifier
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



