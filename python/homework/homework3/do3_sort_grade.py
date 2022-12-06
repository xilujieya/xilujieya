#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 1:21
# @Author  : pat
# @FileName: do3_sort_grade.py
# @Software: PyCharm

"""3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出"""

lists = []
with open('./file/grade.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split('    ')
        lists.append(line)
lists.sort(key=lambda x: int(x[2]), reverse=True)
print(lists)
