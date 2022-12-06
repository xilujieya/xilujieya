# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 16:49
# @Author  : pat
# @FileName: do_file1.py
# @Software: PyCharm

# 打开一个文件
f = open(r'E:\python\exercise\file\foo.txt', "w", encoding='gbk') # r: 代表不处理转义现象，正则表达式的一种
f.write("python是一门非常好的语言")
f.close()

print(type(f))
