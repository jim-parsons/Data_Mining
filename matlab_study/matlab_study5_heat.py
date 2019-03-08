import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 数据准备
#
# 数据准备
flights = sns.load_dataset("flights")
data = flights.pivot('year', 'month', 'passengers')
sns.heatmap(data)
plt.show()