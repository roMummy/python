import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s =2)

# 突出起点和终点
plt.scatter(0, 0, c='yellow', edgecolors='none', s=10)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# 设置窗口尺寸
# plt.figure(figsize=(10,6), dpi=1440*900)

plt.show()