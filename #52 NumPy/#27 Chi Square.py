from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''
x = random.chisquare(df=12, size=10) # df means degree of freedom, and size is The shape of the returned array. 

print(x)
'''

#visualization

sns.displot(random.chisquare(df=12, size=1000), kind="kde")

plt.show()