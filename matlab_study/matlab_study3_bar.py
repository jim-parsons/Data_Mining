import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a = np.random.randn(100)
s = pd.Series(a)

# 用matplotlib
plt.hist(s)
plt.show()

# seaborn
sns.distplot(s, kde=False)
plt.show()
sns.distplot(s, kde=True)
plt.show()