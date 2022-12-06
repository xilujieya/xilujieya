#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 17:33
# @Author  : pat
# @FileName: do_list_input..py
# @Software: PyCharm

"""列表初始化-2.5'
从键盘上输入一组数据(要求一行输入)，用空格隔开；并将这一组数据（如果其中的数据能转换成整数，请转换成整数）存放到一个列表中；并打印输出列表的值；"""

str_ = input('从键盘上输入一组数据(要求一行输入)，用空格隔开:')
lists = str_.strip().split(' ')
count = 0
for i in lists:
    if i.isdigit():
        lists[count] = int(i)
    count += 1
print(lists)

