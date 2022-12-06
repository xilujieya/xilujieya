#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 1:18
# @Author  : pat
# @FileName: do1_setup_file.py
# @Software: PyCharm

"""写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中"""

with open("./file/index.txt", 'a') as file:
    text = input('请输入文件内容：')
    while text:
        file.write(text)
        file.write('\n')
        text = input('请输入文件内容：')