import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.normal(0.0, 5.0, 1000)
print(x)

sns.displot(x, kind="kde")
plt.show()