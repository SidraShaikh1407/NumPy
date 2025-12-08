import numpy as np
#1-D ARRAY
arr=np.array([1,2,3,4,5,6,7,8],dtype= int)
#arr.shape=(2,2,2)
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
print(arr[1:6])
print(arr[1:6:2])
for i in arr:
    print(i)

#2-D ARRAY
arr1=np.array([[1,2,3],
              [4,5,6]])
print(arr1)
print(arr1.shape)
print(arr1.ndim)
print(arr1.size)
print(arr1.dtype)
print(arr1.itemsize)
print(arr1[0,0:2])
print(arr1[0:2,1])
#for printing each elt in the array
for i in arr1:
    for j in i:
        print(j)
#for printing each row
for i in arr1:
    print(i)

#3-D array
arr2=np.array([[[1,2,3],
               [4,5,6]],
               [[7,8,9],
                [10,11,12]]])
print(arr2)
print(arr2.shape)
print(arr2.ndim)
print(arr2.size)
print(arr2.dtype)
print(arr2.itemsize)
print(arr2[0,1,1:3])
print(arr2[1,1,0:3])

#copy(own the data)/doesnt change copied array if org is changed
#view(doesnt own the data)/ change view array if org is changed
x=arr.copy()
y=arr.view()
arr[0]=42
print(x)
print(arr)
print(y)
print(arr)
#base to check if its copy or view
# for copy> none and for view> org array
print(x.base)
print(y.base)




