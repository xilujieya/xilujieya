# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 23:43
# @Author  : pat
# @FileName: do_listscore.py
# @Software: PyCharm

"""用列表定义10个同学的成绩,输出最高分,最低分,总分和平均值;"""

import random

stu = []
for i in range(10):
    stu.append(random.randint(0, 100))

print(max(stu))
print(min(stu))

sum = 0
for i in stu:
    sum = sum+i
print(sum/10)