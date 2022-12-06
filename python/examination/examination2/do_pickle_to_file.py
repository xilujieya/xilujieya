#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 17:47
# @Author  : pat
# @FileName: do_pickle_to_file.py
# @Software: PyCharm

"""利用pickle模块，将数据序列化保存到文件--2.5'
利用字典解析式，生成记录一组学生2门课的成绩的字典列表，将这个字典列表序列化以后，保存到一个文件中（列表中的每一个元素，保存为文件中的一行）；"""

import pickle
import random
import string


def randletter(x, y):
    return chr(random.randint(ord(x), ord(y)))


stu = []
for x in range(3):
    d = {"name": ''.join(random.sample(string.ascii_letters, 3)),
         "english": random.randint(0, 101),
         "math": random.randint(0, 101)}
    stu.append(d)
print(stu)

f = open('dump.txt', 'wb')
for i in stu:
    pickle.dump(i, f)
    pickle.dump('\n', f)
f.close()
