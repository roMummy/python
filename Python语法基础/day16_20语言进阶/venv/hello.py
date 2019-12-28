# coding=utf-8
"""
数据结构和算法
"""

# def select_sort(origin_items, comp=lambda x, y : x < y):
#     """简单选择排序"""
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         min_index = 1
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#             items[i], items[min_index] = items[min_index], items[i]
#     return items
#
# def bubble_sort(origin_items, comp=lambda x, y : x > y):
#     """冒泡排序（搅拌排序）"""
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range(i, len(items) - 1 - i):
#             if comp(items[j], items[j + 1]):
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#             for j in range(len(items) - 2 - i, i, -1):
#                 if comp(items[j - 1], items[j]):
#                     items[j], items[j - 1] = items[j - 1], items[j]
#                     swapped = True
#         if not swapped:
#             break
#     return items

"""
推导式
"""

# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)

"""
heapq itertools
"""
import heapq


# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
#
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(list1))

"""
函数
"""

# items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1,10))))
# itmes2 = list[x ** 2 for x in range(1, 10) if x % 2]

"""
装饰器
"""

# from functools import wraps
#
# def singleton(cls):
#     """非线性安全的装饰器"""
#     instance = {}
#
#     def wrapper(*args, **kwargs):
#         if cls not in instance:
#             instance[cls] = cls(*args, **kwargs)
#         return instance[cls]
#
#
# from threading import Lock
#
# def singleton(cls):
#     """线程安全装饰器"""
#     instance = {}
#     locker = Lock()
#
#     def wrapper(*args, **kwargs):
#         if cls not in instance:
#             with locker:
#                 instance[cls] = cls(*args, **kwargs)
#         return instance[cls]
#     return wrapper

"""
工程模式
"""

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月星"""
        pass

class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000

class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200 * self.working_hour

class Salesman(Employee):

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800 + self.sales * 0.05

class EmployeeFactory():
    """工厂"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == "M":
            emp = Manager(*args, **kwargs)
        elif emp_type == "P":
            emp = Programmer(*args, **kwargs)
        elif emp_type == "S":
            emp = Salesman(*args, **kwargs)
        return emp

# def main():
#     emps = [
#         EmployeeFactory.create("M", "刘备"),
#         EmployeeFactory.create("P", "张云", 100),
#         EmployeeFactory.create("S", "诸葛亮", 1231111)
#     ]
#
#     for emp in emps:
#         print("%s: %.2f元" % (emp.name, emp.get_salary()))
#
# if __name__ == '__main__':
#     main()

"""
策略模式
"""
class StreamHasher():
    """哈希摘要生成器"""

    def __init__(self, alg="md5", size=4096):
        self.size = size
        alg = alg.upper()
        self.hasher = getattr(__import__("hashlib"), alg.lower())()

    def __call__(self, stream):
        """改变自己的实例"""
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成16进制的摘要"""
        for buf in iter(lambda: stream.read(self.size), b""):
            self.hasher.update(buf)
        return self.hasher.hexdigest()


def main():
    """主函数"""
    hasher1 = StreamHasher()
    with open('hello.py', 'rb') as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher('sha1')
    with open('hello.py', 'rb') as stream:
        print(hasher2(stream))


if __name__ == '__main__':
    main()

"""
迭代器 生成器
"""

def fib(num):
    """生成器"""

    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a

class Fib(object):
    """迭代器"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        return StopIteration()

