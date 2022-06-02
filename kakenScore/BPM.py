import numpy as np
import statistics

a=[2,1,1,1,3,4,5,6,32,7,45,2,4,3,3,2,2,2,3,4,5,]
#b=np.average(a) #平均値

#print(b)

c=statistics.mode(a)

#print(c)

BPM=1800/c

print(BPM)