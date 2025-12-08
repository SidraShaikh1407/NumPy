from numpy import random
import numpy as np
#shuffle
arr=np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

#permutation
arr1=np.array([11,22,33,44,55])
k=random.permutation(arr1)
print(k)
print(arr1)
