import numpy as np
import cupy as cp
import time

x_cpu = np.ones((1000, 1000, 500))
x_gpu = cp.ones((1000, 1000, 500))


def do_some_math(x):
    x *= 10
    x *= x
    x += x
    x /= x


# CPU (numpy)
t = time.time()
do_some_math(x_cpu)
print(time.time() - t)

# GPU (CuPy)
t = time.time()
do_some_math(x_gpu)
print(time.time() - t)
