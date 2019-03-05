import numpy as np

# 从[1, 11) 间隔为2创建 array
x1 = np.arange(1, 11, 2)
# 从[1, 9] 创建5个等差 array
x2 = np.linspace(1, 9, 5)
print(x1)
print(x2)

print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))  # 取余
print(np.mod(x1, x2))  # 取余
