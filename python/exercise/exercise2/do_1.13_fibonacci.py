# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 20:26
# @Author  : pat
# @FileName: do_1.13_fibonacci.py
# @Software: PyCharm

"""通过函数来实现斐波那契数列输出"""


def fibonacci(n):
    fibonacci = [0, 1]
    i = 0
    while fibonacci[i] + fibonacci[i + 1] < n:
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])
        i = i + 1
    print(fibonacci)


n = int(input("请输入最大的数字"))
fibonacci(n)

