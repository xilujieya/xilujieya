#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/2 21:29
# @Author  : pat
# @FileName: do_1_getlen.py
# @Software: PyCharm

"""写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。"""


def getlen(x):
    return len(x)


str1 = 'dwqdqw'
list1 = [15, 'fewf', 48, 24, 55]
tuple1 = (141, 'dqw', 'dwfd')

print(getlen(str1))
print(getlen(list1))
print(getlen(tuple1))
