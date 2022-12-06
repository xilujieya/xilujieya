# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 15:49
# @Author  : pat
# @FileName: ab.py
# @Software: PyCharm

with open(r"E:\python\exercise\exercise3\file\b_file\a.txt", "r+") as f:
    f.write("hello")
    f.seek(0)
    print(f.read())
