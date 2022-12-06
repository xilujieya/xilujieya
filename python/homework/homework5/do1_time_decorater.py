#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/12 22:05
# @Author  : pat
# @FileName: do1_time_decorater.py
# @Software: PyCharm

"""编写一个装饰器，能计算其他函数的运行时间；"""

import functools
import time


def time_dec(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("运行时间为%s" % (end_time - start_time))
        return res
    return inner


@time_dec
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@time_dec
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
