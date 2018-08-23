"""使用matplotlib绘制折线图"""
import matplotlib.pyplot as plt

input_value = [1,2,3,4,5]
squares = [1, 4, 9, 14, 25]
# 设定线条宽度
plt.plot(input_value, squares, linewidth=5)

# 设置标题 添加x、y轴标题
plt.title("Squares Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)

plt.show()