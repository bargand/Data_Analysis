import numpy as np
from numpy import random

arr = np.array([1,2,3,4,5])

#using shuffle we can parmutation the array
random.shuffle(arr)
print(arr)

#using permutation() we can do also

print(random.permutation(arr))

#remember this 2 syntax for the one work