#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/3 16:51
# @Author  : pat
# @FileName: do_7_grade.py
# @Software: PyCharm

"""随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
    A---成绩>=90;
    B-->成绩在 [80,90)
    C-->成绩在 [70,80)
    D-->成绩<70"""

import random

list = [random.randint(1, 100) for i in range(20)]


def detection(score):
    for i in score:
        if i >= 90:
            print("A", end=" ")
        elif i >= 80:
            print("B", end=" ")
        elif i >= 70:
            print("C", end=" ")
        else:
            print("D", end=" ")


print(list)
detection(list)
