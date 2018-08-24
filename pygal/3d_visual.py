# 3D图形

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import  cm
from mpl_toolkits.mplot3d import  Axes3D

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()