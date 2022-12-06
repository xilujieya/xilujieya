#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/1 23:21
# @Author  : pat
# @FileName: do_2.1_caculate.py
# @Software: PyCharm

"""       定义一个高阶函数, 实现加,减,乘,除计算器功能;
      highfunc(a ,b  ,func)"""


def highfunc(a, b, func):
    if isinstance(a, int) and isinstance(a, int):
        func(a, b)
    else:
        print("传参错误")


def add(a, b):
    print(a + b)


def delete(a, b):
    print(a - b)


def multiply(a, b):
    print(a * b)


def divide(a, b):
    if b != 0:
        print(a / b)
    else:
        print("除数为零，无法计算")


a = 1
while a:
    print("1.加法")
    print("2.减法")
    print("3.乘法")
    print("4.除法")
    num1 = int(input("参数1:"))
    num2 = int(input("参数2:"))
    num3 = int(input("方法:"))
    if num3 == 1:
        highfunc(num1, num2, add)
    elif num3 == 2:
        highfunc(num1, num2, delete)
    elif num3 == 3:
        highfunc(num1, num2, multiply)
    elif num3 == 4:
        highfunc(num1, num2, divide)
    else:
        print("输入方法不合理")
    a = int(input("是否继续1/0"))
