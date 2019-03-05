import pandas as pd
from pandas import Series, DataFrame
import numpy as np

"""
Series 是个定长的字典序列

Series有两个基本属性：index 和 values。在 Series 结构中，index 默认是 0,1,2,递增的整数序列
，当然我们也可以自己来指定索引，比如 index=[‘a’, ‘b’, ‘c’, ‘d’]

"""
x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)

x3 = Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(x3)

"""
DataFrame 类型数据结构类似数据库表
包括了行索引和列索引

"""

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data,
                index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)


"""
去重复的值
"""
df2 = df2.drop_duplicates()  # 去除重复行

"""
更改数据格式

astype 函数来规范数据格式
比如我们把 Chinese 字段的值改成 str 类型，int64 可以这么写

"""
df2['Chinese'].astype('str')
df2['Chinese'].astype(np.int64)

"""
数据间的空格

"""
# 删除左右两边空格
# df2['Chinese'] = df2['Chinese'].map(str.strip)
# 删除左边空格
# df2['Chinese'] = df2['Chinese'].map(str.lstrip)
# 删除右边空格
# df2['Chinese'] = df2['Chinese'].map(str.rstrip)
# 例如有$符号,删除
# df2['Chinese'] = df2['Chinese'].str.strip('$')

"""
大小写转换

"""
# 全部大写
df2.columns = df2.columns.str.upper()
# 全部小写
df2.columns = df2.columns.str.lower()
# 首字母大写
df2.columns = df2.columns.str.title()

"""
查找空值
"""
df2.isnull()
# 哪列存在空值
# df2.isnull.any()

"""
使用 apply 函数对数据进行清洗
"""
# df2['Chinese'] = df2['Chinese'].apply(str.upper())


# 定义函数
def double_df(x):
    return 2 * x


df1[u'Chinese'] = df1[u'Chinese'].apply(double_df)


# 新增两列, 'new1'列 为 语文和英语列和的m倍
# args 是传递的两个参数
# 即 n=2, m=3，在 plus 函数中使用到了 n 和 m，从而生成新的 df
def plus(df, n, m):
    df['new1'] = (df[u'Chinese'] + df[u'English']) * m
    df['new2'] = (df[u'Chinese'] + df[u'English']) * n
    return df


df1 = df1.apply(plus, axis=1, args=(2, 3,))

"""
count() 统计个数,空值不计算
describe() 一次性出多个统计指标,包括 count, mean, std, min, max
min()/max()/sum()/mean()/median()/var()/std()
argmin() 统计最小值的索引位置
argmax() 统计最大值的索引位置
idxmin() 统计最小值的索引值
idxmax() 统计最大值的索引值
"""


"""
重命名列名 columns，让列表名更容易识别
"""
df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace=True)

print("重命名列名")
print(df2)



"""
删除 DataFrame 中的不必要的列或行
"""
# df2 = df2.drop(columns=['Chinese'])
# print("删除 Chinese 这列")
# print(df2)
# df2 = df2.drop(index=['ZhangFei'])
# print("删除 ZhangFei 这行")
# print(df2)
