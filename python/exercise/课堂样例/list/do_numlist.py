# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 16:15
# @Author  : pat
# @FileName: do_numlist.py
# @Software: PyCharm

import random

list = []
for i in range(10):
    list.append(random.randint(0, 100))
print(list)

for x in list:
    if x % 2 == 0:
        print(x)
