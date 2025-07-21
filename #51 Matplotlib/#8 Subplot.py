import matplotlib.pyplot as plt


'''
#mainplot 1st subplot
xplot = [2,6,8,3,5]
yplot = [3,7,9,1,3]

plt.subplot(1, 2, 1) #subplot first 1 is coloum, second 2 is row, third 1 is the number
plt.plot(xplot, yplot, ":", c="r")
plt.title("Deposit")


#mainplot 2nd subplot
xplot = [2,6,8,3,5]
yplot = [3,7,9,1,3]

plt.subplot(1,2,2) #subplot first 1 is coloum, second 2 is row, third 2 is the number
plt.plot(xplot,yplot)
plt.title("Withdraw")


plt.suptitle("Main title", c="r")
plt.show()

'''


x = [1,2,3,4,5]
y = [3,7,9,6,3]

plt.subplot(3,3,1) #3 ti row, 3 ti coloum and 1 number plot
plt.plot(x, y)
plt.xlabel("A")
plt.ylabel("B")
plt.title("subplot")


x = [1,2,3,4,5]
y = [3,7,9,6,3]

plt.subplot(3,3,2) #3 ti row, 3 ti coloum and 2 number plot
plt.plot(x, y)


x = [1,2,3,4,5]
y = [3,7,9,6,3]

plt.subplot(3,3,3) #3 ti row, 3 ti coloum and 3 number plot
plt.plot(x, y)


x = [1,2,3,4,5]
y = [3,7,9,6,3]

plt.subplot(3,3,4) #3 ti row, 3 ti coloum and 4 number plot
plt.plot(x, y)


x = [1,2,3,4,5]
y = [3,7,9,6,3]

plt.subplot(3,3,5) #3 ti row, 3 ti coloum and 5 number plot
plt.plot(x, y)


x = [1,2,3,4,5]
y = [3,7,9,6,3]

plt.subplot(3,3,6) #3 ti row, 3 ti coloum and 6 number plot
plt.plot(x, y)


x = [1,2,3,4,5]
y = [3,7,9,6,3]

plt.subplot(3,3,7) #3 ti row, 3 ti coloum and 7 number plot
plt.plot(x, y)


x = [1,2,3,4,5]
y = [3,7,9,6,3]

plt.subplot(3,3,8) #3 ti row, 3 ti coloum and 8 number plot
plt.plot(x, y)


x = [1,2,3,4,5]
y = [3,7,9,6,3]

plt.subplot(3,3,9) #3 ti row, 3 ti coloum and 9 number plot
plt.plot(x, y)


plt.suptitle("main plot title")
plt.show()