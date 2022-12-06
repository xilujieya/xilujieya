#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/2 22:23
# @Author  : pat
# @FileName: do_5_dictvalue.py
# @Software: PyCharm

""" 写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;"""


def detection(d):
    for i, j in d.items():
        if len(j) > 2:
            d[i] = j[0:2]
    return d


dict1 = {'a': 'av', 'b': 'avch', 'c': 'aue'}
print(dict1)
d1 = detection(dict1)
print(d1)
