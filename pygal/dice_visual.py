from die import Die
import pygal

# 创建2个D6
die1 = Die()
die2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)

# 对结果进行可视化
# hist = pygal.
hist = pygal.Radar(fill=True)

hist.title = "Die"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6+D6', frequencies)
hist.render_to_file('radar_visual.svg')