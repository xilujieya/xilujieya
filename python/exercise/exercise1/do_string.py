#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 18:55
# @Author  : pat
# @FileName: do_string.py
# @Software: PyCharm

"""输入一个字符串，比如 abcdef；1 通过字符串切片方式反向输出；2 存放到列表中，然后反向输出：fedcba"""

a = input()

print(a)
a = a[::-1]
print(a)

list1 = list(a)
list1.reverse()
print(''.join(list1))

