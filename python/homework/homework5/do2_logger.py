#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/12 22:21
# @Author  : pat
# @FileName: do2_logger.py
# @Software: PyCharm

"""编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；"""

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
