import matplotlib.pyplot as plt

xplot = [2,6,8,3,5]
yplot = [3,7,9,1,3]

plt.plot(xplot, yplot, ":")

font1 = {"family":"poppins", "color": "red", "size": "20"}
font2 = {"family":"poppins", "color": "yellow", "size": "15"}
font3 = {"family":"poppins", "color": "blue", "size": "15"}


plt.title("Bargand Label", loc="center", fontdict=font1)
plt.xlabel("X axix label", fontdict=font2)
plt.ylabel("Y axis label", fontdict=font3)

plt.show()



'''
use a variable for font and in plot we use fontdict for the use of the font

we use xlabel and ylabel function for the labelling the graph plot
'''