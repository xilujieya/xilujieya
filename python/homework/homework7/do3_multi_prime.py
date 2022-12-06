#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 15:46
# @Author  : pat
# @FileName: do3_multi_prime.py
# @Software: PyCharm

"""多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度"""

import time
import math
from concurrent.futures import ThreadPoolExecutor


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def pricessPool(count):
    pool = ThreadPoolExecutor(max_workers=count)

    is_prime = []
    start_time = time.time()
    for i in range(1, 100000):
        if pool.submit(isPrime, i):
            is_prime.append(i)

    print('success,result = %d' % (sum(is_prime)))
    print('运行时间为:%s' % (time.time() - start_time))


def notpricessPool():
    is_prime = []
    start_time = time.time()
    for i in range(1, 100000):
        if isPrime(i):
            is_prime.append(i)
    print('success,result = %d' % (sum(is_prime)))
    print('运行时间为:%s' % (time.time() - start_time))


if __name__ == '__main__':
    notpricessPool()
    pricessPool(10)
    pricessPool(4)
