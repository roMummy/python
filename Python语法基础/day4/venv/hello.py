# sum = 0
# for x in range(100):
#     sum += x
# print(sum)

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

# import random
#
# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input("请输入："))
#     if number < answer:
#         print("大一点")
#     elif number > answer:
#         print("小一点")
#     else:
#         print("success")
#         break
# print ("总共猜了%d次" % counter)

"""
*
**
***
****
*****
"""

row = int(input("输入层数："))
for i in range(row) :
    for _ in range(i + 1):
        print ("*", end='')
    print ()