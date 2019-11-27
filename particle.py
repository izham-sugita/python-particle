import numpy as np
import time 


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

    def DFO(self):
        print("Hey!")

    
    
xp = np.random.random()
yp = np.random.random()

N = int( input("Enter number of particle ") )
print(N)

#The keypoint in using numpy array to store
#an object is dtype=numpy.object.
pg = np.ndarray((N,),dtype=np.object) 

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


for i in range(N):
    print(pg[i].xp, pg[i].yp,
          pg[i].rank, pg[i].DFO() )


print("Ranking the particles based",
"on distance from origin")

#sorting DOF


