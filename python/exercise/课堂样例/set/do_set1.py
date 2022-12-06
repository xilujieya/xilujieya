# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 17:25
# @Author  : pat
# @FileName: do_set1.py
# @Software: PyCharm

s1 = set([1, 2, 3, 4, 3, 2])  # 集合自己去除重复的元素
print(s1)

s2 = set([4, 5, 6])
print(s2)
print(s1 & s2)  # 求交集
print(s1 | s2)  # 求并集
