import numpy as np

a = np.array([[4, 8, 15], [16, 23, 42]])
print(a.shape)
print(a[:, 1])
print(a.mean(axis=0))
print(a * 2)
print(a[a > 10])