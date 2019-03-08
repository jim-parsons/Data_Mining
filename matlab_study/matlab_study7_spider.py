import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

# 数据准备

labels = np.array([u" 推进 ","KDA",u" 生存 ",u" 团战 ",u" 发育 ",u" 输出 "])
stats = [83, 61, 95, 67, 76, 88]
# 画图数据准备,角度,状态值
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
# np.concatenate() 两个list进行拼接
stats = np.concatenate((stats, [stats[0]]))
angles = np.concatenate((angles, [angles[0]]))

# matplotlib

fig = plt.figure() # 准备空白画板
ax = fig.add_subplot(111, polar=True) # 把画板划分成1行1列
ax.plot(angles, stats, 'o-', linewidth=2) # 进行连线
ax.fill(angles, stats, alpha=0.25) # 上色

# 设置中文字体
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties=font)
plt.show()

