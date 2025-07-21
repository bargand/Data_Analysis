import matplotlib.pyplot as plt

xplot = [2,6,8,3,5]
yplot = [3,7,9,1,3]

plt.plot(xplot, yplot, "-", marker="o")

# plt.grid()  #for x and y axis grid

# plt.grid(axis="x")  #for x axis grid
# plt.grid(axis="y")  #for y axis grid

'''
style the grid
'''
plt.grid(ls=":", c="r", lw="1")

plt.show()