import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([61,70,18,96,10])

a = np.diff(arr1) #simple substruction
print(a)

'''
We can perform this operation repeatedly by giving parameter n.

E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
'''
b1 = np.diff(arr2, n=1)
b2 = np.diff(arr2, n=2)
b3 = np.diff(arr2, n=3)
b4 = np.diff(arr2, n=4)

print(b1)
print(b2)
print(b3)
print(b4)