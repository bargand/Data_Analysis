import numpy as np

'''
arr = np.array([1,2,1,3,4,5,1,6,7])

new_arr = np.where(arr == 1)

print(new_arr)
'''
'''
#find even number
arr = np.array([1,2,3,4,5,6,7,8])

new_arr = np.where(arr%2 == 0)

print(new_arr)
'''
'''
#find the odd number
arr = np.array([1,2,3,4,5,6,7,8])

new_arr = np.where(arr%2 == 1)

print(new_arr)
'''
'''
#searchsorted() method where exicuted code is just show the first element in the array

arr = np.array([1,2,1,3,4,5,1,6,7,8])

new_arr = np.searchsorted(arr, 1)
print(new_arr)

'''
'''
#searchshorted in different direction
arr = np.array([1,2,1,3,4,5,1,6,7,8])

new_arr = np.searchsorted(arr, 1, side="right")
print(new_arr)
'''