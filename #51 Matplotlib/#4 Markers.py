import matplotlib.pyplot as plt

xplot = [1,3,5,8]
yplot = [8,2,5,2]

'''
plt.plot(xplot, yplot, "o") #this "o" is called marker. that will mark the passing value point
plt.show()
'''

'''
There are verious types of marker like

'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
'''
'''
plt.plot(xplot, yplot, "v")

#or we can write

plt.plot(xplot, yplot, marker = "*")
plt.show()
'''
'''
There was various line and color methods like:
'-'	Solid line	
':'	Dotted line	
'--' Dashed line	
'-.' Dashed/dotted line

'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
'''
'''
plt.plot(xplot, yplot, "o:r") #marker|line|color (here we use o for marker, : for dotted line and r for red)
plt.show()
'''

'''
#marker size

plt.plot(xplot, yplot, "-o", ms = "20")  #here ms is marker size that is 20 px
plt.show()

'''


# marker edge color MarkerEdgeColor = mec
'''
plt.plot(xplot,yplot,"-o", ms=20, mec="r")
plt.show()
'''

#marker face color MarkerFaceColor = mfc

plt.plot(xplot, yplot, ":H" , ms="20" , mec="k", mfc="g")
plt.show()