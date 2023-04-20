#Advanced Guide To Python 3 Programming by John Hunt Chapter 05 Introduction To Matplotlib
import matplotlib.pyplot as pyplot
pyplot.plot([1, 0.25, 0.5, 2, 3, 3.75, 3.5]) #the plot() functions recvies y-axis values.  The x-axis vlaues are implied by the position of the y values in the list.
pyplot.show() #line chart plot points (0,1), (1,0.25), (2,0.5), (3,2), (4,3), (5.375), (6,3.5)
'''
Plot components
pyplot.axes.Axes An Axes defined to maintain the chart elements.
pyplot.title("Chart tile")
pyplot.axis.ticks.  Major ticks are larger and may be labeled.  Minor ticks are smaller and may be labeled.
Tick Labels Major and Minor are labels on a Tick.
pyplot.axis.Axis defines an Axis object within a parent Axes instance
Axis Labels to describe the Axis
Plot identify the chart type such as line chart or scatter plot chart.
Grid dispaly with a variety of different line styles such as solid or dash, colors, and line widths.
'''

#Advanced Guide To Python 3 Programming by John Hunt Chapter 06 Graphing With Matplotlib Pyplot
import matplotlib.pyplot as pyplot
import numpy as np
xcoordinates = [0, 1, 2, 3, 4, 5, 6]
ycoordinates = [0, 2, 6, 14, 30, 43, 75]
pyplot.xlabel("xaxis label Time", fontsize=12)
pyplot.ylabel("yaxis label Speed", fontsize=12)
pyplot.title("line chart title Speed v Time")
pyplot.plot(xcoordinates, ycoordinates, "bo-")
pyplot.show() #line chart bo- blue color circle marker solid line
'''
Code format strings colors
b blue
g green
r red
c cyan
m magenta
y yellow
k black
w white

Code format strings markers
. point marker
, pixel
o circle
v triangle down
^ triangle up
< triangle left
> triangle right
s square
p pentagon
* star
h hexagon1
+ plus
x x marker
D Diamond marker

Code format strings line
-  solid line
-- double dash
-. dash dot
:  dotted
'''
pyplot.plot(xcoordinates, ycoordinates, "rs--")
pyplot.show() #line chart bo- red color square marker double dash line
ridingscattercoordinates = ((17, 18, 21, 22, 19, 21, 25, 22, 25, 24), (3, 6, 3.5, 4, 5, 6.3, 4.5, 5, 4.5, 4))
swimmingscattercoordinates = ((17, 18, 20, 19, 22, 21, 23, 19, 21, 24), (8, 9, 7, 10, 7.5, 9, 8, 7, 8.5, 9))
sailingscattercoordinates = ((31, 28, 29, 36, 27, 32, 34, 35, 33, 39), (4, 6.3, 6, 3, 5, 7.5, 2, 5, 7, 4))
pyplot.scatter(x=ridingscattercoordinates[0], y=ridingscattercoordinates[1], c="red", marker="o", label="legend label riding")
pyplot.scatter(x=swimmingscattercoordinates[0], y=swimmingscattercoordinates[1], c="green", marker="^", label="legend label riding")
pyplot.scatter(x=sailingscattercoordinates[0], y=sailingscattercoordinates[1], c="blue", marker="*", label="legend label riding")
pyplot.xlabel("xaxis label Age")
pyplot.ylabel("yaxis label Hours")
pyplot.title("scatter plot title Activities")
pyplot.legend()
pyplot.show() #scatter graph riding red circle, swimming green triangle, sailing blue star with legend top right
xscattercoordinates = (5, 5.5, 6, 6.5, 7, 8, 9, 10)
yscattercoordinates = (120, 115, 100, 112, 80, 85, 69, 65)
#The polyfit() function performs a least squares polynomial fit for the data it is given. A poly1d class is then created based on the array returned by polyfit().
z = np.polyfit(xscattercoordinates, yscattercoordinates, 1)
p = np.poly1d(z)
pyplot.scatter(xscattercoordinates, yscattercoordinates)
pyplot.title("scatter plot with trend line using numpy")
pyplot.plot(xscattercoordinates, p(xscattercoordinates), color="red")
pyplot.show() #scatter graph with red color trend line from northwest to southeast
labelspiechart = ("Python", "Java", "Scala", "C#")
sizespiechart = [45, 30, 15, 10]
pyplot.pie(sizespiechart, labels=labelspiechart, autopct="%1.f%%", counterclock=False, startangle=90) #The start angle startangle is moved 90 degrees for the first segment starts at the top of the pie chart
pyplot.show() #pie chart 45% Python blue, 30% Java orange, 15% Scala green, 10% C# red
labelsbarchart = ('Python', 'Scala', 'C#', 'Java', 'PHP')
indexbarchartlabelxaxisposition = (1, 2, 3, 4, 5)
sizesbarchartyaxisvalues = [45, 10, 15, 30, 22]
pyplot.bar(indexbarchartlabelxaxisposition, sizesbarchartyaxisvalues, tick_label=labelsbarchart)
pyplot.xlabel("xaxis label Programming Languages")
pyplot.ylabel("yaxis label Usage Number")
pyplot.show() #vertical bar chart blue bars
pyplot.barh(indexbarchartlabelxaxisposition, sizesbarchartyaxisvalues, tick_label=labelsbarchart, color="red")
pyplot.show() #horizontal bar chart red bars.  xlabels start from bottom Python going to the top PHP.
labelsbarchart = ('Python', 'Scala', 'C#', 'Java', 'PHP')
indexbarchartlabelxaxisposition = (1, 2, 3, 4, 5)
webusagebarchartyaxisvalues = [20, 2, 5, 10, 14]
datascienceusagebarchartyaxisvalues = [15, 8, 5, 15, 2]
gamesusagebarchartyaxisvalues = [10, 1, 5, 5, 4]
pyplot.bar(indexbarchartlabelxaxisposition, webusagebarchartyaxisvalues, tick_label=labelsbarchart, label="Web", color="blue")
pyplot.bar(indexbarchartlabelxaxisposition, datascienceusagebarchartyaxisvalues, tick_label=labelsbarchart, label="Data Science", color="red")
pyplot.xlabel("xaxis label Programming Languages")
pyplot.ylabel("yaxis label Usage Number")
pyplot.legend()
pyplot.show() #vertical stacked bar chart web in blue top of the stack, data science in red bottom of the stack.  Legend top right.
pyplot.bar(indexbarchartlabelxaxisposition, webusagebarchartyaxisvalues, tick_label=labelsbarchart, label="Web", color="blue")
pyplot.bar(indexbarchartlabelxaxisposition, datascienceusagebarchartyaxisvalues, tick_label=labelsbarchart, label="Data Science", color="red", bottom=webusagebarchartyaxisvalues) #The bottom parameter specifies the bottom location or the bottom of the stacked bars
webandgameusagesum = [webusagebarchartyaxisvalues[i] + datascienceusagebarchartyaxisvalues[i] for i in range(0, len(webusagebarchartyaxisvalues))]
print(webandgameusagesum) #print [35, 10, 10, 25, 16]
pyplot.bar(indexbarchartlabelxaxisposition, gamesusagebarchartyaxisvalues, tick_label=labelsbarchart, label="Games", color="green", bottom=webandgameusagesum) #The bottom parameter specifies the bottom location or the bottom of the stacked bars
pyplot.xlabel("xaxis label Programming Languages")
pyplot.ylabel("yaxis label Usage Number")
pyplot.legend()
pyplot.show() #vertical stacked bar chart web in blue bottom, data science in red middle, games in green top.  Legend top right.
#Specify the bottom locations for the next sets of bars using the bottom parameter after the first set of values.  First set is webusagebarchartyaxisvalues.  Second set is datascienceusagebarchartyaxisvalues with webusagebarchartyaxisvalues as the bottom.  Third set is gamesusagebarchartyaxisvalues with webandgameusagesum adding webusagebarchartyaxisvalues and datascienceusagebarchartyaxisvalues as the bottom using list comprehension.  First set to third set bottom to top.
groupbarwidth = 0.35
teamaresults = (60, 75, 56, 62, 58)
teambresults = (55, 68, 80, 73, 55)
indexteama = (1, 2, 3, 4, 5)
indexteamb = [i + groupbarwidth for i in indexteama]
print(indexteamb) #print [1.35, 2.35, 3.35, 4.35, 5.35]
midpointticks = [i + groupbarwidth / 2 for i in indexteama]
print(midpointticks) #print [1.175, 2.175, 3.175, 4.175, 5.175]
midpointtickslabels = ("Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5")
pyplot.bar(indexteama, teamaresults, groupbarwidth, color="b", label="Team A")
pyplot.bar(indexteamb, teambresults, groupbarwidth, color="g", label="Team B")
pyplot.xlabel("x label Labs")
pyplot.ylabel("y label Scores")
pyplot.title("Group bar schart Scores By Lab")
pyplot.xticks(midpointticks, midpointtickslabels)
pyplot.legend()
pyplot.show() #group vertical stacked bar chart Team A blue left group, Team B green right group.  Legend top right.
#The midpointticks are calculated for the two bars to be next to each other.  indexteama is 1, indexteamb is 1.35, midpointticks 1.175; indexteama is 2, indexteamb is 2.35, midpointticks 2.175; indexteama is 3, indexteamb is 3.35, midpointticks 3.175. . . .  The midpointtickslabels places the tick labels at 1,175, 2.175, 3,175, . . . which is the center for indexteama and indexteamb.
#Multiple line charts in one chart.  Subplots.
txaxiscoordinatesrange = range(0, 20)
syaxiscoordinatesrange = range(30, 10, -1)
print(list(txaxiscoordinatesrange)) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(syaxiscoordinatesrange)) #print [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
gridsize = "22"
figure = pyplot.figure() #initialize a figure
firstposition = int(gridsize + "1")
print("Adding first subplot to position", firstposition)
axis1 = figure.add_subplot(firstposition)
axis1.set(title="subplot(2 rows,2 columns,1 top left)")
axis1.plot(txaxiscoordinatesrange, syaxiscoordinatesrange)
secondposition = int(gridsize + "2")
print("Adding second subplot to position", secondposition)
axis2 = figure.add_subplot(secondposition)
axis2.set(title="subplot(2 rows,2 columns,1 top right)")
axis2.plot(txaxiscoordinatesrange, syaxiscoordinatesrange, "r-.")
thirdposition = int(gridsize + "3")
print("Adding third subplot to position", thirdposition)
axis3 = figure.add_subplot(thirdposition)
axis3.set(title="subplot(2 rows,2 columns,1 bottom left)")
axis3.plot(txaxiscoordinatesrange, syaxiscoordinatesrange, "g:")
fourthposition = int(gridsize + "4")
print("Adding fourth subplot to position", fourthposition)
axis4 = figure.add_subplot(fourthposition)
axis4.set(title="subplot(2 rows,2 columns,1 bottom right)")
axis4.plot(txaxiscoordinatesrange, syaxiscoordinatesrange, "y--")
pyplot.show() #one chart with four subcharts as line charts
'''
Adding first subplot to position 221
Adding second subplot to position 222
Adding third subplot to position 223
Adding fourth subplot to position 224
'''