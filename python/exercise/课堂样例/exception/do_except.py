# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 17:17
# @Author  : pat
# @FileName: do_except.py
# @Software: PyCharm

while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")