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
