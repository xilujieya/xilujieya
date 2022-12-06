# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 20:43
# @Author  : pat
# @FileName: do_1.17_ospath.py
# @Software: PyCharm

"""练习:  在window平台下运行程序； 练习os.path 相关方法的使用! 观察输出结果;
    1 编写一个程序，运行起来，打印输出此程序文件所在的 文件夹路径；
    2 编写一个程序，在指定目录下，创建一个目录；
    3 列出一个指定目录下的所有文件；"""

import os

print(os.getcwd())


def newfolder(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("创建成功")
    else:
        print("已有目录")


newfolder('test')


print(os.listdir())
