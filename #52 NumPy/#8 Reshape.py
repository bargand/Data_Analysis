import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

new_arr = arr.reshape(2,4)

# print(new_arr)

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr2.reshape(4,3))


#convert 1D array to 3D array

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr2.reshape(4,1,3))