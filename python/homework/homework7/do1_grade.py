#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 0:13
# @Author  : pat
# @FileName: do1_grade.py
# @Software: PyCharm


"""有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；"""

import random
import threading
import threadpool
from concurrent.futures import ThreadPoolExecutor

list1 = [random.randint(1, 101) for i in range(100)]


# A 利用多线程程序
def output(*args):
    list2 = [args]
    for i in list2:
        print(i)


for i in range(5):
    t = threading.Thread(target=output, args=(list1[i * 20:(i + 1) * 20]))
    t.start()

# B 利用线程池来实现；
print('\n')
pool = ThreadPoolExecutor(max_workers=5)
for i in range(5):
    future1 = pool.submit(output, list1[i * 20:(i + 1) * 20])
