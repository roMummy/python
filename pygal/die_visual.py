from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)

print(frequencies)