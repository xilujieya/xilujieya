# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 16:15
# @Author  : pat
# @FileName: do_1.17_readfile2.py
# @Software: PyCharm

"""一个文件内容的如下,请读取文件的内容, 并输出;
            姓名      学号      分数
     -------------------------------------------
            张三      101         78
            李四      102         87
            王五       103        83"""

f = open('readfile.txt', 'r', encoding="utf-8")
print(f.read())
f.close()