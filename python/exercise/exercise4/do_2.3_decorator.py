#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/1 22:44
# @Author  : pat
# @FileName: do_2.3_decorator.py
# @Software: PyCharm

"""请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间："""
import functools
import time


def metric(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("运行时间为%s" % (end_time - start_time))
        return res
    return inner


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

