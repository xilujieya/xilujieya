# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 23:49
# @Author  : pat
# @FileName: do_tuple.py
# @Software: PyCharm

"""定义元组,进行基本的操作(元组的基本运算,元素的输出,内置函数的使用); """

import random

tup1 = (12, 34, 56)
tup2 = ('abc', 'xyz')

tup3 = tup1 + tup2
print(tup3)


tup4 = tup1 * 4
print(tup4)

bool1 = 3 in tup1
print(bool1)

for i in tup3:
    print(i)

print(len(tup3))
print(max(tup1))
print(min(tup1))

alist = [123, 'xyz', 'zara', 'abc']
atupe = tuple(alist)

print(atupe)


"""定义一个元组,来保存成绩,输出最高分"""

grade = (random.randint(1, 100) for _ in range(6))
print(max(grade))
