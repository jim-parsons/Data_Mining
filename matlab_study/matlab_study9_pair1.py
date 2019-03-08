import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

# 数据准备
iris = sns.load_dataset("iris")
sns.pairplot(iris)
plt.show()