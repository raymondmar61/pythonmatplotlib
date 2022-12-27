#Python Data Analytics And Visualization by Phuong Vo.T.H Chapter 04 Data Visualization
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 3, 6)
print(x) #print [0.  0.6 1.2 1.8 2.4 3. ]
y = np.power(x, 2)
print(y) #print [0.   0.36 1.44 3.24 5.76 9.  ]
plt.figure()
plt.plot(x, y, "r") #r is the color red.  Red color graph.
plt.xlabel("xlabel x")
plt.ylabel("ylabel y")
plt.title("title Data visualization in Matlab like API")
plt.axis([0, 6, 0, 12]) #set x-axis range from 0 to 6.  Set y-axis range from 0 to 12.
plt.show() #return standard x-y chart
redline = plt.plot(y, color="red", linestyle="--", linewidth=2.0, marker="o")
plt.show() #return red chart dotted line solid dots at x-y coordinates
plt.figure("a")
plt.subplot(221) #2x2 figure.  First position top left.  Same as plt.subplot(2,2,1).
plt.title("Top left in a 2x2 first position")
plt.plot(y + y, "r--")
plt.subplot(222) #2x2 figure.  Second position top right.
plt.title("Top right in a 2x2 second position")
plt.plot(y * 3, "ko")
plt.subplot(223) #2x2 figure.  Third position bottom left.
plt.title("Bottom left in a 2x2 third position")
plt.plot(y * y, "b^")
plt.subplot(224) #2x2 figure.  Fourth position bottom right.
plt.title("Bottom right in a 2x2 fourth position")
plt.show() #Four small charts in a 2x2 formation.  No need to worry what the charts look like.
#Scatterplot
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
print(x) #print [-1.42014577e+00  1.41498808e+00 -1.92571021e+00 -1.57359781e+00  -7.97586176e-01 -1.50737748e+00  2.07114641e-01  1.24583292e-01 . . . ]
print(y) #print [-1.7096309   0.34671556 -0.36682387  0.31231977 -0.845551   -0.03432209 -1.1454793  -1.29103334 -0.6136159   0.67799502 -1.64767171  0.32590703 . . . ]
plt.scatter(x, y)
plt.show()
#Barplot
x = np.arange(5)
y = 3.15 + 2.71 * np.random.rand(5) #five random numbers between zern and one
plt.subplots(2)
plt.subplot(211) #2x1 figure.  First position top.
plt.bar(x, y, align="center", alpha=0.4, color="y") #yellow color.  Alpha modifies the color(?)
plt.xlabel("xlabel x")
plt.ylabel("ylabel y")
plt.title("Vertical bar plot yellow color")
plt.subplot(212) #2x1 figure.  Second position bottom.
plt.barh(x, y, align="center", color="c") #RM:  I can't recognize the "c".  It looks like aqua.
plt.xlabel("xlabel x")
plt.ylabel("ylabel y")
plt.title("Horizontal bar plot cyan color")
plt.show()
#Histogram
number1 = 100
number2 = 25
fig, (firsthistogram, secondhistogram) = plt.subplots(ncols=2) #Two plots or two smaller charts in one plot horizontally
x = number1 + (number2 * np.random.randn(200))
print(x) #print [ 71.76978937 147.61551217 130.60093239 123.58679138 134.31369272 . . . 120.96724422 114.43237061 108.07863633 100.39644355  85.14706441]
firsthistogram.hist(x, 20, histtype="stepfilled", facecolor="g", alpha=0.75)
firsthistogram.set_title("First histogram stepfilled left")
secondhistogram.hist(x, bins=[100, 150, 165, 170, 185], histtype="bar", rwidth=0.8)
secondhistogram.set_title("Second histogram uniquel (RM:  unequal?) bins right")
plt.tight_layout() #Improves padding.  Adjust subplots parameters to give specified padding.  RM:  what specified padding?
plt.show()
#Legends and annotations in chart.  RM:  skipped annotations
x = np.linspace(0, 1, 20)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
plt.plot(x, y1, "c", label="y=sin(x) color is c aqua or bright neon teal")
plt.plot(x, y2, "y", label="y=cos(x) color is y yellow")
plt.plot(x, y3, "r", label="y=tan(x) color is r red")
plt.legend(loc="upper left") #Display legend upper left of chart.  Valid location options: lower left, right, upper left, lower center, upper right, center, lower right, upper right, center right, best, upper center, and center left. The default position setting is upper right.
plt.show() #return three lines sin, cos, and tan in different colors
#Plot charts using Pandas as the data source
import pandas as pd
pandaseries = pd.Series(np.random.normal(10, 8, 20))
pandaseries.plot(style="ko-", alpha=0.4, label="Pandas data source plot line chart")
plt.legend()
plt.show() #return a gray color line chart with solid dots at each x-y coodinate gray color, too
datasource = {"medianage": [24.2, 26.4, 28.5, 30.3], "density": [244, 256, 268, 279]}
indexlabel = ["2000", "2005", "2010", "2014"]
pandasdataframe = pd.DataFrame(datasource, index=indexlabel)
pandasdataframe.plot(kind="bar", subplots=True, sharex=True) #subplots=True means each data column is in its own subplot or own chart.  sharex or sharey shares the same x or y axis, linking sticks, and limits.
plt.tight_layout()
plt.show() #return two bar charts vertically medianage top blue color and density bottom orange color
