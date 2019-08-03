import numpy as np
a = np.array([0, 1, 2, 3, 4, 5])

print(a.ndim)
print(a.shape)

b = a.reshape(2, 3)
print(b)
print(b.ndim)
print(b.shape)

print(a)
b[1][0] = 77

print(a)
print(b)

print(b**2)
print(a>4)
print(a[a>4])
