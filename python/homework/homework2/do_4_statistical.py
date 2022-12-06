#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/2 21:57
# @Author  : pat
# @FileName: do_4_statistical.py
# @Software: PyCharm

"""写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果"""


def get_count(s):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in s:
        if i.isdigit():
            a = a + 1
        elif i.isalpha():
            b = b + 1
        elif i == ' ':
            c = c + 1
        else:
            d = d + 1
    return a, b, c, d


s = "151gef 15 few9#"
a, b, c, d = get_count(s)
print("数字个数:", a)
print("字母个数:", b)
print("空格个数:", c)
print("其他个数:", d)
