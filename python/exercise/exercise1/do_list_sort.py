# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 23:45
# @Author  : pat
# @FileName: do_list_sort.py
# @Software: PyCharm

"""输入5个同学的成绩,进行排序输出;进行添加新的数据操作"""

import random

stu = []
for i in range(5):
    stu.append(random.randint(60, 100))
stu.sort()
print(stu)

print('请输入要添加的数据')
x = int(input())
stu.append(x)
print(stu)

