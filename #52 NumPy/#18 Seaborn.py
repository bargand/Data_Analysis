import matplotlib.pyplot as plt
import seaborn as sns

'''
sns.displot([1,5,3,2,5]) # here one histogram is generated but why i dont know

plt.show()
'''

sns.displot([1,2,3,4,5], kind='kde')
# sns.displot([1,2,3,4,5], kind='ecdf')
# sns.displot([1,2,3,4,5], kind='hist')

plt.show()