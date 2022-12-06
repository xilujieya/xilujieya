# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 16:18
# @Author  : pat
# @FileName: do_1.17_readfile3.py
# @Software: PyCharm

"""一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
            姓名      学号      分数
            张三      101         78
            李四      102         87
            王五       103        83"""

list = []
f = open('readfile2.txt', 'r+', encoding='utf-8')
for i in range(4):
    line = f.readline()
    if i == 0:
        with open("result.txt", "a") as mon:
            mon.write(line)
    else:
        line = line.strip()
        list.append(line)
f.close()
print(list)

list.sort(key=lambda x: x.split('       ')[2], reverse=True)
print(list)

with open("result.txt", "a") as mon:
    for i in list:
        mon.write(i+'\n')

with open("result.txt", "r") as mon:
    print(mon.read())
