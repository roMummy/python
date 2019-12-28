# coding=utf-8

"""
寻找水仙花数。

说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
"""

# for num in  range(100,1000):
#     low = num % 10
#     mid = num // 10 % 10
#     hight = num // 100
#     if num == low ** 3 + mid ** 3 + hight ** 3 :
#         print (num)

"""
正整数反转，例如：将12345变成54321
"""

# num = int(input("num = "))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     print (reversed_num)
#     num //= 10
# print ("end: %d" % reversed_num)

"""
百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + y * 3 + z / 3 == 100:
#             print ("公鸡：%d, 母鸡：%d，🐥：%d" % (x, y, z))

"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
"""

# from random import  randint
#
# money = 1000
# while money > 0 :
#     print ("你的总资产为：", money)
#     needs_go_on = False
#     while True:
#         debt = int(input("请下注："))
#         if 0 < debt <= 1000 :
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print ("玩家点数：", first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了, 游戏结束!')

"""
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列
"""

# n = int(input("次数："))
#
# res = 1
# pre = 1
# temp = 0
# for i in range(n):
#     if i == 0 or i == 1:
#         print (1)
#     else:
#         temp = res
#         res += pre
#         pre = temp
#         print(res)

"""

"""