import numpy as np

# dtype: 定义结构类型
# 'names', 'formats' 固定写法
person_type = np.dtype({'names': ['name', 'age', 'chinese', 'math', 'english'],
                        'formats': ['S32', 'i', 'i', 'i', 'f']})
# 中文为U32
#

peoples = np.array([("ZhangFei", 32, 75, 100, 90),
                    ("GuanYu", 24, 85, 96, 88.5),
                    ("ZhaoYun", 28, 85, 92, 96.5),
                    ("HuangZhong", 29, 65, 85, 100)],
                   dtype=person_type)

print(peoples)
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(ages)
print(chineses)
print(maths)
print(englishs)

print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))