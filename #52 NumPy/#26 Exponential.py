from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''
x = random.exponential(scale=2, size=(2,3)) #2 row and 3 coloum
print(x)
'''

#visualization

sns.displot(random.exponential(scale=3, size=1000), kind='kde') #scale means inverse of rate

plt.show()