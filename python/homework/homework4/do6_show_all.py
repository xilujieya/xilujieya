#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 17:21
# @Author  : pat
# @FileName: do6_show_all.py
# @Software: PyCharm

import os
import time

path = r'E:\python\homework\homework4'
for f in os.listdir(path):
    f_path = os.path.join(path, f)
    if os.path.isfile(f_path):
        t1 = os.path.getmtime(f_path)
        t2 = time.localtime(t1)
        t3 = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        print(f, '       ', t3, '        ', '文件', '        ', os.path.getsize(f_path))
    if os.path.isdir(f_path):
        t1 = os.path.getmtime(f_path)
        t2 = time.localtime(t1)
        t3 = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        print(f, '       ', t3, '        ', '文件', '        ', '文件夹')
