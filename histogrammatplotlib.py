#NumPy Tutorial Part - 2 _ NumPy Array _ Python NumPy Tutorial Part -2_ Python Tutorial _ Simplilearn [720p]
#Ctrl+W closes chart window

import numpy as np
from matplotlib import pyplot as plt
a = np.array([20,87,4,40,53,74,56,51,11,20,40,15,79,25,27])
bins = [0, 20, 40, 60, 80, 100]
plt.hist(a, bins)
plt.title("Histogram x-axis or bins range inclusive to exclusive")
plt.show()