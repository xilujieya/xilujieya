#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/3 16:48
# @Author  : pat
# @FileName: do_6_Fibon.py
# @Software: PyCharm

"""定义一个函数, 打印输出n以内的斐波那契数列;"""


def fibonacci(n):
    fibonacci = [0, 1]
    i = 0
    while fibonacci[i] + fibonacci[i + 1] < n:
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])
        i = i + 1
    print(fibonacci)


fibonacci(int(input("请输入最大数字")))
