import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 数据准备
# 0-1 之间的 10*4 维度数据
#
data = np.random.normal(size=(10, 4))
labels = ['A', 'B', 'C', 'D']
# 用 Matplotlib
plt.boxplot(data, labels=labels)
plt.show()
# 用 Seaborn
df = pd.DataFrame(data, columns=labels)
sns.boxplot(data=df)
plt.show()
