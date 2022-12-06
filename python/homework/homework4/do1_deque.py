#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 15:05
# @Author  : pat
# @FileName: do1_deque.py
# @Software: PyCharm

""" 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
    提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)"""
from datetime import *
import random
from collections import deque


list1 = [random.randint(1, 100) for i in range(10)]
t1 = datetime.timestamp(datetime.now())
print(t1)
list1.insert(0, 0)
list1.append(10)
# time.sleep(2)
t2 = datetime.timestamp(datetime.now())
print(t2)
t3 = datetime.timestamp(datetime.now())
print(t3)
list2 = deque([list1])
list2.append(11)
list2.appendleft(0)
t4 = datetime.timestamp(datetime.now())
print(t4)
print(t4-t3-t2+t1)

