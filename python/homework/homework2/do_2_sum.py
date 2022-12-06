#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/2 21:43
# @Author  : pat
# @FileName: do_2_sum.py
# @Software: PyCharm

"""编写一个函数,接收n个数字，求这些参数数字的和"""


def sum(*n):
    sum = 0
    for i in n:
        sum += i
    return sum


print(sum(1, 2, 3, 4, 5, 8))
