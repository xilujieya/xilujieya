#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 1:25
# @Author  : pat
# @FileName: do4_add_picture.py
# @Software: PyCharm

"""4 题目要求：
 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
 将当前img目录所有以.png结尾的后缀名改为.jpg."""
import os

img_list1 = os.listdir('./img')
for item in img_list1:
    old = item
    new = item.replace('.png', '.jpg')
    os.rename('./img/'+old, './img/'+new)