#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 1:21
# @Author  : pat
# @FileName: do2_read_file.py
# @Software: PyCharm

"""2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
第一行： xxxx
第二行： xxxx"""

with open('./file/index.txt', 'r') as file:
    num = 0
    for line in file:
        num += 1
        print('第{}行：'.format(num).format() + line)