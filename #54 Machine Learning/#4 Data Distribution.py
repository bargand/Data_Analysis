import numpy as np

'''
Data Distribution
Earlier in this tutorial we have worked with very small amounts of data in our examples, just to understand the different concepts.

In the real world, the data sets are much bigger, but it can be difficult to gather real world data, at least at an early stage of a project.

How Can we Get Big Data Sets?
To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.
'''

print(np.random.uniform(0.0, 7.0, 500))

#to create a histogram
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 500) 

plt.hist(x, 5)
plt.show()
