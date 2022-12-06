#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/1 21:51
# @Author  : pat
# @FileName: do_2.2_closure.py
# @Software: PyCharm

"""利用闭包返回一个计数器函数，每次调用它返回递增整数"""


def createCounter():
    num = 0

    def increase():
        nonlocal num
        num += 1
        return num

    return increase


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
