# coding=utf-8
"""
函数

"""

# def f(num):
#     """求阶乘"""
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return  result
#
# m = int(input("m = "))
# n = int(input("n = "))
# print (f(m)//f(n)//f(m-n))

"""
可变参数
"""
# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total
# # print (add(1))
# # print (add(1,2,3))
# # print (add())
#
# if __name__ == '__main__':
#     """这里面的代码不会在被导入的时候执行"""
#     print ("hello ：",add(0),"你好")

"""
最大公约数 
"""

def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for f in range(y, 0 , -1):
        if x % f == 0 and y % f == 0:
            return f

"""
最小公倍数
"""

def lcm(x, y):
    return x * y // gcd(x, y)

if __name__ == "__main__":
    print (gcd(12,16))
    print (lcm(12,16))