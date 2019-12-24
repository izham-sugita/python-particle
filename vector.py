import numpy as np

imax = 101
jmax = 101

u = np.ndarray((imax,jmax),dtype=np.float32)
v = np.ndarray((imax,jmax),dtype=np.float32)

x = np.ndarray((imax,jmax),dtype=np.float32)
y = np.ndarray((imax,jmax),dtype=np.float32)

dx = 1.0/(imax-1)
dy = 1.0/(imax-1)
xc = 0.5
yc = 0.5
om = 2.0 # rad/sec

for i in range(imax):
    for j in range(imax):
        x[i][j] = i*dx
        y[i][j] = j*dy

for i in range(imax):
    for j in range(jmax):
        u[i][j] = -(y[i][j] - yc)*om
        v[i][j] = (x[i][j] -xc)*om

        
fp = open("vector-field.csv","w")
fp.write("x,y,z,u,v\n")
for i in range(imax):
    for j in range(jmax):
        str_x = str(x[i][j])
        str_y = str(y[i][j])
        str_z = str( 0.0 )
        str_u = str(u[i][j])
        str_v = str(v[i][j])
        str_all = str_x+","+str_y+","+str_z+","+str_u+","+str_v+"\n"
        fp.write(str_all)

fp.close()

fp = open("grid.csv","w")
fp.write("x,y,z\n")
for i in range(imax):
    for j in range(jmax):
        str_x = str(x[i][j])
        str_y = str(y[i][j])
        str_z = str( 0.0 )
        str_all = str_x+","+str_y+","+str_z+"\n"
        fp.write(str_all)

fp.close()
