# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 19:56
# @Author  : pat
# @FileName: do_1.11_findprime.py
# @Software: PyCharm

"""如下实例用于查询质数的循环例子"""

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
