import numpy as np

# Rank 1 Array. Don't use it!
a = np.random.randn(5)  # a.shape = (5,)
print(a)
print(a.T)
print(np.dot(a, a.T), "\n")

# Vector
a = np.random.randn(5, 1)  # a.shape = (5,1)
print(a)
print(a.T)
print(np.dot(a, a.T), "\n")
