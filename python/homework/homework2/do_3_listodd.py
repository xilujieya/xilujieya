#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/2 21:48
# @Author  : pat
# @FileName: do_3_listodd.py
# @Software: PyCharm

"""编写一个函数, 传入一个数字列表, 输出列表中的奇数;
   数字列表请用随机数函数生成"""

import random

list1 = [random.randint(0, 100) for i in range(10)]


def getodd(list):
    for i in list:
        if i % 2 == 1:
            print(i)


getodd(list1)
