import numpy as np

N = int(input("Enter maximum elements "))
f = np.ndarray((N,N), dtype=np.float32)
xg = np.ndarray((N,N), dtype=np.float32)
yg = np.ndarray((N,N), dtype=np.float32)

dx = 1.0/(N-1)
dy = dx

for i in range(N):
    for j in range(N):
        f[i][j] = np.sin(i*dx*np.pi)*np.sin(j*dy*np.pi)
        xg[i][j] = i*dx
        yg[i][j] = j*dy

