from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''
x = random.multinomial(n=2, pvals=[1/2, 1/2])
print(x) 
'''

sns.displot(random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6]), kind='kde')

plt.show()