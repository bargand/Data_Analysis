import numpy as np

'''
arr = np.array([1,45,90,34,12,67])

filter_arr = [True, True, False, True, False, False]

print(arr[filter_arr])
'''
'''
#using for loops filter array
arr = np.array([1,45,90,34,12,67])

filter_arr = []

for i in arr:
    if i > 12:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

print(filter_arr)
print(arr[filter_arr])

'''
#
arr = np.array([1,45,90,34,12,67])

filter_arr = arr > 12

print(arr[filter_arr])
