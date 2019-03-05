import pandas as pd

data = {'Chinese': [66, 95, 93, 90, 80, 80],
        'English': [65, 85, 92, 88, 90, 90],
        'Math': [None, 98, 96, 77, 90, 90]}

df = pd.DataFrame(data=data, index=['张飞', '关羽', '赵云', '黄忠', '典韦', '典韦'],
                  columns=['English', 'Math', 'Chinese'])
# 去重复行
df.drop_duplicates(inplace=True)
print(df)
# 列名重新排序
cols = ['Chinese', 'English', 'Math']
df = df.filter(cols, axis=1)
print(df)
# 该列名为中文名
df.rename(columns={'Chinese': '语文', 'English': '英语', 'Math': '数学'}, inplace=True)
print(df)


# 求成绩和
def total_score(df):
    df['总分'] = df['语文'] + df['英语'] + df['数学']
    return df

# 横向
df = df.apply(total_score, axis=1)
print(df)

# 按总分排序,高到底
df.sort_values(['总分'], ascending=False, inplace=True)
print(df)

print("打印显示成绩单信息")
# 打印显示成绩单信息
print(df.isnull().sum())
print(df.describe())

print("使用数学成绩均值填充张飞同学的缺失值")
# 使用数学成绩均值填充张飞同学的缺失值
df['数学'].fillna(df['数学'].mean(), inplace=True)
df = df.apply(total_score, axis=1)
print(df.describe())
print(df)