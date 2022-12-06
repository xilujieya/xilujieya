# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 22:28
# @Author  : pat
# @FileName: do5_random.py
# @Software: PyCharm

"""使用random模块，生成随机数，来初始化一个列表，元组
     使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法"""

import random

list1 = [random.randint(0, 100) for i in range(10)]
tup1 = tuple(random.randint(0, 100) for i in range(10))
print(list1)
print(tup1)

