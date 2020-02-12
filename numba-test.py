import numpy as np
from numba import jit, njit

x = np.arange(100).reshape(10,10)

@njit
def go_fast(a):
    trace = 0
    for i in range(a.shape[0]):
        trace +=np.tanh(a[i,i])
    return a+trace

def go_slow(a):
    trace = 0
    for i in range(a.shape[0]):
        trace +=np.tanh(a[i,i])
    return a+trace

#first run

import time

go_fast(x)

start = time.time()
go_fast(x)
end = time.time()
fast_time = end-start
print("Fast time ", fast_time)

start = time.time()
go_slow(x)
end = time.time()
slow_time = end-start
print("Slow time ", slow_time)

speedup = slow_time/fast_time
print("Speed up ", speedup)
