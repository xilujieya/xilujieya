# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 20:16
# @Author  : pat
# @FileName: do_1.13_apple.py
# @Software: PyCharm

"""定义一个函数,来计算苹果的价格(重量*价格); 通过键盘输入重量和价格,然后调用函数来计算"""


def apple(weight, price):
    return weight * price


a = int(input("请输入重量"))
b = int(input("请输入价格"))
print("苹果的价格是"+str(apple(a, b)))
