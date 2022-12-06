#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/3 17:09
# @Author  : pat
# @FileName: do_8_findmax.py
# @Software: PyCharm

"""请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
 例如，输入 aaaabbc，输出：a:4"""

import string


def getmax(str):
    a = max(string.ascii_lowercase, key=str.count)
    n = 0
    for i in str:
        if i == a:
            n += 1
    return a, n


str1 = str(input("请输入字符串"))
x, n = getmax(str1);
print(x, n)
