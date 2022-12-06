# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 16:37
# @Author  : pat
# @FileName: do_var_global.py
# @Software: PyCharm

num = 10


def demo1():
    global num
    num = 100
    print("demo1===>%d" % num)


def demo2():
    print("demo2===>%d" % num)


demo1()
demo2()
