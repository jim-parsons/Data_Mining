import os
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.feature_extraction import DictVectorizer

data_base_path = '../scikit/data'

# 1. 加载数据
train_data = pd.read_csv(os.path.join(data_base_path, 'train.csv'))
test_data = pd.read_csv(os.path.join(data_base_path, 'test.csv'))

# 2. 数据清洗
# 使用平均年龄来填充年龄的Nan值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)

# 均价填充
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)

# 使用登录最多的港口填充
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)

# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]

# 将符号化的Embarked对象处理成0/1进行表示
dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
test_features = dvec.fit_transform(test_features.to_dict(orient='record'))

# 决策树弱分类器
dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
dt_stump.fit(train_features, train_labels)
print(u'决策树弱分类器准确率为 %.4lf'
      % np.mean(cross_val_score(dt_stump, train_features, train_labels, cv=10)))

# 决策树分类器
dt = DecisionTreeClassifier()
dt.fit(train_features, train_labels)
print(u'决策树分类器准确率为 %.4lf'
      % np.mean(cross_val_score(dt, train_features, train_labels, cv=10)))

# AdaBoost
ada = AdaBoostClassifier()
ada.fit(train_features, train_labels)
print(u'AdaBoost 分类器准确率为 %.4lf'
      % np.mean(cross_val_score(ada, train_features, train_labels, cv=10)))
