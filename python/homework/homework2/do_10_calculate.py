#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/3 19:04
# @Author  : pat
# @FileName: do_10_calculate.py
# @Software: PyCharm

"""编写一个函数calculate, 可以实现2个数的运算(加,减 乘,除)"""

def calculate(x):
    if x[1] == '+':
        return int(x[0]) + int(x[2])
    elif x[1] == '-':
        return int(x[0]) - int(x[2])
    elif x[1] == '*':
        return int(x[0]) * int(x[2])
    elif x[1] == '/':
        return int(x[0]) / int(x[2])

x = input("请输入一个两个数的运算：")
print(calculate(x))