from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''
x = random.logistic(loc=2, scale=2, size=(2,3))

print(x)

# sns.displot(x, kind='kde')

# plt.show()
'''
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
'''
sns.displot(random.logistic(loc=2, scale=2, size=1000), kind='kde')
plt.show()
'''

#differents

data={
    "normal": random.normal(loc=2, scale=2, size=1000),
    "binomial": random.binomial(n=2, p=0.5, size=1000),
    "poisson": random.poisson(lam=2, size=1000),
    "uniform": random.uniform(size=1000),
    "logistic": random.logistic(loc=2, scale=2, size=1000)
}

sns.displot(data, kind="kde")
plt.show()