#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 17:29
# @Author  : pat
# @FileName: do6_findsame.py
# @Software: PyCharm

"""有两个列表
 list1 = [aa，11, 22, 33] ；list2 = [bb，22, 33, 44]
        请找出它们中相同的元素；"""

list1 = ['aa', 11, 22, 33];
list2 = ['bb', 22, 33, 44];

set1 = set(list1) & set(list2)
list3 = list(set1)
print(list3)
