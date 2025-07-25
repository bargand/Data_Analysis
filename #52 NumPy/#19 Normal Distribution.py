import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(size=(2,3))

print(x)

'''
loc - (Mean) where the peak of the bell exists.
    This is the mean (center) of the distribution.
    The data will be centered around 2.

scale - (Standard Deviation) how flat the graph distribution should be.
    This is the standard deviation.
    It controls how spread out the data is.
    A larger value means wider spread.

size - The shape of the returned array.
    This means you generate 500 random values.
    Each value is drawn from the normal distribution defined by loc and scale
'''

sns.displot(random.normal(loc=2, scale=2, size=500), kind='kde')
plt.show()