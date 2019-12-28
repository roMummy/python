# coding=utf-8
"""
正则表达式
"""

import re

def main():
    username = str(input("请输入用户名："))
    qq = str(input("请输入qq："))
    m1 = re.match(r"^[1-9a-zA-Z]{6,20}$", username)
    if not m1:
        print("请输入有效的用户名")
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print("请输入有效的qq")
    if m1 and m2:
        print ("ok")

if __name__ == '__main__':
    main()

