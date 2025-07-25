from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
'''
Used to describe probability where every event has equal chances of occuring.

E.g. Generation of random numbers.

It has three parameters:

low - lower bound - default 0 .0.

high - upper bound - default 1.0.

size - The shape of the returned array.
'''
#create a uniform array with 2 row and 3 coloum
'''
x = random.uniform(size=(2,3))
print(x)
'''

#visualization

sns.displot(random.uniform(size=1000), kind='kde')

plt.show()