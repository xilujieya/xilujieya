# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 17:23
# @Author  : pat
# @FileName: do_1.19_copy.py
# @Software: PyCharm

""" 将一个文件夹下的某个文件,拷贝到另外一个文件夹下去;
     提示:    写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个#参数是目标位置，将源文件copy到目标位置。
                还需要判断一下这个文件之前是否存在;  读源文件的内容; 创建目标文件; 读到的内容,再写入到目标文件"""


def copy(path1, path2):
    with open(path1, 'r+') as f1:
        origin = f1.read()
        with open(path2, 'w') as f2:
            f2.write(origin)


copy(r'E:\python\exercise\exercise3\file\b_file\a.txt', r'E:\python\exercise\exercise3\file\a_file\aa.txt')
