#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/3 18:42
# @Author  : pat
# @FileName: do_9_sort.py
# @Software: PyCharm


"""定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);"""


def sort_array(arr):
    arr.sort()
    return arr


arr = [2, 58, 8, 9, 3, 4, 85, 4]
print(sort_array(arr))
