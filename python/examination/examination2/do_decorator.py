#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 18:10
# @Author  : pat
# @FileName: do_decorator.py
# @Software: PyCharm

"""装饰器使用--2.5'
定义一个记录日志到文件的函数（使用logging模块）；定义一个装饰器，当该装饰器装饰一个函数时，可以记录这个函数被调用了的事实（就是记录日志）和时间"""

import time
import logging


def logger(fn):
    def inner(*args, **kwargs):
        f = open("log", mode="a", encoding="utf-8")
        ret = fn(*args, **kwargs)
        f.write("在%s, 访问了%s函数,结果为%s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), fn.__name__, ret))
        print("end call")
        return ret

    print("begin call")
    return inner


@logger
def add(x, y):
    print(x+y)
    return x + y


add(int(input("请输入参数1")), int(input("请输入参数2")))