import numpy as np

"""
计数组 / 矩阵中的最大值函数 amax()，最小值函数 a
"""
print("计数组 / 矩阵中的最大值函数 amax()，最小值函数 a")
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(np.shape(a))

print(np.amin(a))  # 全部元素最小值
# 是沿着axis=0轴的最小值,axis=0把元素看成
# [1,4,7], [2,5,8], [3,6,9] 三个元素,然后取每个元素的最小值,所以最小值为 [1,2,3]
print(np.amin(a, 0))
# amin(a,1) 是延着 axis=1 轴的最小值，axis=1 轴是把元素看成了 [1,2,3], [4,5,6], [7,8,9] 三个元素
# 所以最小值为[1, 4, 7]
print(np.amin(a, 1))

print(np.amax(a))
print(np.amax(a, 0))
print(np.amax(a, 1))

"""
统计最大值与最小值之差 ptp()
"""
print("统计最大值与最小值之差 ptp()")
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(np.ptp(b))
print(np.ptp(b, 0))
print(np.ptp(b, 1))

"""
统计数组的百分位数 percentile()
"""
print("统计数组的百分位数 percentile()")
c = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
# p% 的百分位数
# 第二个参数为 p 百分比,取值0-100
# 如果为0,则为最小值
# 如果为100,则为最大值
print(np.percentile(c, 50))
print(np.percentile(c, 50, axis=0))
print(np.percentile(c, 50, axis=1))

"""
统计数组中的中位数 median()、平均数 mean()
"""
print("统计数组中的中位数 median()、平均数 mean()")
d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 求中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
# 求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

"""
统计数组中的加权平均值 average()
"""
print("统计数组中的加权平均值 average()")
e = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])  # (1*1+2*2+3*3+4*4)/(1+2+3+4)
print(np.average(e))
print(np.average(e, weights=wts))

"""
NumPy 排序
"""
print("NumPy 排序")

f = np.array([[4, 3, 2], [2, 4, 1]])
print(np.sort(f))
print(np.sort(f, axis=None))
print(np.sort(f, axis=0))
print(np.sort(f, axis=1))
