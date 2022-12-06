#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 17:18
# @Author  : pat
# @FileName: do5_student_grade.py
# @Software: PyCharm

"""定义一个列表，通过键盘输入10个同学的姓名，以及其Python成绩保存到该列表；计算出平均分、最高分，最低分并打印；
   提示：可以将姓名，成绩组合成一个元组，然后存放到列表中，比如"""

list = []
sum = 0
max = min = 0
for i in range(10):
    tup1 = (input("姓名"))
    tup2 = (int(input("成绩")))
    sum += tup2
    if max < tup2:
        max = tup2
    if min > tup2:
        min = tup2
    list.append((tup1 + ',' + str(tup2)))

print('平均分：'+sum / 10)
print('最高分'+max)
print('最低分'+min)
print(list)
