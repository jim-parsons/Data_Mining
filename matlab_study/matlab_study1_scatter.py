import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 散点图
# 随机1000个点
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
# 用matlib
plt.scatter(x, y, marker='x')
plt.show()

# 用seaborn
df = pd.DataFrame({'x': x, 'y': y})
sns.jointplot(x="x", y='y', data=df, kind='scatter')
plt.show()
