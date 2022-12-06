#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 17:16
# @Author  : pat
# @FileName: do4_sort.py
# @Software: PyCharm

list = []
for i in range(3):
    list.append(int(input()))

list.sort()
for i in list:
    print(i)
