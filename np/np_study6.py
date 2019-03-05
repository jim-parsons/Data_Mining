import numpy as np

"""
假设一个团队里有 5 名学员,
1. 用 NumPy 统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出
"""

score_type = np.dtype({'names': ['name', 'chinese', 'english', 'math'],
                       'formats': ['S32', 'i', 'i', 'i']})

people = np.array(
    [
        ("zhangfei", 66, 65, 30),
        ("guanyu", 95, 85, 98),
        ("zhaoyun", 93, 92, 96),
        ("huangzhong", 90, 88, 77),
        ("dianwei", 80, 90, 90)
    ], dtype=score_type)

print(people)

chinese = people[:]['chinese']
english = people[:]['english']
math = people[:]['math']


def show(name, arr):
    print()
    print(f"{name} | {np.mean(arr)} | {np.min(arr)} | {np.max(arr)} | {np.var(arr)} | {np.std(arr)}", )


print("科目 | 平均成绩 | 最小成绩 | 最大成绩 | 方差 | 标准差")
show("chinese", chinese)
show("english", english)
show("math", math)

print("排名: ")
