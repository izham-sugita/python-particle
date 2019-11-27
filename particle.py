import numpy as np
import time 
import sys # getsizeof() function to check memory size

class ryushi:
    #rank is the sorting number
    #for particle location ranking
    #with the nearest to origin is 0
    rank=0

    #ptype is the particle type
    # ptype =1 : fluid
    # ptype =0 : boundary
    ptype = 1

    #initial position
    def __init__(self, xp, yp):
        self.xp = xp
        self.yp = yp

    def dfo(self):
        d = np.sqrt( self.xp*self.xp + self.yp*self.yp  )
        return d

    
xp = np.random.random()
yp = np.random.random()

N = int( input("Enter number of particle ") )
print(N)

#The keypoint in using numpy array to store
#an object is dtype=numpy.object.
pg = np.ndarray((N,),dtype=np.object)
pg1 = np.ndarray((N,),dtype=np.object) 

#threshold value
alpha = 0.05
beta = 0.95

for i in range(N):
    xp = np.random.random()
    if(xp < alpha or xp > beta):
        xp = np.random.random()
    else:
        xp = xp
    
    yp = np.random.random()
    if(yp < alpha or yp > beta):
        yp = np.random.random()
    else:
        yp = yp
    
    pg[i] = ryushi(xp,yp)
    pg1[i] = ryushi(xp,yp)

'''
for i in range(N):
    print(pg[i].xp, pg[i].yp,
          pg[i].rank )
'''

print("Ranking the particles based",
"on distance from origin")
#sorting DOF
    
temp = np.ndarray((N,), dtype=np.float)
for i in range(N):
    temp[i] = pg[i].dfo()

#ranking
sorted_array = np.sort(temp)

for i in range(N):
    for j in range(N):
        if(sorted_array[i] == pg[j].dfo()):
            pg[j].rank = i

for i in range(N):
    for j in range(N):
        if(pg[j].rank == i):
            pg1[i].rank = i
            pg1[i].xp = pg[j].xp
            pg1[i].yp = pg[j].yp

for i in range(N):
    print(pg1[i].rank," ", pg1[i].xp,"  ", pg1[i].yp,"  ", pg1[i].dfo())

print( sys.getsizeof(pg), " bytes" )
print( sys.getsizeof(pg1), " bytes" )
