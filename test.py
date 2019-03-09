import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([1, 5, 3, 4])
c = np.array([1, 3, 4, 0])

mut_a_b = np.matmul(a, b)
mut_a_c = np.matmul(a, c)

A = np.linalg.norm(a)
B = np.linalg.norm(b)
C = np.linalg.norm(c)

AB = float(mut_a_b) / (A + B)
AC = float(mut_a_c) / (A + C)

print(AB * 0.5 + 0.5)
print(AC * 0.5 + 0.5)
