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
