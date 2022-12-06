# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 16:40
# @Author  : pat
# @FileName: do_func0.py
# @Software: PyCharm

def myfunc():
    print("this is my function")


def add(a, b):
    return a + b


# 程序我的入口
if __name__ == "__main__":
    myfunc()

    res = add(2, 5)
    print(res)


def printNumber(myList):
    for i in myList:
        if i % 2 == 0:
            print(i)


l1 = [i for i in range(10)]
printNumber(l1)


def calculateFac(n):
    res = 1
    i = 1
    while i <= n:
        res *= i
        i += 1
    return res


print(calculateFac(5))
