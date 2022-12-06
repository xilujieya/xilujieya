#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 17:29
# @Author  : pat
# @FileName: do7_sum_file.py
# @Software: PyCharm

"""使用python代码统计一个文件夹中所有文件的总大小"""

import os


def size_sum(path):
    sum = 0
    for f in os.listdir(path):
        f_path = os.path.join(path, f)
        if os.path.isfile(f_path):
            sum = sum + os.path.getsize(f_path)
        if os.path.isdir(f_path):
            size_sum(f_path)
    return sum


if __name__ == '__main__':
    path = r'E:\python\homework\homework4'
    sum = size_sum(path)
    print(sum)
