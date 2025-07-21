import matplotlib.pyplot as plt

#normal pie chart
'''
x = [25,25,40,10]

plt.pie(x)
plt.show()

'''

'''
#labels of the every plot of a chart

x = [25,25,40,10]
labels = ["apple", "banana", "jackfruit", "Guava"]

plt.pie(x, labels=labels)
plt.show()

'''

'''
#we can manupulate the start angle, but it will default start in -x axis
x = [25,25,40,10]
labels = ["apple", "banana", "jackfruit", "Guava"]

plt.pie(x, labels=labels, startangle=180)
plt.show()

'''

'''
# we can exploid that function can cut it down the value 
x = [25,25,40,10]
labels = ["apple", "banana", "jackfruit", "Guava"]
my_explode = [0.2, 0, 0.2, 0] #exploid value is high means it will far away from the parent chart

plt.pie(x, labels=labels, startangle=180, explode=my_explode)
plt.show()

'''

'''
#using shadow function

x = [25,25,40,10]
labels = ["apple", "banana", "jackfruit", "Guava"]
my_explode = [0.2, 0, 0, 0] #exploid value is high means it will far away from the parent chart

plt.pie(x, labels=labels, startangle=180, explode=my_explode, shadow=True)
plt.show()

'''

'''
#color method
x = [25,25,40,10]
labels = ["apple", "banana", "jackfruit", "Guava"]
my_explode = [0.2, 0, 0, 0] #exploid value is high means it will far away from the parent chart
colors = ["red", "green","yellow","black"]

plt.pie(x, labels=labels, startangle=180, explode=my_explode, colors=colors)
plt.show()

'''

x = [25,25,40,10]
labels = ["apple", "banana", "jackfruit", "Guava"]
my_explode = [0.2, 0, 0, 0] #exploid value is high means it will far away from the parent chart
colors = ["red", "green","yellow","black"]

plt.pie(x, labels=labels, startangle=180, explode=my_explode, colors=colors)
plt.legend(title = "Four Fruits:")
plt.show()











































