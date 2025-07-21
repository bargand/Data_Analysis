import matplotlib.pyplot as plt

x = [2,2,8,1,15,8,12,9,7,3,11,4,7,14,12]
y = [100,105,84,105,90,99,90,95,94,100,79,112,91,80,85]

#bar method to up and down bar diagram
'''
plt.bar(x, y, color="red") # here we write color in full and the color argument in full writing then this is exicuted
'''

#barh method to draw left to right bar diagram
plt.barh(x,y, color="yellow", height=0.3) # here height paramiter is use to give bar width

plt.show()