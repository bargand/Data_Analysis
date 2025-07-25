from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''
lam = 2
This is the λ (lambda) parameter.

It represents the expected number of events per interval.

Example: If you're simulating customer arrivals at a shop, then on average, you expect 2 customers per time unit (e.g., per minute).

But remember: Poisson values are not fixed, they vary around that average. You may see 0, 1, 2, 3, 4, or more — but the mean will tend toward 2 over many samples.
'''

'''
size = 10
This tells NumPy to generate 10 random samples from the Poisson distribution with λ = 2.

Each sample represents how many events happened in one interval.

You’re simulating 10 intervals, each with an expected rate of 2 events.
'''
'''
sns.displot(random.poisson(lam=2, size=500), kind='kde')

plt.show()
'''


#differents between normal, binomial and poison distribution

data = {
    "normal": random.normal(loc=2, scale=2, size=1000),
    "binomial": random.binomial(n=2, p=0.5, size=1000),
    "poisson": random.poisson(lam=2, size=1000)
}

sns.displot(data, kind='kde')

plt.show()