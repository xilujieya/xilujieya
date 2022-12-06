# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 16:56
# @Author  : pat
# @FileName: do_1.17_readfile4.py
# @Software: PyCharm

"""一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出;
            姓名      学号      分数
            张三      101         78
            李四      102         87
            王五       103        83"""


list = []
f = open('readfile2.txt', 'r+', encoding='utf-8')
for i in range(4):
    line = f.readline()
    if i == 0:
        pass
    else:
        line = line.strip()
        list.append(line)
f.close()
list.sort(key=lambda x: x.split('       ')[2], reverse=True)
print(list)
