import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr.shape) #output is (2,5) because row is 2 and colom is 5

arr2 = np.array([1,2,3,4,5], ndmin=5)
print(arr2.shape)

#output is (1,1,1,1,5)
'''
1 "batch" of

1 "group" of

1 "item" of

1 "row" of

5 elements.
'''