# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 16:01
# @Author  : pat
# @FileName: do1_stu_list.py
# @Software: PyCharm
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

