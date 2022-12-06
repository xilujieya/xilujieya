# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 16:52
# @Author  : pat
# @FileName: do_func1.py
# @Software: PyCharm

def changeInt(a):
    print("a原始参数地址", id(a))
    a = 10
    print("a重新赋值后的地址", a)
    print("a重新赋值后的地址", id(a))


b = 5
print("b变量的地址", id(b))

changeInt(b)


print("传参后b的地址", id(b))
print("传参后b的值", b)
