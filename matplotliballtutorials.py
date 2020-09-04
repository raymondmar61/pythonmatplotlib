import matplotlib.pyplot as plt

xcurve = [1,2,3,4,5]
ycurve = [1,4,9,16,25]
xvalues = [58, 89, 12, 73, 55, 61, 52, 43, 74, 84]
yvalues = [35, 51, 41, 14, 76, 34, 65, 54, 34, 27]
plt.title("plt.title()", fontsize=20)
plt.xlabel("plt.xlabel()")
plt.ylabel("plt.ylabel())")
plt.axis([0,100,0,100])
plt.tick_params(axis="both",labelsize=14)
plt.plot(xcurve,ycurve,linewidth=5)
plt.scatter(xvalues,yvalues,c="red",edgecolor="none",s=50)
plt.show()
plt.savefig("curveplot.png",bbox_inches='tight') #bbox_inches trims extra whitespace from the plot. If you want the extra whitespace around the plot, you can omit bbox_inches.

plainnumbers = [x for x in range(1,6)]
squarenumbers = [x**2 for x in range(1,6)]
plt.title("List Comprehension Square Numbers", fontsize=24)
plt.xlabel("X-Axis label Value", fontsize=10)
plt.ylabel("Y-Axis label Square of Value", fontsize=10)
plt.tick_params(axis="x", labelsize=5) #want tick_params to be same size, axis="both"
plt.tick_params(axis="y", labelsize=20) #want tick_params to be same size, axis="both"
plt.plot(squarenumbers) #can plot more than one line in a chart
plt.plot(plainnumbers, squarenumbers, linewidth=5)
plt.show()
#To plot a single point, use the scatter() function. Pass the single (x, y) values of the point of interest to scatter().
plt.scatter(2, 4, s = 200) #s is size of dots
plt.show()
#To plot a series of points, we can pass scatter() separate lists of x- and y-values.  No line connecting the points.  Points only.
xvalues = [1, 2, 3, 4, 5]
yvalues = [1, 4, 9, 16, 25]
plt.scatter(xvalues, yvalues, s=100)
plt.show()
xvalues1000 = list(range(1,1001))
yvalues1000 = [x**2 for x in xvalues1000]
plt.scatter(xvalues1000, yvalues1000, s=20) #default is blue dots with a black outline.  RM:  my Ubuntu Linux Python doesn't show a black outline
plt.show()
plt.scatter(xvalues1000, yvalues1000, c="red", edgecolor="none", s=15) #remove onlines around points set edgecolor = "none". Set color of points or dots c="red" or c=(R, G, B) values between 0 and 1.
plt.show()
plt.scatter(xvalues1000, yvalues1000, c=yvalues1000, cmap=plt.cm.Blues, edgecolor="none", s=40) #A colormap cmap is a series of colors in a gradient that moves from a starting to ending color. Colormaps are used in visualizations to emphasize a pattern in the data. For example, you might make low values a light color and high values a darker color.  Here’s how to assign each point a color based on its y-value in blue.
plt.show()
plt.scatter(xvalues1000, yvalues1000, c="green", edgecolor="none", s=10)
plt.axis([0,1100,0,1100000]) #the axis() function to specify the range of each axis w. Requires four values: the minimum and maximum values for the x-axis and the y-axis. Here, we run the x-axis from 0 to 1100 and the y-axis from 0 to 1,100,000.
plt.show()
#If you want your program to automatically save the plot to a file, you can replace the call to plt.show() with a call to plt.savefig().  File saved in same directory of python file.
plt.scatter(xvalues1000, yvalues1000, c="orange", edgecolor="none", s=10)
plt.axis([0,1100,0,1100000])
plt.savefig("filename.png", bbox_inches="tight") #bbox_inches trims extra whitespace from the plot. If you want the extra whitespace around the plot, you can omit bbox_inches.

highs = ['64', '71', '64', '59', '69', '62', '61', '55', '57', '61', '57', '59', '57', '61', '64', '61', '59', '63', '60', '57', '69', '63', '62', '59', '57', '57', '61', '59', '61', '61', '66']
fig = plt.figure(dpi=128, figsize=(100,6))  #dpi is dots per inch.  figsize is (length size, height size)
plt.plot(highs, c="red")  #highs is assumed as y-axis because there's one set of numbers in plt.plot
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("No xlabel leave blank with two quotes", fontsize=16)
fig.autofmt_xdate() #fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="x", which="major", labelsize=16) #which major is bigger than which minor
plt.tick_params(axis="y", which="minor", labelsize=16) #which major is bigger than which minor
plt.show()
xaxisnumbers = [x for x in range(1,11)]
brainnumbersone = [5,9,4,3,5,9,7,6,2,9]
brainnumberstwo = [56,89,45,12,34,98,15,23,83,92]
plt.scatter(brainnumbersone, brainnumberstwo,c="red", alpha=0.5) #alpha controls a color's transparency between 0 transparent and 1 opaque
plt.scatter(brainnumberstwo, brainnumbersone,c="blue", alpha=0.3) #alpha controls a color's transparency between 0 transparent and 1 opaque
plt.show()
#Shade an area between lines
plt.plot(xaxisnumbers, brainnumbersone, c="red")
plt.plot(xaxisnumbers, brainnumberstwo, c="blue")
plt.fill_between(xaxisnumbers, brainnumbersone, brainnumberstwo, facecolor='blue', alpha=0.1) #fill_between() the list dates for the x-values and then the two y-value series highs and lows. The facecolor determines the color of the shaded region
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()