from numpy import random
import numpy as np
arr1=random.randint(1,100,(2,3))
arr2=random.randint(1,100,(2,3))
print(arr1)
print(arr2)
add=arr1+arr2
sub=arr1-arr2
mul=arr1*arr2
print(add)
print(sub)
print(mul)


print(arr1.min())
print(arr1.max())
print(arr1.mean())
print(arr1.var())
print(arr1.std())

print(arr1.mean(axis=0))
print(arr1.mean(axis=1))
