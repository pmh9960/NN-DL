import numpy as np
import time

# vec

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
sum = np.dot(a, b)
toc = time.time()

print("vectorization version : " + str(1000 * (toc - tic)) + "ms")

# non-vec
sum = 0

tic = time.time()

for i in range(1000000):
    sum += a[i] * b[i]

toc = time.time()

print("non-vectorization version : " + str(1000 * (toc - tic)) + "ms")
