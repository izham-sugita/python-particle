import numpy as np

N = int(input("Enter N "))
xp = np.ndarray((N,N), dtype=np.float32)
yp = np.ndarray((N,N), dtype=np.float32)
f = np.ndarray((N,N), dtype=np.float32)

for i in range(N):
    for j in range(N):
        xp[i][j] = np.random.random()
        yp[i][j] = np.random.random()
        f[i][j] = np.sin(xp[i][j]*np.pi ) * np.sin(yp[i][j]*np.pi )
        

fp = open("random.csv","w")
fp.write("x,y,z,f\n")
for i in range(N):
    for j in range(N):
        str_x = str(xp[i][j])
        str_y = str(yp[i][j])
        str_z = str( 0.0 )
        str_f = str(f[i][j])
        str_all = str_x+","+str_y+","+str_f+","+str_f+"\n"
        fp.write(str_all)

fp.close()
