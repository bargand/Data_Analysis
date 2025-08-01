import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(1.0, 5.0, 1000)
y = np.random.normal(4.0, 10.0, 1000)

plt.scatter(x, y)
plt.show()