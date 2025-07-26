import numpy as np
'''
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

print(np.unique(arr)) #to find the unique elements in the array

'''
'''
#To find the unique values of two arrays, use the union1d() method.

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print(np.union1d(arr1, arr2))
'''
'''
#To find only the values that are present in both arrays, use the intersect1d() method.

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print(np.intersect1d(arr1, arr2, assume_unique=True))
'''

#To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print(np.setdiff1d(arr1, arr2, assume_unique=True))


#To find only the values that are NOT present in BOTH sets, use the setxor1d() method.

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print(np.setxor1d(arr1, arr2, assume_unique=True))

