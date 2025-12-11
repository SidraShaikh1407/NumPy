from numpy import random
import numpy as np
#avg of 2nd column
x=random.randint(0,100,(5,3))
print(x)
print(x[:,2].mean())

#avg of first 5 rows of third and fourth column
y=random.randint(0,100,(6,5))
print(y)
print(y[0:6,3:5].mean())

#rowise sum of all possible values in array (axis=0 columnwise sum do oppo )
z=random.randint(0,100,(4,3))
print(z)
print(z.sum(axis=0))

#rowise mean of all possible values in array (axis=0 columnwise sum do oppo)
m=random.randint(0,100,(4,3))
print(m)
print(m.mean(axis=0))                 
                 
