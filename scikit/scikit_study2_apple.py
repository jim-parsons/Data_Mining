from sklearn import tree
import sys
import os
import graphviz
import numpy as np
os.environ['PATH'] += os.pathsep + 'c:\program files\python\lib\site-packages\graphviz'

"""
红      大       好苹果
是      是       是
是      否       是
否      是       否
否      否       否
"""

# 创建数据[红, 大], 1==是, 0==否
data = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
# 数据标注
target = np.array([1, 1, 0, 0])

# 创建决策树分类器模型
clf = tree.DecisionTreeClassifier()
clf = clf.fit(data, target)

dot_data = tree.export_graphviz(clf, out_file='./tree.dot')
graph = graphviz.Source(dot_data)
graph