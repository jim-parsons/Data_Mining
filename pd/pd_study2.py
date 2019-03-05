import pandas as pd
from pandas import Series, DataFrame
from pandasql import sqldf, load_meat, load_births

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})
print(df1)
print(df2)

# 1. 基于指定列进行连接
df3 = pd.merge(df1, df2, on='name')
print(df3)

# 2. inner内连接, 也就是键连接, 这里是相同的键 name
df3 = pd.merge(df1, df2, how='inner')
print(df3)

# 3. left左链接, 以第一个df为主,也就是 第一个df有的index,最后merge的结果都存在,如果df2没有这些列,则NaN
df3 = pd.merge(df1, df2, how='left')
print(df3)

# 4. outer 外连接
df3 = pd.merge(df1, df2, how='outer')
print(df3)

# 使用sql
# lambda argument_list: expression
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='ZhangFei'"
print(pysqldf(sql))
