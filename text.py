import sys
import pprint

# a, b = 0, 1
# while b < 10:
# 	print(b)
# 	a, b = b, a + b
# 	pass	

print("hello")

#if 
def ifFunc():
	x = int(input("hello:"))
	if x < 0:
		x = 0
		print('changed to zero')
	elif x == 0:
		print('zero')
	elif x == 1:
		print('single')
	else:
		print('more') 
# ifFunc()
	
#for 
def forFunc():
	words = ['cat', 'window', '13']
	for x in words:
		print(x, len(x))
# forFunc()

#range()
'''
for x in range(1,10):
	pass
	print(x)
'''

#custom func
def ask_ok(n, retries = 4, reminder = 'please try again'):
	while True:
		ok = input(n)
		if ok in ('y', 'True','yes'):
			return True
		if ok in ('n', 'no', 'false'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('error')
			pass
		print(reminder)
	pass
# ask_ok('yes')

#开头之母变成大写
name = "aBc asdf"
print(name.title())

#大写、小写转换
print(name.upper())
print(name.lower())

#合并字符串
print("123" + "321")

#保证字符串后面没有空格
favorite_language = "python   "
print(favorite_language)
print(favorite_language.rstrip())

#删除两端的空格
print(favorite_language.strip())

####数字######

#使用str（）避免类型错误
age = 23
message = "Happly" + str(age) + "birthday"

print(message)

###列表####
bicyles = ["treak", "cannondale"]
print(bicyles)
#删除列表元素
bicyles[0] = "one"
print(bicyles)
#添加元素
bicyles.append("two")
print(bicyles)
#插入元素
bicyles.insert(1,"three")
print(bicyles)
#删除元素
del bicyles[0]
print(bicyles)
fooder = bicyles.pop() #删除尾部数据 有返回值
print(fooder)
one = bicyles.pop(1)
print(one)
bicyles.remove("three") #根据值删除元素
print(bicyles)


####整数和浮点数###
from decimal import getcontext, Decimal
getcontext().prec = 2
decimal_flate = Decimal(0.1) + Decimal(0.1)
print(decimal_flate)

'''
decimal(https://docs.python.org/2/library/decimal.html)，用于定点运算和浮点运算。
• math(https://docs.python.org/2/library/math.html)，可以使用 C 语言标准所定义的数学函数。
• numpy(http://docs.scipy.org/doc/numpy/reference/routines.math.html)，Python 科 学 计
算的基础包。
• sympy(http://docs.sympy.org/latest/index.html)，用于符号数学的 Python 库。
• mpmath(http://mpmath.org/)用于任意精度实数和复数浮点运算的 Python 库
'''
#字典
animal_counts = {"cats": 2, "dogs": 1, "horses": 5, "house": {"one": 1}}
dogs = animal_counts["dogs"]
print(dogs)

#type返回数据类型
print(type(animal_counts))
#dir返回属性列表和方法
print(dir(animal_counts))

#help 帮助文档
print(help(animal_counts.clear))
print(animal_counts)
pprint.pprint(animal_counts)
