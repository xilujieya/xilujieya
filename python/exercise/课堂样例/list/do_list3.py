# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 16:46
# @Author  : pat
# @FileName: do_list3.py
# @Software: PyCharm

"""列表的初始化"""

import random

# list1 = [90, 20]
# print(list1)

# list2 = []
# list2.append(1, 10, 50)
# print(list2)


# list3 = []
# list3 = list(map(int, input("一次性输入多个值，空格隔开").split()))


# list4 = []
# for s in input("一次性输入多个值，空格隔开").split():
#     if s.isdigit():
#         s = int(s)
#     list4.append(s)
# print(list4)


# list5 = []
# for i in range(1, 101):
#     list5.append(i)
# print(list5)


# list6 = [random.randint(0, 6)]
# print(list6)


list7 = [random.randint(1, 100) for _ in range(1, 6)]
print(list7)
