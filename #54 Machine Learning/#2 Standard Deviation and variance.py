import numpy as np

data_set = [34,67,90,12,45,76,98,34,23,67,34,34]
data_set2 = [1,2,3,4,5,6,7,8,9]

'''
What is Standard Deviation?
Standard deviation is a number that describes how spread out the values are.

A low standard deviation means that most of the numbers are close to the mean (average) value.

A high standard deviation means that the values are spread out over a wider range.
'''
#to calculate the standard deviation
print(round(np.std(data_set)))
print(round(np.std(data_set2)))

'''
Variance
Variance is another number that indicates how spread out the values are.

In fact, if you take the square root of the variance, you get the standard deviation!

Or the other way around, if you multiply the standard deviation by itself, you get the variance!
'''
#to calculate the variance
print(round(np.var(data_set)))
print(round(np.var(data_set2)))