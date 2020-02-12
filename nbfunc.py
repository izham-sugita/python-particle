import numpy as np
from numba import jit, njit
from numba import stencil

@stencil
def kernel(a):
    return 0.25*( a[0,1] + a[1,0] + a[0,-1] + a[-1,0]  )

#@jit(nopython=True)
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

#first run to compile

'''
go_fast(x)

import time

start = time.time()
go_fast(x)
end = time.time()
fast_time = end-start
print("go_fast time: %s"%(fast_time))

start = time.time()
go_slow(x)
end = time.time()
slow_time = end-start
print("go_slow time: %s"%(slow_time))

speedup = slow_time/fast_time
print("Speed up %f"%(speedup))

input_arr = np.arange(100).reshape(10,10)

output_arr = kernel(input_arr)

print(output_arr)
'''
