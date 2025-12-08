from numpy import random
import numpy as np
#to get random int from 0 to 100
x=random.randint(100)
print(x)
#to get random float from 0 to 1
y=random.rand()
print(y)
#to get 1d array of random of 5 random int from 0-100
z=random.randint(0,100,5)
print(z)
#to get 1d array of random of 5 random float from 0-1
a=random.rand(5)
print(a)
#to get 2d array of random of random int from 0-100
b=random.randint(0,100,(2,3))
print(b)
#to get 2d array of random of random float from 0-1
c=random.rand(2,3)
print(c)
#
d=random.choice([1,2,3,4])
print(d)
#
e=random.choice([1,2,3,4],size=(2,3))
print(e)
