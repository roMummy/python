# coding=utf-8

"""
字符串和常用数据结构
"""

# s = """
# 1
# 2
# 3
# """
# print (s)
# s1 = r"\hello, world"
# print (s1)
# str = "abc123456"
# print (str[2])
# print (str[2:5])
# print (str[2::2])
# print (str[::-1])
#
# print(len(str))
# print(s1.capitalize())
# print(s1.title())
# print(s1.upper())
#
# a, b = 1, 2
# print(f"{a} * {b} = {a * b}")

"""
列表
"""

# list = [1,2,3,4,5]
#
# list1 = [1] * 4
# print(list1)
# list.append(6)
# list.insert(1,10)
# print(list)
# if 2 in list:
#     list.remove(2)
# print(list)
# #从指定位置删除
# list.pop(0)
# print(list)
#
# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# # 列表切片
# fruits2 = fruits[1:4]
# print(fruits2) # apple strawberry waxberry
# # 可以通过完整切片操作来复制列表
# fruits3 = fruits[:]
# print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
# fruits4 = fruits[-3:-1]
# print(fruits4) # ['pitaya', 'pear']
# # 可以通过反向切片操作来获得倒转后的列表的拷贝
# fruits5 = fruits[::-1]
# print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
#
# list2 = sorted(list)
# fruits5.sort(key=len)
# print(fruits5)

"""
生成器
"""
import sys
#
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in "abcd" for y in "1234567"]
# print(f)
# f = [x ** 2 for x in range(1,1000)]
# print(sys.getsizeof(f))
# print(type(f))
# #生成一个生成器对象
# f = (x ** 2 for x in range(1,1000))
# print(sys.getsizeof(f))
# print(type(f))
#
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
# def main():
#     for val in fib(20):
#         print(val)
#
# if __name__ == "__main__":
#     main()

"""
元组 不能修改元素
"""
# t = ("张三", 12, False, "傻逼")
# print(t)
# print(t[0])
# print(type(t))
# # t[0] = "asdf"
# person = list(t)
# print(person)
# print(type(person))
# p = ["张三", 12, False, "傻逼"]
# print(p)
# print(sys.getsizeof(t))
# print(sys.getsizeof(p))

"""
集合
"""
# set1 = {1,2,3,4,3,2}
# print(set1)
# set2 = set(range(1,10))
# print(set2)
# set3 = {num for num in range(1, 100) if num % 3 == 0 and num % 5 == 0}
# print(set3)
#
# set1.add(5)
# set1.update([1])
# print(set1)
# set1.discard(5)
# print(set1)
#
# print(set1 & set2)
# print(set1 | set2)
# print(set2 - set1)
# print(set1 ^ set2)
# # print(set1.symmetric_difference(set2))
# # 判断子集和超集
# print(set2 <= set1)
# # print(set2.issubset(set1))
# print(set3 <= set1)
# # print(set3.issubset(set1))
# print(set1 >= set2)
# # print(set1.issuperset(set2))
# print(set1 >= set3)
# # print(set1.issuperset(set3))

"""
字典
"""
# dic1 = {"张三": 1, "李四": 2}
#
# print(dic1)
# dic2 = dict(one=1, two=2)
# print(dic2)
# dic3 = dict(zip(["a","b","c"], "123"))
# print(dic3)
# dic4 = {num: num**2 for num in range(1, 10)}
# print(dic4)
#
# for key in dic1:
#     print(key)
# print(dic1.popitem())

"""
跑马灯
"""
# import os
# import time
#
# def main():
#     content = "hello world!"
#     while True:
#         os.system("cls")
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
# if __name__ == "__main__":
#     main()

"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random

def generade_code(code_len = 6):
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_pos = len(all_chars) - 1
    code = ""
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code

print(generade_code())

"""
练习3：设计一个函数返回给定文件名的后缀名。
"""

def get_suffix(filename, has_dot=False):
    pos = filename.rfind(".")
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ""

print(get_suffix("123123.asd"))

"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
"""

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

print(max2([1,3,1,5]))

"""
练习5：计算指定的年月日是这一年的第几天。
"""
def is_leap_year(year):
    """
    判断是否是闰年
    :param year: 年
    :return: 是否是闰年
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    """
    计算传入的时间是哪一天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 哪一天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    print(is_leap_year(year))
    print(days_of_month)
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

print(which_day(2019, 10, 22))

"""
杨辉三角
"""

def main():
    num = int(input("number of rows:"))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end="\t")
        print()

if __name__ == '__main__':
    main()
