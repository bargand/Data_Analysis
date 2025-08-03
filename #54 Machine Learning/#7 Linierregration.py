import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

x = np.random.uniform(1,100,100)
y = np.random.uniform(1,100,100)

slope, intercept, r, p, std_err = stats.linregress(x, y)

'''
slope: How much y increases for each unit increase in x.(protek y unit barar sathe sathe x kotota barche )

intercept: The value of y when x = 0.

r: Correlation coefficient (strength and direction of the relationship).

p: P-value (how likely it is that the relationship occurred by chance).

std_err: Standard error of the estimate.
'''
print(slope)
print(intercept)
print(r)
print(p)
print(std_err)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()