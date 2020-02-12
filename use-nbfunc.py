import numpy as np
import nbfunc 
import time

x = np.arange(100).reshape(10,10)

if  __name__ == "__main__":

    nbfunc.go_fast(x)
    nbfunc.go_slow(x)

    
    start = time.time()
    nbfunc.go_fast(x)
    end = time.time()
    fast_time = end-start
    print("Fast time: ", fast_time)

    start = time.time()
    nbfunc.go_slow(x)
    end = time.time()
    slow_time = end - start
    print("Slow time: ", slow_time)

    speedup = slow_time/fast_time
    print("Speed up ", speedup)
