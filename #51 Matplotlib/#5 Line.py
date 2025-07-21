import matplotlib.pyplot as plt

xplot = [2,6,8,3,5]
yplot = [3,7,9,1,3]


#Line Style(ls)
'''
There are various line style like:

'solid'(default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	'' or ' '
'''

'''
plt.plot(xplot, yplot, ls = ":")
plt.show()
'''

'''
Line color, we write it as just c
'''
'''
plt.plot(xplot, yplot, "-", c="r")
plt.show()
'''

'''
Line width we just write lw and write the line width as a string
'''
'''
plt.plot(xplot, yplot, ":", c="k", lw="20")
plt.show()

'''

'''
double line in a single image
'''

plt.plot(xplot, "-", c="r")
plt.plot(yplot, ":", c="y")
plt.show()
















