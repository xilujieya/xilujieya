# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 22:16
# @Author  : pat
# @FileName: do3_list_findsame.py
# @Software: PyCharm

"""定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出"""

list1 = [1, 2, 3, 'e', "qwe"]
list2 = [5, 8, 1, "wee", 'e']

for i in list1:
    for j in list2:
        if i == j:
            print(j)
