import numpy as np

N = int(input("Enter maximum elements "))
f = np.ndarray((N,N), dtype=np.float32)
fx = np.ndarray((N,N), dtype=np.float32)
xg = np.ndarray((N,N), dtype=np.float32)
yg = np.ndarray((N,N), dtype=np.float32)

dx = 1.0/(N-1)
dy = dx

for i in range(N):
    for j in range(N):
        f[i][j] = np.sin(i*dx*np.pi)*np.sin(j*dy*np.pi)
        xg[i][j] = i*dx
        yg[i][j] = j*dy

xp = np.ndarray( (N,N), dtype=np.float32 )
yp = np.ndarray( (N,N), dtype=np.float32 )

for i in range(N):
    for j in range(N):
        xp[i][j] = np.random.random()
        yp[i][j] = np.random.random()
        fx[i][j] = np.sin(xp[i][j]*np.pi)*np.sin(yp[i][j]*np.pi)

