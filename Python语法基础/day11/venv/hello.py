# import time
#
# def main():
#     f = None
#     try:
#         # f = open("1.txt","r",encoding="utf-8")
#         # 一次性读完
#         with open("1.txt", "r", encoding="utf-8") as f:
#             print(f.read())
#         # 逐行
#         with open("1.txt", mode="r") as f:
#             for line in f:
#                 print(line, end="")
#                 time.sleep(0.5)
#         # 读取文件按行读取到列表中
#         with open("1.txt") as f:
#             lines = f.readlines()
#         print(lines)
#
#     except FileNotFoundError:
#         print("找不到文件")
#     except LookupError:
#         print("指定了未知的编码")
#     except UnicodeDecodeError:
#         print("编码错误")
#     # finally:
#     #     if f:
#     #         f.close()
#
# if __name__ == '__main__':
#     main()

"""
写入
"""
# from math import sqrt
#
# def is_prime(n):
#     """判断是否是素数"""
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False
#
# def main():
#     filenames = ["a.txt", "b.txt", "c.txt"]
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename, "w", encoding="utf-8"))
#         for number in range(1, 10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + "\n")
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + "\n")
#                 else:
#                     fs_list[2].write(str(number) + "\n")
#     except IOError as ex:
#         print(ex)
#         print("写文件时发生错误")
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print("over")
#
# if __name__ == '__main__':
#     main()

"""
读写二进制文件
"""
#
# def main():
#     try:
#         with open("1.txt", "rb") as f1:
#             data = f1.read()
#             print(type(data))
#             print(data)
#         with open("2.txt", "wb") as f2:
#             f2.write(data)
#     except FileNotFoundError as e:
#         print(e)
#     except IOError as e:
#         print(e)
#     print("over")
#
# if __name__ == '__main__':
#     main()

"""
读写json文件
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""

import json

def main():
    mydict = {
        "name": "张三",
        "age": 18,
        "qq": 12345,
        "friends": ["李四", "王五"],
        "cars": [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(mydict, f)
    except IOError as e:
        print(e)
    print("over")

if __name__ == '__main__':
    main()

