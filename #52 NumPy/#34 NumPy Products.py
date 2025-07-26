import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

a = np.prod(arr1) #simple multiplication
print(a)

b = np.prod([arr1 ,arr2]) #it will multiply the all elements in array
print(b)

c = np.prod([arr1, arr2], axis=1) #it will multiply with wise element
print(c)

d = np.cumprod(arr1) #it will multiplyone by one with first element
print(d)