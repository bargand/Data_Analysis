import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:/Python New/#53 Pandas/data.csv")

'''
# to show a simple graph
df.plot()
plt.show()
'''
'''
#to create a simple histogram
df.plot(kind="hist", x="Duration", y="Pulse", xlabel="Duration", ylabel="Pulse")
plt.show()
'''

#to create a simple scatter plot
df.plot(kind="scatter", x="Duration", y="Calories", xlabel="duration", ylabel="calories", title="Scatter plot between Calories with duration")
plt.show()