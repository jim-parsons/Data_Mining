import pandas as pd

"""

"""
# 对 df[‘Age’] 中缺失的数值用平均年龄进行填充
# df['Age'].fillna(df['Age'].mean(), inplace=True)

# 最高频的数据进行填充
# age_maxf = train_features['Age'].value_counts().index[0]
# train_features['Age'].fillna(age_maxf, inplace=True)

# 空行
#
# 删除全空的行
# df.dropna(how='all',inplace=True)


#列数据的单位不统一

#千克作为统一的度量单位，将磅（lbs）转化为千克（kgs）

# 获取 weight 数据列中单位为 lbs 的数据

# rows_with_lbs = df['weight'].str.contains('lbs').fillna(False)
# print df[rows_with_lbs]
# # 将 lbs 转换为 kgs, 2.2lbs=1kgs
# for i,lbs_row in df[rows_with_lbs].iterrows():
# 	# 截取从头开始到倒数第三个字符之前，即去掉 lbs。
# 	weight = int(float(lbs_row['weight'][:-3])/2.2)
# 	df.at[i,'weight'] = '{}kgs'.format(weight)


# 删除非 ASCII 字符
# df['first_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
# df['last_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)


# 一列有多个参数
#在数据中不难发现，姓名列（Name）包含了两个参数 Firtname 和 Lastname。为了达到数
# 据整洁目的，我们将 Name 列拆分成 Firstname和 Lastname 两个字段,我们使用 Python 的 split 方法
# str.split(expand=True)，将列表拆成新的列，再将原来的 Name 列删除

# 切分名字，删除源数据列
# df[['first_name','last_name']] = df['name'].str.split(expand=True)
# df.drop('name', axis=1, inplace=True)


# 重复数据

# 删除重复数据行
# df.drop_duplicates(['first_name','last_name'],inplace=True)
