#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/1 23:09
# @Author  : pat
# @FileName: do_2.4_logger.py
# @Software: PyCharm

"""定义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志;"""

import time


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
