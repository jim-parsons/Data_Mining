import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm, metrics

# 加载数据集
data = pd.read_csv('data/data.csv')

# 探索数据
# 因为列较多,把dataframe中单全部显示出来
pd.set_option('display.max_columns', None)
# print(data.columns)
# print(data.head())
# print(data.describe())


# 将特征字段分成3组
# mean:平均值
# se: 标准差
# worst: 最大值(3个最大值的平均值)
features_mean = list(data.columns[2: 12])
features_se = list(data.columns[12: 22])
features_worst = list(data.columns[22: 32])

# 数据清理
# ID 没有用,删除
data.drop('id', axis=1, inplace=True)
# 将B良性替换为0,M恶性替换为1
data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

# 特征字段的筛选
# 首先观察features_map各变量之间的关系

# 将肿瘤诊断结果可视化
sns.countplot(data['diagnosis'], label='Count')
plt.show()
# 用热力图呈现features_mean字段之间的相关性
corr = data[features_mean].corr()
# annot = True显示每个方格的数据
# 对角线上的为单变量自身的相关系数是1
# 颜色越浅相关性越大
# 所以radius_mean,perimeter_mean,area_mean相关性非常大
# compactness)mean,concavity_mean,concavity_mean也是相关的
# 因此可以选取其中一个座位代表
sns.heatmap(corr, annot=True)
plt.show()

# 特征选择的目的是降维,少量特征数据的特性,增强分类器的泛化能力
# 保留mean这组特征,从上面两类相关性大的选择一个属性作为代表
# 如radius_mean, compactness_mean
features_remain = ['radius_mean', 'texture_mean', 'smoothness_mean', 'compactness_mean', 'symmetry_mean',
                   'fractal_dimension_mean']

# 抽取30%数据作为测试集,其余为训练集
train, test = train_test_split(data, test_size=0.3)
# 抽取特征选择的数值作为训练和测试数据
train_X = train[features_remain]
train_y = train['diagnosis']
test_X = train[features_remain]
test_y = train['diagnosis']

# 训练前针对数据进行规范化,让数据在同一个量级,避免因为维度问题造成数据误差
# Z-Score进行数据规范化,保证每个特征维度的数据均值为0,方差为0,即符合高斯分布
ss = StandardScaler()
train_X = ss.fit_transform(train_X)
test_X = ss.fit_transform(test_X)

# 训练和预测
# 创建SVM 分类器
model = svm.SVC()
# 训练
model.fit(train_X, train_y)
# 预测
predition = model.predict(test_X)
print('准确率', metrics.accuracy_score(predition, test_y))