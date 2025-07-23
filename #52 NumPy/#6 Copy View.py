import numpy as np

'''
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
'''

'''
#if we chnage the main arrya then it will not effect in copy array
arr = np.array([1,2,3,4,5])

copy_arr = arr.copy()

arr[0] = 68

print(arr)
print(copy_arr)

'''
'''
#if we change the eliment in copy array then it will not effect in the main array
arr = np.array([1,2,3,4,5])
copy_arr = arr.copy()

copy_arr[0] = 90

print(arr)
print(copy_arr)

'''

arr = np.array([1,2,3,4,5])

copy_arr = arr.copy()

arr[1] = 45
view_arr = arr.view()

print(copy_arr)
print(view_arr)










































