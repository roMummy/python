"""散点图"""
import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]


plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置标题 添加x、y轴标题
plt.title("Squares Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)

# plt.show()

# 自动保存图表
plt.savefig('squares_plt.png')