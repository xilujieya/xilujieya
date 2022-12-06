# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 15:47
# @Author  : pat
# @FileName: xxx.py
# @Software: PyCharm

"""构造上述文件结构,分别在指定位置打开文件进行写入操作(同级文件夹里面打开;同级目录下的子目录里面打开;上一级文件目录中的其他文件夹中打开);"""

with open(r"b_file\a.txt", "r+") as file:
    file.write("i have written")
    file.seek(0)
    print(file.read())
