# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 19:52
# @Author  : pat
# @FileName: do_1.11_numlist.py
# @Software: PyCharm

"""创建一个有10个数字的列表,先输出此列表,然后再输出其中为偶数元素"""

import random

list1 = []
for i in range(10):
    list1.append(random.randint(0, 100))
print(list1)


def findeven(list):
    for x in list:
        if x % 2 == 0:
            print(x)


findeven(list1)
