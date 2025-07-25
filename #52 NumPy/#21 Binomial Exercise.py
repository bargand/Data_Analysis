import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''
1. Change the Probability of Success
Modify the original code to simulate a binomial distribution with:

n = 10 trials

p = 0.7 probability of success

size = 1000

✅ Task: Plot the histogram and observe how the distribution shifts.
'''
'''
sns.displot(random.binomial(n=10, p=0.7, size=1000), kind='hist')
plt.show()
'''

'''
2. Change the Number of Trials
Keep p = 0.5, but now set:

n = 20 trials

size = 1000

✅ Task: Plot it and compare with the original (n=10). How does the spread change?
'''
'''
data={
    "x": random.binomial(n=20, p=0.5, size=1000),
    "y": random.binomial(n=10, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()
'''


'''
3. Small Sample Size
Try:

n = 10

p = 0.5

size = 30

✅ Task: Plot it and notice how the shape of the distribution is less smooth. Why?
'''
'''
sns.displot(random.binomial(n=10, p=0.5, size=30), kind='kde')

plt.show()
'''


'''
4. Compare Two Different Distributions
Plot two histograms side by side:

Distribution A: n=10, p=0.3

Distribution B: n=10, p=0.7

✅ Task: Use two sns.displot or subplots. Compare how the distributions are skewed.
'''
'''
data={
    "x": random.binomial(n=10, p=0.3, size=1000),
    "y": random.binomial(n=10, p=0.7, size=1000)
}

sns.displot(data, kind="hist")
plt.show()
'''


x= random.binomial(n=10, p=0.5, size=500)

y = np.bincount(x)
most_fre = np.argmax(y)

print(most_fre)

sns.displot(x, color="yellow")
plt.axvline(most_fre, ls=":", c="red")

plt.show()