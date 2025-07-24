import numpy as np

'''
arr = np.array([1,2,3,4,5,6])

new_arr = np.array_split(arr, 3)
new_arr2 = np.array_split(arr, 4)
new_arr3 = np.array_split(arr, 6)

print(new_arr)
print(new_arr2)
print(new_arr3)
'''
'''
arr = np.array([1,2,3,4,5,6,7,8])

new_arr = np.array_split(arr, 4)

print(new_arr)

print(new_arr[1])
print(new_arr[3])
print(new_arr[2])
'''
'''
#normal split with array_split()
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

new_arr = np.array_split(arr, 3)

print(new_arr)
print(new_arr[0])
'''
'''
#split with hsplit()
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

new_arr = np.hsplit(arr,3)
print(new_arr)
'''

#split with vsplit()
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

new_arr = np.vsplit(arr, 3)
print(new_arr)