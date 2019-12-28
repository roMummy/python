"""
运算符	            描述
[] [:]	            下标，切片
**	                指数
~ + -	            按位取反, 正负号
* / % //	        乘，除，模，整除
+ -	                加，减
>> <<	            右移，左移
&	                按位与
^ |	                按位异或，按位或
<= < > >=	        小于等于，小于，大于，大于等于
== !=	            等于，不等于
is is not	        身份运算符
in not in	        成员运算符
not or and	        逻辑运算符
= += -= *= /= %= //= **= &= `	        = ^= >>= <<=`

"""

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

# a = 10
# b = 3
# a += b
# a *= b + 1
# print(a)

# f = float(input("请输入华式温度："))
# c = (f - 32) / 1.8
# print("%.1f华式度 = %.1f列斯杜" % (f,c))

####计算面积、周长#######
# import math
#
# r = float(input("请输入半径："))
# area = r ** 2 * math.pi
# p = 2 * math.pi * r
# print("圆的周长：%.1f,面积：%.1f" % (p,area))

#####判断是否是润年#######
year = int(input("请输入年份："))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap)