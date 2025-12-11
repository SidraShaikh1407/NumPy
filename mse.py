from numpy import random
import numpy as np
y_p=random.rand(10)
y=random.rand(10)
y_p.shape=(10,1)
y.shape=(10,1)
mse=(y_p-y)*(y_p-y)
print(y_p)
print(y)
print(mse.mean())
